/* Copyright (c) 1996,97,98 by Lele Gaifax.  All Rights Reserved
 * Copyright (c) 2002, 2003 Ronald Oussoren
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
#include <objc/Protocol.h>

#include <unistd.h>


#ifdef MACOSX
/* OSX 10.1 doesn't define LLONG_MIN, LLONG_MAX and ULLONG_MAX */
#ifndef LLONG_MIN
#error "Mac OS X 10.1 not supported"
#endif
#endif

#import <Foundation/NSInvocation.h>
#import <Foundation/NSData.h> 
#import <Foundation/NSValue.h> 
#import <Foundation/NSDecimalNumber.h> 

#ifdef MACOSX
#include <CoreFoundation/CFNumber.h>
#endif /* MACOSX */

/*
 * Category on NSObject to make sure that every object supports 
 * the method  __pyobjc_PythonObject__, this helps to simplify
 * pythonify_c_value.
 */
@interface NSObject (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
+(PyObject*)__pyobjc_PythonObject__;
@end /* PyObjCSupport */

@implementation NSObject (PyObjCSupport)

-(PyObject*)__pyobjc_PythonObject__
{
	PyObject *rval;

	rval = PyObjC_FindPythonProxy(self);
	if (rval == NULL) {
		rval = (PyObject *)PyObjCObject_New(self, 
				PyObjCObject_kDEFAULT, YES);
		PyObjC_RegisterPythonProxy(self, rval);
	}

	return rval;
}

+(PyObject*)__pyobjc_PythonObject__
{
	PyObject *rval;

	//rval = PyObjC_FindPythonProxy(self);
	rval = NULL;
	if (rval == NULL) {
		rval = (PyObject *)PyObjCClass_New(self);
		//PyObjC_RegisterPythonProxy(self, rval);
	}

	return rval;
}

@end /* PyObjCSupport */

@interface NSProxy (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
+(PyObject*)__pyobjc_PythonObject__;
@end /* PyObjCSupport */

@implementation NSProxy (PyObjCSupport)

-(PyObject*)__pyobjc_PythonObject__
{
	PyObject *rval;

	rval = PyObjC_FindPythonProxy(self);
	if (rval == NULL) {
		rval = (PyObject *)PyObjCObject_New(self,
				PyObjCObject_kDEFAULT, YES);
		PyObjC_RegisterPythonProxy(self, rval);
	}
	return rval;
}

+(PyObject*)__pyobjc_PythonObject__
{
	PyObject *rval;

	rval = NULL;
	//rval = PyObjC_FindPythonProxy(self);
	if (rval == NULL) {
		rval = (PyObject *)PyObjCClass_New(self);
		//PyObjC_RegisterPythonProxy(self, rval);
	}
	return rval;
}

@end /* PyObjCSupport */

@interface Protocol (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
@end /* PyObjCSupport */

@implementation Protocol (PyObjCSupport)

-(PyObject*)__pyobjc_PythonObject__
{
	PyObject *rval;

	rval = PyObjC_FindPythonProxy(self);
	if (rval == NULL) {
		rval = PyObjCFormalProtocol_ForProtocol(self);
	}
	return rval;
}

@end /* PyObjCSupport */

@interface Object (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
@end /* PyObjCSupport */

@implementation Object (PyObjCSupport)

-(PyObject*)__pyobjc_PythonObject__
{
	PyObject *rval;

	rval = PyObjC_FindPythonProxy(self);
	if (rval == NULL) {
		rval = (PyObject *)PyObjCObject_New(self,
				PyObjCObject_kCLASSIC, NO);
		PyObjC_RegisterPythonProxy(self, rval);
	}
	return rval;
}

@end /* PyObjCSupport */

@interface NSString (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
@end /* NSString (PyObjCSupport) */

@implementation NSString (PyObjCSupport)

-(PyObject*)__pyobjc_PythonObject__
{
	/* Don't register the proxy, see XXX */
	PyObject *rval = (PyObject *)PyObjCUnicode_New(self);
	return rval;
}

@end /* NSString (PyObjCSupport) */

@interface NSNumber (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
@end /* NSNumber (PyObjCSupport) */

@implementation NSNumber (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__
{
	/* FIXME: rewrite PyObjC_NSNumberWrapper in C */
	PyObject *rval;


#ifdef MACOSX
	/* shortcut for booleans */
	if (kCFBooleanTrue == (CFBooleanRef)self) {
		return PyBool_FromLong(1);
	} else if (kCFBooleanFalse == (CFBooleanRef)self) {
		return PyBool_FromLong(0);
	}
#endif
	
	rval = PyObjC_FindPythonProxy(self);
	if (rval == NULL) {
		rval= PyObjCObject_New(self,
				PyObjCObject_kDEFAULT, YES);

		if (PyObjC_NSNumberWrapper && rval) {
			PyObject *val = rval;
			rval = PyObject_CallFunctionObjArgs(
					PyObjC_NSNumberWrapper, val, NULL);
			Py_DECREF(val);
		}
	}
	return rval;
}
@end

@interface NSDecimalNumber (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
@end /* NSDecimalNumber (PyObjCSupport) */

@implementation NSDecimalNumber (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__
{
	PyObject *rval;

	rval = PyObjC_FindPythonProxy(self);
	if (rval == NULL) {
		rval = (PyObject *)PyObjCObject_New(self,
				PyObjCObject_kDEFAULT, YES);
		PyObjC_RegisterPythonProxy(self, rval);
	}

	return rval;
}
@end

#ifndef MAX
static inline int
MAX(int x, int y)
{
	return x > y ? x : y;
}
#endif

#if 0
static inline int
ROUND(int v, int a)
{
	return a * ((v+a-1)/a);
}
#else
static inline int 
ROUND(int v, int a)
{
	if (v % a == 0) {
		return v;
	} else {
		return v + a - (v % a);
	}
}
#endif


static inline const char*
PyObjCRT_SkipTypeQualifiers (const char* type)
{
	while (
			*type == _C_CONST ||
			*type == _C_IN ||
			*type == _C_INOUT ||
			*type == _C_OUT ||
			*type == _C_BYCOPY ||
			*type == _C_ONEWAY) {
		type++;
	}
	while (*type && isdigit(*type)) type++;
	return type;
}


const char * 
PyObjCRT_SkipTypeSpec (const char *type)
{
	type = PyObjCRT_SkipTypeQualifiers (type);

	switch (*type) {
	/* The following are one character type codes */
	case _C_UNDEF:
	case _C_CLASS:
	case _C_SEL:
	case _C_CHR:
	case _C_UCHR:
	case _C_CHARPTR:
#ifdef _C_ATOM
	case _C_ATOM:
#endif
#ifdef _C_BOOL
	case _C_BOOL:
#endif
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
	case _C_BFLD: /* Not really 1 character, but close enough  */
		++type;
		break;

	case _C_ID:
		++type;
#ifdef MACOSX
		if (*type == '"') {
			/* embedded field name in an ivar_type */
			type=strchr(type+1, '"');
			if (type != NULL) {
				type++;
			}
		}
#endif
		break;

	case _C_ARY_B:
		/* skip digits, typespec and closing ']' */

		while (isdigit (*++type));
		type = PyObjCRT_SkipTypeSpec (type);
		assert (type == NULL || *type == _C_ARY_E);
		if (type) type++;
		break;
  
	case _C_STRUCT_B:
		/* skip name, and elements until closing '}'  */
		while (*type != _C_STRUCT_E && *type++ != '='); 
		while (type && *type != _C_STRUCT_E) {
			if (*type == '"') {
				/* embedded field names */
				type = strchr(type+1, '"');
				if (type != NULL) {
					type++;
				} else {
					return NULL;
				}
			}
			type = PyObjCRT_SkipTypeSpec (type);
		}
		if (type) type++;
		break;

	case _C_UNION_B:
		/* skip name, and elements until closing ')'  */
		while (*type != _C_UNION_E && *type++ != '='); 
		while (type && *type != _C_UNION_E) { 
			type = PyObjCRT_SkipTypeSpec (type); 
		}
		if (type) type++;
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
		PyErr_Format(PyObjCExc_InternalError,
			"PyObjCRT_SkipTypeSpec: Unhandled type '%#x'", *type); 
		return NULL;
	}

	/* The compiler inserts a number after the actual signature, 
	 * this number may or may not be usefull depending on the compiler
	 * version. We never use it.
	 */
	while (type && *type && isdigit(*type)) type++;
	return type;
}

/*
Return the alignment of an object specified by type 
*/

/*
*  On MacOS X, the elements of a struct are aligned differently inside the
*  struct than outside. That is, the maximum alignment of any struct field
*  (except the first) is 4, doubles outside of a struct have an alignment of
*  8.
*
*  Other platform don't seem to have this inconsistency.
*  
*  XXX: sizeof_struct, alignof_struct and {de,}pythonify_c_struct should
*  probably be moved to platform dependend files. As long as this is the
*  only platform dependent code this isn't worth the effort.
*/
#ifdef MACOSX

static inline int
PyObjC_EmbeddedAlignOfType (const char*  type)
{
	int align = PyObjCRT_AlignOfType(type);

	if (align < 4) {
		return align;
	} else {
		return 4;
	}
}

#else

static inline int
PyObjC_EmbeddedAlignOfType (const char*  type)
{
	int align =  PyObjCRT_AlignOfType(type);

	/* GNUstep/ix86 seems to behave like this: */
	if (align < 4) {
		return align;
	} else {
		return 4;
	}
}

#endif

int
PyObjCRT_AlignOfType (const char *type)
{
	switch (*type) {
	case _C_ID:    return __alignof__ (id);
	case _C_CLASS: return __alignof__ (Class);
	case _C_SEL:   return __alignof__ (SEL);
	case _C_CHR:   return __alignof__ (char);
	case _C_UCHR:  return __alignof__ (unsigned char);
	case _C_SHT:   return __alignof__ (short);
	case _C_USHT:  return __alignof__ (unsigned short);
#ifdef _C_BOOL
	case _C_BOOL:   return __alignof__ (bool);
#endif
	case _C_INT:   return __alignof__ (int);
	case _C_UINT:  return __alignof__ (unsigned int);
	case _C_LNG:   return __alignof__ (long);
	case _C_ULNG:  return __alignof__ (unsigned long);
	case _C_FLT:   return __alignof__ (float);
	case _C_DBL:   return __alignof__ (double);
	case _C_CHARPTR: return __alignof__ (char *);
#ifdef _C_ATOM
	case _C_ATOM: return __alignof__ (char *);
#endif
	case _C_PTR:   return __alignof__ (void *);
	case _C_LNGLNG: return __alignof__(long long);
	case _C_ULNGLNG: return __alignof__(unsigned long long);

	case _C_ARY_B:
		while (isdigit(*++type)) /* do nothing */;
		return PyObjCRT_AlignOfType (type);
  
	case _C_STRUCT_B:
	{
		/* The alignment of a struct is the alignment of it's first
		 * member
		 */

		struct { int x; double y; } fooalign;
		while(*type != _C_STRUCT_E && *type++ != '=') /* do nothing */;
		if (*type != _C_STRUCT_E) {
			int have_align = 0;
			int align = 0;

			while (type != NULL && *type != _C_STRUCT_E) {
				if (*type == '"') {
					type = strchr(type+1, '"');
					if (type) type++;
				}
				if (have_align) {
					align = MAX(align, 
					   PyObjC_EmbeddedAlignOfType(type));
				} else {
					align = PyObjCRT_AlignOfType(type);
					have_align = 1;
				}
				type = PyObjCRT_SkipTypeSpec(type);
			}
			if (type == NULL) return -1;
			return align;
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
			int item_align = PyObjCRT_AlignOfType(type);
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
		return PyObjCRT_AlignOfType(type+1);

	default:
		PyErr_Format(PyObjCExc_InternalError, 
			"PyObjCRT_AlignOfType: Unhandled type '%#x'", *type);
		return -1;
	}
}

/*
The aligned size if the size rounded up to the nearest alignment.
*/

static int
PyObjCRT_AlignedSize (const char *type)
{
	int size = PyObjCRT_SizeOfType (type);
	int align = PyObjCRT_AlignOfType (type);

	if (size == -1 || align == -1) return -1;
	return ROUND (size, align);
}

/*
return the size of an object specified by type 
*/

int
PyObjCRT_SizeOfType (const char *type)
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
#ifdef _C_BOOL
	case _C_BOOL:    return sizeof(bool);
#endif
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
#ifdef _C_ATOM
	case _C_ATOM:
#endif
		return sizeof(char*);
  
	case _C_ARY_B:
	{
		int len = atoi(type+1);
		int item_align;
		while (isdigit(*++type))
			;
		item_align = PyObjCRT_AlignedSize(type);
		if (item_align == -1) return -1;
		return len*item_align;
	}
	break; 

	case _C_STRUCT_B:
	{
		int acc_size = 0;
		int have_align =  0;
		int align;
		int max_align = 0;

		while (*type != _C_STRUCT_E && *type++ != '=')
			; /* skip "<name>=" */
		while (*type != _C_STRUCT_E) {
			if (*type == '"') {
				type = strchr(type+1, '"');
				if (type) type++;
			}
			if (have_align) {
				align = PyObjC_EmbeddedAlignOfType(type);
				if (align == -1) return -1;
			} else {
				align = PyObjCRT_AlignOfType(type);
				if (align == -1) return -1;
				have_align = 1;
			}
			max_align = MAX(align, max_align);
			acc_size = ROUND (acc_size, align);

			itemSize = PyObjCRT_SizeOfType (type); 
			if (itemSize == -1) return -1;
			acc_size += itemSize;
			type = PyObjCRT_SkipTypeSpec (type);
		}
		if (max_align) {
			acc_size = ROUND(acc_size, max_align);
		}
		return acc_size;
	}

	case _C_UNION_B:
	{
		int max_size = 0;
		type++;
		while (*type != _C_UNION_E) {
			itemSize = PyObjCRT_SizeOfType (type);
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
		return PyObjCRT_SizeOfType(type+1);

	default:
		PyErr_Format(PyObjCExc_InternalError, 
			"PyObjCRT_SizeOfType: Unhandled type '%#x", *type);
		return -1;
	}
}


/*#F Returns a tuple of objects representing the content of a C array
of type @var{type} pointed by @var{datum}. */
static PyObject *
pythonify_c_array (const char *type, void *datum)
{
	PyObject *ret;
	int nitems, itemidx, sizeofitem;
	unsigned char* curdatum;

	nitems = atoi (type+1);
	while (isdigit (*++type))
		;
	sizeofitem = PyObjCRT_SizeOfType (type);
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
	PyObject *converted;
	unsigned int offset, itemidx;
	const char *item;
	int have_align = 0, align;
	int haveTuple;
	const char* type_start = type;
	const char* type_end = PyObjCRT_SkipTypeSpec(type);

	const char* type_real_start = type;
	int type_real_length = type_end - type_start;

	/* The compiler adds useless digits at the end of the signature */
	while (type_end != type_start+1 && type_end[-1] != _C_STRUCT_E) {
		type_end--;
	}

	while (*type != _C_STRUCT_E && *type++ != '=') {
		/* skip "<name>=" */
	}

	haveTuple = 0;
	ret = PyObjC_CreateRegisteredStruct(type_start, type_end-type_start);
	if (ret == NULL) {
		int nitems;

		nitems = 0;
		item = type;
		while (*item != _C_STRUCT_E) {
			nitems ++;
			if (*item == '"') {
				item = strchr(item+1, '"');
				if (item) item ++;
			}
			item = PyObjCRT_SkipTypeSpec(item);
		}

		haveTuple = 1;
		ret = PyTuple_New (nitems);
		if (!ret) return NULL;
	}

	item = type;
	offset = itemidx = 0;
	while (*item != _C_STRUCT_E) {
		PyObject *pyitem;

		if (*item == '"') {
			item = strchr(item+1, '"');
			if (item) item ++;
		}

		if (!have_align) {
			align = PyObjCRT_AlignOfType(item);
			have_align = 1;
		} else {
			align = PyObjC_EmbeddedAlignOfType(item);
		}

		offset = ROUND(offset, align);

		pyitem = pythonify_c_value (item, ((char*)datum)+offset);

		if (pyitem) {
			if (haveTuple) {
				PyTuple_SET_ITEM (ret, itemidx, pyitem);
			} else {
				int r;
				r = PySequence_SetItem(ret, itemidx, pyitem);
				Py_DECREF(pyitem);
				if (r == -1) {
					Py_DECREF(ret);
					return NULL;
				}
			}
		} else {
			Py_DECREF(ret);
			return NULL;
		}

		itemidx++;
		offset += PyObjCRT_SizeOfType (item);
		item = PyObjCRT_SkipTypeSpec (item);
	}

	converted = [OC_PythonObject __pythonifyStruct:ret withType:type_real_start length:type_real_length];
	Py_DECREF(ret);
	return converted;
}

/*#F Extracts the elements from the tuple @var{arg} and fills a C array
of type @var{type} pointed by @var{datum}. Returns an error message, or
NULL on success. */
static int
depythonify_c_array (const char *type, PyObject *arg, void *datum)
{
	int nitems, itemidx, sizeofitem;
	unsigned char* curdatum;
	PyObject* seq;

	nitems = atoi (type+1);
	while (isdigit (*++type))
		;
	sizeofitem = PyObjCRT_AlignedSize (type);
	if (sizeofitem == -1) {
		PyErr_Format(PyExc_ValueError, 
			"cannot depythonify array of unknown type");
		return -1;
	}

	seq = PySequence_Fast(arg, "depythonifying array, got no sequence");
	if (seq == NULL) {
		return -1;
	}

	if (nitems != PySequence_Fast_GET_SIZE(seq)) {
		Py_DECREF(seq);
		PyErr_Format(PyExc_ValueError,
			"depythonifying array of %d items, got one of %d",
			nitems, PyTuple_Size(arg));
		return -1;
	}

	curdatum = datum;
	for (itemidx=0; itemidx < nitems; itemidx++) {
		PyObject *pyarg = PySequence_Fast_GET_ITEM(seq, itemidx);
		int err;

		err = depythonify_c_value (type, pyarg, curdatum);
		if (err == -1) {
			Py_DECREF(seq);
			return err;
		}
	  
		curdatum += sizeofitem;
	}

	Py_DECREF(seq);
	return 0;
}

/*#F Extracts the elements from the tuple @var{arg} and fills a C structure
of type @var{type} pointed by @var{datum}. Returns an error message, or
NULL on success. */
static int
depythonify_c_struct(const char *types, PyObject *arg, void *datum)
{
	int nitems, offset, itemidx;
	int have_align = 0, align;
	const char *type;
	PyObject* seq;

	while (*types != _C_STRUCT_E && *types++ != '='); /* skip "<name>=" */

	type=types;
	nitems=0;
	while (*type != _C_STRUCT_E) {
		if (*type == '"') {
			type = strchr(type+1, '"');
			type++;
		}
		nitems++;
		type = PyObjCRT_SkipTypeSpec (type);
	}

	seq = PySequence_Fast(arg, "depythonifying struct, got no sequence");
	if (seq == NULL) {
		return -1;
	}

	if (nitems != PySequence_Fast_GET_SIZE(seq)) {
		Py_DECREF(seq);
		PyErr_Format(PyExc_ValueError,
			"depythonifying struct of %d members, got tuple of %d",
			nitems, PyTuple_Size (arg));
		return -1;
	}

	type=types;
	offset = itemidx = 0;

	while (*type != _C_STRUCT_E) {
		PyObject *argument;

		if (*type == '"') {
			type = strchr(type+1, '"');
			type++;
		}


		argument = PySequence_Fast_GET_ITEM(seq, itemidx);
		int error;
		if (!have_align) {
			align = PyObjCRT_AlignOfType(type);
			have_align = 1;
		} else {
			align = PyObjC_EmbeddedAlignOfType(type);
		}

		offset = ROUND(offset, align);

		error = depythonify_c_value(type, argument, 
				((char*)datum)+offset);
		if (error == -1) {
			Py_DECREF(seq);
			return error;
		}
  
		itemidx++;
		offset += PyObjCRT_SizeOfType (type);
		type = PyObjCRT_SkipTypeSpec (type);
	}
	Py_DECREF(seq);
	return 0;
}

PyObject *
pythonify_c_value (const char *type, void *datum)
{
	PyObject *retobject = NULL;

	type = PyObjCRT_SkipTypeQualifiers (type);

	switch (*type) {
	case _C_CHR:
		/* 
		 * We don't return a string because BOOL is an alias for
		 * char (at least on MacOS X)
		 */
		retobject = (PyObject*)PyInt_FromLong ((int)(*(char*)datum));
		break;

	case _C_UCHR:
		retobject = (PyObject*)PyInt_FromLong (
			(long)(*(unsigned char*)datum));
		break;

	case _C_CHARPTR: 
#ifdef _C_ATOM
	case _C_ATOM:
#endif
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

#ifdef _C_BOOL
	case _C_BOOL:
		retobject = (PyObject *) PyInt_FromLong (*(bool*) datum);
		break;
#endif

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

#if 1
		/* In theory this is a no-op, in practice this gives us EOF 4.5 
		 * support.
		 *
		 * EOF can return references to 'to-be-restored' objects, 
		 * calling any method on them fully restores them, 'self' is
		 * the safest method to call.
		 */
		obj = [obj self];
#endif

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
			retobject = PyString_FromString(PyObjCRT_SELName(*(SEL*)datum)); 
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
		if (*(void**)datum == NULL) {
			retobject = Py_None;
			Py_INCREF(retobject);
		} else {
			retobject = PyObjCPointerWrapper_ToPython(type, datum);
			if (retobject == NULL && !PyErr_Occurred()) {
				retobject = (PyObject*)PyObjCPointer_New(
					*(void**) datum, type+1);
			}
		}
		break;
  
	case _C_UNION_B:
	{
		int size = PyObjCRT_SizeOfType (type);
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
		PyErr_Format(PyObjCExc_Error, 
			"pythonify_c_value: unhandled value type (%c|%d|%s)",
			*type, *type, type);
		break;
	}

	return retobject;
}


int PyObjCRT_SizeOfReturnType(const char* type)
{
	switch(*type) {
	case _C_CHR:
	case _C_UCHR:
	case _C_SHT:
	case _C_USHT:
		return sizeof(int);
	default:
		return PyObjCRT_SizeOfType(type);
	}
}

/*
* Convert a python value to a basic C unsigned integer value.
*/
static int
depythonify_unsigned_int_value(
		PyObject* argument, char* descr,
		unsigned long long* out, unsigned long long max)
{
	if (PyInt_Check (argument)) {
		long temp = PyInt_AsLong(argument);
		if (temp < 0) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying '%s', got negative '%s'",
					descr,
					argument->ob_type->tp_name);
			return -1;

		} else if ((unsigned long long)temp > max) {
			PyErr_Format(PyExc_ValueError,
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
			PyErr_Format(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					argument->ob_type->tp_name);
			return -1;
		}

		if (*out > max) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					argument->ob_type->tp_name);
			return -1;
		}
		return 0;

	} else {
		PyObject* tmp;

		if (PyString_Check(argument) || PyUnicode_Check(argument)) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying '%s', got '%s'",
					descr,
					argument->ob_type->tp_name);
			return -1;
		}

		tmp = PyNumber_Long(argument);
		if (tmp != NULL) {
			*out = PyLong_AsUnsignedLongLong(tmp);
			Py_DECREF(tmp);

			if (*out <= max) {
				return 0;
			}
		}

		PyErr_Format(PyExc_ValueError,
			"depythonifying '%s', got '%s'",
				descr,
				argument->ob_type->tp_name);
		return -1;
	}
}

/*
* Convert a python value to a basic C signed integer value.
*/
static int
depythonify_signed_int_value(
		PyObject* argument, char* descr,
		long long* out, long long min, long long max)
{
	if (PyInt_Check (argument)) {
		*out = (long long)PyInt_AsLong(argument);
		if (*out < min || *out > max) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					argument->ob_type->tp_name);
			return -1;
		}
		return 0;

	} else if (PyLong_Check(argument)) {
		*out = PyLong_AsLongLong(argument);
		if (PyErr_Occurred()) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					argument->ob_type->tp_name);
			return -1;
		}

		if (*out < min || *out > max) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					argument->ob_type->tp_name);
			return -1;
		}
		return 0;

	} else {
		PyObject* tmp;

		if (PyString_Check(argument) || PyUnicode_Check(argument)) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying '%s', got '%s' of %d",
					descr,
					argument->ob_type->tp_name,
					PyString_Size(argument));
			return -1;
		}

		
		tmp = PyNumber_Long(argument);
		if (tmp != NULL) {
			*out = PyLong_AsLongLong(tmp);
			Py_DECREF(tmp);

			if (*out >= min && *out <= max) {
				return 0;
			}
		}

		PyErr_Format(PyExc_ValueError,
			"depythonifying '%s', got '%s'",
				descr,
				argument->ob_type->tp_name);
		return -1;
	}
}

int depythonify_c_return_value(
const char* type, PyObject* argument, void* datum)
{
	long long temp;
	unsigned long long utemp;
	int       r;

#ifndef __i386__
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

#else 
	return depythonify_c_value(type, argument, datum);
#endif
}

PyObject *
pythonify_c_return_value (const char *type, void *datum)
{
#ifndef __i386__
	/*
 	 * On PowerPC short and char return values are passed
 	 * as full-size ints.
	 */
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

#else
	return pythonify_c_value(type, datum);

#endif
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
#ifdef _C_ATOM
	case _C_ATOM:
#endif
	case _C_CHARPTR:
		if (!PyString_Check (argument) && argument != Py_None) {
			PyErr_Format(PyExc_ValueError,
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

#ifdef _C_BOOL
	case _C_BOOL:
		*(bool*)datum = PyObject_IsTrue(argument);
		return 0;
#endif

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
		/*
			XXX
			
			This should, for values other than Py_None, always return the same id
			for the same PyObject for as long as that id lives.  I think that the
			implementation of this should be moved to OC_PythonObject,
			which would itself have a map of PyObject->id.  The dealloc
			of each of these custom objects should notify OC_PythonObject
			to remove map entry.  We need to significantly change how immutable types
			are bridged, and create OC_PythonString, OC_PythonBool, etc. which are 
			subclasses of what they should be from the the Objective C side.

			If we don't do this, we break binary plist serialization, and likely
			other things, which assume that foo[bar] is foo[bar] for the duration of
			the serialization process.  I would imagine that other things also
			assume this kind of invariant, so we should do it here rather than in every
			container object.
		*/
				

		return [OC_PythonObject wrapPyObject:argument toId:(id *)datum];

	case _C_CLASS:
		if (PyObjCClass_Check(argument))  {
			*(Class*) datum = PyObjCClass_GetClass(argument);
		} else if (argument == Py_None) {
			*(Class*) datum = nil;
		} else {
			PyErr_Format(PyExc_ValueError,
				"depythonifying 'Class', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		}
		break;

	case _C_SEL:
		if (argument == Py_None) {
			*(SEL*)datum = NULL;
		} else if (PyObjCSelector_Check (argument)) {
			*(SEL *) datum = PyObjCSelector_GetSelector(argument); 
		} else if (PyString_Check(argument)) {
			char *selname = PyString_AsString (argument);
			SEL sel;

			if (*selname == '\0') {
				*(SEL*)datum = NULL;
			} else {
				sel = PyObjCRT_SELUID (selname);

				if (sel)  {
					*(SEL*) datum = sel;
				} else {
					PyErr_Format(PyExc_ValueError,
						"depythonifying 'SEL', cannot "
						"register string with runtime");
					return -1;
				}
			}
		} else {
			PyErr_Format(PyExc_ValueError,
				"depythonifying 'SEL', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		}
		break;


	case _C_PTR:
		if (argument == Py_None) {
			*(void**)datum = NULL;
			return 0;
		} 
		r = PyObjCPointerWrapper_FromPython(type, argument, datum);
		if (r == -1) {
			if (PyErr_Occurred()) {
				return -1;
			} else if (PyObjCPointer_Check (argument)) {
				*(void **) datum = PyObjCPointer_Ptr(argument);
			} else {
				PyErr_Format(PyExc_ValueError,
					"depythonifying 'pointer', got '%s'",
						argument->ob_type->tp_name);
				return -1;
			}
		}
		break;

	case _C_FLT:
		if (PyFloat_Check (argument)) {
			*(float *) datum = (float)PyFloat_AsDouble (argument);
		} else if (PyInt_Check (argument)) {
			*(float *) datum = (float) PyInt_AsLong (argument);
		} else if (PyString_Check(argument) || PyUnicode_Check(argument)) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying 'float', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		} else {
			PyObject* tmp = PyNumber_Float(argument);
			if (tmp != NULL) {
				double dblval = PyFloat_AsDouble(tmp);
				Py_DECREF(tmp);
				*(float*) datum = dblval;
				return 0;
			}

			PyErr_Format(PyExc_ValueError,
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
		} else if (PyString_Check(argument) || PyUnicode_Check(argument)) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying 'float', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		} else {
			PyObject* tmp = PyNumber_Float(argument);
			if (tmp != NULL) {
				double dblval = PyFloat_AsDouble(tmp);
				Py_DECREF(tmp);
				*(double*) datum = dblval;
				return 0;
			}

			PyErr_Format(PyExc_ValueError,
				"depythonifying 'double', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		}
		break;

	case _C_UNION_B:
		if (PyString_Check (argument)) {
			int expected_size = PyObjCRT_SizeOfType (type);

			if (expected_size == -1) {
				PyErr_Format(PyExc_ValueError,
					"depythonifying 'union' of "
					"unknown size");
				return -1;
			} else if (expected_size != PyString_Size (argument)) {
				PyErr_Format(PyExc_ValueError,
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
			PyErr_Format(PyExc_ValueError,
				"depythonifying 'union', got '%s'",
					argument->ob_type->tp_name);
			return -1;
		}
		break;

	case _C_STRUCT_B:
		return depythonify_c_struct (type, argument, datum);

	case _C_ARY_B:
		return depythonify_c_array (type, argument, datum);

	default:
		PyErr_Format(PyExc_ValueError,
			"depythonifying unknown typespec %#x", *type);
		return -1;
	}
	return 0;
}
