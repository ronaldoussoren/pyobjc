/* Copyright (c) 1996,97,98 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: ObjC.m,v
 * Revision: 1.38
 * Date: 1998/08/18 15:41:13
 *
 * Created Tue Jun 18 12:28:42 1996.
 */

/* Long time ago, Jon M. Kutemeier wrote a module to interface Python
   with Objective-C and for a while Guido van Rossum "revamped and
   maintained" it. Sadly, on Mon, 22 Jul 1996 Guido announced the he
   will drop that module from the Python distribution. Since I'm a
   NeXTSTEP fan(atic), I considered that a bad news: for months I dreamed
   about working on its beautiful UI from Python; more than that, the
   two languages are so similar that Objective-C may be viewed as the
   compiled cousin of Guido's creation, at least while we all wait for
   a Python compiler...

   So I rewrote it: it provides an easier way of sending messages to
   Objective-C objects, and (will) support(s) the GNU Objective-C runtime.

   Now I just hope Guido will reconsider his decision... */

#include "ObjC.h"
#include "objc_support.h"
#include "osdefs.h"

#ifndef STRINGIFY               // GNUstep defines it.
#define STRINGIFY(a) _STRINGIFY(a)
#define _STRINGIFY(a) #a
#endif

static char ObjC_doc[] = "\
Objective-C Interface module Version " STRINGIFY(PyObjC_VERSION) ".\n\
Copyright (C) 1996,97,98 - Lele Gaifax <lele@seldati.it>\n\n\
This module implements an Objective-C interface layer, allowing the use\n\
of Objective-C functionalities from Python scripts.\n\n\
You can access any known Objective-C class as a member of the `.runtime'\n\
object. The Python idiom ``ClassName()'' gets translated in the equivalent\n\
Objective-C ``[[ClassName alloc] init]''.\n\n\
You can use specialized initializers by specifying the name of the ``init''\n\
selector you want as a keyword parameter of the same name, as in\n\
\tma=ObjC.runtime.NSMutableArray (10, init='initWithCapacity:')\n\
Since Python has a different calling syntax, Objective-C method names\n\
change slightly: given the method ``-initId:(int)i andName:(NSString *)n''\n\
you can call it within Python as ``o.initId_andName_ (1, \"Lele Gaifax\")''.\n\
In other words, if the signature of an Objective-C method is\n\
`someMethod:withSecondArg:andAnother:', which takes three arguments, the\n\
Python equivalent results by replacing each colon `:' with an underscore\n\
`_', then feeding the arguments in row, as usual.\n\
";

static char ObjC_lookup_class_doc[] =
FUNDOC("Locate a class in the Objective-C runtime",
       ".lookup_class (CLASS)",
       "CLASS\t: the name of an Objective-C class",
       "An ObjCObject wrapping the given class");
static PyObject *
ObjC_lookup_class (PyObject *self, PyObject *args)
{
  char *classname;
  id    class;

  if (!PyArg_ParseTuple (args, "s;class name", &classname))
    return NULL;

  if (!(class = LOOKUPCLASS(classname)))
    {
#define ERRMSG "Objective-C class `%s' is unknown to the runtime"
      char errmsg[sizeof ERRMSG + strlen (classname)];

      sprintf (errmsg, ERRMSG, classname);
      PyErr_SetString (ObjC_Error, errmsg);
#undef ERRMSG
      return NULL;
    }

  return (PyObject *) ObjCObject_new (class);
}

static char ObjC_make_pointer_doc[] =
FUNDOC("Cast an integer value to a generic pointer.",
       ".make_pointer (INT)",
       "INT\t: the integer value",
       "An ObjCPointer instance");
static PyObject *
ObjC_make_pointer (PyObject *self, PyObject *args)
{
  long value;

  if (PyArg_ParseTuple (args, "l;an integer", &value))
    return (PyObject *) ObjCPointer_new ((void *) value, @encode (void));

  return NULL;
}

static PyMethodDef ObjC_methods[] =
{
  { "lookup_class",             (PyCFunction) ObjC_lookup_class,        METH_VARARGS,   ObjC_lookup_class_doc },
  { "make_pointer",             (PyCFunction) ObjC_make_pointer,        METH_VARARGS,   ObjC_make_pointer_doc },
  { 0, 0, 0, 0 }
};

PyObject *ObjC_Error;
NSString *PyObjCException = @"PyObjCException";

#include "OC_PythonBundle.h"

#if 0

#include <Python/PyNSBundledModule.h>

@interface PyObjCModule : PyNSBundledModule <PyNSBundledModule>

@end

@implementation PyObjCModule

+ (void) initModule
#else
void
initpyobjc (void)
#endif
{
  PyObject *m, *d;
  extern void ObjCObject_initialize (void);

  m = Py_InitModule4 ("pyobjc", ObjC_methods, ObjC_doc, NULL, PYTHON_API_VERSION);
  d = PyModule_GetDict (m);

  ObjC_Error = PyString_FromString ("pyobjc.error");
  PyDict_SetItemString (d, "error", ObjC_Error);

  PyDict_SetItemString (d, "runtime", (PyObject *) ObjCRuntime_new());
  PyDict_SetItemString (d, "__version__", PyString_FromString(PyObjC_VERSION));

  // Force the load of these classes/categories
  [OC_PythonBundle class];
  
  ObjCObject_initialize();

  // sdm7g 2002-1-22: if -v ($PYVERBOSE) log all message sends to /tmp file
  // [see:  objc*/runtime/objc-class.m in Darwin sources]
  if (Py_VerboseFlag) instrumentObjcMessageSends(YES);
  
  if (PyErr_Occurred())
    Py_FatalError ("can't initialize module pyobjc");
  
#if defined(WITH_THREAD) && !defined(GNU_RUNTIME)
  objc_setMultithreaded (1);
#endif
}

#if 0
@end
#endif
