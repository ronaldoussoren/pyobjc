"""
Compatibility module
"""
import warnings

warnings.warn(
    "import PyObjCTools.NibClassBuilder instead of AppKit.NibClassBuilder",
    DeprecationWarning)

from PyObjCTools.NibClassBuilder import *


