"""CLI 接口"""

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.syntax import Syntax
from pathlib import Path

from .core import FewShotSelector
from .utils import load_qa_data, FewShotError, DatabaseNotInitializedError

app = typer.Typer(help="动态选择最相关的 few-shot 示例")
console = Console()


@app.command()
def query(
    question: str = typer.Argument(..., help="用户问题"),
    n_examples: int = typer.Option(3, "--num", "-n", help="返回示例数量")
):
    """查询相似示例并生成 Prompt"""
    try:
        selector = FewShotSelector()
        console.print(Panel(question, title="查询问题", border_style="blue"))

        examples = selector.search_similar(question, n_examples)

        table = Table(title="相似示例", show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim")
        table.add_column("类别", style="cyan")
        table.add_column("问题", style="green")
        table.add_column("相似度", justify="right", style="yellow")

        for ex in examples:
            similarity = f"{(1 - ex['distance']) * 100:.1f}%" if ex['distance'] else "N/A"
            table.add_row(
                ex['id'],
                ex['category'],
                ex['question'][:50] + "..." if len(ex['question']) > 50 else ex['question'],
                similarity
            )

        console.print(table)

        prompt = selector.format_prompt(question, examples)
        syntax = Syntax(prompt, "text", theme="monokai", line_numbers=False)
        console.print(Panel(syntax, title="生成的 Prompt", border_style="green"))

    except DatabaseNotInitializedError:
        console.print("[red]错误: 数据库未初始化,请先运行 'few-shot-selector init'[/red]")
        raise typer.Exit(1)
    except FewShotError as e:
        console.print(f"[red]错误: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def init():
    """初始化数据库(首次使用)"""
    try:
        data_path = Path(__file__).parent / "data" / "qa_examples.json"
        qa_pairs = load_qa_data(str(data_path))

        with console.status("[bold green]正在初始化数据库..."):
            selector = FewShotSelector()
            selector.initialize_database(qa_pairs)

        console.print(f"[green]成功初始化数据库,共加载 {len(qa_pairs)} 条 QA 数据[/green]")

    except FileNotFoundError as e:
        console.print(f"[red]错误: {e}[/red]")
        raise typer.Exit(1)
    except FewShotError as e:
        console.print(f"[red]错误: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def stats():
    """显示数据库统计信息"""
    try:
        selector = FewShotSelector()
        stats = selector.get_stats()

        console.print(f"\n[bold]总 QA 数量:[/bold] {stats['total']}")

        if stats['categories']:
            table = Table(title="类别分布", show_header=True, header_style="bold magenta")
            table.add_column("类别", style="cyan")
            table.add_column("数量", justify="right", style="green")

            for cat, count in sorted(stats['categories'].items()):
                table.add_row(cat, str(count))

            console.print(table)

    except FewShotError as e:
        console.print(f"[red]错误: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def add(
    question: str = typer.Argument(..., help="问题"),
    answer: str = typer.Argument(..., help="答案"),
    category: str = typer.Option("", "--category", "-c", help="类别"),
):
    """添加自定义 QA 对"""
    try:
        selector = FewShotSelector()
        new_id = selector.add_qa_pair(question, answer, category)
        console.print(f"[green]成功添加 QA 对,ID: {new_id}[/green]")

    except FewShotError as e:
        console.print(f"[red]错误: {e}[/red]")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
