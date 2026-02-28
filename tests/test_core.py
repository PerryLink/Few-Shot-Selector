"""核心功能测试"""

import pytest
from few_shot_selector.core import FewShotSelector
from few_shot_selector.utils import DatabaseNotInitializedError


def test_selector_initialization():
    """测试选择器初始化"""
    selector = FewShotSelector(db_path="./.test_chroma_db")
    assert selector is not None


def test_search_empty_database():
    """测试空数据库查询"""
    selector = FewShotSelector(db_path="./.test_chroma_db")
    with pytest.raises(DatabaseNotInitializedError):
        selector.search_similar("测试问题")


def test_add_and_search():
    """测试添加和搜索"""
    selector = FewShotSelector(db_path="./.test_chroma_db")

    qa_pairs = [
        {
            "id": 1,
            "question": "如何使用Python？",
            "answer": "Python是一种编程语言",
            "category": "编程",
            "tags": ["python"]
        }
    ]

    selector.initialize_database(qa_pairs)
    results = selector.search_similar("Python教程", n_results=1)

    assert len(results) == 1
    assert "Python" in results[0]["question"]


def test_format_prompt():
    """测试Prompt格式化"""
    selector = FewShotSelector(db_path="./.test_chroma_db")

    examples = [
        {
            "question": "问题1",
            "answer": "答案1"
        }
    ]

    prompt = selector.format_prompt("新问题", examples)
    assert "问题1" in prompt
    assert "答案1" in prompt
    assert "新问题" in prompt
