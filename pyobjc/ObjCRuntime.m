/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: ObjCRuntime.m,v
 * Revision: 1.8
 * Date: 1998/01/04 17:59:29
 *
 * Created Mon Oct 28 12:34:34 1996.
 */

#include "ObjC.h"
#include "objc_support.h"


static void
ObjCRuntime_dealloc (ObjCRuntime *self)
{
  Py_DECREF (self->classes);
  PyMem_DEL (self);
}

static char ObjCRuntime_sel_is_mapped_doc[] =
FUNDOC("Check whether the given selector is known by the Objective-C runtime.",
       ".sel_is_mapped (SELNAME)",
       "SELNAME\t: name of the selector",
       "True if it is known, False otherwise");
static PyObject *
ObjCRuntime_sel_is_mapped (ObjCRuntime *self, PyObject *args)
{
  char *selname;

  if (PyArg_ParseTuple (args, "s;selector name", &selname))
    {
      SEL sel = SELUID(selname);

      if (ISSELECTOR (sel))
        {
          Py_INCREF (Py_True);
          return Py_True;
        }
      else
        {
          Py_INCREF (Py_False);
          return Py_False;
        }
    }

  return NULL;
}

static PyMethodDef ObjCRuntime_methods[] =
{
  { "sel_is_mapped",            (PyCFunction) ObjCRuntime_sel_is_mapped,METH_VARARGS,   ObjCRuntime_sel_is_mapped_doc },
  { 0, 0, 0, 0 }
};

static void
add_objc_classes (PyObject *list)
{
  Class classid;
#ifdef GNU_RUNTIME

  void *es = NULL;
#define ENUMERATE_CLASSES(c) (c = objc_next_class (&es))

#else

  NXHashTable *class_hash = objc_getClasses();
  NXHashState state = NXInitHashState (class_hash);
#define ENUMERATE_CLASSES(c) (NXNextHashState (class_hash, &state, (void**) &c))

#endif

  while (ENUMERATE_CLASSES(classid))
    {
      PyObject *name = PyString_FromString ((char *) NAMEOF(classid));

      PyList_Append (list, name);
      Py_DECREF(name);
    }
}

static PyObject *
ObjCRuntime_getattro (ObjCRuntime *self, PyObject *name)
{
  PyObject *attr;

  attr = PyDict_GetItem (self->classes, name);
  if (!attr)
    {
      char *cname = PyString_AsString (name);

      PyErr_Clear();
      if ((attr = Py_FindMethod (ObjCRuntime_methods, (PyObject *) self, cname)))
        return attr;
      else
        {
          PyErr_Clear();
          if (!strcmp (cname, "__kind__"))
#ifdef GNU_RUNTIME
            return PyString_FromString ("GNU");
#else
            return PyString_FromString ("NeXT");
#endif
          else if (!strcmp (cname, "__members__"))
            {
              const char *members[] = { "__kind__", "__members__", "__objc_classes__" };
              PyObject *list;
              unsigned int idx;
              
              idx = sizeof (members) / sizeof (members[0]);
              list = PyList_New (idx);
              while (idx--)
                PyList_SetItem (list, idx, PyString_FromString ((char *) members[idx]));
	      add_objc_classes (list);
              return list;
            }
	  else if (!strcmp (cname, "__objc_classes__"))
	    {
	      PyObject *list;

	      list = PyList_New (0);
	      add_objc_classes (list);
	      return list;
	    }
          else
            {
              id class = LOOKUPCLASS(cname);
              
              if (class)
                {
                  attr =  (PyObject *) ObjCObject_new (class);
                  
                  PyDict_SetItem (self->classes, name, attr);
                }
              else
                {
#define ERRMSG "Objective-C class `%s' is unknown to the runtime"
                  char errmsg[sizeof ERRMSG + PyString_Size (name)];
                  
                  sprintf (errmsg, ERRMSG, cname);
                  PyErr_SetString (ObjC_Error, errmsg);
#undef ERRMSG
                }
            }
        }
    }
  else
    Py_INCREF (attr);

  return attr;
}

static
PyTypeObject ObjCRuntime_Type =
{
  PyObject_HEAD_INIT(&PyType_Type)
  0,                                          /*ob_size*/
  "ObjCRuntime",                              /*tp_name*/
  sizeof(ObjCRuntime),                        /*tp_basicsize*/
  0,                                          /*tp_itemsize*/
  
  /* methods */
  (destructor) ObjCRuntime_dealloc,           /*tp_dealloc*/
  (printfunc) 0,                              /*tp_print*/
  (getattrfunc) 0,                            /*tp_getattr*/
  (setattrfunc) 0,                            /*tp_setattr*/
  (cmpfunc) 0,                                /*tp_compare*/
  (reprfunc) 0,                               /*tp_repr*/
  0,                                          /*tp_as_number*/
  0,                                          /*tp_as_sequence*/
  0,                                          /*tp_as_mapping*/
  (hashfunc) 0,                               /*tp_hash*/
  (ternaryfunc) 0,                            /*tp_call*/
  (reprfunc) 0,                               /*tp_str*/
  (getattrofunc) ObjCRuntime_getattro,        /*tp_getattro*/
  (setattrofunc) 0,                           /*tp_setattro*/

  /* Space for future expansion */
  0L,0L,
  
  "Wrapper around Objective-C Runtime"        /* Documentation string */
};

ObjCRuntime *
ObjCRuntime_new (void)
{
  ObjCRuntime *self = PyObject_NEW (ObjCRuntime, &ObjCRuntime_Type);

  if (self == NULL)
    return NULL;

  self->classes = PyDict_New();
  return self;
}
