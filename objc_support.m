/* Copyright (c) 1996,97,98 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: objc_support.m,v
 * Revision: 1.24
 * Date: 1998/08/18 15:35:58
 *
 * Created Tue Sep 10 14:16:02 1996.
 */

#include "ObjC.h"
#include "objc_support.h"
#include <unistd.h>
// #include "myctype.h"

#import <Foundation/NSInvocation.h>      /* sdm7g - changed #include to #import */
#import <Foundation/NSMethodSignature.h> /* sdm7g */

#ifndef GNU_RUNTIME

#ifndef MAX
#define MAX(x,y) ({ unsigned int __x=(x), __y=(y); (__x > __y ? __x : __y); })
#define MIN(x,y) ({ unsigned int __x=(x), __y=(y); (__x < __y ? __x : __y); })
#endif
static inline const int
ROUND(int v, int a)
{
  return a * ((v+a-1)/a);
}

const char * 
objc_skip_typespec (const char *type)
{
  type = objc_skip_type_qualifiers (type);

  switch (*type)
    {
      /* The following are one character type codes */
    case _C_ID:

    case _C_CLASS:
    case _C_SEL:
    case _C_CHR:
    case _C_UCHR:
    case _C_CHARPTR:
    case _C_SHT:
    case _C_USHT:
    case _C_INT:
    case _C_UINT:
    case _C_LNG:
    case _C_ULNG:
    case _C_FLT:
    case _C_DBL:
    case _C_VOID:
      return ++type;
      break;

    case _C_ARY_B:
      /* skip digits, typespec and closing ']' */
    
      while (isdigit (*++type));
      type = objc_skip_typespec (type);
      //assert (*type == _C_ARY_E);
      return ++type;
      break;
      
    case _C_STRUCT_B:
      /* skip name, and elements until closing '}'  */
    
      while (*type != _C_STRUCT_E && *type++ != '=');
      while (*type != _C_STRUCT_E)
        type = objc_skip_typespec (type);
      return ++type;

    case _C_UNION_B:
      /* skip name, and elements until closing ')'  */
      type++;
      while (*type != _C_UNION_E) { type = objc_skip_typespec (type); }
      return ++type;
      
    case _C_PTR:
      /* Just skip the following typespec */
      return objc_skip_typespec (++type);
    
    default:
      fprintf (stderr, "objc_skip_typespec: Unhandled type '%c'\n", *type);
      abort();
    }
}

/*
  Return the alignment of an object specified by type 
*/

static int
objc_alignof_type (const char *type)
{
  switch (*type)
    {
    case _C_ID:
      return __alignof__ (id);
      break;

    case _C_CLASS:
      return __alignof__ (Class);
      break;
    
    case _C_SEL:
      return __alignof__ (SEL);
      break;

    case _C_CHR:
      return __alignof__ (char);
      break;
    
    case _C_UCHR:
      return __alignof__ (unsigned char);
      break;

    case _C_SHT:
      return __alignof__ (short);
      break;

    case _C_USHT:
      return __alignof__ (unsigned short);
      break;

    case _C_INT:
      return __alignof__ (int);
      break;

    case _C_UINT:
      return __alignof__ (unsigned int);
      break;

    case _C_LNG:
      return __alignof__ (long);
      break;

    case _C_ULNG:
      return __alignof__ (unsigned long);
      break;

    case _C_FLT:
      return __alignof__ (float);
      break;

    case _C_DBL:
      return __alignof__ (double);
      break;

    case _C_CHARPTR:
      return __alignof__ (char *);
      break;

    case _C_PTR:
      return __alignof__ (void *);
      break;
      
    case _C_ARY_B:
      while (isdigit(*++type)) /* do nothing */;
      return objc_alignof_type (type);
      
    case _C_STRUCT_B:
      {
        struct { int x; double y; } fooalign;
        while(*type != _C_STRUCT_E && *type++ != '=') /* do nothing */;
        if (*type != _C_STRUCT_E)
          return MAX (objc_alignof_type (type), __alignof__ (fooalign));
        else
          return __alignof__ (fooalign);
      }

    case _C_UNION_B:
      {
        int maxalign = 0;
        type++;
        while (*type != _C_UNION_E)
          {
            maxalign = MAX (maxalign, objc_alignof_type (type));
            type = objc_skip_typespec (type);
          }
        return maxalign;
      }
    
    default:
      fprintf (stderr, "objc_align_type: Unhandled type '%c'\n", *type);
      abort();
    }
}

/*
  The aligned size if the size rounded up to the nearest alignment.
*/

static int
objc_aligned_size (const char *type)
{
  static int objc_sizeof_type (const char *type);
  
  int size = objc_sizeof_type (type);
  int align = objc_alignof_type (type);
  return ROUND (size, align);
}

/*
  return the size of an object specified by type 
*/

int
objc_sizeof_type (const char *type)
{
  switch (*type)
    {
    case _C_VOID:
      return 0;
      
    case _C_ID:
      return sizeof(id);
      break;
      
    case _C_CLASS:
      return sizeof(Class);
      break;
      
    case _C_SEL:
      return sizeof(SEL);
      break;
      
    case _C_CHR:
      return sizeof(char);
      break;
      
    case _C_UCHR:
      return sizeof(unsigned char);
      break;
      
    case _C_SHT:
      return sizeof(short);
      break;
      
    case _C_USHT:
      return sizeof(unsigned short);
      break;
      
    case _C_INT:
      return sizeof(int);
      break;
      
    case _C_UINT:
      return sizeof(unsigned int);
      break;
      
    case _C_LNG:
      return sizeof(long);
      break;
      
    case _C_ULNG:
      return sizeof(unsigned long);
      break;
      
    case _C_FLT:
      return sizeof(float);
      break;
      
    case _C_DBL:
      return sizeof(double);
      break;
      
    case _C_PTR:
    case _C_CHARPTR:
      return sizeof(char*);
      break;
      
    case _C_ARY_B:
      {
        int len = atoi(type+1);
        while (isdigit(*++type));
        return len*objc_aligned_size (type);
      }
    break; 
    
    case _C_STRUCT_B:
      {
        int acc_size = 0;
        int align;
        while (*type != _C_STRUCT_E && *type++ != '='); /* skip "<name>=" */
        while (*type != _C_STRUCT_E)
          {
            align = objc_alignof_type (type);       /* padd to alignment */
            acc_size = ROUND (acc_size, align);
            acc_size += objc_sizeof_type (type);   /* add component size */
            type = objc_skip_typespec (type);            /* skip component */
          }
        return acc_size;
      }
    
    case _C_UNION_B:
      {
        int max_size = 0;
        type++;
        while (*type != _C_UNION_E)
          {
            max_size = MAX (max_size, objc_sizeof_type (type));
            type = objc_skip_typespec (type);
          }
        return max_size;
      }
    
    default:
      fprintf (stderr, "objc_sizeof_type: Unhandled type '%c'\n", *type);
      abort();
    }
}

#endif

/*#F Returns a tuple of objects representing the content of a C array
  of type @var{type} pointed by @var{datum}. */
static PyObject *
pythonify_c_array (const char *type, void *datum, ObjCMethod *meth)
{
  PyObject *ret;
  unsigned int nitems, offset, itemidx, sizeofitem;
  
  nitems = atoi (type+1);
  while (isdigit (*++type));
  sizeofitem = objc_sizeof_type (type);

  ret = PyTuple_New (nitems);
  if (!ret)
    return NULL;

  for (offset=itemidx=0; itemidx < nitems; itemidx++)
    {
      PyObject *pyitem = NULL;

      pyitem = pythonify_c_value (type, datum+offset, meth);

      if (pyitem)
        PyTuple_SET_ITEM (ret, itemidx, pyitem);
      else
        {
          Py_DECREF(ret);
          return NULL;
        }

      offset += sizeofitem;
    }
  
  return ret;
}

/*#F Returns a tuple of objects representing the content of a C structure
  of type @var{type} pointed by @var{datum}. */
static PyObject *
pythonify_c_struct (const char *type, void *datum, ObjCMethod *meth)
{
  PyObject *ret;
  unsigned int nitems, offset, itemidx;
  const char *item;

  while (*type != _C_STRUCT_E && *type++ != '='); /* skip "<name>=" */
  for (item=type, nitems=0; *item != _C_STRUCT_E; item = objc_skip_typespec (item))
    nitems++;

  ret = PyTuple_New (nitems);
  if (!ret)
    return NULL;

  for (item=type, offset=itemidx=0; *item != _C_STRUCT_E; item = objc_skip_typespec (item))
    {
      PyObject *pyitem;

      pyitem = pythonify_c_value (item, datum+offset, meth);

      if (pyitem)
        {
          PyTuple_SET_ITEM (ret, itemidx, pyitem);
        }
      else
        {
          Py_DECREF(ret);
          return NULL;
        }

      itemidx++;
      offset += objc_sizeof_type (item);
    }
  
  return ret;
}

/*#F Extracts the elements from the tuple @var{arg} and fills a C array
  of type @var{type} pointed by @var{datum}. Returns an error message, or
  NULL on success. */
static const char *
depythonify_c_array (const char *type, PyObject *arg, void *datum)
{
  unsigned int nitems, offset, itemidx, sizeofitem;

  nitems = atoi (type+1);
  while (isdigit (*++type));
  sizeofitem = objc_sizeof_type (type);

  if (nitems != PyTuple_Size (arg))
    {
#define ERRMSG "a tuple of %d items, got one of %d"
      static char errmsg[sizeof ERRMSG + 4];

      sprintf (errmsg, ERRMSG, nitems, PyTuple_Size (arg));
      return errmsg;
#undef ERRMSG
    }

  for (offset=itemidx=0; itemidx < nitems; itemidx++)
    {
      PyObject *pyarg = PyTuple_GetItem (arg, itemidx);
      const char *error;

      error = depythonify_c_value (type, pyarg, datum+offset);
      if (error)
        return error;
      
      offset += sizeofitem;
    }

  return NULL;
}

/*#F Extracts the elements from the tuple @var{arg} and fills a C structure
  of type @var{type} pointed by @var{datum}. Returns an error message, or
  NULL on success. */
static const char *
depythonify_c_struct (const char *types, PyObject *arg, void *datum)
{
  unsigned int nitems, offset, itemidx;
  const char *type;

  while (*types != _C_STRUCT_E && *types++ != '='); /* skip "<name>=" */
  for (type=types, nitems=0; *type != _C_STRUCT_E; type = objc_skip_typespec (type))
    nitems++;

  if (nitems != PyTuple_Size (arg))
    {
#define ERRMSG "a tuple of %d items, got one of %d"
      static char errmsg[sizeof ERRMSG + 4];

      sprintf (errmsg, ERRMSG, nitems, PyTuple_Size (arg));
      return errmsg;
#undef ERRMSG
    }

  for (type=types, offset=itemidx=0; *type != _C_STRUCT_E; type = objc_skip_typespec (type))
    {
      PyObject *argument = PyTuple_GetItem (arg, itemidx);
      const char *error;

      error = depythonify_c_value (type, argument, datum+offset);
      if (error)
        return error;
      
      itemidx++;
      offset += objc_sizeof_type (type);
    }
  return NULL;
}

PyObject *
pythonify_c_value (const char *type, void *datum, ObjCMethod *meth)
{
  PyObject *retobject = NULL;

  type = objc_skip_type_qualifiers (type);

  switch (*type)
    {
    case _C_CHR:
    case _C_UCHR:
      retobject = (PyObject *) PyInt_FromLong ((int) (*(char **) datum));
      break;

    case _C_CHARPTR:
      {
        char *cp = *(char **) datum;

        if (! cp)
          cp = "(null pointer)"; /* XXX */
        retobject = (PyObject *) PyString_FromString (cp);
        break;
      }

    case _C_INT:
    case _C_UINT:
      retobject = (PyObject *) PyInt_FromLong (*(int *) datum);
      break;

    case _C_SHT:
    case _C_USHT:
      retobject = (PyObject *) PyInt_FromLong (*(short *) datum);
      break;

    case _C_LNG:
    case _C_ULNG:
      retobject = (PyObject *) PyInt_FromLong (*(long *) datum);
      break;

    case _C_FLT:
      retobject = (PyObject *) PyFloat_FromDouble (*(float *) datum);
      break;

    case _C_DBL:
      retobject = (PyObject *) PyFloat_FromDouble (*(double *) datum);
      break;
      
    case _C_ID:
      {
        id obj = *(id *) datum;

        if (obj == nil)
          {
            /* XXX What should I do in this case? I used to treat it
               as an error, but for example `-superclass' on Object
               returns nil... */
            // retobject = NULL;
            retobject = Py_None;
            Py_INCREF (retobject);
          }
        else /* XXX if (meth && obj == [meth->inv target]) // did it return itself?
          {
            retobject = (PyObject *) meth->obj;
            Py_INCREF(retobject);
          } 
        else */
          {
            if ([obj conformsToProtocol:@protocol (PythonObject)])
              {
                retobject = [(OC_PythonObject *) obj pyObject];
                Py_INCREF(retobject);
              }
            else if ([obj isKindOfClass:[NSString class]]) // XXX FIXME_1: Should work on NSInlineCString (and maybe others) too.
	      retobject = PyString_FromStringAndSize ([obj cString], [(NSString *)obj length]);
	    else
              retobject = (PyObject *) ObjCObject_new (obj);
          }
        break;
      }

    case _C_SEL:
      retobject = (PyObject *) ObjCMethod_new_with_selector (NULL,
                                                             *(SEL *) datum);
      break;

    case _C_CLASS:
      {
        Class c = *(Class *) datum;

        if (c == Nil)
          {
            retobject = Py_None;
            Py_INCREF (retobject);
          }
        else
          retobject = (PyObject *) ObjCObject_new (c);
        break;
      }

    case _C_PTR:
      retobject = (PyObject *) ObjCPointer_new (*(void **) datum, type+1);
      break;
      
    case _C_UNION_B:
      {
        unsigned int size = objc_sizeof_type (type);
        char *buffer = alloca (size);

        memcpy (buffer, (void *) datum, size);
        retobject = PyString_FromStringAndSize (buffer, size);
        break;
      }
    
    case _C_STRUCT_B:
      retobject = pythonify_c_struct (type, datum, meth);
      break;

    case _C_ARY_B:
      retobject = pythonify_c_array (type, datum, meth);
      break;

    case _C_VOID:
      retobject = Py_None;
      Py_INCREF (retobject);
      break;

    default:
      {
#ifdef GNU_RUNTIME
        [NSException raise:NSInternalInconsistencyException 
                     format:@"unhandled value type (%c)", *type];
#else
#define ERRMSG "pythonify_c_value: unhandled value type (%c)"
        char msg[sizeof ERRMSG];
        sprintf (msg, ERRMSG, *type);
        PyErr_SetString (ObjC_Error, msg);
#undef ERRMSG
#endif
        break;
      }
    }

  return retobject;
}

#ifdef WITH_THREAD
#warning Does not support multiple threads yet.
#endif

/* This is used as an array of pointers: both the memory for the array
   and that for each array's slot is dinamically allocated with malloc().
   We use it when we have to give an ObjC method a pointer to some datum:
   since from the Python point of view we always work on values, not pointers,
   when an ObjC does actually want a pointer, we allocate memory in the
   next free slot (eventually growing the array), depythonify the argument
   in that space and feed it to the method.
   On the next method call this space will be freed. */

void **arguments_arena;

/* Count of used slots in arguments_arena. */
static unsigned int arguments_arena_current_count;

/* Total number of slots in arguments_arena. */
static unsigned int arguments_arena_slots;

static inline void
xfree (void *ptr)
{
  if (ptr)
    free (ptr);
}

static inline void *
xmalloc (unsigned int size)
{
  void *ptr = malloc (size);

  if (ptr == 0)
    {
#define ERRMSG "xmalloc: memory exausted"
      write (fileno (stderr), ERRMSG, sizeof (ERRMSG)-1);
      exit (1);
#undef ERRMSG
    }
  return ptr;
}

static inline void *
xrealloc (void *ptr, unsigned int size)
{
  if (ptr == 0)
    return xmalloc (size);
  ptr = realloc (ptr, size);
  if (ptr == 0)
    {
#define ERRMSG "xrealloc: memory exausted"
      write (fileno (stderr), ERRMSG, sizeof (ERRMSG)-1);
      exit (1);
#undef ERRMSG
    }
  return ptr;
}

/* If the arena is not empty, free it. Then initialize counters. */
static inline void
initialize_arguments_arena(void)
{
  if (arguments_arena)
    {
      while (arguments_arena_current_count--)
        xfree (arguments_arena[arguments_arena_current_count]);

      xfree (arguments_arena);
    }
  arguments_arena_current_count = arguments_arena_slots = 0;
  arguments_arena = NULL;
}

/* Calculates the space needed to keep a value of type TYPE, then if
   the arena isn't big enough reallocates a bigger array for it;
   allocates the needed amount of memory for the value recording
   its address in the next free slot and returns that pointer. */ 
static void *
get_space_on_arena_for_type (const char *type)
{
  unsigned int needed = objc_sizeof_type (type);
  
  if (arguments_arena_current_count == arguments_arena_slots)
    {
      if (arguments_arena_slots)
        arguments_arena_slots *= 2;
      else
        arguments_arena_slots = 2;
      arguments_arena = xrealloc (arguments_arena,
                                  arguments_arena_slots * sizeof (arguments_arena[0]));
    }
  return arguments_arena[arguments_arena_current_count++] = xmalloc (needed);
}

const char *
depythonify_c_value (const char *type, PyObject *argument, void *datum)
{
  const char *error = NULL;

  type = objc_skip_type_qualifiers (type);
  
  switch (*type)
    {
    case _C_CHR:
      if (! PyString_Check (argument) &&
          ! PyInt_Check (argument))
        error = "a string or an integer";
      else
        if (PyInt_Check (argument))
          *(char *) datum = PyInt_AsLong (argument);
        else
          *(char *) datum = PyString_AsString (argument)[0];
      break;

    case _C_UCHR:
      if (! PyString_Check (argument) &&
          ! PyInt_Check (argument))
        error = "a string or an integer";
      else
        if (PyInt_Check (argument))
          *(unsigned char *) datum = PyInt_AsLong (argument);
        else
          *(unsigned char *) datum = PyString_AsString (argument)[0];
      break;

    case _C_CHARPTR:
      if (! PyString_Check (argument) && argument != Py_None)
        error = "a string or None";
      else
        if (argument == Py_None)
          *(char **) datum = NULL;
        else
          *(char **) datum = PyString_AS_STRING ((PyStringObject *) argument);
      break;

    case _C_INT:
      if (! PyInt_Check (argument))
        error = "an integer";
      else
        *(int *) datum = PyInt_AsLong (argument);
      break;

    case _C_SHT:
      if (! PyInt_Check (argument))
        error = "an integer";
      else
        *(short *) datum = PyInt_AsLong (argument);
      break;

    case _C_UINT:
      if (! PyInt_Check (argument))
        error = "an integer";
      else
        *(unsigned int *) datum = PyInt_AsLong (argument);
      break;

    case _C_USHT:
      if (! PyInt_Check (argument))
        error = "an integer";
      else
        *(unsigned short *) datum = PyInt_AsLong (argument);
      break;

    case _C_LNG:
      if (! PyInt_Check (argument))
        error = "an integer";
      else
        *(long *) datum = PyInt_AsLong (argument);
      break;

    case _C_ULNG:
      if (! PyInt_Check (argument))
        error = "an integer";
      else
        *(unsigned long *) datum = PyInt_AsLong (argument);
      break;

    case _C_ID:
      if (argument == Py_None)
        *(id *) datum = nil;
      else if (ObjCObject_Check (argument))
        *(id *) datum = ((ObjCObject *) argument)->oc_object;
      else if (PyString_Check (argument))
	*(id *) datum = [NSString stringWithCString:PyString_AS_STRING ((PyStringObject *) argument)
				  length:PyString_GET_SIZE ((PyStringObject *) argument)];
      else if (PyInt_Check (argument))
	*(id *) datum = [NSNumber numberWithLong:PyInt_AS_LONG (argument)];
      else
        *(id *) datum = [OC_PythonObject newWithObject:argument];
      break;

    case _C_CLASS:
      if (! (ObjCObject_Check (argument) &&
             ISCLASS(((ObjCObject *) argument)->oc_object))
          && argument != Py_None)
        error = "a ObjC class or None";
      else
        *(Class *) datum = (argument == Py_None
                            ? nil
                            : ((ObjCObject *)(argument))->oc_object);
      break;

    case _C_SEL:
      if (! ObjCMethod_Check (argument) && ! PyString_Check (argument))
        error = "a ObjC method or a string";
      else
        if (ObjCMethod_Check (argument))
          *(SEL *) datum = [((ObjCMethod *) argument)->inv selector];
        else
          {
            char *selname = PyString_AsString (argument);
            SEL sel = SELUID (selname);

            /* XXX this is questionable */
            if (sel)
              *(SEL *) datum = sel;
            else
              *(char **) datum = selname;
          }
      break;

    case _C_PTR:
      if (PyString_Check (argument))
        {
	  if (*(type+1) != _C_VOID)
	    {
	      unsigned int expected_size = objc_sizeof_type (++type);
	      
	      if (expected_size != PyString_Size (argument))
		{
#define ERRMSG "a string of size %d instead of %d"
		  static char errmsg[sizeof (ERRMSG)+6+6];
		  
		  sprintf (errmsg, ERRMSG, expected_size, PyString_Size (argument));
		  error = errmsg;
#undef ERRMSG
		  break;
		}
	    }
	  *(void **) datum = PyString_AS_STRING ((PyStringObject *) argument);
        }
      else if (ObjCPointer_Check (argument))
        *(void **) datum = ((ObjCPointer *) argument)->ptr;
      else             
        {
          *(void **) datum = get_space_on_arena_for_type (++type);
          error = depythonify_c_value (type, argument, *(void **) datum);
        }
      break;

    case _C_FLT:
      if (PyFloat_Check (argument))
        *(float *) datum = (float) PyFloat_AsDouble (argument);
      else if (PyInt_Check (argument))
        *(float *) datum = (float) PyInt_AsLong (argument);
      else
        error = "a float or an integer";
      break;

    case _C_DBL:
      if (PyFloat_Check (argument))
        *(double *) datum = PyFloat_AsDouble (argument);
      else if (PyInt_Check (argument))
        *(double *) datum = (double) PyInt_AsLong (argument);
      else
        error = "a float or an integer";
      break;

    case _C_UNION_B:
      if (PyString_Check (argument))
        {
          unsigned int expected_size = objc_sizeof_type (type);
          
          if (expected_size != PyString_Size (argument))
            {
#define ERRMSG "a string of size %d instead of %d"
              static char errmsg[sizeof (ERRMSG)+6+6];

              sprintf (errmsg, ERRMSG, expected_size, PyString_Size (argument));
              error = errmsg;
#undef ERRMSG
            }
          else
            memcpy ((void *) datum, PyString_AS_STRING ((PyStringObject *) argument), expected_size);
        }
      else
        error = "a string";
      break;

    case _C_STRUCT_B:
      if (! PyTuple_Check (argument))
        error = "a tuple";
      else
        error = depythonify_c_struct (type, argument, datum);
      break;

    case _C_ARY_B:
      if (! PyTuple_Check (argument))
        error = "a tuple";
      else
        error = depythonify_c_array (type, argument, datum);
      break;

    default:
      {
#define ERRMSG "unhandled typespec %c"
        static char msg[sizeof ERRMSG];

        sprintf (msg, ERRMSG, *type);
        error = msg;
        break;
#undef ERRMSG
      }
    }

  return error;
}

PyObject *
execute_and_pythonify_objc_method (ObjCMethod *meth, PyObject *args)
{
  NSMethodSignature *methinfo;
  unsigned int argcount;

  initialize_arguments_arena();

  methinfo = [meth->inv methodSignature];
  argcount = [methinfo numberOfArguments];
  
  if (PyTuple_Size (args) != argcount-2)
    {
      char error[100];

      sprintf (error, "wrong number of arguments, expected to be %d", argcount-2);
      PyErr_SetString (ObjC_Error, error);
      return NULL;
    }
  else
    {
      int i;
      const char *error = NULL;
      
      for (i = 2; i < argcount; i++)
        {
          PyObject *argument;
#ifdef MACOSX
	  const char *argtype = [methinfo getArgumentTypeAtIndex:i];
#else
	  const char *argtype = [methinfo argumentInfoAtIndex:i].type;
#endif
	  char argbuffer[objc_sizeof_type (argtype)];

          argument = PyTuple_GET_ITEM (args, i-2);

          error = depythonify_c_value (argtype, argument, argbuffer);
	  
          if (error)
            break;

	  [meth->inv setArgument:argbuffer atIndex:i];
        }
            
      if (error)
        {
#if 0
          const char *typeend = objc_skip_typespec (type);
#define ERRMSG "expected %s for argument %d: its type is `%.*s'"
          char errmsg[sizeof ERRMSG + strlen (error) + typeend-type];

          sprintf (errmsg, ERRMSG, error, i-2, (int) (typeend-type), type);
          PyErr_SetString (ObjC_Error, errmsg);
#undef ERRMSG
#else
#define ERRMSG "expected %s for argument %d"
          char errmsg[sizeof ERRMSG + strlen (error)];

          sprintf (errmsg, ERRMSG, error, i-2);
          PyErr_SetString (ObjC_Error, errmsg);
#undef ERRMSG
#endif
          return NULL;
        }
      else
	{
	  const char *rettype;
	  
	  PyErr_Clear();
	  NS_DURING
	    [meth->inv invoke];
	  NS_HANDLER
	    PyErr_SetObject (ObjC_Error, (PyObject *) ObjCObject_new (localException));
	    return NULL;
	  NS_ENDHANDLER

	  rettype = [methinfo methodReturnType];
	  if ( (*rettype != _C_VOID) && ([methinfo isOneway] == NO) )
	    {
	      char *retbuffer = alloca ([methinfo methodReturnLength]);

	      [meth->inv getReturnValue:retbuffer];
	  
	      return pythonify_c_value ([methinfo methodReturnType],
					retbuffer, meth);
	    }
	  else
	    {
	      Py_INCREF(Py_None);
	      return Py_None;
	    }
	}
    }
}
