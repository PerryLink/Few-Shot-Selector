<div align="center">

# Few-Shot-Selector
[![Gitee](https://img.shields.io/badge/Gitee-mirror-c71d23?logo=gitee)](https://gitee.com/perrylink/few-shot-selector)

**A CLI tool that dynamically selects the most relevant few-shot examples for LLM prompts using vector similarity.**

*Ported into [dsh-library](https://github.com/PerryLink/dsh-library) — part of the PerryLink DSH Plugin Family.*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## Problem & solution

Prompts often use fixed few-shot examples, which can mismatch the user's question:

- A user asks about "sports" but the prompt contains "programming" examples, hurting results
- Manually maintaining multiple prompt templates is tedious and hard to scale
- Examples cannot be adjusted dynamically based on user input

`few-shot-selector` solves this with vector-similarity retrieval: it matches the user's question to
the most relevant stored examples and generates the prompt automatically.

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

## Project structure

```
few-shot-selector/
├── src/few_shot_selector/
│   ├── cli.py               # CLI interface
│   ├── core.py              # Core vector retrieval logic
│   ├── utils.py             # Utility functions
│   └── data/qa_examples.json  # QA example data
├── tests/                   # Unit tests
├── pyproject.toml           # Poetry configuration
└── README.md
```

## Tech stack

- **ChromaDB** — lightweight vector database
- **Sentence Transformers** — local embedding model (all-MiniLM-L6-v2)
- **Rich** — terminal formatting and styling
- **Typer** — CLI framework

## Development

```bash
git clone https://github.com/PerryLink/few-shot-selector.git
cd few-shot-selector
poetry install

poetry run pytest
poetry run black .
poetry run ruff check .
```

## Related

- [dsh-library](https://github.com/PerryLink/dsh-library) — the DSH plugin this project was ported into
- [PerryLink](https://github.com/PerryLink) — the PerryLink DSH Plugin Family

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink
