# 旧モジュール名との互換性を維持する
import warnings

warnings.warn(
    "kplot.pltstyle is deprecated; use kplot.style instead.",
    DeprecationWarning,
    stacklevel=2,
)

from .style import (
    SetDefaultFont,
    SetLoadLatex,
    SetDefaultFigSize,
    SetDefaultSettings,
)