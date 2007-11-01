#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, Extension

VERSION = '0.7.2'
DESCRIPTION = "Python module dependency analysis tool"
LONG_DESCRIPTION = """
modulegraph determines a dependency graph between Python modules primarily
by bytecode analysis for import statements.

modulegraph uses similar methods to modulefinder from the standard library,
but uses a more flexible internal representation, has more extensive 
knowledge of special cases, and is extensible.
"""

CLASSIFIERS = filter(None, map(str.strip,
"""                 
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: Build Tools
""".splitlines()))

setup(
    name="modulegraph",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    author="Bob Ippolito",
    author_email="bob@redivi.com",
    url="http://undefined.org/python/#modulegraph",
    license="MIT License",
    packages=['modulegraph'],
    platforms=['any'],
    install_requires=["altgraph>=0.6.7"],
    zip_safe=True,
)
