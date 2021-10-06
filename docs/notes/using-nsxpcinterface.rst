Using NSXPCInterface from Python
================================

The Foundation class ``NSXPCInterface`` requires an Objective-C
protocol to define the API of the interface. Those protocols
cannot be defined in Python using :class:`objc.formal_protocol`
because the Cocoa class requires some data ("extended method signatures")
that cannot be registered using the public API for the Objectie-C
runtime.

If you do try to use a protocol defined in Python with ``NSXPCInterface``
you'll get an error similar to this:

.. sourcecode:: none

       NSInvalidArgumentException - NSXPCInterface: Unable to get extended method signature from Protocol data (MyProtocol / runCommand:withReply:). Use of clang is required for NSXPCInterface.


This means that any custom protocols that will be used
with ``NSXPCInterface`` need to be defined in a C extension which
is compiled using the clang compiler (the compiler used by Xcode).

The compiler will elide protocol information from the binary for
all protocols that aren't actually used. To ensure that the protocol
information is included add an (unused) function that appears to
use the protocol, for example:

.. sourcecode:: objc

   static void __attribute__((__unused__))
   use_protocol(void)
   {
       printf("%p\n", @protocol(MyProtocol));
   }


A template extension
--------------------

The code below is a simple complete extension for exposing a
protocol.

.. sourcecode:: python
   :caption: setup.py

   from setuptools import setup, Extension

   setup(
      name="sample",
      version="0.1",
      ext_modules=[
        Extension(
            "protocol_ext",
            ["protocol_ext.m"],
            extra_link_args=["-framework", "Cocoa"],
            py_limited_api=True,
        )
      ]
   )

.. sourcecode:: objc
   :caption: protocol_ext.m

   #define Py_LIMITED_API 0x03060000
   #define PY_SSIZE_T_CLEAN
   #include "Python.h"
   #import <Cocoa/Cocoa.h>

   @protocol MyProtocol
   -(id)doSomething:(NSString*)name withReply:(int (^)(NSObject*))completion;
   @end


   static void __attribute__((__unused__))
   use_protocol(void)
   {
       printf("%p\n", @protocol(MyProtocol));
   }

   static PyMethodDef mod_methods[] = {
       {0, 0, 0, 0} /* sentinel */
   };

   static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
        "protocol_ext",
        NULL,
        0,
        mod_methods,
        NULL,
        NULL,
        NULL,
        NULL};

   PyObject* PyInit_protocol_ext(void);

   PyObject* __attribute__((__visibility__("default")))
   PyInit_protocol_ext(void)
   {
       PyObject* m;
       m = PyModule_Create(&mod_module);
       if (!m) { return NULL; }

       return m;
   }
