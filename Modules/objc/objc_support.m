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

#import <Foundation/NSInvocation.h>
#import <Foundation/NSMethodSignature.h>
#import <Foundation/NSData.h> 
#import <Foundation/NSValue.h> 

#ifdef MACOSX
#include <CoreFoundation/CFNumber.h>
#endif


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

#if 1

/*
 * Automaticly mapping from NSNumber to python numbers doesn't work when
 * you want to add the result of NSNumber.numberWithBool_ to a property list.
 */

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

#endif

@interface NSString (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
@end /* NSString (PyObjCSupport) */

@implementation NSString (PyObjCSupport)

-(PyObject*)__pyobjc_PythonObject__
{
	return PyObjCUnicode_New(self);
}

@end /* NSString (PyObjCSupport) */



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
		type = objc_skip_typespec (type);
		assert (*type == _C_ARY_E);
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
		ObjCErr_Set(ObjCExc_internal_error,
			"objc_skip_typespec: Unhandled type '%#x'", *type); 
		return NULL;
	}

	while (isdigit(*type)) type++;
	return type;
}

/*
  Return the alignment of an object specified by type 
*/

int
objc_alignof_type (const char *type)
{
	switch (*type) {
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
		/* XXX Ronald: Is this valid? */
		struct { int x; double y; } fooalign;
		int    item_align;
		while(*type != _C_STRUCT_E && *type++ != '=') /* do nothing */;
		if (*type != _C_STRUCT_E) {
			item_align = objc_alignof_type(type);
			if (item_align == -1) return -1;
			return MAX (item_align, __alignof__ (fooalign));
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
		ObjCErr_Set(ObjCExc_internal_error, 
			"objc_align_type: Unhandled type '%#x'", *type);
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
		break;
      
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
			type = objc_skip_typespec (type);
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

	default:
		ObjCErr_Set(ObjCExc_internal_error, 
			"objc_sizeof_type: Unhandled type '%#x", *type);
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
			*item != _C_STRUCT_E; item = objc_skip_typespec (item)){
		nitems++;
	}

	ret = PyTuple_New (nitems);
	if (!ret) return NULL;

	for (item=type, offset=itemidx=0; 
			*item != _C_STRUCT_E; item = objc_skip_typespec (item)){
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
		ObjCErr_Set(ObjCExc_error, 
			"cannot depythonify array of unknown type");
		return -1;
	}

	if (nitems != PyTuple_Size (arg)) {
		ObjCErr_Set(ObjCExc_error,
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
			*type != _C_STRUCT_E; type = objc_skip_typespec (type)){
		nitems++;
	}

	if (nitems != PyTuple_Size (arg)) {
		ObjCErr_Set(ObjCExc_error,
			"depythonifying struct of %d members, got tuple of %d",
			nitems, PyTuple_Size (arg));
		return -1;
	}

	for (type=types, offset=itemidx=0; 
			*type != _C_STRUCT_E; type = objc_skip_typespec (type)){
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

	type = objc_skip_type_qualifiers (type);

	switch (*type) {
	case _C_CHR:
		// We don't return a string because BOOL is an alias for
		// char (at least on MacOS X)
		retobject = (PyObject*)PyInt_FromLong ((int)(*(char*)datum));
		break;

	case _C_UCHR:
		retobject = (PyObject*)PyInt_FromLong ((long)(*(unsigned char*)datum));
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
		retobject = (PyObject*)PyLong_FromUnsignedLongLong(*(unsigned long long*)datum);
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
		retobject = (PyObject*)PyObjCPointer_new(*(void**) datum, type+1);
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
			ObjCErr_Set(ObjCExc_error,
				"depythonifying '%s', got negative '%s'",
					descr,
					argument->ob_type->tp_name);
			return -1;

		} else if (temp > max) {
			ObjCErr_Set(ObjCExc_error,
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
			ObjCErr_Set(ObjCExc_error,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					argument->ob_type->tp_name);
			return -1;
		}

		if (*out > max) {
			ObjCErr_Set(ObjCExc_error,
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

		ObjCErr_Set(ObjCExc_error,
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
		*out = PyInt_AsLong(argument);
		if (*out < min || *out > max) {
			ObjCErr_Set(ObjCExc_error,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					argument->ob_type->tp_name);
			return -1;
		}
		return 0;

	} else if (PyLong_Check(argument)) {
		*out = PyLong_AsLongLong(argument);
		if (PyErr_Occurred()) {
			ObjCErr_Set(ObjCExc_error,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					argument->ob_type->tp_name);
			return -1;
		}

		if (*out < min || *out > max) {
			ObjCErr_Set(ObjCExc_error,
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

		ObjCErr_Set(ObjCExc_error,
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




/* TODO: Examine whether using PyArg_Parse would be usefull to translate
 *       basic types (range checking for free!)
 *
 * This function is way too large!
 */
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

	type = objc_skip_type_qualifiers (type);
  
	switch (*type) {
	case _C_CHARPTR:
		if (!PyString_Check (argument) && argument != Py_None) {
			ObjCErr_Set(ObjCExc_error,
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
				ObjCErr_Set(ObjCExc_error,
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
				ObjCErr_Set(ObjCExc_error,
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
			ObjCErr_Set(ObjCExc_error,
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
				ObjCErr_Set(ObjCExc_error,
					"depythonifying 'SEL', cannot "
					"register string with runtime");
				return -1;
			}
		} else {
			ObjCErr_Set(ObjCExc_error,
				"depythonifying 'SEL', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		}
		break;

 
	case _C_PTR:
		/* Pointers are hard and the code below
		 * (1) Uses PyString in an unsafe way
		 * (2) Is not threadsafe
		 * (3) Is not needed for *most* Cocoa code
		 *     [We should only get here for pointers inside data 
		 *      structures]
		 */

		if (PyObjCPointer_Check (argument)) {
			*(void **) datum = ((PyObjCPointer *) argument)->ptr;
		} else {
			ObjCErr_Set(ObjCExc_error,
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

			ObjCErr_Set(ObjCExc_error,
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

			ObjCErr_Set(ObjCExc_error,
				"depythonifying 'double', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		}
		break;

	case _C_UNION_B:
		if (PyString_Check (argument)) {
			unsigned int expected_size = objc_sizeof_type (type);

			if (expected_size == (unsigned int)-1) {
				ObjCErr_Set(ObjCExc_error,
					"depythonifying 'union' of "
					"unknown size");
				return -1;
			} else if (expected_size != PyString_Size (argument)) {
				ObjCErr_Set(ObjCExc_error,
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
			ObjCErr_Set(ObjCExc_error,
				"depythonifying 'union', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		}
		break;

	case _C_STRUCT_B:
		if (! PyTuple_Check (argument)) {
			ObjCErr_Set(ObjCExc_error,
				"depythonifying 'struct', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		} else {
			return depythonify_c_struct (type, argument, datum);
		}
		break;

	case _C_ARY_B:
		if (! PyTuple_Check (argument)) {
			ObjCErr_Set(ObjCExc_error,
				"depythonifying 'array', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		} else {
			return depythonify_c_array (type, argument, datum);
		}
		break;

	default:
		ObjCErr_Set(ObjCExc_error,
			"depythonifying unknown typespec %#x", *type);
		return -1;
	}
	return 0;
}

#ifndef OC_USE_FFI_SHORTCUTS
  /* execute_and_pythonify_objc_method is not used when we're in 'full libffi'
   * mode. Might as wel not compile it then...
   */

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
	int               itemSize;

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
			itemSize = objc_sizeof_type(argtype+1);
			if (itemSize == -1) return NULL;
			argbuf_len += itemSize;
			break;

		case _C_INOUT:
			if (argtype[1] == _C_PTR) {
				byref_out_count ++;
				byref_in_count ++;
				itemSize = objc_sizeof_type(argtype+2);
				if (itemSize == -1) return NULL;
				argbuf_len += itemSize;
			}
			break;

		case _C_IN: case _C_CONST:
			if (argtype[1] == _C_PTR) {
				byref_in_count ++;
				itemSize = objc_sizeof_type(argtype+2);
				if (itemSize == -1) return NULL;
				argbuf_len += itemSize;
			}
			break;

		case _C_OUT:
			if (argtype[1] == _C_PTR) {
				byref_out_count ++;
				itemSize = objc_sizeof_type(argtype+2);
				if (itemSize == -1) return NULL;
				argbuf_len += itemSize;
			}
			break;

		case _C_STRUCT_B: case _C_UNION_B: case _C_ARY_B:
			plain_count++;
			itemSize = objc_sizeof_type(argtype);
			if (itemSize == -1) return NULL;
			argbuf_len += itemSize;
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
	inv = [[NSInvocation alloc] initWithMethodSignature:methinfo];

	/* Set 'self' argument, for class methods we use the class */ 
	if (meth->sel_flags & ObjCSelector_kCLASS_METHOD) {
		if (PyObjCObject_Check(self)) {
			self_obj = GETISA(PyObjCObject_GetObject(self));
		} else if (PyObjCClass_Check(self)) {
			self_obj = PyObjCClass_GetClass(self);
		} else {
			PyErr_SetString(PyExc_TypeError, 
				"Need objective-C object or class as self");
			goto error_cleanup;
		}
	} else {
		int err;

		if (PyObjCObject_Check(self)) {
			self_obj = PyObjCObject_GetObject(self);

		} else {
			err = depythonify_c_value("@", self, &self_obj);
			if (err == -1) {
				goto error_cleanup;
			}
		}
	}

	[inv setTarget:self_obj];
	[inv setSelector:meth->sel_selector];

	py_arg = 0;
	for (curspec = objc_skip_typespec(meth->sel_signature), i = 0; *curspec; curspec = objc_skip_typespec(curspec), i ++) {
		int error;
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

					if (error == 0) {
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

					if (error == 0) {
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

					if (error == 0) {
						[inv setArgument:&arg atIndex:i];
					}
				} else {
					/* just encode */
	  				error = depythonify_c_value (
						argtype+1, 
						argument, 
						argbuffer);
					if (error == 0) {
						[inv setArgument:argbuffer atIndex:i];
					}
				}
				break;
			default:
	  			error = depythonify_c_value (
					argtype, 
					argument, 
					argbuffer);
				if (error == 0) {
					[inv setArgument:argbuffer atIndex:i];
				}
			}

			if (error == -1) {
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
		int retSize = objc_sizeof_type(rettype);
		char *retbuffer;

		if (retSize == -1) {
			objc_result = NULL;
		} else {
			retbuffer = alloca (retSize);
			[inv getReturnValue:retbuffer];
			objc_result = pythonify_c_value (rettype, retbuffer);
		}
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
		PyObjCObject_ClearObject(self);
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

#endif /* ! OC_USE_FFI_SHORTCUTS */

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
