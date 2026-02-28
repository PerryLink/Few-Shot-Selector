"""工具函数测试"""

import pytest
from few_shot_selector.utils import validate_qa_pair, FewShotError


def test_validate_qa_pair():
    """测试QA对验证"""
    assert validate_qa_pair("问题", "答案") is True
    assert validate_qa_pair("", "答案") is False
    assert validate_qa_pair("问题", "") is False
    assert validate_qa_pair("  ", "  ") is False


def test_few_shot_error():
    """测试自定义异常"""
    with pytest.raises(FewShotError):
        raise FewShotError("测试错误")
