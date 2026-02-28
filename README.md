# Few-Shot Selector

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> Dynamically select the most relevant few-shot examples to solve the rigid prompt problem

> 动态选择最相关的 few-shot 示例，解决 Prompt 僵化问题

---

## English

### Core Problem

When using LLMs, we typically provide fixed examples (few-shot examples) in prompts to guide model output. However:
- When users ask about "sports", the prompt may contain "programming" examples, leading to poor results
- Manually maintaining multiple prompt templates is tedious and difficult to scale
- Unable to dynamically adjust examples based on user input

### Solution

Use **vector similarity matching** technology to dynamically retrieve the most relevant examples based on user questions and automatically generate optimal prompts.

### Features

- 🚀 Dynamic example selection based on semantic similarity
- 💾 Lightweight vector database (ChromaDB)
- 🔍 Local embedding model (no API calls required)
- 🎨 Modern CLI with rich formatting
- 📦 Easy to extend with custom QA pairs

### Quick Start

#### Installation

```bash
pip install few-shot-selector
```

#### Usage

```bash
# Initialize database (first time use)
few-shot-selector init

# Query similar examples
few-shot-selector query "How to read a CSV file?"

# View database statistics
few-shot-selector stats

# Add custom QA pair
few-shot-selector add "question" "answer"
```

### Project Structure

```
few-shot-selector/
├── src/
│   └── few_shot_selector/
│       ├── cli.py          # CLI interface
│       ├── core.py         # Core vector retrieval logic
│       ├── utils.py        # Utility functions
│       └── data/           # QA example data
├── tests/                  # Unit tests
├── pyproject.toml          # Project configuration
└── README.md
```

### Tech Stack

- **ChromaDB**: Lightweight vector database
- **Sentence Transformers**: Local embedding model (all-MiniLM-L6-v2)
- **Rich**: Terminal formatting and styling
- **Typer**: Modern CLI framework

### Development

```bash
# Clone repository
git clone https://github.com/PerryLink/few-shot-selector.git
cd few-shot-selector

# Install dependencies
pip install poetry
poetry install

# Run tests
poetry run pytest

# Code formatting
poetry run black .
poetry run ruff check .
```

### License

Apache License 2.0 - see [LICENSE](LICENSE) file for details

Copyright 2026 Chance Dean <novelnexusai@outlook.com>

---

## 中文

### 核心痛点

在使用 LLM 时，我们通常在 Prompt 中提供固定的示例（few-shot examples）来引导模型输出。但是：
- 用户问关于"体育"的问题时，Prompt 里可能是"编程"的例子，导致效果不佳
- 手动维护多套 Prompt 模板既繁琐又难以扩展
- 无法根据用户输入动态调整示例

### 解决方案

使用**向量相似度匹配**技术，根据用户问题动态检索最相关的示例，自动生成最优 Prompt。

### 核心特性

- 🚀 基于语义相似度的动态示例选择
- 💾 轻量级向量数据库（ChromaDB）
- 🔍 本地 Embedding 模型（无需 API 调用）
- 🎨 现代化 CLI 界面，支持丰富格式化
- 📦 易于扩展自定义 QA 对

### 快速开始

#### 安装

```bash
pip install few-shot-selector
```

#### 使用

```bash
# 初始化数据库（首次使用）
few-shot-selector init

# 查询相似示例
few-shot-selector query "如何读取 CSV 文件？"

# 查看数据库统计
few-shot-selector stats

# 添加自定义 QA 对
few-shot-selector add "问题" "答案"
```

### 项目结构

```
few-shot-selector/
├── src/
│   └── few_shot_selector/
│       ├── cli.py          # CLI 接口
│       ├── core.py         # 核心向量检索逻辑
│       ├── utils.py        # 工具函数
│       └── data/           # QA 示例数据
├── tests/                  # 单元测试
├── pyproject.toml          # 项目配置
└── README.md
```

### 技术栈

- **ChromaDB**: 轻量级向量数据库
- **Sentence Transformers**: 本地 Embedding 模型（all-MiniLM-L6-v2）
- **Rich**: 终端格式化和样式
- **Typer**: 现代化 CLI 框架

### 开发

```bash
# 克隆仓库
git clone https://github.com/PerryLink/few-shot-selector.git
cd few-shot-selector

# 安装依赖
pip install poetry
poetry install

# 运行测试
poetry run pytest

# 代码格式化
poetry run black .
poetry run ruff check .
```

### 许可证

Apache License 2.0 - 详见 [LICENSE](LICENSE) 文件

版权所有 2026 Chance Dean <novelnexusai@outlook.com>
