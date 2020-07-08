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

PyObjC 6.2.2 was released on 2020-07-08. See the :doc:`changelog <changelog>` for more information. PyObjC 6.2.2 supports Python 3.6 and later.

PyObjC 5.3 was released on 2019-10-16. See the :doc:`changelog <changelog>` for more information.

Supported platforms
-------------------

PyObjC supports Python 3.6 ("CPython") or later on macO 10.9 or later.

The binary wheels support x86_64, building from source should still work
for users that still require 32-bit code.

Unsupported platforms
---------------------

The following platforms are not supported:

* Operating systems other than macOS, such as Windows, Linux and iOS

  PyObjC provides interfaces for the system APIs on macOS and as such
  cannot support Linux and Windows.

  It might be possible to support iOS, but that will require significant
  engineering, as well as making sure that PyObjC's implementation is
  compatible with AppStore rules (in particular the usage of dynamic
  code generation).

* Python 2.x

  The latest releaes of PyObjC that supports Python 2.7 is version 5.3. Note
  that this version is no longer maintained.

* Alternative Python implementations, like PyPy and Jython.

  PyObjC uses some low-level trickery that is not supported by those
  implementations.



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

PyObjC development is hosted at GitHub, in particular at <https://github.com/ronaldoussoren/pyobjc/>.

Important resources:

* `Issue tracker <https://github.com/ronaldoussoren/pyobjc/issues>`_

* `PyObjC-dev mailing list <https://sourceforge.net/projects/pyobjc/lists/pyobjc-dev>`_

  A low-volume mailinglist for PyObjC development.

* `Mailing list for the PythonMac SIG <https://www.python.org/community/sigs/current/pythonmac-sig/>`_

  A mailing list for anyone developing with Python on macOS.

* `Repository browser <https://github.com/ronaldoussoren/pyobjc>`_

* Creating a checkout of the respository:

  .. sourcecode:: sh

     $ git clone https://github.com/ronaldoussoren/pyobjc

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
