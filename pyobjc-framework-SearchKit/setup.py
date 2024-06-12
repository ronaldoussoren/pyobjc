"""
Deprecated wrappers for the "SearchKit" framework on macOS.

Use the CoreServices package instead.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup  # noqa: E402

VERSION = "10.3.2"

setup(
    name="pyobjc-framework-SearchKit",
    description="Wrappers for the framework SearchKit on macOS",
    min_os_level="10.5",
    packages=["SearchKit"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-CoreServices>=" + VERSION,
    ],
    long_description=__doc__,
)
