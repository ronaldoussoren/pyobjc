/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: ObjCPointer.m,v
 * Revision: 1.6
 * Date: 1998/01/04 17:59:28
 *
 * Created Mon Oct 28 12:38:18 1996.
 *
 * XXX (Ronald): How usefull is this type? 
 */

#include "pyobjc.h"
#include "objc_support.h"

static void
ObjCPointer_dealloc (ObjCPointer *self)
{
  Py_DECREF (self->type);
  PyMem_DEL (self);
}

PyDoc_STRVAR(ObjCPointer_unpack_doc,
	"Unpack the pointed value accordingly to its type.\n"
        "obj.unpack() -> value");
static PyObject *
ObjCPointer_unpack (ObjCPointer *self, PyObject *args)
{
  if (PyArg_ParseTuple (args, ""))
    {
      if (self->ptr)
        {
          const char *type = PyString_AS_STRING (self->type);

          if (!strcmp (type, @encode (void)))
            {
              PyErr_SetString (ObjCExc_error, "Cannot dereference a pointer to void");
              return NULL;
            }
          else
            return pythonify_c_value (PyString_AS_STRING (self->type),
                                      self->ptr);
        }
      else
        {
          Py_INCREF (Py_None);
          return Py_None;
        }
    }
            
  return NULL;
}

static PyMethodDef ObjCPointer_methods[] =
{
  { "unpack",   (PyCFunction) ObjCPointer_unpack,       METH_VARARGS,   ObjCPointer_unpack_doc },
  { 0, 0, 0, 0 }
};

static PyObject *
ObjCPointer_getattr (ObjCPointer *self, char *name)
{
  PyObject *method;

  method = Py_FindMethod (ObjCPointer_methods, (PyObject *) self, name);
  if (method)
    return method;
  else
    {
      PyErr_Clear();

      if (!strcmp (name, "type"))
        {
          Py_INCREF (self->type);
          return (PyObject *) self->type;
        }
      else if (!strcmp (name, "pointerAsInteger"))
        return PyInt_FromLong ((long) self->ptr);
      else if (!strcmp (name, "__members__"))
        {
          const char *members[] = { "type", "pointerAsInteger" };
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
  return method;
}
    
PyTypeObject ObjCPointer_Type =
{
  PyObject_HEAD_INIT(&PyType_Type)
  0,                                          /*ob_size*/
  "ObjCPointer",                              /*tp_name*/
  sizeof (ObjCPointer),                       /*tp_basicsize*/
  sizeof (char),                              /*tp_itemsize*/
  
  /* methods */
  (destructor) ObjCPointer_dealloc,           /*tp_dealloc*/
  (printfunc) 0,                              /*tp_print*/
  (getattrfunc) ObjCPointer_getattr,          /*tp_getattr*/
  (setattrfunc) 0,                            /*tp_setattr*/
  (cmpfunc) 0,                                /*tp_compare*/
  (reprfunc) 0,                               /*tp_repr*/
  0,                                          /*tp_as_number*/
  0,                                          /*tp_as_sequence*/
  0,                                          /*tp_as_mapping*/
  (hashfunc) 0,                               /*tp_hash*/
  (ternaryfunc) 0,                            /*tp_call*/
  (reprfunc) 0,                               /*tp_str*/
  (getattrofunc) 0,                           /*tp_getattro*/
  (setattrofunc) 0,                           /*tp_setattro*/

  /* Space for future expansion */
  0L,0L,
  
  "Wrapper around a Objective-C Pointer"      /* Documentation string */
};

ObjCPointer *
ObjCPointer_new (void *p, const char *t)
{
  unsigned int size = objc_sizeof_type (t);
  const char *typeend = objc_skip_typespec (t);
  ObjCPointer *self = PyObject_NEW_VAR (ObjCPointer, &ObjCPointer_Type, size);

  NSLog(@"ObjCPointer created: at %p of type %s", p, t);

  if (self == NULL)
    return NULL;

  self->type = (PyStringObject *) PyString_FromStringAndSize ((char *) t, typeend-t);

  if (size && p)
    memcpy ((self->ptr = self->contents), p, size);
  else
    self->ptr = p;
  
  return self;
}
