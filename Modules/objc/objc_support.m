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

#include "pyobjc.h"
#include "objc_support.h"
#include <unistd.h>
#include "objc/objc.h"
// #include "myctype.h"

#import <Foundation/NSInvocation.h>      /* sdm7g - changed #include to #import */
#import <Foundation/NSMethodSignature.h> /* sdm7g */
#import <Foundation/NSData.h> 
#import <Foundation/NSValue.h> 

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
    case _C_LNGLNG:
    case _C_ULNGLNG:
      ++type;
      break;

    case _C_ARY_B:
      /* skip digits, typespec and closing ']' */
    
      while (isdigit (*++type));
      type = objc_skip_typespec (type);
      //assert (*type == _C_ARY_E);
      ++type;
      break;
      
    case _C_STRUCT_B:
      /* skip name, and elements until closing '}'  */
    
      while (*type != _C_STRUCT_E && *type++ != '=');
      while (*type != _C_STRUCT_E)
        type = objc_skip_typespec (type);
      ++type;
      break;

    case _C_UNION_B:
      /* skip name, and elements until closing ')'  */
      type++;
      while (*type != _C_UNION_E) { type = objc_skip_typespec (type); }
      ++type;
      break;
      
    case _C_PTR:
    case _C_CONST:
    case _C_IN:
    case _C_INOUT:
    case _C_OUT:
    case _C_BYCOPY:
    case _C_ONEWAY:

      /* Just skip the following typespec */
      type = objc_skip_typespec (type+1);
      break;

    
    default:
      PySys_WriteStderr("PyObjC: objc_skip_typespec: Unhandled type '%c' (%d)\n", 
			*type, *type);
      abort();
    }

    while (isdigit(*type)) type++;
    return type;
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

    case _C_CONST:
    case _C_IN:
    case _C_INOUT:
    case _C_OUT:
    case _C_BYCOPY:
    case _C_ONEWAY:
	    return objc_alignof_type(type+1);

    case _C_LNGLNG:
	    return __alignof__(long long);

    case _C_ULNGLNG:
	    return __alignof__(unsigned long long);
    
    default:
      PySys_WriteStderr("PyObjC: objc_align_type: Unhandled type '%c'\n", 
      	*type);
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

    case _C_CONST:
    case _C_IN:
    case _C_INOUT:
    case _C_OUT:
    case _C_BYCOPY:
    case _C_ONEWAY:
	    return objc_sizeof_type(type+1);

    case _C_LNGLNG:
	    return sizeof(long long);

    case _C_ULNGLNG:
	    return sizeof(unsigned long long);

    default:
      PySys_WriteStderr("PyObjC: objc_sizeof_type: Unhandled type '%c' (%d)\n", 
			*type, *type);
      abort();
    }
}

#endif

/*#F Returns a tuple of objects representing the content of a C array
  of type @var{type} pointed by @var{datum}. */
static PyObject *
pythonify_c_array (const char *type, void *datum)
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

      pyitem = pythonify_c_value (type, datum+offset);

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
pythonify_c_struct (const char *type, void *datum)
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

      pyitem = pythonify_c_value (item, datum+offset);

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

      snprintf (errmsg, sizeof(errmsg), ERRMSG, nitems, PyTuple_Size (arg));
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

      snprintf (errmsg, sizeof(errmsg), ERRMSG, nitems, PyTuple_Size (arg));
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
pythonify_c_value (const char *type, void *datum)
{
  PyObject *retobject = NULL;

  type = objc_skip_type_qualifiers (type);

  switch (*type)
    {
    case _C_LNGLNG: case _C_ULNGLNG:
      retobject = (PyObject*) PyLong_FromLongLong(*(long long*)datum);
      break;

    case _C_CHR:
    case _C_UCHR:
      retobject = (PyObject *) PyInt_FromLong ((int) (*(char *) datum));
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
        retobject = Py_None;
        Py_INCREF (retobject);
      }
      else
      {
        if ([obj isKindOfClass:[OC_PythonArray class]])
        {
          retobject = [(OC_PythonArray *)obj pyObject];
          Py_INCREF(retobject);
        }
        else if ([obj isKindOfClass:[OC_PythonDictionary class]])
        {
          retobject = [(OC_PythonDictionary *)obj pyObject];
          Py_INCREF(retobject);
        }
        else if ([obj isKindOfClass:[NSString class]])
        {
          /* All string classes seem to be subclasses of NSString.
          * We convert to a python string where possible, and a python
          * unicode object otherwise.
          * XXX: are we too smart here?
          */
          NSData* data = [(NSString*)obj dataUsingEncoding:NSASCIIStringEncoding];
          if (data == NULL) {
            const char* utf8 = [(NSString*)obj UTF8String];

            retobject = PyUnicode_DecodeUTF8(utf8, strlen(utf8), "strict");
          } else {
            retobject = PyString_FromStringAndSize(
                                                   [data bytes], [data length]);
          }
        }
        else if ([obj conformsToProtocol:@protocol (PythonObject)])
        {
          retobject = [(OC_PythonObject *) obj pyObject];
          Py_INCREF(retobject);
        }

        else if (ObjC_HasPythonImplementation(obj))
        {
          retobject =  ObjC_GetPythonImplementation(obj);
	  OC_CheckRevive(retobject);
          Py_INCREF(retobject);
        }
	else if (ISCLASS(obj))
	{
	  retobject = (PyObject*) ObjCClass_New((Class)obj);
	}
        else
        {
          retobject = (PyObject *) ObjCObject_New (obj);
        }
      }
      break;
    }

    case _C_SEL:
	/* Ronald: We don't have a seperate type for methods that are not 
	 * bound to a class, may need to add this, but using strings probably
	 * works just as well.
	 */
#if 0
      retobject = (PyObject *) ObjCMethod_new_with_selector (NULL,
                                                             *(SEL *) datum);
#else
      retobject = PyString_FromString(SELNAME(*(SEL*)datum));
#endif

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
          retobject = (PyObject *) ObjCClass_New(c);
        break;
      }

    case _C_PTR:
      retobject = (PyObject *) ObjCPointer_new (*(void **) datum, type+1);
      break;
      
    case _C_UNION_B:
      {
        unsigned int size = objc_sizeof_type (type);
        retobject = PyString_FromStringAndSize ((void*)datum, size);
        break;
      }
    
    case _C_STRUCT_B:
      retobject = pythonify_c_struct (type, datum);
      break;

    case _C_ARY_B:
      retobject = pythonify_c_array (type, datum);
      break;

    case _C_VOID:
      retobject = Py_None;
      Py_INCREF (retobject);
      break;

    default:
	ObjCErr_Set(ObjCExc_error, 
		"pythonify_c_value: unhandled value type (%c|%d|%s)",
		*type, *type, *type);
        break;
    }

  return retobject;
}

#if 0 /* def OBJC_WITH_ARGUMENTS_ARENA */
 /* Ronald: The arguments arena is not the right way (tm) to deal with
  * pointer arguments. You'll have to have additional knowlegde about a pointer
  * to know how to deal with it.
  *
  * For now we try to do without support for _C_PTR in this file, except for
  * special support in 'execute_and_pythonify_objc_method'. Datastructures
  * containing pointers require custom C code for now.
  */

#ifdef WITH_THREAD
#warning Does not support multiple threads yet.
#endif

/* This is used as an array of pointers: both the memory for the array
   and that for each array's slot is dynamically allocated with malloc().
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

#endif /* OBJC_WITH_ARGUMENTS_ARENA */

const char *
depythonify_c_value (const char *type, PyObject *argument, void *datum)
{
  const char *error = NULL;

  /* Pass by reference output arguments are sometimes passed a NULL pointer,
   * this surpresses a core dump.
   */
  if (!datum) return error;

  type = objc_skip_type_qualifiers (type);
  
  switch (*type)
    {
    case _C_LNGLNG: case _C_ULNGLNG:
      if (PyInt_Check(argument)) {
	      *(long long*)datum = PyInt_AsLong(argument);
      } else if (PyLong_Check(argument)) {
      	      if (*type == _C_LNGLNG) {
		      *(long long*)datum = PyLong_AsLongLong(argument);
	      } else {
		      *(unsigned long long*)datum = PyLong_AsUnsignedLongLong(argument);
	      }
      }
      break;
    case _C_CHR:
      if (! PyString_Check (argument) &&
          ! PyInt_Check (argument) )
	  {
        error = "a string or an integer";
	  }
      else
        if (PyInt_Check (argument) || PyBool_Check(argument))
          *(char *) datum = PyInt_AsLong (argument);
        else
          *(char *) datum = PyString_AsString (argument)[0];
      break;

    case _C_UCHR:
      if (! PyString_Check (argument) &&
          ! PyInt_Check (argument) &&
          ! PyBool_Check (argument))
        error = "a string or an integer";
      else
        if (PyInt_Check (argument) || PyBool_Check(argument))
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
      else if (ObjCClass_Check (argument))
        *(id *) datum = (id)ObjCClass_GetClass(argument);
      else if (ObjCObject_Check (argument)) {
        *(id *) datum = ObjCObject_GetObject(argument);
      } else if (PyString_Check (argument))
        {
	/* We should probably translate to unicode using the default python
	 * encoding (which is ASCII and may be different from the NSString
	 * default encoding)
	 */
	*(id *) datum = [NSString 
			stringWithCString:PyString_AS_STRING(argument)
				  length:PyString_GET_SIZE(argument)];
	}
      else if (PyUnicode_Check(argument)) 
	{
		PyObject* utf8 = PyUnicode_AsUTF8String(argument);

		if (utf8) {
			*(id *) datum = [NSString 
				stringWithUTF8String:PyString_AS_STRING(utf8)];
			Py_DECREF(utf8);
		} else {
			error = "Cannot convert Unicode string";
		}
	}
      else if (PyInt_Check (argument))
	*(id *) datum = [NSNumber numberWithLong:PyInt_AS_LONG (argument)];
      else if (PyFloat_Check (argument))
	*(id *) datum = [NSNumber numberWithDouble:PyFloat_AS_DOUBLE (argument)];
      else if (PyLong_Check(argument)) 
	*(id *) datum = [NSNumber numberWithLongLong:PyLong_AsLongLong(argument) ];
      else if (PyList_Check(argument) || PyTuple_Check(argument))  
	*(id *) datum = [OC_PythonArray newWithPythonObject:argument];
      else if (PyDict_Check(argument))  
	*(id *) datum = [OC_PythonDictionary newWithPythonObject:argument];
      else
        *(id *) datum = [OC_PythonObject newWithObject:argument];

      break;

    case _C_CLASS:
      if (ObjCClass_Check(argument)) 
	      *(Class*) datum = ObjCClass_GetClass(argument);
      else if (argument == Py_None) 
	      *(Class*) datum = nil;
      else
        error = "a ObjC class or None";

      break;

    case _C_SEL:
      if (! ObjCSelector_Check (argument) && ! PyString_Check (argument))
        error = "a ObjC method or a string";
      else
        if (ObjCSelector_Check (argument))
          *(SEL *) datum = ObjCSelector_Selector(argument); 
        else
          {
            char *selname = PyString_AsString (argument);
            SEL sel = SELUID (selname);

	    if (sel) 
	      *(SEL*) datum = sel;
	    else
	      error = "cannot register selector name";
          }
      break;

 
    case _C_PTR:
	/* Pointers are hard and the code below
	 * (1) Uses PyString in an unsafe way
	 * (2) Is not threadsafe
	 * (3) Is not needed for *most* Cocoa code
	 *     [We should only get here for pointers inside data structures]
	 */
#if 0 /* def OBJC_WITH_ARGUMENTS_ARENA */
      if (PyString_Check (argument))
        {
	  /* XXX: The use of PyString here is outdated! Python strings cache
	   * their hashvalue. If this depythonified value is used as an output
	   * parameter that cached hashvalue will most likely be incorrect. 
	   * And then there's string interning...
	   */
	  if (*(type+1) != _C_VOID)
	    {
	      unsigned int expected_size = objc_sizeof_type (++type);
	      
	      if (expected_size != PyString_Size (argument))
		{
#define ERRMSG "a string of size %d instead of %d"
		  static char errmsg[sizeof (ERRMSG)+6+6];
		  
		  snprintf (errmsg, sizeof(errmsg), ERRMSG, expected_size, PyString_Size (argument));
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

#else /* !OBJC_WITH_ARGUMENTS_ARENA */

      if (ObjCPointer_Check (argument))
        *(void **) datum = ((ObjCPointer *) argument)->ptr;
      else
	error = "nested pointers unimplemented";

#endif /* !OBJC_WITH_ARGUMENTS_ARENA */


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

              snprintf (errmsg, sizeof(errmsg), ERRMSG, expected_size, PyString_Size (argument));
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

        snprintf (msg, sizeof(msg), ERRMSG, *type);
        error = msg;
        break;
#undef ERRMSG
      }
    }

  return error;
}

/*
 * This function is used to call the objective-C implementation of a method.
 * We use an NSInvocation for convenience (1).
 *
 * This method can process pass-by-reference arguments. When the signature 
 * contains specifiers for wether those arguments are in, out or inout 
 * parameters that information is used to determine wether the argument must
 * be present in the python call (in and inout) and wether the argument must 
 * be returned to the user (inout and out). If the extra information is not
 * available the argument is assumed to be an inout argument.
 *
 * TODO:
 * - Remove all references to an argument arena in the rest of this file 
 * - But: argument arena's are used for all pointers, not only for pass-by-
 *   reference arguments but also for pointers in structs/arrays/...
 * - Deal with return values that are pointers
 * - Deal with pointer arguments that are arrays (probably need to add special
 *   markup to say 'this is a pointer to X values, where X is the Yth argument')
 * - At the moment we cannot override methods with pass-by-reference arguments
 *   (stub-generator doesn't deal with those)
 *
 * Footnotes
 * 1. It may be better to directly call objc_sendMessage or even 
 *    objc_sendMessageSuper, but that would require us to use libffi-style
 *    technology (or rely on platform specific tricks like DllCall uses).
 *    If we'd directly call objc_sendMessageSuper we can use the same function
 *    for normal and 'super-method' calls.
 *
 * FIXME: Alignment is not dealt with.
 */
PyObject *
execute_and_pythonify_objc_method (PyObject *aMeth, PyObject* self, PyObject *args)
{
	size_t            argbuf_len = 0;
	size_t            argbuf_cur = 0;
	unsigned char*    argbuf = NULL;	/* by-reference arguments */
	size_t            byref_in_count = 0;
	size_t            byref_out_count = 0;
	size_t            plain_count = 0;
	size_t            objc_argcount;
	size_t            py_arg;
	int               i;
	int*		  byref = NULL; /* offset for arguments in argbuf */
	NSInvocation*     inv = nil;
	const char* 	  rettype;
	NSMethodSignature*  methinfo;
	ObjCNativeSelector* meth = (ObjCNativeSelector*)aMeth;
	PyObject*	  objc_result = NULL;
	PyObject*	  result = NULL;
	id		  self_obj = nil;
	id                nil_obj = nil;
	const char*	  curspec;

	if (meth->sel_oc_signature) {
		methinfo = meth->sel_oc_signature;
	} else {
	 	methinfo = [NSMethodSignature signatureWithObjCTypes:meth->sel_signature];
		meth->sel_oc_signature = methinfo;
	}

	/* First count the number of by reference parameters, and the number
	 * of bytes of storage needed for them. Note that arguments 0 and 1
	 * are self and the selector, no need to count counted or checked those.
	 */
	objc_argcount = 0;
	for (curspec = objc_skip_typespec(meth->sel_signature), i=0; *curspec; curspec = objc_skip_typespec(curspec), i++) {
		const char *argtype = curspec;
		objc_argcount += 1;

		if (i < 2) continue;

		switch (*argtype) {
		case _C_PTR: 
			byref_in_count ++;
			byref_out_count ++;
			argbuf_len += objc_sizeof_type(argtype+1);
			break;

		case _C_INOUT:
			if (argtype[1] == _C_PTR) {
				byref_out_count ++;
				byref_in_count ++;
				argbuf_len += objc_sizeof_type(argtype+2);
			}
			break;

		case _C_IN: case _C_CONST:
			if (argtype[1] == _C_PTR) {
				byref_in_count ++;
				argbuf_len += objc_sizeof_type(argtype+2);
			}
			break;

		case _C_OUT:
			if (argtype[1] == _C_PTR) {
				byref_out_count ++;
				argbuf_len += objc_sizeof_type(argtype+2);
			}
			break;

		case _C_STRUCT_B: case _C_UNION_B: case _C_ARY_B:
			plain_count++;
			argbuf_len += objc_sizeof_type(argtype);
			break;

		default:
			plain_count++;
			break;
		}
	}

	/* 
	 * We need input arguments for every normal argument and for every
	 * input argument that is passed by reference.
	 */
	if (PyTuple_Size(args) != (plain_count + byref_in_count)) {
		ObjCErr_Set(PyExc_TypeError, "Need %d arguments, got %d",
			plain_count + byref_in_count, PyTuple_Size(args));
		goto error_cleanup;
	}

	if (argbuf_len) {
		argbuf = alloca(argbuf_len);
		if (argbuf == 0) {
			PyErr_NoMemory();
			goto error_cleanup;
		}
		byref = alloca(sizeof(int) * objc_argcount);
		if (byref == NULL) {
			PyErr_NoMemory();
			goto error_cleanup;
		}
		
	} else {
		argbuf = NULL;
		byref = NULL;
	}

	/* Allocate the invocation. We 'retain' the invocation to avoid 
	 * loosing it prematurely when this happens to be a call to the 
	 * dealloc function of an NSAutoreleasePool
	 */
	inv = [NSInvocation invocationWithMethodSignature:methinfo];
	[inv retain]; 


	/* Set 'self' argument, for class methods we use the class */ 
	if (meth->sel_flags & ObjCSelector_kCLASS_METHOD) {
		if (ObjCObject_Check(self)) {
			self_obj = GETISA(ObjCObject_GetObject(self));
		} else if (ObjCClass_Check(self)) {
			self_obj = ObjCClass_GetClass(self);
		} else {
			PyErr_SetString(PyExc_TypeError, 
				"Need objective-C object or class as self");
			goto error_cleanup;
		}
	} else {
		const char* err;

		if (ObjCObject_Check(self)) {
			self_obj = ObjCObject_GetObject(self);

		} else {
			err = depythonify_c_value("@", self, &self_obj);
			if (err) {
				PyErr_SetString(PyExc_TypeError, 
					"Need objective-C object as self");
				goto error_cleanup;
			}
		}
	}

	[inv setTarget:self_obj];
	[inv setSelector:meth->sel_selector];

	py_arg = 0;
	for (curspec = objc_skip_typespec(meth->sel_signature), i = 0; *curspec; curspec = objc_skip_typespec(curspec), i ++) {
		const char* error;
		PyObject *argument;
		const char *argtype = curspec;

		if (i < 2) continue; /* Skip self, _sel */

		if (argtype[0] == _C_OUT && argtype[1] == _C_PTR) {
			/* Just allocate room in argbuf and set that*/
			void* arg;
			byref[i] = argbuf_cur;
			arg = argbuf + argbuf_cur;
	  		[inv setArgument:&arg atIndex:i];

			argbuf_cur += objc_sizeof_type(argtype+2);
		} else {
			/* Encode argument, maybe after allocating space */
			char argbuffer[objc_sizeof_type (argtype)];

			if (argtype[0] == _C_OUT) argtype ++;

			argument = PyTuple_GET_ITEM (args, py_arg);
			switch (*argtype) {
			case _C_STRUCT_B: case _C_ARY_B: case _C_UNION_B:
				/* Allocate space and encode */
				{
					void* arg = argbuf + argbuf_cur;
					argbuf_cur += objc_sizeof_type(argtype);
					byref[i] = argbuf_cur;
	  				error = depythonify_c_value (
						argtype, 
						argument, 
						arg);

					if (!error) {
						[inv setArgument:arg atIndex:i];
					}
				} 
				break;

			case _C_PTR:
				/* Allocate space and encode */
				{
					void* arg = argbuf + argbuf_cur;
					argbuf_cur += objc_sizeof_type(argtype+2);
					byref[i] = argbuf_cur;
	  				error = depythonify_c_value (
						argtype+2, 
						argument, 
						arg);

					if (!error) {
						[inv setArgument:&arg atIndex:i];
					}
				} 
				break;

			case _C_INOUT:
			case _C_IN:
			case _C_CONST:
				if (argbuf[1] == _C_PTR) {
					/* Allocate space and encode */
					void* arg = argbuf + argbuf_cur;
					argbuf_cur += objc_sizeof_type(argtype+2);
					byref[i] = argbuf_cur;
	  				error = depythonify_c_value (
						argtype+2, 
						argument, 
						arg);

					if (!error) {
						[inv setArgument:&arg atIndex:i];
					}
				} else {
					/* just encode */
	  				error = depythonify_c_value (
						argtype+1, 
						argument, 
						argbuffer);
					if (!error) {
						[inv setArgument:argbuffer atIndex:i];
					}
				}
				break;
			default:
	  			error = depythonify_c_value (
					argtype, 
					argument, 
					argbuffer);
				if (!error) {
					[inv setArgument:argbuffer atIndex:i];
				}
			}

			if (error) {
				const char* typeend = objc_skip_typespec(argtype);
				ObjCErr_Set(PyExc_TypeError,
					"expected %s for argument %d: its "
					"typespec is '%.*s'",
					error, py_arg+1, typeend-argtype, argtype);
				goto error_cleanup;
			}
			py_arg++;
		}
	}

	PyErr_Clear();
	NS_DURING
		[inv invoke];
	NS_HANDLER
		ObjCErr_FromObjC(localException);
	NS_ENDHANDLER
	if (PyErr_Occurred()) goto error_cleanup;

	rettype = meth->sel_signature; 
	if ( (*rettype != _C_VOID) && ([methinfo isOneway] == NO) )
	{
		char *retbuffer = alloca (objc_sizeof_type(rettype));

		[inv getReturnValue:retbuffer];

		objc_result = pythonify_c_value (rettype, retbuffer);
	} else {
		Py_INCREF(Py_None);
		objc_result =  Py_None;
	}

	if ( (meth->sel_flags & ObjCSelector_kRETURNS_SELF)
		&& (objc_result != self)) {

		/* meth is a method that returns a possibly reallocated
		 * version of self and self != return-value, the current
		 * value of self is assumed to be no longer valid
		 */
		ObjCObject_ClearObject(self);
	}


	if (byref_out_count == 0) {
		result = objc_result;
	} else {
		result = PyTuple_New(byref_out_count+1);
		if (result == 0) goto error_cleanup;

		if (PyTuple_SetItem(result, 0, objc_result) < 0) {
			goto error_cleanup;
		}
		objc_result = NULL;

		py_arg = 1;
		for (curspec = objc_skip_typespec(meth->sel_signature), i = 0; *curspec; curspec = objc_skip_typespec(curspec), i ++) {
			const char *argtype = curspec;
			void*       arg;
			PyObject*   v;

			if (i < 2) continue;

			switch (*argtype) {
			case _C_PTR: 
				arg = argbuf + byref[i];
				v = pythonify_c_value(argtype+1, arg);
				if (!v) goto error_cleanup;
				if (PyTuple_SetItem(result, py_arg++, v) < 0) {
					Py_DECREF(v);
					goto error_cleanup;
				}
				break;

			case _C_INOUT:
			case _C_OUT:
				if (argtype[1] == _C_PTR) {
					arg = argbuf + byref[i];
					v = pythonify_c_value(argtype+2, arg);
					if (!v) goto error_cleanup;
					if (PyTuple_SetItem(result, 
							py_arg++, v) < 0) {
						Py_DECREF(v);
						goto error_cleanup;
					}
				}
				break;
			}
		}
	}

	self_obj = nil;
	if (*rettype == _C_ID) {
		[inv setReturnValue:&nil_obj];
	}
	[inv setTarget:nil];
	[inv release];
	inv = nil;

	argbuf = NULL;
	byref = NULL;
	methinfo = nil;
	
	return result;

error_cleanup:

	if (inv) {
		self_obj = nil;
		// FIXME: Shouldn't use this...
		if (*[methinfo methodReturnType] == _C_ID) {
			[inv setReturnValue:&self_obj];
		}
		[inv setTarget:nil];
		[inv release];
		inv = nil;
	}
	if (objc_result) {
		Py_DECREF(objc_result);
		objc_result = NULL;
	}
	if (result) {
		Py_DECREF(result);
		result = NULL;
	}
	return NULL;
}

#ifdef GNU_RUNTIME

Ivar_t class_getInstanceVariable(Class aClass, const char *name)
{
  if (!aClass || !name)
    return NULL;

  for (; aClass != Nil; aClass = aClass->super_class)
    {
      int i;

      if (!aClass->ivars)
	continue;

      for (i = 0; i < aClass->ivars->ivar_count; i++)
	{
	  if (!strcmp(aClass->ivars->ivar_list[i].ivar_name, name))
	    return &aClass->ivars->ivar_list[i];
	}
    }

  return NULL;
}

Ivar_t object_getInstanceVariable(id obj, const char *name, void **out)
{
  Ivar_t var = NULL;

  if (obj && name)
    {
      void **varIndex = NULL;

      if ((var = class_getInstanceVariable(obj->class_pointer, name)))
	varIndex = (void **)((char *)obj + var->ivar_offset);

      if (out)
	*out = *varIndex;
    }

  return var;
}

struct objc_method_list *class_nextMethodList(Class aClass, void **ptr)
{
  struct objc_method_list **list;

  list = (struct objc_method_list **)ptr;

  if (*list == NULL)
    *list = aClass->methods;
  else
    *list = (*list)->method_next;

  return *list;
}

Ivar_t object_setInstanceVariable(id obj, const char *name, void *value)
{
  Ivar_t var = NULL;

  if (obj && name)
    {
      void **varIndex;

      if ((var = class_getInstanceVariable(obj->class_pointer, name)))
	{
	  varIndex = (void **)((char *)obj + var->ivar_offset);

	  *varIndex = value;
	}
    }

  return var;
}

void objc_addClass(Class aClass)
{
#warning objc_addClass() not implemented !
}

id objc_msgSendSuper(struct objc_super *super, SEL op, ...)
{
  arglist_t arg_frame;
  Method *m_imp;
  const char *type;

  if (super->self)
    {
      arg_frame = __builtin_apply_args ();

      m_imp = class_get_instance_method(super->class, op);
      *((id*)method_get_first_argument (m_imp, arg_frame, &type)) = super->self;
      *((SEL*)method_get_next_argument (arg_frame, &type)) = op;
      return __builtin_apply((apply_t)m_imp,
			     arg_frame,
			     method_get_sizeof_arguments (m_imp));
    }

  return nil;
}

struct objc_method_list *objc_allocMethodList(int numMethods)
{
  struct objc_method_list *mlist;

  mlist = calloc(1, sizeof(struct objc_method_list)
		 + (numMethods) * sizeof(struct objc_method));

  return mlist;
}

void objc_freeMethodList(struct objc_method_list *list)
{
  struct objc_method_list *next;

  while (list)
    {
      next = list->method_next;

      free(list);

      list = next;
    }
}

#else

struct objc_method_list *objc_allocMethodList(int numMethods)
{
  struct objc_method_list *mlist;

  mlist = malloc(sizeof(struct objc_method_list)
		 + (numMethods) * sizeof(struct objc_method));

  if (mlist == NULL)
    return NULL;

  memset(mlist, 0, sizeof(struct objc_method_list)
	 + (numMethods) * sizeof(struct objc_method));

  mlist->method_count = 0;
  mlist->obsolete = NULL; /* DEBUG */

  return mlist;
}

void objc_freeMethodList(struct objc_method_list **list)
{
  if (list)
    {
      if (list[0])
	free(list[0]);

      free(list);
    }
}

#endif
