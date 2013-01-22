'''
Wrappers for the "CoreText" framework on MacOSX 10.5 or later. Core Text is an
advanced, low-level technology for laying out text and handling fonts. It is
designed for high performance and ease of use.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

NEWS
====

2.4
---

* The wrappers now cover all useful functionality (see the documentation
  for the exceptions)
'''
from pyobjc_setup import setup, Extension

setup(
    min_os_level='10.5',
    name='pyobjc-framework-CoreText',
    version="2.5.1",
    description = "Wrappers for the framework CoreText on Mac OS X",
    packages = [ "CoreText" ],
    ext_modules = [
            Extension('CoreText._manual',
                [ 'Modules/_manual.m' ],
                extra_link_args=['-framework', 'CoreServices'],
            ),
    ],
    setup_requires = [
        'pyobjc-core>=2.5.1',
    ],
    install_requires = [
        'pyobjc-core>=2.5.1',
        'pyobjc-framework-Cocoa>=2.5.1',
        'pyobjc-framework-Quartz>=2.5.1',
    ],
)
