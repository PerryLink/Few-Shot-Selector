<div align="center">

# Few-Shot-Selector

**基于向量相似度动态选择最相关 few-shot 示例的 CLI 工具。**

*已移植到 [dsh-library](https://github.com/PerryLink/dsh-library) —— PerryLink DSH 插件家族的一员。*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## 功能简介

`few-shot-selector` 使用本地 Embedding 模型（`all-MiniLM-L6-v2`）将问答示例存入本地 ChromaDB。
给定用户问题后，它按向量相似度检索最相似的示例并格式化为 Prompt，使 few-shot 示例始终贴合主题。

## 特性

- 🚀 基于语义相似度的示例选择
- 💾 轻量级向量数据库（ChromaDB）
- 🔍 本地 Embedding 模型，无需调用 API
- 🎨 Typer + Rich 的现代化 CLI
- 📦 支持添加自定义问答对

## 快速开始

```bash
pip install few-shot-selector

# 首次使用时初始化数据库
few-shot-selector init
```

## 使用方法

```bash
# 检索相似示例（默认 3 条，可用 --num/-n 调整）
few-shot-selector query "如何读取 CSV 文件？"

# 查看数据库统计信息
few-shot-selector stats

# 添加自定义问答对（可用 --category/-c 指定类别）
few-shot-selector add "问题" "答案"
```

## 开发

```bash
poetry install
poetry run pytest
poetry run black .
poetry run ruff check .
```

## 许可证

[Apache License 2.0](LICENSE) © 2026 PerryLink
