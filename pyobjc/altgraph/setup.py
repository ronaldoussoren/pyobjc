#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, Extension

VERSION = '0.6.8'
DESCRIPTION = "Python graph (network) package"
LONG_DESCRIPTION = """
altgraph is a fork of graphlib: a graph (network) package for constructing
graphs, BFS and DFS traversals, topological sort, shortest paths, etc. with
graphviz output.

altgraph includes some additional usage of Python 2.3+ features and
enhancements related to modulegraph and macholib.
"""

CLASSIFIERS = filter(None, map(str.strip,
"""                 
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Scientific/Engineering :: Mathematics
Topic :: Scientific/Engineering :: Visualization
""".splitlines()))

setup(
    name="altgraph",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    author="Bob Ippolito",
    author_email="bob@redivi.com",
    url="http://undefined.org/python/#altgraph",
    license="MIT License",
    packages=['altgraph'],
    platforms=['any'],
    zip_safe=True,
)
