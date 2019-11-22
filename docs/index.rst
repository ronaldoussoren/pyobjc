Introduction
============

The PyObjC project aims to provide a bridge between the Python and Objective-C
programming languages on macOS. The bridge is intended to be fully bidirectional, allowing
the Python programmer to take full advantage of the power provided by various
Objective-C based toolkits and the Objective-C programmer transparent access
to Python based functionality.

PyObjC not only includes the basic bridge, but also bindings to most Apple
frameworks on macOS.

The most important usage of this is writing Cocoa GUI applications on macOS
in pure Python. See our tutorial for an example of this.

Release information
-------------------

PyObjC 6.1 was released on 2019-11-06. See the :doc:`changelog <changelog>` for more information. PyObjC 6.1 supports Python 3.6 and later.

PyObjC 5.3 was released on 2019-10-16. See the :doc:`changelog <changelog>` for more information.

Supported platforms
-------------------

PyObjC supports Python 3.6 or later and does not support Python 2.
PyObjC does not support other python implementation such as PyPy and Jython.

PyObjC is regularly tested on macOS 10.14 and should work on macOS
10.9 or later for the i386 and x86_64 architectures.

PyObjC only supports macOS, and is not supported on other platforms (iOS,
Linux, ...)

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

