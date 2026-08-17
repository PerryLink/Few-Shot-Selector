<div align="center">

# Few-Shot-Selector

**A CLI tool that dynamically selects the most relevant few-shot examples for LLM prompts using vector similarity.**

*Ported into [dsh-library](https://github.com/PerryLink/dsh-library) — part of the PerryLink DSH Plugin Family.*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## What it does

`few-shot-selector` stores question-answer examples in a local ChromaDB with locally computed
embeddings (`all-MiniLM-L6-v2`). Given a user question, it retrieves the most similar examples by
vector similarity and formats them into a prompt, so the few-shot examples always match the topic.

## Features

- 🚀 Semantic-similarity example selection
- 💾 Lightweight vector database (ChromaDB)
- 🔍 Local embedding model — no API calls required
- 🎨 Typer + Rich CLI
- 📦 Add custom QA pairs

## Quick start

```bash
pip install few-shot-selector

# Initialize the database on first use
few-shot-selector init
```

## Usage

```bash
# Retrieve similar examples (default 3; override with --num/-n)
few-shot-selector query "How to read a CSV file?"

# Show database statistics
few-shot-selector stats

# Add a custom QA pair (optional category via --category/-c)
few-shot-selector add "question" "answer"
```

## Development

```bash
poetry install
poetry run pytest
poetry run black .
poetry run ruff check .
```

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink
