/* Copyright (c) 1996,97,98 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: ObjCMethod.m,v
 * Revision: 1.9
 * Date: 1998/08/18 15:35:54
 *
 * Created Mon Oct 28 12:33:43 1996.
 */

#include "ObjC.h"
#include "objc_support.h"

#import  <Foundation/NSInvocation.h>     /* sdm7g -- chg #include to #import */
#import <Foundation/NSMethodSignature.h> /* sdm7g */ 

ObjCMethod *
ObjCMethod_new_with_selector (ObjCObject *obj, SEL sel)
{
  ObjCMethod *self = PyObject_NEW (ObjCMethod, &ObjCMethod_Type);
  NSMethodSignature *aSignature;
  
  if (!self)
    return NULL;

  aSignature = [obj->oc_object methodSignatureForSelector:sel];
  if (!aSignature)
    {
      char error_msg[100];

      sprintf (error_msg, "receiver does not respond to method"); //XXX better msg
      PyErr_SetString (ObjC_Error, error_msg);
      return NULL;
    }
  
  self->inv = [NSInvocation invocationWithMethodSignature:aSignature];
  [self->inv retain];
  
  [self->inv setSelector:sel];
  if (obj)
    [self->inv setTarget:obj->oc_object];
  
  return self;
}

ObjCMethod *
ObjCMethod_new_with_name (ObjCObject *obj, const char *meth_name)
{
  id mName = [NSString stringWithCString:meth_name];
  SEL sel = NSSelectorFromString (mName);

  if (!sel)
    {
      char error_msg[100];

      sprintf (error_msg, "Unknown method name: `%s'", meth_name);
      PyErr_SetString (ObjC_Error, error_msg);
      return NULL;
    }
  else
    return ObjCMethod_new_with_selector (obj, sel);
}

static void
ObjCMethod_dealloc (ObjCMethod *self)
{
  [self->inv release];
  PyMem_DEL (self);
}

static PyObject *
ObjCMethod_repr (ObjCMethod *self)
{
  char buffer[512];

  sprintf (buffer, "<Objective-C method `%s' on %s at %lx>",
	   [[self->inv description] cString],
	   [[[self->inv target] description] cString], (long) self);
  return PyString_FromString (buffer);
}

static char ObjCMethod_pack_argument_doc[] =
FUNDOC("Pack one of the method's arguments into an object suitable to be used in a\n\
succeding call of the method, possibly initialized with a value. This is valid\n\
only for pointer-argument, aka pass-by-reference.",
       ".pack_argument (N, VALUE)",
       "N\t: apply to the Nth argument of this method\n\
\t\tVALUE\t: optional initializer value",
       "An ObjCPointer instance");
static PyObject *
ObjCMethod_pack_argument (ObjCMethod *meth, PyObject *args)
{
  unsigned int argn;
  PyObject *value = NULL;
  
  if (PyArg_ParseTuple (args, "i|O;argument number and a facultative initializator object", &argn, &value))
    {
      NSMethodSignature *methinfo;
      unsigned int argcount;
      
      methinfo = [meth->inv methodSignature];
      argcount = [methinfo numberOfArguments];
  
      if (argn < argcount-2)
        {
#ifdef MACOSX
          const char *type = [methinfo getArgumentTypeAtIndex:argn+2];
#else
          const char *type = [methinfo argumentInfoAtIndex:argn+2].type;
#endif
          unsigned int size;
          char *buffer;

          if (*type != _C_PTR)
            {
              PyErr_SetString (ObjC_Error, ".pack_argument() can be used on pointer-argument only");
              return NULL;
            }

          size = objc_sizeof_type (type+1);
          
          buffer = alloca (size);
          if (value)
            {
              const char *error = depythonify_c_value (type+1, value, &buffer);

              if (error)
                {
                  const char *typeend = objc_skip_typespec (type+1);
#define ERRMSG "expected %s for argument %d: its type is `%.*s'"
                  char errmsg[sizeof ERRMSG + strlen (error) + typeend-type];

                  sprintf (errmsg, ERRMSG, error, argn, (int) (typeend-type-1), type+1);
                  PyErr_SetString (ObjC_Error, errmsg);
#undef ERRMSG
                  return NULL;
                }
            }
          else
            memset (buffer, 0, size);
          
          return (PyObject *) ObjCPointer_new (buffer, type+1);
        }
      else
        {
          PyErr_SetString (ObjC_Error, "argument index out of range");
          return NULL;
        }
    }
  return NULL;
}

static char ObjCMethod_unpack_argument_doc[] =
FUNDOC("Translate a pass-by-reference argument' content into the Python representation.",
       ".unpack_argument (N, VALUE)",
       "N\t: apply to the Nth argument of this method\n\
\t\tVALUE\t: its packed value",
       "A Python object");
static PyObject *
ObjCMethod_unpack_argument (ObjCMethod *meth, PyObject *args)
{
  unsigned int argn;
  PyObject *value;
  
  if (PyArg_ParseTuple (args, "iO;argument number and the value to unpack (a string or ObjCPointer instance)",
                        &argn, &value))
    {
      NSMethodSignature *methinfo;
      unsigned int argcount;
      
      methinfo = [meth->inv methodSignature];
      argcount = [methinfo numberOfArguments];
  
      if (argn < argcount-2)
        {

#ifdef NOTOSX
          const char *type = [methinfo argumentInfoAtIndex:argn+2].type;
#else
          const char *type = [methinfo getArgumentTypeAtIndex:argn+2];
#endif
          char *buffer;

          if (*type != _C_PTR)
            {
              PyErr_SetString (ObjC_Error, ".unpack_argument() can be used on pointer-argument only");
              return NULL;
            }

          type++;
          if (PyString_Check (value))
            {
              unsigned int expected_size = objc_sizeof_type (type);

              if (expected_size != PyString_Size (value))
                {
#define ERRMSG "a string of size %d instead of %d"
                  char errmsg[sizeof (ERRMSG)+6+6];
                  
                  sprintf (errmsg, ERRMSG, expected_size, PyString_Size (value));
                  PyErr_SetString (ObjC_Error, errmsg);
                  return NULL;
#undef ERRMSG
                }

              buffer = PyString_AS_STRING ((PyStringObject *) value);
            }
          else if (ObjCPointer_Check (value))
            {
              const char *typeend = objc_skip_typespec (type);
              const char *vtype = PyString_AS_STRING (((ObjCPointer *) value)->type);
              
              if (strncmp (vtype, type, typeend - type))
                {
#define ERRMSG "a pointer to `%.*s' instead of `%s'"
                  char errmsg[sizeof (ERRMSG)+
                             (typeend-type)+
                             PyString_Size ((PyObject *) ((ObjCPointer *) value)->type)];
                  
                  sprintf (errmsg, ERRMSG, (int) (typeend-type), type, vtype);

                  PyErr_SetString (ObjC_Error, errmsg);
                  return NULL;
#undef ERRMSG
                }

              buffer = ((ObjCPointer *) value)->ptr;
            }
          else
            {
              PyErr_BadArgument();
              return NULL;
            }
          return pythonify_c_value (type, buffer, meth);
        }
      else
        {
          PyErr_SetString (ObjC_Error, "argument index out of range");
          return NULL;
        }
    }
  return NULL;
}

static PyMethodDef ObjCMethod_methods[] =
{
  { "pack_argument",    (PyCFunction) ObjCMethod_pack_argument, METH_VARARGS, ObjCMethod_pack_argument_doc },
  { "unpack_argument",  (PyCFunction) ObjCMethod_unpack_argument,       METH_VARARGS, ObjCMethod_unpack_argument_doc },
  { 0, 0, 0, 0 }
};
          
static PyObject *
ObjCMethod_getattr (ObjCMethod *self, char *name)
{
  PyObject *method;
  
  method = Py_FindMethod (ObjCMethod_methods, (PyObject *) self, name);
  if (method)
    return method;
  else
    {
      PyErr_Clear();
      
      if (!strcmp (name, "name"))
        return PyString_FromString ((char *) [NSStringFromSelector ([self->inv selector]) cString]);
      else if (!strcmp (name, "__members__"))
        {
          const char *members[] = { "name" };
          PyObject *list;
          unsigned int idx;

          idx = sizeof (members) / sizeof (members[0]);
          list = PyList_New (idx);
          while (idx--)
            PyList_SetItem (list, idx, PyString_FromString ((char *) members[idx]));
          return list;
        }
    }

  PyErr_SetString (PyExc_AttributeError, name);
  return NULL;
}

static PyObject *
ObjCMethod_call (ObjCMethod *self, PyObject *args, PyObject *kw)
{
  PyObject *retobject = execute_and_pythonify_objc_method (self, args);

  return retobject;
}

PyTypeObject ObjCMethod_Type =
{
  PyObject_HEAD_INIT(&PyType_Type)
  0,                                          /*ob_size*/
  "ObjCMethod",                               /*tp_name*/
  sizeof(ObjCMethod),                         /*tp_basicsize*/
  0,                                          /*tp_itemsize*/
  
  /* methods */
  (destructor) ObjCMethod_dealloc,            /*tp_dealloc*/
  (printfunc) 0,                              /*tp_print*/
  (getattrfunc) ObjCMethod_getattr,           /*tp_getattr*/
  (setattrfunc) 0,                            /*tp_setattr*/
  (cmpfunc) 0,                                /*tp_compare*/
  (reprfunc) ObjCMethod_repr,                 /*tp_repr*/
  0,                                          /*tp_as_number*/
  0,                                          /*tp_as_sequence*/
  0,                                          /*tp_as_mapping*/
  (hashfunc) 0,                               /*tp_hash*/
  (ternaryfunc) ObjCMethod_call,              /*tp_call*/
  (reprfunc) 0,                               /*tp_str*/
  (getattrofunc) 0,                           /*tp_getattro*/
  (setattrofunc) 0,                           /*tp_setattro*/

  /* Space for future expansion */
  0L,0L,
  
  "Wrapper around Objective-C selector"       /* Documentation string */
};
