#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, Extension

VERSION = '1.2.1'
DESCRIPTION = "Mach-O header analysis and editing"
LONG_DESCRIPTION = """
macholib can be used to analyze and edit Mach-O headers, the executable
format used by Mac OS X.

It's typically used as a dependency analysis tool, and also to rewrite dylib
references in Mach-O headers to be @executable_path relative.

Though this tool targets a platform specific file format, it is pure python
code that is platform and endian independent.
"""

CLASSIFIERS = filter(None, map(str.strip,
"""                 
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Operating System :: MacOS :: MacOS X
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: Build Tools
""".splitlines()))

setup(
    name="macholib",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    author="Bob Ippolito",
    author_email="bob@redivi.com",
    url="http://undefined.org/python/#macholib",
    license="MIT License",
    packages=['macholib'],
    platforms=['any'],
    install_requires=["altgraph>=0.6.6"],
    zip_safe=True,
    entry_points=dict(
        console_scripts=[
            'macho_find = macholib.macho_find:main',
            'macho_standalone = macholib.macho_standalone:main',
        ],
    ),
)
