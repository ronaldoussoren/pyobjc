:layout: landing
:description: PyObjC provides bindings for Objective-C frameworks on macOS

PyObjC
======

.. rst-class:: lead

   PyObjC provides bindings to most Objective-C frameworks on macOS, build
   upon a generic bidirectional bridge between Python and Objective-C.

   PyObjC aims to get as close as possible to having Python and a first class
   language for developing applications and scripts on macOS using Apple's high
   level system APIs.

.. container:: buttons

   `GitHub <https://github.com/ronaldoussoren/pyobjc>`_

.. tabs::
   .. tab:: Python

      .. sourcecode:: Python
         :caption: Cocoa class definition in Python

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
         :caption: Cocoa class definition in Objective-C

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
      :link: changelog
      :link-type: doc

      PyObjC 12.1 was released on 2025-11-14.  See the :doc:`changelog <changelog>` for more information.


   .. grid-item-card:: Supported Platforms
      :link: supported-platforms
      :link-type: doc

      - macOS 10.9 and later
      - Python 3.10 and later
      - x86_64 and arm64

   .. grid-item-card:: Installing PyObjC
      :link: install
      :link-type: doc

      .. sourcecode:: sh

         $ python3 -mpip \
           install -U pyobjc


.. toctree::
   :hidden:

   install
   changelog
   supported-platforms


.. grid:: 1 1 2 2
   :gutter: 2

   .. grid-item-card::

      .. toctree::
         :caption: Introduction
         :maxdepth: 1

         core/intro
         tutorials/index
         notes/framework-wrappers.rst
         examples/index
         core/introspecting

   .. grid-item-card::

      .. toctree::
         :caption: Technical Notes
         :maxdepth: 1

         notes/free-threading
         notes/instantiating
         core/super
         notes/exceptions
         notes/fsref
         core/protocols
         core/blocks
         notes/ctypes
         core/kvo
         core/serializing
         notes/codesigning
         deprecations

   .. grid-item-card::

      .. toctree::
         :caption: Internals
         :maxdepth: 2

         metadata/index
         core/typemapping
         core/type-wrapper


   .. grid-item-card::

      .. toctree::
         :caption: API Documentation
         :maxdepth: 1

         api/module-objc
         api/module-objc.simd
         api/module-PyObjCTools
         api/coregraphics-context-managers
         api/threading-helpers
         api/module-PyObjCTools.AppCategories
         api/module-PyObjCTools.FndCategories
         apinotes

   .. grid-item-card::

      .. toctree::
         :caption: Development
         :maxdepth: 2

         team
         release-workflow
         dev/index

   .. grid-item-card::

      .. toctree::
         :caption: Historical
         :maxdepth: 1

         xcode
         notes/using-nsxpcinterface
