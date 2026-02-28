"""自定义异常类和工具函数"""

import json
from pathlib import Path
from typing import List, Dict, Any


class FewShotError(Exception):
    """基础异常类"""
    pass


class DatabaseNotInitializedError(FewShotError):
    """数据库未初始化异常"""
    pass


class EmbeddingError(FewShotError):
    """Embedding 生成异常"""
    pass


def load_qa_data(file_path: str) -> List[Dict[str, Any]]:
    """加载 QA 数据"""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"QA 数据文件不存在: {file_path}")

    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_qa_pair(question: str, answer: str) -> bool:
    """验证 QA 对的有效性"""
    return bool(question.strip() and answer.strip())
