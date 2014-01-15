Welcome to the PyObjC repository
================================

This repository contains a number of Python packages/distributions
for the PyObjC project:

* 'pyobjc': a meta package that is used for easy installation
  using easy_install or pip

* 'pyobjc-core': the actual bridge

* 'pyobjc-framework-*': wrappers for specific frameworks (or sets of frameworks)

* 'pyobjc-xcode': Mostly unmaintained Xcode templates for Python projects


Supported Python versions
-------------------------

PyObjC is regularly tested using Python 2.7, 3.3 and 3.4.

I'm also regularly testing using the development version of Python,
although support for that might be broken when there are large changes in
the implementation.

PyPy, Jython and IronPython are not supported, and it is unlikely that this
will change anytime soon.

Installing
----------

The easiest way to install PyObjC from the repository is by using the
"install.py" script next to this file.

First create a check-out::

  $ hg clone https://bitbucket.org/ronaldoussoren/pyobjc

Then perform the installation::

  $ pythonX.Y pyobjc/install.py


