Welcome to the PyObjC repository
================================

.. image:: https://github.com/ronaldoussoren/pyobjc/workflows/pre-commit/badge.svg


.. note::

   The master branch is currently used for feature development, as such it should
   be considered unstable. Use the latest release instead.


Introduction
------------

This repository contains a number of Python packages/distributions
for the PyObjC project:

* 'pyobjc': a meta package that is used for easy installation
  using easy_install or pip

* 'pyobjc-core': the actual bridge

* 'pyobjc-framework-*': wrappers for specific frameworks (or sets of frameworks)


Supported Python versions
-------------------------

PyObjC is regularly tested using Python 3.6, 3.7 and 3.8.

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

  $ git clone https://github.com/ronaldoussoren/pyobjc

Then perform the installation::

  $ pythonX.Y pyobjc/install.py
