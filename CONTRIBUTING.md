# Contributing to Few-Shot Selector

# 贡献指南

---

## English

### Project Status

This is currently a personal project maintained by [PerryLink](https://github.com/PerryLink). While external contributions are welcome, please note that this project is primarily developed and maintained by the owner.

### How to Report Issues

If you encounter any bugs or have feature requests:

1. Check the [existing issues](https://github.com/PerryLink/few-shot-selector/issues) to avoid duplicates
2. Create a new issue with a clear title and description
3. Include:
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (Python version, OS)
   - Relevant code snippets or error messages

### Development Environment Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/PerryLink/few-shot-selector.git
   cd few-shot-selector
   ```

2. **Install Poetry** (if not already installed)
   ```bash
   pip install poetry
   ```

3. **Install dependencies**
   ```bash
   poetry install
   ```

4. **Activate virtual environment**
   ```bash
   poetry shell
   ```

5. **Run tests**
   ```bash
   poetry run pytest
   ```

### Code Standards

This project follows **PEP 8** style guidelines:

- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters (Black formatter default)
- Use meaningful variable and function names
- Add docstrings for public functions and classes
- Write type hints where appropriate

**Automated formatting:**
```bash
# Format code with Black
poetry run black .

# Check code with Ruff
poetry run ruff check .
```

### Pull Request Process

1. **Fork the repository** and create a new branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code standards

3. **Run tests and linters**
   ```bash
   poetry run pytest
   poetry run black .
   poetry run ruff check .
   ```

4. **Commit your changes** with clear commit messages
   ```bash
   git commit -m "Add: brief description of your changes"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** with:
   - Clear title describing the change
   - Detailed description of what and why
   - Reference to related issues (if any)

### Questions?

Feel free to open an issue for any questions or reach out to:
- Email: novelnexusai@outlook.com
- GitHub: [@PerryLink](https://github.com/PerryLink)

---

## 中文

### 项目状态

这是一个由 [PerryLink](https://github.com/PerryLink) 个人维护的项目。虽然欢迎外部贡献，但请注意该项目主要由所有者开发和维护。

### 如何报告问题

如果您遇到任何 bug 或有功能请求：

1. 检查[现有 issues](https://github.com/PerryLink/few-shot-selector/issues) 避免重复
2. 创建新 issue，包含清晰的标题和描述
3. 包括：
   - 重现步骤（针对 bug）
   - 预期行为 vs 实际行为
   - 您的环境（Python 版本、操作系统）
   - 相关代码片段或错误信息

### 开发环境搭建

1. **克隆仓库**
   ```bash
   git clone https://github.com/PerryLink/few-shot-selector.git
   cd few-shot-selector
   ```

2. **安装 Poetry**（如果尚未安装）
   ```bash
   pip install poetry
   ```

3. **安装依赖**
   ```bash
   poetry install
   ```

4. **激活虚拟环境**
   ```bash
   poetry shell
   ```

5. **运行测试**
   ```bash
   poetry run pytest
   ```

### 代码规范

本项目遵循 **PEP 8** 风格指南：

- 使用 4 个空格缩进（不使用 tab）
- 最大行长度：88 字符（Black 格式化器默认值）
- 使用有意义的变量和函数名
- 为公共函数和类添加文档字符串
- 适当使用类型提示

**自动格式化：**
```bash
# 使用 Black 格式化代码
poetry run black .

# 使用 Ruff 检查代码
poetry run ruff check .
```

### Pull Request 流程

1. **Fork 仓库**并创建新分支
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **进行修改**，遵循代码规范

3. **运行测试和检查工具**
   ```bash
   poetry run pytest
   poetry run black .
   poetry run ruff check .
   ```

4. **提交更改**，使用清晰的提交信息
   ```bash
   git commit -m "Add: 简要描述您的更改"
   ```

5. **推送到您的 fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **创建 Pull Request**，包含：
   - 描述更改的清晰标题
   - 详细说明做了什么以及为什么
   - 引用相关 issues（如有）

### 有问题？

欢迎通过以下方式提问或联系：
- 邮箱：novelnexusai@outlook.com
- GitHub：[@PerryLink](https://github.com/PerryLink)
