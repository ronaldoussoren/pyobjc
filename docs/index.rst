Introduction
============

The PyObjC project aims to provide a bridge between the Python and Objective-C
programming languages. The bridge is intended to be fully bidirectional, allowing
the Python programmer to take full advantage of the power provided by various
Objective-C based toolkits and the Objective-C programmer transparent access
to Python based functionality.

The most important usage of this is writing Cocoa GUI applications on macOS
in pure Python. See our tutorial for an example of this.

Release information
-------------------

PyObjC 5.1.1 was released on 2018-10-31. See the :doc:`changelog <changelog>` for more information.

Supported platforms
-------------------

PyObjC is regularly tested with Python 2.7, 3.4, 3.5 and 3.6.
PyObjC does not support other python implementation such as PyPy and Jython.

PyObjC is regularly tested on macOS 10.13 and should work on macOS
10.5 or later for the i386, x86_64 and ppc architectures. PPC64 (64-bit
on PowerMac G5 or iMac G5 systems) is not supported at all.

.. note::

   PPC support, and support for versions of macOS before 10.9 is
   no longer actively developed and may be removed in future versions
   of PyObjC.

.. warning:: **Platform Removal**

   PyObjC 6, which will be released in 2019, will drop
   support for the following platforms:

   - Python 2.7
   - Python 3.4
   - PowerPC




General documentation
=====================

.. toctree::
   :maxdepth: 1

   install
   changelog
   core/intro
   core/protocols
   core/blocks
   core/vector-types
   core/typemapping
   core/fsref-fsspec
   core/type-wrapper
   core/introspecting
   core/serializing
   core/kvo
   core/objc-gc
   metadata/index
   tutorials/index
   notes/quartz-vs-coregraphics
   examples/index
   notes/framework-wrappers.rst
   apinotes
   deprecations
   team
   release-workflow
   xcode


API documentation
=================

.. toctree::
   :maxdepth: 2

   api/index
   api/coregraphics-context-managers
   api/threading-helpers
   api/module-PyObjCTools.AppCategories
   api/module-PyObjCTools.FndCategories



PyObjC Developement
===================

PyObjC development is hosted at bickbucket, in particular at <https://bitbucket.org/ronaldoussoren/pyobjc/>.

Important resources:

* `Issue tracker <https://bitbucket.org/ronaldoussoren/pyobjc/issues>`_

* `PyObjC-dev mailing list <https://sourceforge.net/projects/pyobjc/lists/pyobjc-dev>`_

  A low-volume mailinglist for PyObjC development.

* `Mailing list for the PythonMac SIG <https://www.python.org/community/sigs/current/pythonmac-sig/>`_

  A mailing list for anyone developing with Python on macOS.

* `Repository browser <https://bitbucket.org/ronaldoussoren/pyobjc/src>`_

* Creating a checkout of the respository:

  .. sourcecode:: sh

     $ hg clone https://bitbucket.org/ronaldoussoren/pyobjc pyobjc

  You can then use the "install.py" at the root of the checkout to
  install this version of PyObjC.

.. toctree::
   :maxdepth: 1
   :glob:

   dev/*


Indices and tables
==================

* :ref:`modindex`
* :ref:`search`

