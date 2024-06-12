"""
Wrappers for the framework "LatentSemanticMapping" on macOS 10.5 or later.

The Latent Semantic Mapping framework supports the classification of text and
other token-based content into developer-defined categories.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks.

NOTE: Apple's documentation for this framework is very minimal at the moment,
making it very hard to actually use the framework.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup  # noqa: E402

VERSION = "10.3.2"

setup(
    name="pyobjc-framework-LatentSemanticMapping",
    description="Wrappers for the framework LatentSemanticMapping on macOS",
    min_os_level="10.5",
    packages=["LatentSemanticMapping"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
