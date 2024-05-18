:layout: landing

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
      :link: changelog
      :link-type: doc

      PyObjC 10.2 was released on 2024-03-16.  See the :doc:`changelog <changelog>` for more information.


   .. grid-item-card:: Supported Platforms
      :link: supported-platforms
      :link-type: doc

      - macOS 10.9 and later
      - Python 3.7 and later
      - x86_64 and arm64

   .. grid-item-card:: Installing PyObjC
      :link: install
      :link-type: doc

      .. sourcecode:: sh

         $ python3 -mpip \
           install pyobjc


.. toctree::
   :hidden:

   install
   changelog
   supported-platforms


.. grid:: 1 1 2 2
   :gutter: 2

   .. grid-item-card:: Introduction

      .. toctree::
         :maxdepth: 1

         core/intro
         tutorials/index
         notes/framework-wrappers.rst
         apinotes
         examples/index
         core/introspecting

   .. grid-item-card:: Technical Notes

      .. toctree::
         :maxdepth: 1

         notes/instantiating
         core/super
         notes/exceptions
         notes/fsref
         core/protocols
         core/blocks
         notes/ctypes
         core/vector-types
         core/kvo
         core/serializing
         notes/quartz-vs-coregraphics
         notes/codesigning
         deprecations

   .. grid-item-card:: Internals

      .. toctree::
         :maxdepth: 2

         metadata/index
         core/typemapping
         core/type-wrapper

   .. grid-item-card:: Development

      .. toctree::
         :maxdepth: 2

         team
         release-workflow
         dev/index

   .. grid-item-card:: API documentation

      .. toctree::
         :maxdepth: 2

         api/index
         api/coregraphics-context-managers
         api/threading-helpers
         api/module-PyObjCTools.AppCategories
         api/module-PyObjCTools.FndCategories

   .. grid-item-card:: Historical

      .. toctree::
         :maxdepth: 1

         xcode
         core/objc-gc
         notes/using-nsxpcinterface
