"""
Compatibility module
"""
import warnings

warnings.warn(
    "import PyObjCTools.Conversion instead of Foundation.Conversion",
    DeprecationWarning)

from PyObjCTools.Conversion import *
