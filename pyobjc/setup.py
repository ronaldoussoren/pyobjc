#!/usr/bin/env python.exe

from distutils.core import setup, Extension

sourceFiles = ["OC_PythonBundle.m",
               "OC_PythonInt.m",
               "OC_PythonObject.m",
               "OC_PythonString.m",
               "ObjC.m",
               "ObjCMethod.m",
               "ObjCObject.m",
               "ObjCPointer.m",
               "ObjCRuntime.m",
               "objc_support.m"]

try:
    setup (name = "pyobjc",
           version = "0.9",
           description = "Python<->ObjC Interoperability Module",
           author = "bbum, SteveM, many others stretching back through the reaches of time...",
           author_email = "bbum@codefab.com",
           url = "http://pyobjc.sourceforge.net/",
           ext_modules = [Extension("pyobjc", sourceFiles)],
           )
except:
    import sys
    import traceback
    traceback.print_exc()
