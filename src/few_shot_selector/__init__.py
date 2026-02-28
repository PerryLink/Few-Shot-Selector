"""few-shot-selector: 动态选择最相关的 few-shot 示例"""

__version__ = "0.1.0"

from .core import FewShotSelector
from .utils import FewShotError

__all__ = ["FewShotSelector", "FewShotError", "__version__"]
