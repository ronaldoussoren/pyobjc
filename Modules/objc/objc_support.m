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

#ifdef MACOSX
/* OSX 10.1 doesn't define LLONG_MIN, LLONG_MAX and ULLONG_MAX */
#ifndef LLONG_MIN
#define LLONG_MIN (-0x7fffffffffffffffLL-1)
#define LLONG_MAX (-0x7fffffffffffffffLL)
#define ULLONG_MAX (-0xffffffffffffffffULL)
#endif
#endif

#import <Foundation/NSInvocation.h>
#import <Foundation/NSMethodSignature.h>
#import <Foundation/NSData.h> 
#import <Foundation/NSValue.h> 

#ifdef MACOSX
#include <CoreFoundation/CFNumber.h>
#endif /* MACOSX */

/*
 * Category on NSObject to make sure that every object supports 
 * the method  __pyobjc_PythonObject__, this helps to simplify
 * pythonify_c_value.
 *
 * The class-method is a experiment to do away with the ISCLASS 
 * test in pythonify_c_value.
 */
@interface NSObject (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
+(PyObject*)__pyobjc_PythonObject__;
@end /* PyObjCSupport */

@implementation NSObject (PyObjCSupport)

-(PyObject*)__pyobjc_PythonObject__
{
        return (PyObject *) PyObjCObject_New(self);
}

+(PyObject*)__pyobjc_PythonObject__
{
	return PyObjCClass_New(self);
}

@end /* PyObjCSupport */


@interface NSNumber (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
@end /* NSNumber (PyObjCSupport) */

@implementation NSNumber (PyObjCSupport)

-(PyObject*)__pyobjc_PythonObject__
{
	const char* typestr = [self objCType];
	char        buf[objc_sizeof_type(typestr)];

	[self getValue:buf];

#ifdef MACOSX
	/* NSNumber seems to be toll-free bridged to CFNumber,
	 * this check allows us to return the proper python objects
	 * for boolean True and False values.
	 */
	if (kCFBooleanTrue == (CFBooleanRef)self) {
		return PyObjCBool_FromLong(1);
	} else if (kCFBooleanFalse == (CFBooleanRef)self) {
		return PyObjCBool_FromLong(0);
	}
#endif
	return pythonify_c_value(typestr, buf);
}

@end /* NSNumber (PyObjCSupport) */

@interface NSString (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
@end /* NSString (PyObjCSupport) */

@implementation NSString (PyObjCSupport)

-(PyObject*)__pyobjc_PythonObject__
{
	return PyObjCUnicode_New(self);
}

@end /* NSString (PyObjCSupport) */



#ifndef MAX
#define MAX(x,y) ({ unsigned int __x=(x), __y=(y); (__x > __y ? __x : __y); })
#endif
static inline const int
ROUND(int v, int a)
{
	return a * ((v+a-1)/a);
}

static inline const char*
PyObjCRT_SkipTypeQualifiers (const char* type)
{
	while (*type == _C_CONST ||
	       *type == _C_IN ||
	       *type == _C_INOUT ||
	       *type == _C_OUT ||
	       *type == _C_BYCOPY ||
	       *type == _C_ONEWAY) {
			type++;
	}
	return type;
}


const char * 
PyObjCRT_SkipTypeSpec (const char *type)

{
	type = PyObjCRT_SkipTypeQualifiers (type);

	switch (*type) {
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
		type = PyObjCRT_SkipTypeSpec (type);
		assert (*type == _C_ARY_E);
		++type;
		break;
      
	case _C_STRUCT_B:
		/* skip name, and elements until closing '}'  */
    
		while (*type != _C_STRUCT_E && *type++ != '=');
		while (*type != _C_STRUCT_E)
			type = PyObjCRT_SkipTypeSpec (type);
		++type;
		break;

	case _C_UNION_B:
		/* skip name, and elements until closing ')'  */
		type++;
		while (*type != _C_UNION_E) { type = PyObjCRT_SkipTypeSpec (type); }
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
		type = PyObjCRT_SkipTypeSpec (type+1);
		break;

    
	default:
		ObjCErr_Set(ObjCExc_internal_error,
			"PyObjCRT_SkipTypeSpec: Unhandled type '%#x'", *type); 
		abort();
		return NULL;
	}

	while (isdigit(*type)) type++;
	return type;
}

/*
  Return the alignment of an object specified by type 
*/

#ifndef GNU_RUNTIME

int
objc_alignof_type (const char *type)
{
	switch (*type) {
	case _C_ID:    return __alignof__ (id);
	case _C_CLASS: return __alignof__ (Class);
	case _C_SEL:   return __alignof__ (SEL);
	case _C_CHR:   return __alignof__ (char);
	case _C_UCHR:  return __alignof__ (unsigned char);
	case _C_SHT:   return __alignof__ (short);
	case _C_USHT:  return __alignof__ (unsigned short);
	case _C_INT:   return __alignof__ (int);
	case _C_UINT:  return __alignof__ (unsigned int);
	case _C_LNG:   return __alignof__ (long);
	case _C_ULNG:  return __alignof__ (unsigned long);
	case _C_FLT:   return __alignof__ (float);
	case _C_DBL:   return __alignof__ (double);
	case _C_CHARPTR: return __alignof__ (char *);
	case _C_PTR:   return __alignof__ (void *);
	case _C_LNGLNG: return __alignof__(long long);
	case _C_ULNGLNG: return __alignof__(unsigned long long);

	case _C_ARY_B:
		while (isdigit(*++type)) /* do nothing */;
		return objc_alignof_type (type);
      
	case _C_STRUCT_B:
	{
		/* The align of a struct is the largest alignment of one of 
		 * its members
		 */
		struct { int x; double y; } fooalign;
		while(*type != _C_STRUCT_E && *type++ != '=') /* do nothing */;
		if (*type != _C_STRUCT_E) {
			int    item_align;
			int    maxalign = 0;
			while (*type != _C_STRUCT_E) {
				item_align = objc_alignof_type(type);
				if (item_align == -1) return -1;
				type = PyObjCRT_SkipTypeSpec(type);
				maxalign = MAX(item_align, maxalign);
			}
			return maxalign;
		} else {
			return __alignof__ (fooalign);
		}
	}

	case _C_UNION_B:
	{
		int maxalign = 0;
		type++;
		while (*type != _C_UNION_E)
		{
			int item_align = objc_alignof_type(type);
			if (item_align == -1) return -1;
			maxalign = MAX (maxalign, item_align);
			type = PyObjCRT_SkipTypeSpec (type);
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

	default:
		ObjCErr_Set(ObjCExc_internal_error, 
			"objc_align_type: Unhandled type '%#x'", *type);
		abort();
		return -1;
	}
}

/*
  The aligned size if the size rounded up to the nearest alignment.
*/

static int
objc_aligned_size (const char *type)
{
	int size = objc_sizeof_type (type);
	int align = objc_alignof_type (type);

	if (size == -1 || align == -1) return -1;
	return ROUND (size, align);
}

/*
  return the size of an object specified by type 
*/

int
objc_sizeof_type (const char *type)
{
	int itemSize;
	switch (*type) {
	case _C_VOID:    return 0;
	case _C_ID:      return sizeof(id);
	case _C_CLASS:   return sizeof(Class);
	case _C_SEL:     return sizeof(SEL);
	case _C_CHR:     return sizeof(char);
	case _C_UCHR:    return sizeof(unsigned char);
	case _C_SHT:     return sizeof(short);
	case _C_USHT:    return sizeof(unsigned short);
	case _C_INT:     return sizeof(int);
	case _C_UINT:    return sizeof(unsigned int);
	case _C_LNG:     return sizeof(long);
	case _C_ULNG:    return sizeof(unsigned long);
	case _C_FLT:     return sizeof(float);
	case _C_DBL:     return sizeof(double);
	case _C_LNGLNG:  return sizeof(long long);
	case _C_ULNGLNG: return sizeof(unsigned long long);

	case _C_PTR:
	case _C_CHARPTR:
		return sizeof(char*);
      
	case _C_ARY_B:
	{
		int len = atoi(type+1);
		int item_align;
		while (isdigit(*++type))
			;
		item_align = objc_aligned_size(type);
		if (item_align == NULL) return -1;
		return len*item_align;
	}
	break; 
    
	case _C_STRUCT_B:
	{
		int acc_size = 0;
		int align;
		while (*type != _C_STRUCT_E && *type++ != '=')
			; /* skip "<name>=" */
		while (*type != _C_STRUCT_E) {
			align = objc_alignof_type (type); 
			if (align == -1) return -1;
			acc_size = ROUND (acc_size, align);
			itemSize = objc_sizeof_type (type); 
			if (itemSize == -1) return -1;
			acc_size += itemSize;
			type = PyObjCRT_SkipTypeSpec (type);
		}
		return acc_size;
	}
    
	case _C_UNION_B:
	{
		int max_size = 0;
		type++;
		while (*type != _C_UNION_E) {
			itemSize = objc_sizeof_type (type);
			if (itemSize == -1) return -1;
			max_size = MAX (max_size, itemSize);
			type = PyObjCRT_SkipTypeSpec (type);
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

	default:
		ObjCErr_Set(ObjCExc_internal_error, 
			"objc_sizeof_type: Unhandled type '%#x", *type);
		abort();
		return -1;
	}
}

#endif

/*#F Returns a tuple of objects representing the content of a C array
  of type @var{type} pointed by @var{datum}. */
static PyObject *
pythonify_c_array (const char *type, void *datum)
{
	PyObject *ret;
	unsigned int nitems, itemidx, sizeofitem;
	unsigned char* curdatum;
  
	nitems = atoi (type+1);
	while (isdigit (*++type))
		;
	sizeofitem = objc_sizeof_type (type);
	if (sizeofitem == -1) return NULL;

	ret = PyTuple_New (nitems);
	if (!ret) return NULL;

	curdatum = datum;
	for (itemidx=0; itemidx < nitems; itemidx++) {
		PyObject *pyitem = NULL;

		pyitem = pythonify_c_value (type, curdatum);

		if (pyitem) {
			PyTuple_SET_ITEM (ret, itemidx, pyitem);
		} else {
			Py_DECREF(ret);
			return NULL;
		}

		curdatum += sizeofitem;
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
	for (item=type, nitems=0; 
			*item != _C_STRUCT_E; 
			item = PyObjCRT_SkipTypeSpec (item)){
		nitems++;
	}

	ret = PyTuple_New (nitems);
	if (!ret) return NULL;

	for (item=type, offset=itemidx=0; 
			*item != _C_STRUCT_E; 
			item = PyObjCRT_SkipTypeSpec (item)){
		PyObject *pyitem;

		pyitem = pythonify_c_value (item, datum+offset);

		if (pyitem) {
			PyTuple_SET_ITEM (ret, itemidx, pyitem);
		} else {
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
static int
depythonify_c_array (const char *type, PyObject *arg, void *datum)
{
	unsigned int nitems, itemidx, sizeofitem;
	unsigned char* curdatum;

	nitems = atoi (type+1);
	while (isdigit (*++type))
		;
	sizeofitem = objc_aligned_size (type);
	if (sizeofitem == -1) {
		ObjCErr_Set(PyExc_ValueError, 
			"cannot depythonify array of unknown type");
		return -1;
	}

	if (nitems != PyTuple_Size (arg)) {
		ObjCErr_Set(PyExc_ValueError,
			"depythonifying array of %d items, got one of %d",
			nitems, PyTuple_Size(arg));
		return -1;
	}

	curdatum = datum;
	for (itemidx=0; itemidx < nitems; itemidx++) {
		PyObject *pyarg = PyTuple_GetItem (arg, itemidx);
		int err;

		err = depythonify_c_value (type, pyarg, curdatum);
		if (err == -1) return err;
      
		curdatum += sizeofitem;
	}

	return 0;
}

/*#F Extracts the elements from the tuple @var{arg} and fills a C structure
  of type @var{type} pointed by @var{datum}. Returns an error message, or
  NULL on success. */
static int
depythonify_c_struct (const char *types, PyObject *arg, void *datum)
{
	unsigned int nitems, offset, itemidx;
	const char *type;

	while (*types != _C_STRUCT_E && *types++ != '='); /* skip "<name>=" */
	for (type=types, nitems=0; 
			*type != _C_STRUCT_E; 
			type = PyObjCRT_SkipTypeSpec (type)){
		nitems++;
	}

	if (nitems != PyTuple_Size (arg)) {
		ObjCErr_Set(PyExc_ValueError,
			"depythonifying struct of %d members, got tuple of %d",
			nitems, PyTuple_Size (arg));
		return -1;
	}

	for (type=types, offset=itemidx=0; 
			*type != _C_STRUCT_E; 
			type = PyObjCRT_SkipTypeSpec (type)){
		PyObject *argument = PyTuple_GetItem (arg, itemidx);
		int error;

		error = depythonify_c_value (type, argument, datum+offset);
		if (error == -1) return error;
      
		itemidx++;
		offset += objc_sizeof_type (type);
	}
	return 0;
}

PyObject *
pythonify_c_value (const char *type, void *datum)
{
	PyObject *retobject = NULL;

	type = PyObjCRT_SkipTypeQualifiers (type);

	switch (*type) {
	case _C_CHR:
		// We don't return a string because BOOL is an alias for
		// char (at least on MacOS X)
		retobject = (PyObject*)PyInt_FromLong ((int)(*(char*)datum));
		break;

	case _C_UCHR:
		retobject = (PyObject*)PyInt_FromLong (
			(long)(*(unsigned char*)datum));
		break;

	case _C_CHARPTR:
	{
		char *cp = *(char **) datum;

		if (cp == NULL) {
			Py_INCREF(Py_None);
			retobject = Py_None;
		} else {
			retobject = (PyObject*)PyString_FromString(cp);
		}
		break;
	}

	case _C_INT:
		retobject = (PyObject *) PyInt_FromLong (*(int*) datum);
		break;

	case _C_UINT:
		if (*(unsigned int*)datum > LONG_MAX) {
			retobject = (PyObject*)PyLong_FromUnsignedLongLong(
				*(unsigned int*)datum);
		} else {
			retobject = (PyObject*)PyInt_FromLong (
				*(unsigned int *) datum);
		}
		break;

	case _C_SHT:
		retobject = (PyObject *) PyInt_FromLong (*(short *) datum);
		break;

	case _C_USHT:
		retobject = (PyObject *) PyInt_FromLong (
			*(unsigned short *) datum);
		break;

	case _C_LNG:
		retobject = (PyObject *) PyInt_FromLong (*(long *) datum);
		break;

	case _C_ULNG:
		if (*(unsigned long*)datum > LONG_MAX) {
			retobject = (PyObject*)PyLong_FromUnsignedLongLong(
				*(unsigned long*)datum);
		} else {
			retobject = (PyObject*)PyInt_FromLong (
				*(unsigned long*) datum);
		}
		break;

	case _C_ULNGLNG:
		retobject = (PyObject*)PyLong_FromUnsignedLongLong(
			*(unsigned long long*)datum);
		break;

	case _C_LNGLNG: 
		retobject = (PyObject*)PyLong_FromLongLong(*(long long*)datum);
		break;

	case _C_FLT:
		retobject = (PyObject *) PyFloat_FromDouble (*(float*) datum);
		break;

	case _C_DBL:
		retobject = (PyObject *) PyFloat_FromDouble (*(double*) datum);
		break;
      
	case _C_ID:
	{
		id obj = *(id *) datum;

		if (obj == nil) {
			retobject = Py_None;
			Py_INCREF (retobject);
		} else {
			retobject = [obj  __pyobjc_PythonObject__];
		}
		break;
	}

	case _C_SEL:
		if (*(SEL*)datum == NULL) {
			retobject = Py_None;
			Py_INCREF(retobject);
		} else {
			retobject = PyString_FromString(SELNAME(*(SEL*)datum)); 
		}
		break;

	case _C_CLASS:
	{
		Class c = *(Class *) datum;

		if (c == Nil) {
			retobject = Py_None;
			Py_INCREF (retobject);
		} else {
			retobject = (PyObject *) PyObjCClass_New(c);
		}
		break;
	}

	case _C_PTR:
		retobject = (PyObject*)PyObjCPointer_new(
			*(void**) datum, type+1);
		break;
      
	case _C_UNION_B:
	{
		int size = objc_sizeof_type (type);
		if (size == -1) return NULL;
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


int objc_sizeof_return_type(const char* type)
{
	switch(*type) {
	case _C_CHR:
	case _C_UCHR:
	case _C_SHT:
	case _C_USHT:
		return sizeof(int);
	default:
		return objc_sizeof_type(type);
	}
}

/*
 * Convert a python value to a basic C unsigned integer value.
 */
static int
depythonify_unsigned_int_value(PyObject* argument, char* descr,
	unsigned long long* out, unsigned long long max)
{
	if (PyInt_Check (argument)) {
		long temp = PyInt_AsLong(argument);
		if (temp < 0) {
			ObjCErr_Set(PyExc_ValueError,
				"depythonifying '%s', got negative '%s'",
					descr,
					argument->ob_type->tp_name);
			return -1;

		} else if (temp > max) {
			ObjCErr_Set(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					argument->ob_type->tp_name);
			return -1;
		}
		*out = temp;
		return 0;

	} else if (PyLong_Check(argument)) {
		*out = PyLong_AsUnsignedLongLong(argument);
		if (PyErr_Occurred()) {
			ObjCErr_Set(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					argument->ob_type->tp_name);
			return -1;
		}

		if (*out > max) {
			ObjCErr_Set(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					argument->ob_type->tp_name);
			return -1;
		}
		return 0;

	} else {
		PyObject* tmp = PyNumber_Long(argument);
		if (tmp != NULL) {
			*out = PyLong_AsUnsignedLongLong(tmp);
			Py_DECREF(tmp);

			if (*out <= max) {
				return 0;
			}
		}

		ObjCErr_Set(PyExc_ValueError,
			"depythonifying '%s', got '%s' of %d",
				descr,
				argument->ob_type->tp_name,
				PyString_Size(argument));
		return -1;
	}
}

/*
 * Convert a python value to a basic C signed integer value.
 */
static int
depythonify_signed_int_value(PyObject* argument, char* descr,
	long long* out, long long min, long long max)
{
	if (PyInt_Check (argument)) {
		*out = (long long)PyInt_AsLong(argument);
		if (*out < min || *out > max) {
			ObjCErr_Set(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					argument->ob_type->tp_name);
			return -1;
		}
		return 0;

	} else if (PyLong_Check(argument)) {
		*out = PyLong_AsLongLong(argument);
		if (PyErr_Occurred()) {
			ObjCErr_Set(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					argument->ob_type->tp_name);
			return -1;
		}

		if (*out < min || *out > max) {
			ObjCErr_Set(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					argument->ob_type->tp_name);
			return -1;
		}
		return 0;

	} else {
		PyObject* tmp = PyNumber_Long(argument);
		if (tmp != NULL) {
			*out = PyLong_AsLongLong(tmp);
			Py_DECREF(tmp);

			if (*out >= min && *out <= max) {
				return 0;
			}
		}

		ObjCErr_Set(PyExc_ValueError,
			"depythonifying '%s', got '%s' of %d",
				descr,
				argument->ob_type->tp_name,
				PyString_Size(argument));
		return -1;
	}
}

int depythonify_c_return_value(
	const char* type, PyObject* argument, void* datum)
{
	long long temp;
	unsigned long long utemp;
	int       r;

	switch (*type) {
	case _C_CHR: 
		if (PyString_Check(argument) && PyString_Size(argument) == 1) {
			*(int*) datum = PyString_AsString (argument)[0];
			return 0;
		}

		r = depythonify_signed_int_value(argument, "char",
			&temp, CHAR_MIN, CHAR_MAX);
		if (r == 0) {
			*(int*)datum = temp;
		}
		return r;

	case _C_UCHR:
		if (PyString_Check(argument) && PyString_Size(argument) == 1) {
			*(unsigned int*) datum = 
				PyString_AsString (argument)[0];
			return 0;
		}
		r = depythonify_unsigned_int_value(argument, "unsigned short",
			&utemp, UCHAR_MAX);
		if (r == 0) {
			*(unsigned int*)datum = utemp;
		}
		return r;

	case _C_SHT:
		r = depythonify_signed_int_value(argument, "short",
			&temp, SHRT_MIN, SHRT_MAX);
		if (r == 0) {
			*(int*)datum = temp;
		}
		return r;

	case _C_USHT:
		r = depythonify_unsigned_int_value(argument, "unsigned short",
			&utemp, USHRT_MAX);
		if (r == 0) {
			*(unsigned int*)datum = utemp;
		}
		return r;

	default:
		return depythonify_c_value(type, argument, datum);
	}
}

PyObject *
pythonify_c_return_value (const char *type, void *datum)
{
static  const char intType[] = { _C_INT, 0 };
static  const char uintType[] = { _C_UINT, 0 };

	switch(*type) {
	case _C_CHR: 
	case _C_SHT:
		return pythonify_c_value(intType, datum);
	case _C_UCHR: case _C_USHT:
		return pythonify_c_value(uintType, datum);

	default:
		return pythonify_c_value(type, datum);
	}
}


int
depythonify_c_value (const char *type, PyObject *argument, void *datum)
{
	/* Pass by reference output arguments are sometimes passed a NULL 
	 * pointer, this surpresses a core dump.
	 */
	long long temp;
	unsigned long long utemp;
	int       r;

	if (!datum) return 0;

	type = PyObjCRT_SkipTypeQualifiers (type);
  
	switch (*type) {
	case _C_CHARPTR:
		if (!PyString_Check (argument) && argument != Py_None) {
			ObjCErr_Set(PyExc_ValueError,
				"depythonifying 'charptr', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		} else if (argument == Py_None) {
			*(char **) datum = NULL;
		} else {
			*(char **) datum = PyString_AS_STRING(
				(PyStringObject*)argument);
		}
		break;

	case _C_CHR:
		if (PyString_Check(argument) && PyString_Size(argument) == 1) {
			*(char*) datum = PyString_AsString (argument)[0];
			return 0;
		}

		r = depythonify_signed_int_value(argument, "char",
			&temp, CHAR_MIN, CHAR_MAX);
		if (r == 0) {
			*(char*)datum = temp;
		}
		return r;

	case _C_UCHR:
		if (PyString_Check(argument) && PyString_Size(argument) == 1) {
			*(unsigned char*) datum = 
				PyString_AsString (argument)[0];
			return 0;
		}
		r = depythonify_unsigned_int_value(argument, "unsigned short",
			&utemp, UCHAR_MAX);
		if (r == 0) {
			*(unsigned char*)datum = utemp;
		}
		return r;

	case _C_SHT:
		r = depythonify_signed_int_value(argument, "short",
			&temp, SHRT_MIN, SHRT_MAX);
		if (r == 0) {
			*(short*)datum = temp;
		}
		return r;

	case _C_USHT:
		r = depythonify_unsigned_int_value(argument, "unsigned short",
			&utemp, USHRT_MAX);
		if (r == 0) {
			*(unsigned short*)datum = utemp;
		}
		return r;

	case _C_INT:
		r = depythonify_signed_int_value(argument, "int",
			&temp, INT_MIN, INT_MAX);
		if (r == 0) {
			*(int*)datum = temp;
		}
		return r;

	case _C_UINT:
		r = depythonify_unsigned_int_value(argument, "unsigned int",
			&utemp, UINT_MAX);
		if (r == 0) {
			*(unsigned int*)datum = utemp;
		}
		return r;

	case _C_LNG:
		r = depythonify_signed_int_value(argument, "long",
			&temp, LONG_MIN, LONG_MAX);
		if (r == 0) {
			*(long*)datum = temp;
		}
		return r;

	case _C_ULNG:
		r = depythonify_unsigned_int_value(argument, "unsigned long",
			&utemp, ULONG_MAX);
		if (r == 0) {
			*(unsigned long*)datum = utemp;
		}
		return r;

	case _C_LNGLNG:
		r = depythonify_signed_int_value(argument, "long long",
			&temp, LLONG_MIN, LLONG_MAX);
		if (r == 0) {
			*(long long*)datum = temp;
		}
		return r;

	case _C_ULNGLNG:
		r = depythonify_unsigned_int_value(argument, 
			"unsigned long long", &utemp, ULLONG_MAX);
		if (r == 0) {
			*(unsigned long long*)datum = utemp;
		}
		return r;

	case _C_ID:
		if (argument == Py_None) {
			*(id *) datum = nil;
		} else if (PyObjCClass_Check (argument)) {
			*(id *) datum = (id)PyObjCClass_GetClass(argument);
		} else if (PyObjCObject_Check (argument)) {
			*(id *) datum = PyObjCObject_GetObject(argument);
		} else if (PyString_Check (argument)) {
			/* NSString values are Unicode strings, convert 
			 * the string to Unicode, assuming the default encoding.
			 */
			unsigned char* strval;
			int   len;
			PyObject* as_unicode;
			PyObject* as_utf8;

			strval = (unsigned char*)PyString_AS_STRING(argument);
			len = PyString_GET_SIZE(argument);

			as_unicode = PyUnicode_Decode(
				strval, 
				len, 
				PyUnicode_GetDefaultEncoding(), 
				"strict");
			if (as_unicode == NULL) {
				ObjCErr_Set(PyExc_UnicodeError,
					"depythonifying 'id', got "
					"a string with a non-default "
					"encoding");
				return -1;
			}

			as_utf8 = PyUnicode_AsUTF8String(as_unicode);
			Py_DECREF(as_unicode);

			if (as_utf8) {
				*(id *) datum = [NSString 
					stringWithUTF8String:
						PyString_AS_STRING(as_utf8)];
				Py_DECREF(as_utf8);
			} else {
				ObjCErr_Set(PyExc_ValueError,
					"depythonifying 'id', failed "
					"to encode unicode string to UTF8");
				return -1;
			}
		} else if (PyObjCUnicode_Check(argument)) {
			*(id*) datum = PyObjCUnicode_Extract(argument);
		} else if (PyUnicode_Check(argument)) {
			PyObject* utf8 = PyUnicode_AsUTF8String(argument);

			if (utf8) {
				*(id *) datum = [NSString 
					stringWithUTF8String:
						PyString_AS_STRING(utf8)];
				Py_DECREF(utf8);
			} else {
				ObjCErr_Set(PyExc_ValueError,
					"depythonifying 'id', failed "
					"to encode unicode string to UTF8");
				return -1;
			}

		} else if (PyObjCBool_Check(argument)) {
			*(id *) datum = [NSNumber 
				numberWithBool:PyInt_AS_LONG (argument)];
		} else if (PyInt_Check (argument)) {
			*(id *) datum = [NSNumber 
				numberWithLong:PyInt_AS_LONG (argument)];
		} else if (PyFloat_Check (argument)) {
			*(id *) datum = [NSNumber 
				numberWithDouble:PyFloat_AS_DOUBLE (argument)];
		} else if (PyLong_Check(argument)) {
			/* XXX: What if the value doesn't fit into a 
			 * 'long long' 
			 */
			*(id *) datum = [NSNumber 
				numberWithLongLong:PyLong_AsLongLong(argument)];
			if (PyErr_Occurred()) {
				/* Probably overflow */
				return -1;
			}
		} else if (PyList_Check(argument) || PyTuple_Check(argument)) {
			*(id *) datum = [OC_PythonArray 
				newWithPythonObject:argument];
		} else if (PyDict_Check(argument)) {
			*(id *) datum = [OC_PythonDictionary 
				newWithPythonObject:argument];
		} else {
#ifdef MACOSX
			*(id*) datum = PyObjC_CFTypeToID(argument);
			if (*(id*)datum != NULL) {
				/* BUG! for some reason the unittests fail
				 * without this retain. This needs further
				 * investigation, as this doesn't look
				 * correct to me
				 */
				[*(id*)datum retain];
				return 0;
			}
#endif /* MACOSX */

			*(id *) datum = [OC_PythonObject 
				newWithObject:argument];
		}
		break;

	case _C_CLASS:
		if (PyObjCClass_Check(argument))  {
			*(Class*) datum = PyObjCClass_GetClass(argument);
		} else if (argument == Py_None) {
			*(Class*) datum = nil;
		} else {
			ObjCErr_Set(PyExc_ValueError,
				"depythonifying 'Class', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		}
		break;

	case _C_SEL:
		if (argument == Py_None) {
			*(SEL*)datum = NULL;
		} if (ObjCSelector_Check (argument)) {
			*(SEL *) datum = ObjCSelector_Selector(argument); 
        	} else if (PyString_Check(argument)) {
			char *selname = PyString_AsString (argument);
			SEL sel = SELUID (selname);

			if (sel)  {
				*(SEL*) datum = sel;
			} else {
				ObjCErr_Set(PyExc_ValueError,
					"depythonifying 'SEL', cannot "
					"register string with runtime");
				return -1;
			}
		} else {
			ObjCErr_Set(PyExc_ValueError,
				"depythonifying 'SEL', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		}
		break;

 
	case _C_PTR:
		if (PyObjCPointer_Check (argument)) {
			*(void **) datum = ((PyObjCPointer *) argument)->ptr;
		} else {
			ObjCErr_Set(PyExc_ValueError,
				"depythonifying 'pointer', got '%s'",
					argument->ob_type->tp_name);
			abort();
			return -1;
		}
		break;

	case _C_FLT:
		if (PyFloat_Check (argument)) {
			*(float *) datum = (float)PyFloat_AsDouble (argument);
		} else if (PyInt_Check (argument)) {
			*(float *) datum = (float) PyInt_AsLong (argument);
		} else {
			PyObject* tmp = PyNumber_Float(argument);
			if (tmp != NULL) {
				double temp = PyFloat_AsDouble(tmp);
				Py_DECREF(tmp);
				*(float*) datum = temp;
				return 0;
			}

			ObjCErr_Set(PyExc_ValueError,
				"depythonifying 'float', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		}
		break;

	case _C_DBL:
		if (PyFloat_Check (argument)) {
			*(double *) datum = PyFloat_AsDouble (argument);
		} else if (PyInt_Check (argument)) {
			*(double *) datum = (double) PyInt_AsLong (argument);
		} else {
			PyObject* tmp = PyNumber_Float(argument);
			if (tmp != NULL) {
				double temp = PyFloat_AsDouble(tmp);
				Py_DECREF(tmp);
				*(double*) datum = temp;
				return 0;
			}

			ObjCErr_Set(PyExc_ValueError,
				"depythonifying 'double', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		}
		break;

	case _C_UNION_B:
		if (PyString_Check (argument)) {
			unsigned int expected_size = objc_sizeof_type (type);

			if (expected_size == (unsigned int)-1) {
				ObjCErr_Set(PyExc_ValueError,
					"depythonifying 'union' of "
					"unknown size");
				return -1;
			} else if (expected_size != PyString_Size (argument)) {
				ObjCErr_Set(PyExc_ValueError,
					"depythonifying 'union' of size %d, "
					"got string of %d",
					       expected_size, 
					       PyString_Size (argument));
				return -1;
			} else {
			    memcpy ((void *) datum, 
			    	PyString_AS_STRING (argument), 
				expected_size);
			}
		} else {
			ObjCErr_Set(PyExc_ValueError,
				"depythonifying 'union', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		}
		break;

	case _C_STRUCT_B:
		if (! PyTuple_Check (argument)) {
			ObjCErr_Set(PyExc_ValueError,
				"depythonifying 'struct', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		} else {
			return depythonify_c_struct (type, argument, datum);
		}
		break;

	case _C_ARY_B:
		if (! PyTuple_Check (argument)) {
			ObjCErr_Set(PyExc_ValueError,
				"depythonifying 'array', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		} else {
			return depythonify_c_array (type, argument, datum);
		}
		break;

	default:
		ObjCErr_Set(PyExc_ValueError,
			"depythonifying unknown typespec %#x", *type);
		return -1;
	}
	return 0;
}


#ifdef GNU_RUNTIME

# error "GNU_RUNTIME not supported at the moment"

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


/* Ronald: Eeks, this is scary code. Maybe we should call the right method
 * directory in libffi_support instead of going though objc_msgSendSuper
 */
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

  mlist = malloc(sizeof(struct objc_method_list)
		 + (numMethods) * sizeof(struct objc_method));
  mlist->method_count = 0;
  mlist->obsolete = NULL;

  printf("new mlist %p\n", mlist);

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
		 + ((numMethods) * sizeof(struct objc_method)));

  if (mlist == NULL)
    return NULL;

  mlist->method_count = 0;
  mlist->obsolete = NULL; 

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
