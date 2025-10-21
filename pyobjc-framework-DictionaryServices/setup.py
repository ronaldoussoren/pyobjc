"""
Deprecated wrappers for the "DictionaryServices" framework on macOS 10.5 or later.

Use package "CoreServices" instead.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup  # noqa: E402

VERSION = "12.0"

setup(
    name="pyobjc-framework-DictionaryServices",
    description="Wrappers for the framework DictionaryServices on macOS",
    min_os_level="10.5",
    packages=["DictionaryServices"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-CoreServices>=" + VERSION,
    ],
    long_description=__doc__,
)
