/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: ObjCObject.m,v
 * Revision: 1.9
 * Date: 1998/08/18 15:35:55
 *
 * Created Mon Oct 28 12:32:11 1996.
 */

#include "ObjC.h"
#include "objc_support.h"

#define IS_MAPPING(obj) (([obj respondsToSelector:@selector (count)] ||	     \
			  [obj respondsToSelector:@selector (length)]) &&    \
			 [obj respondsToSelector:@selector (objectForKey:)])
#define IS_SEQUENCE(obj) (([obj respondsToSelector:@selector (count)] ||       \
			   [obj respondsToSelector:@selector (length)]) &&     \
			  [obj respondsToSelector:@selector (objectAtIndex:)])

enum _oc_object_kind
{
  OK_ANY, OK_MAPPING, OK_SEQUENCE, OK_last
};

static PyTypeObject oc_object_type[OK_last];

static inline int
object_kind (id obj)
{
  if (IS_MAPPING (obj))
    return OK_MAPPING;
  else if (IS_SEQUENCE (obj))
    return OK_SEQUENCE;
  else
    return OK_ANY;
}

ObjCObject *
ObjCObject_new (id obj)
{
  ObjCObject *self;

  self = PyObject_NEW (ObjCObject, &oc_object_type[object_kind (obj)]);
           
  if (self == NULL)
    return NULL;

  /* sdm7g 2002-1-22: isKindOfClass crashes on abstract classes like NSProxy */
  if (obj &&  !ISCLASS(obj) && 
      ([obj isKindOfClass: [NSAutoreleasePool class]] == NO) )
    [obj retain];
  
  self->oc_object = obj;
  self->methods = PyDict_New();
  
  return self;
}

static void
ObjCObject_dealloc (ObjCObject *self)
{
  [self->oc_object release];

  Py_DECREF (self->methods);
  PyMem_DEL (self);
}

static PyObject *
ObjCObject_repr (ObjCObject *self)
{
  char buffer[512];
  char *p;

  if (self->oc_object == nil)
    p = "<Objective-C nil>";
  else
    {
      sprintf(buffer, "<Objective-C `%s' %s at %lx>",
              NAMEOF(self->oc_object),
              (ISCLASS (self->oc_object) ? "class" : "instance"),
              (long) self->oc_object);
      p = buffer;
    }
  return PyString_FromString (p);
}

static PyObject *
ObjCObject_str (ObjCObject *self)
{
  NSString *description = [self->oc_object description];

  return PyString_FromStringAndSize ([description cString], [description length]);
}

static char ObjCObject_is_instance_doc[] =
FUNDOC("Check whether the receiving object is an Objective-C instance or class.",
       ".is_instance()",
       "none",
       "True if it's an instance, False otherwise");
static PyObject *
ObjCObject_is_instance (ObjCObject *self, PyObject *args)
{
  if (PyArg_ParseTuple (args, ""))
    {
      PyObject *yn;

      if (ISCLASS(self->oc_object))
        yn = Py_False;
      else
        yn = Py_True;

      Py_INCREF (yn);
      return yn;
    }

  return NULL;
}

static char ObjCObject_is_class_doc[] =
FUNDOC("Check whether the receiving object is an Objective-C instance or class.",
       ".is_class()",
       "none",
       "True if it's a class, False otherwise");
static PyObject *
ObjCObject_is_class (ObjCObject *self, PyObject *args)
{
  if (PyArg_ParseTuple (args, ""))
    {
      PyObject *yn;

      if (ISCLASS(self->oc_object))
        yn = Py_True;
      else
        yn = Py_False;

      Py_INCREF (yn);
      return yn;
    }

  return NULL;
}

static char ObjCObject_get_class_doc[] =
FUNDOC("Get the class of the receiving Objective-C object.",
       ".Class()",
       "none",
       "An ObjCObject wrapping the Objective-C class");

static PyObject *
ObjCObject_get_class (ObjCObject *self, PyObject *args)
{
  if (PyArg_ParseTuple (args, ""))
    {
      id class = [self->oc_object class];

      return (PyObject *) ObjCObject_new (class);
    }
  return NULL;
}

static PyMethodDef ObjCObject_methods[] =
{
  { "isInstance",       (PyCFunction) ObjCObject_is_instance,   METH_VARARGS, ObjCObject_is_instance_doc },
  { "isClass",          (PyCFunction) ObjCObject_is_class,      METH_VARARGS, ObjCObject_is_class_doc },
  { "Class",            (PyCFunction) ObjCObject_get_class,     METH_VARARGS, ObjCObject_get_class_doc },
  { 0, 0, 0, 0 }
};

extern PyMethodDef ObjCSequenceObject_methods[];
extern PyMethodDef ObjCMappingObject_methods[];

static PyObject *
ObjCObject_getattr (ObjCObject *self, char *name)
{
  PyObject *method;
  
  method = Py_FindMethod (ObjCObject_methods, (PyObject *) self, name);
  if (method)
    return method;

  if (ObjCSequenceObject_Check (self))
    method = Py_FindMethod (ObjCSequenceObject_methods, (PyObject *) self, name);
  else if (ObjCMappingObject_Check (self))
    method = Py_FindMethod (ObjCMappingObject_methods, (PyObject *) self, name);

  if (method)
    return method;
  else
    {
      char meth_name[strlen (name)+1];
      
      PyErr_Clear();
#if PYTHONIFICATION_METHOD != WITH_BOTH
      depythonify_objc_message (name, meth_name);
      method = PyDict_GetItemString (self->methods, meth_name);
      
      if (! method)
        {
          method = (PyObject *) ObjCMethod_new_with_name (self, meth_name);
          
          if (method)
            {
              PyErr_Clear();
              PyDict_SetItemString (self->methods, meth_name, method);
            }
        }
      else
        Py_INCREF (method);
      
      return method;
#else
      depythonify_objc_message (name, meth_name, PYTHONIFICATION_FIRST_TRY);
      method = PyDict_GetItemString (self->methods, meth_name);
      
      if (! method)
        {
          method = (PyObject *) ObjCMethod_new_with_name (self, meth_name);
          
          if (method)
            {
              PyErr_Clear();
              PyDict_SetItemString (self->methods, meth_name, method);
              return method;
            }
        }
      else
        {
          Py_INCREF (method);
          return method;
        }
      
#if PYTHONIFICATION_FIRST_TRY == WITH_DOUBLE_UNDERSCORE
      depythonify_objc_message (name, meth_name, WITH_SINGLE_UNDERSCORE);
#else
      depythonify_objc_message (name, meth_name, WITH_DOUBLE_UNDERSCORE);
#endif
      method = PyDict_GetItemString (self->methods, meth_name);
      
      if (! method)
        {
          method = (PyObject *) ObjCMethod_new_with_name (self, meth_name);
          
          if (method)
            {
              PyErr_Clear();
              PyDict_SetItemString (self->methods, meth_name, method);
              
              if (Py_VerboseFlag)
                {
                  char faster_name[200];
                  
                  fprintf (stderr, "pyobjc Warning: method `%s' matches `%s',\n\t", name, meth_name);
                  
                  pythonify_objc_message (meth_name, faster_name, PYTHONIFICATION_FIRST_TRY);
                  
                  fprintf (stderr, "but `%s' would be faster.\n", faster_name);
                }
            }
        }
      else
        Py_INCREF (method);
      
      return method;
      
#endif /* PYTHONIFICATION_METHOD != WITH_BOTH */
    }

  PyErr_SetString (PyExc_AttributeError, name);
  return NULL;
}

static PyObject *
ObjCObject_call (ObjCObject *self, PyObject *args, PyObject *kw)
{
  if (ISCLASS(self->oc_object))
    {
      if (kw)
        {
#define INITMSG "init"
          PyObject *initselname = PyDict_GetItemString (kw, INITMSG);
          char *selname;
          SEL sel;
          
          if (initselname && PyString_Check (initselname))
            {
              selname = PyString_AS_STRING (initselname);
            }
          else
            {
              int nargs = PyTuple_Size (args);
              register char *selarg;

              PyErr_Clear();
              
              selname = alloca (sizeof (INITMSG) + nargs);
              strcpy (selname, INITMSG);
              selarg = selname + sizeof (INITMSG) - 1;
              while (nargs--)
                *selarg++ = ':';
              *selarg = '\0';
            }

          sel = SELUID(selname);

          if (sel && [self->oc_object instancesRespondToSelector:sel])
            {
              ObjCObject *instance = ObjCObject_new ([self->oc_object alloc]);
              ObjCMethod *initsel = ObjCMethod_new_with_name (instance,
                                                              PyString_AsString (initselname));
              PyObject *result;
              
              result = execute_and_pythonify_objc_method (initsel, args);
              
              Py_DECREF (instance);
              Py_DECREF (initsel);
              
              return result;
            }
          else
            {
#define ERRORMSG " does not recognize "
              const char *whoiam = NAMEOF(self->oc_object);
              char buffer[strlen (whoiam) + sizeof ERRORMSG + 1 + strlen (selname) + 1];
              
              strcpy (buffer, whoiam);
              strcat (buffer, ERRORMSG);
              strcat (buffer, (ISCLASS(self->oc_object) ? "+" : "-"));
              strcat (buffer, selname);
              PyErr_SetString (ObjC_Error, buffer);
#undef ERRORMSG
              return NULL;
            }
        }
      else
        if (PyArg_ParseTuple (args, ""))
          {
            id instance = [self->oc_object new];
            
            return (PyObject *) ObjCObject_new (instance);
          }
    }
  else
    PyErr_SetString (ObjC_Error, "call syntax allowed only for classes");

  return NULL;
}

// SEQUENCING

#import  <Foundation/NSArray.h> // for -objectAtIndex:

#define RETURN_WRAP(result) do {                        \
  id wrap = result;                                     \
                                                        \
  if (wrap)                                             \
    {                                                   \
      PyObject *ret;                                    \
                                                        \
      if ([wrap isKindOfClass:[OC_PythonObject class]]) \
        {                                               \
          ret = [(OC_PythonObject *) wrap pyObject];    \
          Py_INCREF (ret);                              \
        }                                               \
      else                                              \
         ret = (PyObject *) ObjCObject_new (wrap);      \
                                                        \
      return ret;                                       \
    }                                                   \
  else                                                  \
    return NULL;                                        \
} while(0)

static PyObject *
WRAP (id result)
{
  RETURN_WRAP (result);
}

static int
ObjCObject_sq_length (ObjCObject *self)
{
  if ([self->oc_object respondsToSelector:@selector (count)])
    return [self->oc_object count]; 
  else if ([self->oc_object respondsToSelector:@selector (length)])
    return [self->oc_object length];
  else
    {
      PyErr_SetString (PyExc_TypeError, "len() of unsized object");
      return -1;
    }
}

static PyObject *
ObjCObject_sq_concat (ObjCObject *self, PyObject *other)
{
  if (!ObjCSequenceObject_Check (self) ||
      !PySequence_Check (other))
    {
      PyErr_BadArgument();
      return NULL;
    }
  else
    {
      int mysize = ObjCObject_sq_length (self);
      int size;
      int i;
      PyListObject *np;

      if (ObjCSequenceObject_Check (other))
        size = mysize + ObjCObject_sq_length ((ObjCObject *) other);
      else
        size = mysize + PySequence_Length (other);
      np = (PyListObject *) PyList_New (size);
      
      if (np == NULL)
        {
          return NULL;
        }

      for (i = 0; i < mysize; i++)
        {
          PyObject *v = WRAP([self->oc_object objectAtIndex:i]);

          np->ob_item[i] = v;
        }

      if (ObjCSequenceObject_Check (other))
        {
          for (; i < size; i++)
            {
              PyObject *v = WRAP([ObjCObject_OBJECT(other) objectAtIndex:i-mysize]);

              np->ob_item[i] = v;
            }
        }
      else
        {
          for (; i < size; i++)
            {
              PyObject *v = ((PyListObject *) other)->ob_item[i-mysize];
              
              Py_INCREF(v);
              np->ob_item[i] = v;
            }
        }
      
      return (PyObject *) np;
    }
}

static PyObject *
ObjCObject_sq_repeat (ObjCObject *self, int n)
{
  int size, mysize = ObjCObject_sq_length (self);
  PyListObject *np;
  PyObject **p;
  
  size = mysize*n;
  np = (PyListObject *) PyList_New (size);
  
  if (np == NULL)
    {
      return NULL;
    }

  p = np->ob_item;
  while (n--)
    {
      int i;

      for (i=0; i<mysize; i++)
        {
          *p = WRAP([self->oc_object objectAtIndex:i]);
          p++;
        }
    }

  return (PyObject *) np;
}

static PyObject *
ObjCObject_sq_item (ObjCObject *self, int n)
{
  if (n < ObjCObject_sq_length (self))
    RETURN_WRAP([self->oc_object objectAtIndex:n]);

  PyErr_SetString (PyExc_IndexError, "sequence index out of range");
  return NULL;
}

static PyObject *
ObjCObject_sq_slice (ObjCObject *self, int ilow, int ihigh)
{
  PyListObject *np;
  int i, mysize = ObjCObject_sq_length (self);
  
  if (ilow < 0)
    ilow = 0;
  else if (ilow > mysize)
    ilow = mysize;

  if (ihigh < 0)
    ihigh = 0;
  if (ihigh < ilow)
    ihigh = ilow;
  else if (ihigh > mysize)
    ihigh = mysize;

  np = (PyListObject *) PyList_New (ihigh - ilow);
  if (np == NULL)
    return NULL;

  for (i=ilow; i<ihigh; i++)
    {
      PyObject *v = WRAP([self->oc_object objectAtIndex:i]);
      
      np->ob_item[i-ilow] = v;
    }

  return (PyObject *) np;
}

static int
ObjCObject_sq_ass_item (ObjCObject *self, int i, PyObject *v)
{
  if (i < 0 || i >= ObjCObject_sq_length (self))
    {
      PyErr_SetString (PyExc_IndexError, "sequence assignment index out of range");
      return -1;
    }

  if (v == NULL)
    {
      if ([self->oc_object respondsToSelector:@selector (removeObjectAtIndex:)])
        {
          [self->oc_object removeObjectAtIndex:i];
        }
      else
        {
          PyErr_SetString (PyExc_TypeError, "cannot remove objects from sequence");
          return -1;
        }
    }
  else
    {
      if ([self->oc_object respondsToSelector:@selector (replaceObjectAtIndex:withObject:)])
        {
          id new = [OC_PythonObject newWithObject:v];
          
          [self->oc_object replaceObjectAtIndex:i withObject:new];
        }
      else
        {
          PyErr_SetString (PyExc_TypeError, "cannot replace objects in sequence");
          return -1;
        }
    }

  return 0;
}

static int
ObjCObject_sq_ass_slice (ObjCObject *self, int ilow, int ihigh, PyObject *v)
{
  PyErr_SetString (PyExc_SystemError, "ObjCObject_sq_ass_slice not implemented yet");
  return -1;
}

static PySequenceMethods ObjCObject_as_sequence =
{
  (inquiry) ObjCObject_sq_length,
  (binaryfunc) ObjCObject_sq_concat,
  (intargfunc) ObjCObject_sq_repeat,
  (intargfunc) ObjCObject_sq_item,
  (intintargfunc) ObjCObject_sq_slice,
  (intobjargproc) ObjCObject_sq_ass_item,
  (intintobjargproc) ObjCObject_sq_ass_slice
};

static PyObject *
ObjCSequenceObject_append (ObjCObject *self, PyObject *args)
{
  PyErr_SetString (PyExc_SystemError, "ObjCSequenceObject_append not implemented yet");
  return NULL;
}

static PyObject *
ObjCSequenceObject_index (ObjCObject *self, PyObject *args)
{
  PyErr_SetString (PyExc_SystemError, "ObjCSequenceObject_index not implemented yet");
  return NULL;
}

static PyObject *
ObjCSequenceObject_insert (ObjCObject *self, PyObject *args)
{
  PyErr_SetString (PyExc_SystemError, "ObjCSequenceObject_insert not implemented yet");
  return NULL;
}

static PyObject *
ObjCSequenceObject_sort (ObjCObject *self, PyObject *args)
{
  PyErr_SetString (PyExc_SystemError, "ObjCSequenceObject_sort not implemented yet");
  return NULL;
}

static PyObject *
ObjCSequenceObject_remove (ObjCObject *self, PyObject *args)
{
  PyErr_SetString (PyExc_SystemError, "ObjCSequenceObject_remove not implemented yet");
  return NULL;
}

static PyObject *
ObjCSequenceObject_reverse (ObjCObject *self, PyObject *args)
{
  PyErr_SetString (PyExc_SystemError, "ObjCSequenceObject_reverse not implemented yet");
  return NULL;
}

static PyMethodDef ObjCSequenceObject_methods[] =
{
  { "append",   (PyCFunction) ObjCSequenceObject_append,        METH_VARARGS,   NULL },
  // { "count", (PyCFunction) ObjCSequenceObject_count,         METH_VARARGS,   NULL },
  { "index",    (PyCFunction) ObjCSequenceObject_index,         METH_VARARGS,   NULL },
  { "insert",   (PyCFunction) ObjCSequenceObject_insert,        METH_VARARGS,   NULL },
  { "sort",     (PyCFunction) ObjCSequenceObject_sort,          METH_VARARGS,   NULL },
  { "remove",   (PyCFunction) ObjCSequenceObject_remove,        METH_VARARGS,   NULL },
  { "reverse",  (PyCFunction) ObjCSequenceObject_reverse,       METH_VARARGS,   NULL },
  { 0, 0, 0, 0 }
};

// MAPPING

#import  <Foundation/NSDictionary.h> // for objectForKey:

static PyObject *
ObjCObject_mp_subscript (ObjCObject *self, PyObject *key)
{
  id value;
  
  if (ObjCObject_Check (key))
    value = [(NSDictionary *) self->oc_object objectForKey:ObjCObject_OBJECT(key)];
  else
    {
      id ockey;

      if (PyString_Check (key))
	ockey = [NSString stringWithCString:PyString_AS_STRING (key)
			  length:PyString_GET_SIZE (key)];
      else if (PyInt_Check (key))
	ockey = [NSNumber numberWithLong:PyInt_AS_LONG (key)];
      else
	ockey = [OC_PythonObject newWithObject:key];
  
      value = [(NSDictionary *) self->oc_object objectForKey:ockey];
    }                
  
  if (!value)
    {
      PyErr_SetObject (PyExc_KeyError, key);
      return NULL;
    }
  
  RETURN_WRAP(value);
}

static PyObject *
ObjCObject_mp_ass_subscript (ObjCObject *self, PyObject *key, PyObject *value)
{
  PyErr_SetString (PyExc_SystemError, "ObjCObject_mp_ass_subscript not implemented yet");
  return NULL;
}

static PyMappingMethods ObjCObject_as_mapping =
{
  (inquiry) ObjCObject_sq_length,
  (binaryfunc) ObjCObject_mp_subscript,
  (objobjargproc) ObjCObject_mp_ass_subscript
};

static PyObject *
ObjCMappingObject_has_key (ObjCObject *self, PyObject *key)
{
  PyErr_SetString (PyExc_SystemError, "ObjCMappingObject_has_key not implemented yet");
  return NULL;
}

static PyObject *
ObjCMappingObject_items (ObjCObject *self, PyObject *args)
{
  PyErr_SetString (PyExc_SystemError, "ObjCMappingObject_items not implemented yet");
  return NULL;
}

static PyObject *
ObjCMappingObject_keys (ObjCObject *self, PyObject *args)
{
  PyErr_SetString (PyExc_SystemError, "ObjCMappingObject_keys not implemented yet");
  return NULL;
}

static PyObject *
ObjCMappingObject_values (ObjCObject *self, PyObject *args)
{
  PyErr_SetString (PyExc_SystemError, "ObjCMappingObject_values not implemented yet");
  return NULL;
}

static PyMethodDef ObjCMappingObject_methods[] =
{
  { "has_key",          (PyCFunction) ObjCMappingObject_has_key,        METH_VARARGS,   NULL },
  { "items",            (PyCFunction) ObjCMappingObject_items,          METH_VARARGS,   NULL },
  { "keys",             (PyCFunction) ObjCMappingObject_keys,           METH_VARARGS,   NULL },
  { "values",           (PyCFunction) ObjCMappingObject_values,         METH_VARARGS,   NULL },  
  { 0, 0, 0, 0 }
};

static long
ObjCObject_hash (ObjCObject *self)
{
  return [self->oc_object hash];
}

void
ObjCObject_initialize (void)
{
  int i;

  for (i=0; i<OK_last; i++)
    oc_object_type[i] = ObjCObject_Type;
  oc_object_type[OK_MAPPING].tp_as_mapping = &ObjCObject_as_mapping;
  oc_object_type[OK_SEQUENCE].tp_as_sequence = &ObjCObject_as_sequence;
}

PyTypeObject ObjCObject_Type =
{
  PyObject_HEAD_INIT (&PyType_Type)
  0,                                          /*ob_size*/
  "ObjCObject",                               /*tp_name*/
  sizeof (ObjCObject),                        /*tp_basicsize*/
  0,                                          /*tp_itemsize*/
  
  /* methods */
  (destructor) ObjCObject_dealloc,            /*tp_dealloc*/
  (printfunc) 0,			      /*tp_print*/
  (getattrfunc) ObjCObject_getattr,           /*tp_getattr*/
  (setattrfunc) 0,                            /*tp_setattr*/
  (cmpfunc) 0,                                /*tp_compare*/
  (reprfunc) ObjCObject_repr,                 /*tp_repr*/
  0,                                          /*tp_as_number*/
  0,                                          /*tp_as_sequence*/
  0,                                          /*tp_as_mapping*/
  (hashfunc) ObjCObject_hash,                 /*tp_hash*/
  (ternaryfunc) ObjCObject_call,              /*tp_call*/
  (reprfunc) ObjCObject_str,                  /*tp_str*/
  (getattrofunc) 0,                           /*tp_getattro*/
  (setattrofunc) 0,                           /*tp_setattro*/

  (PyBufferProcs *) 0,		              /*tp_as_buffer*/ 
  
  /* Space for future expansion */
  0L,
  
  "Wrapper around Objective-C id"             /* Documentation string */
};

