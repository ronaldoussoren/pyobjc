:layout: landing

Introduction
============

PyObjC provides bindings to most Objective-C frameworks on macOS, build
upon a generic bidirectional bridge between Python and Objective-C.

PyObjC aims to get as close as possible to having Python and a first class
language for developing applications and scripts on macOS using Apple's high
level system APIs.

.. tabs::

   .. tab:: Python

      .. sourcecode:: Python

         from Foundation import NSObject
         from objc import super

         class MyCocoaObject(NSObject):
             def initWithX_y_(self, x, y):
                 self = super().init()
                 if self is None:
                     return None
                 self.x = x
                 self.y = y
                 return self

   .. tab:: Objective-C

      .. sourcecode:: objective-c

         #import <Foundation/Foundation.h>

         @interfae MyCocoaObject : NSObject {
            int x, y;
         }
         -(instancetype)initWithX:(int)x y:(int)y;
         @end

         @implementation MyCocoaObject
         -(instancetype)initWithX:(int)xValue y:(int)yValue
         {
            self = [super init];
            if (!self) return nil;

            x = xValue;
            y = yValue;
            return self;
         }

.. grid:: 1 1 2 3
   :gutter: 2
   :padding:  0
   :class-row: surface

   .. grid-item-card:: Release Info

      PyObjC 10.2 was released on 2024-03-16.  See the :doc:`changelog <changelog>` for more information.


   .. grid-item-card:: Supported Platforms
      :link: supported-platforms
      :link-type: doc

      - macOS 10.9 or later
      - Python 3.7 or later
      - x86_64 and arm64

   .. grid-item-card:: Installing PyObjC
      :link: install
      :link-type: doc

      .. sourcecode:: sh

         $ python3 -mpip install pyobjc


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
   core/super
   metadata/index
   tutorials/index
   notes/exceptions
   notes/instantiating
   notes/quartz-vs-coregraphics
   notes/using-nsxpcinterface
   notes/ctypes
   examples/index
   notes/framework-wrappers.rst
   notes/codesigning.rst
   apinotes
   deprecations
   team
   release-workflow
   supported-platforms


API documentation
=================

.. toctree::
   :maxdepth: 2

   api/index
   api/coregraphics-context-managers
   api/threading-helpers
   api/module-PyObjCTools.AppCategories
   api/module-PyObjCTools.FndCategories


Historical documents
====================

.. toctree::
   :maxdepth: 1

   xcode
   core/objc-gc


PyObjC Development
===================

PyObjC development is hosted at GitHub, in particular at <https://github.com/ronaldoussoren/pyobjc/>.

Important resources:

* `Issue tracker <https://github.com/ronaldoussoren/pyobjc/issues>`_

* `PyObjC-dev mailing list <https://sourceforge.net/projects/pyobjc/lists/pyobjc-dev>`_

  A low-volume mailinglist for PyObjC development.

* `Mailing list for the PythonMac SIG <https://www.python.org/community/sigs/current/pythonmac-sig/>`_

  A mailing list for anyone developing with Python on macOS.

* `Repository browser <https://github.com/ronaldoussoren/pyobjc>`_

* Creating a checkout of the repository:

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
