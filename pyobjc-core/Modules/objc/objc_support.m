/* Copyright (c) 1996,97,98 by Lele Gaifax.  All Rights Reserved
 * Copyright (c) 2002-2008 Ronald Oussoren
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
#include <sys/socket.h>
#include <netinet/in.h>

#import <Foundation/NSInvocation.h>
#import <Foundation/NSData.h> 
#import <Foundation/NSValue.h> 
#import <Foundation/NSDecimalNumber.h> 

#include <CoreFoundation/CFNumber.h>

/*
 * Category on NSObject to make sure that every object supports 
 * the method  __pyobjc_PythonObject__, this helps to simplify
 * pythonify_c_value.
 */
@interface NSObject (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
+(PyObject*)__pyobjc_PythonObject__;

-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie;
+(PyObject*)__pyobjc_PythonTransient__:(int*)cookie;
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

-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
	PyObject* result = PyObjC_FindPythonProxy(self);
	if (result) {
		*cookie = 0;
		return result;
	}

	*cookie = 1;
	return PyObjCObject_New(self, PyObjCObject_kSHOULD_NOT_RELEASE, NO);
}

+(PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
	*cookie = 0;
	return (PyObject *)PyObjCClass_New(self);
}

@end /* PyObjCSupport */

@interface NSProxy (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
+(PyObject*)__pyobjc_PythonObject__;

-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie;
+(PyObject*)__pyobjc_PythonTransient__:(int*)cookie;
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
	if (rval == NULL) {
		rval = (PyObject *)PyObjCClass_New(self);
	}
	return rval;
}

-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
	PyObject* result = PyObjC_FindPythonProxy(self);
	if (result) {
		*cookie = 0;
		return result;
	}

	*cookie = 1;
	return PyObjCObject_New(self, PyObjCObject_kSHOULD_NOT_RELEASE, NO);
}

+(PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
	*cookie = 0;
	return (PyObject *)PyObjCClass_New(self);
}
@end /* PyObjCSupport */

@interface Protocol (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie;
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

-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
	PyObject *rval;

	*cookie = 0;
	rval = PyObjC_FindPythonProxy(self);
	if (rval == NULL) {
		rval = PyObjCFormalProtocol_ForProtocol(self);
	}
	return rval;
}

@end /* PyObjCSupport */

@interface Object (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie;
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

-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
	PyObject *rval;

	*cookie = 0;
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
-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie;
@end /* NSString (PyObjCSupport) */

@implementation NSString (PyObjCSupport)

-(PyObject*)__pyobjc_PythonObject__
{
	/* Don't register the proxy, see XXX */
	PyObject *rval = (PyObject *)PyObjCUnicode_New(self);
	return rval;
}

-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
	*cookie = 0;
	return (PyObject *)PyObjCUnicode_New(self);
}

@end /* NSString (PyObjCSupport) */

@interface NSNumber (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie;
@end /* NSNumber (PyObjCSupport) */

@implementation NSNumber (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__
{
	/* FIXME: rewrite PyObjC_NSNumberWrapper in C */
	PyObject *rval;


	/* shortcut for booleans */
	if (kCFBooleanTrue == (CFBooleanRef)self) {
		return PyBool_FromLong(1);
	} else if (kCFBooleanFalse == (CFBooleanRef)self) {
		return PyBool_FromLong(0);
	}
	
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

-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
	*cookie = 0;
	return [self __pyobjc_PythonObject__];
}
@end

@interface NSDecimalNumber (PyObjCSupport)
-(PyObject*)__pyobjc_PythonObject__;
-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie;
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

-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
	*cookie = 0;
	return [self __pyobjc_PythonObject__];
}
@end

#ifndef MAX
static inline Py_ssize_t
MAX(Py_ssize_t x, Py_ssize_t y)
{
	return x > y ? x : y;
}
#endif

static inline Py_ssize_t 
ROUND(Py_ssize_t v, Py_ssize_t a)
{
	if (v % a == 0) {
		return v;
	} else {
		return v + a - (v % a);
	}
}


const char*
PyObjCRT_SkipTypeQualifiers (const char* type)
{
	PyObjC_Assert(type != NULL, NULL);

	while (
			*type == _C_CONST ||
			*type == _C_IN ||
			*type == _C_INOUT ||
			*type == _C_OUT ||
			*type == _C_BYCOPY ||
			*type == _C_BYREF ||
			*type == _C_ONEWAY ||
			*type == 'O') {
		type++;
	}
	while (*type && isdigit(*type)) type++;
	return type;
}

const char * 
PyObjCRT_SkipTypeSpec (const char *type)
{
	PyObjC_Assert(type != NULL, NULL);

	type = PyObjCRT_SkipTypeQualifiers (type);

	switch (*type) {
	case '"':
		/* Embedded name in ivar or compound type */
		type++;
		while (*type != '\0' && *type != '"') type++;
		break;

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
	case _C_LNG_LNG:
	case _C_ULNG_LNG:
	case _C_UNICHAR:
	case _C_CHAR_AS_TEXT:
	case _C_CHAR_AS_INT:
	case _C_NSBOOL:
		++type;
		break;

	case _C_BFLD: 
		while (isdigit (*++type));
		break;

	case _C_ID:
		++type;
		if (*type == '?') {
			/* Block pointer */
			type++;
                }
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
  
	case _C_PTR:
	case _C_CONST:
	case _C_IN:
	case _C_INOUT:
	case _C_OUT:
	case _C_BYCOPY:
	case _C_BYREF:
	case _C_ONEWAY:

		/* Just skip the following typespec */
		type = PyObjCRT_SkipTypeSpec (type+1);
		break;


	default:
		PyErr_Format(PyObjCExc_InternalError,
			"PyObjCRT_SkipTypeSpec: Unhandled type '%#x' %s", *type, type); 
		return NULL;
	}

	/* The compiler inserts a number after the actual signature, 
	 * this number may or may not be usefull depending on the compiler
	 * version. We never use it.
	 */
	while (type && *type && isdigit(*type)) type++;
	return type;
}

const char * 
PyObjCRT_NextField(const char *type)
{
	PyObjC_Assert(type != NULL, NULL);

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
	case _C_LNG_LNG:
	case _C_ULNG_LNG:
	case _C_UNICHAR:
	case _C_CHAR_AS_TEXT:
	case _C_CHAR_AS_INT:
	case _C_NSBOOL:
	case _C_BFLD: /* Not really 1 character, but close enough  */
		++type;
		break;

	case _C_ID:
		++type;
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
  
	case _C_PTR:
	case _C_CONST:
	case _C_IN:
	case _C_INOUT:
	case _C_OUT:
	case _C_BYCOPY:
	case _C_BYREF:
	case _C_ONEWAY:

		/* Just skip the following typespec */
		type = PyObjCRT_NextField(type+1);
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

static inline Py_ssize_t
PyObjC_EmbeddedAlignOfType (const char*  type)
{
	PyObjC_Assert(type != NULL, -1);

	Py_ssize_t align = PyObjCRT_AlignOfType(type);

#if defined(__i386__) || defined(__x86_64__)
	return align;

#else
	if (align < 4 || align == 16) {
		return align;
	} else {
		return 4;
	}
#endif
}

Py_ssize_t
PyObjCRT_AlignOfType (const char *type)
{
	PyObjC_Assert(type != NULL, -1);

	switch (*type) {
	case _C_VOID:  return __alignof__(char);
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
	case _C_UNICHAR:	return __alignof__(UniChar);
	case _C_CHAR_AS_TEXT:	return __alignof__(char);
	case _C_CHAR_AS_INT:	return __alignof__(char);
	case _C_NSBOOL:		return __alignof__(BOOL);
	case _C_INT:   return __alignof__ (int);
	case _C_UINT:  return __alignof__ (unsigned int);
	case _C_LNG:   return __alignof__ (long);
	case _C_ULNG:  return __alignof__ (unsigned long);
	case _C_FLT:   return __alignof__ (float);
	case _C_DBL:   
#if defined(__APPLE__) && defined(__i386__)
		/* The ABI says natural alignment is 4 bytes, but 
		 * GCC's __alignof__ says 8. The latter is wrong.
		 */
		return 4;
#else
		return __alignof__ (double);
#endif

	case _C_CHARPTR: return __alignof__ (char *);
#ifdef _C_ATOM
	case _C_ATOM: return __alignof__ (char *);
#endif
	case _C_PTR:   return __alignof__ (void *);
#if defined(__APPLE__) && defined(__i386__)
		/* The ABI says natural alignment is 4 bytes, but 
		 * GCC's __alignof__ says 8. The latter is wrong.
		 */
	case _C_LNG_LNG: return 4;
	case _C_ULNG_LNG: return 4;
#else
	case _C_LNG_LNG: return __alignof__(long long);
	case _C_ULNG_LNG: return __alignof__(unsigned long long);
#endif

	case _C_ARY_B:
		while (isdigit(*++type)) /* do nothing */;
		return PyObjCRT_AlignOfType (type);
  
	case _C_STRUCT_B:
	{
		struct { int x; double y; } fooalign;
		while(*type != _C_STRUCT_E && *type++ != '=') /* do nothing */;
		if (*type != _C_STRUCT_E) {
			int have_align = 0;
			Py_ssize_t align = 0;

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
	case _C_BYREF:
	case _C_ONEWAY:
		return PyObjCRT_AlignOfType(type+1);
	
	case _C_BFLD:
		return 1;

	case _C_UNDEF:
		return __alignof__(void*);

	default:
		PyErr_Format(PyObjCExc_InternalError, 
			"PyObjCRT_AlignOfType: Unhandled type '%#x' %s", *type, type);
		return -1;
	}
}

/*
The aligned size if the size rounded up to the nearest alignment.
*/

Py_ssize_t
PyObjCRT_AlignedSize (const char *type)
{
	PyObjC_Assert(type != NULL, -1);

	Py_ssize_t size = PyObjCRT_SizeOfType (type);
	Py_ssize_t align = PyObjCRT_AlignOfType (type);

	if (size == -1 || align == -1) return -1;
	return ROUND(size, align);
}

/*
return the size of an object specified by type 
*/

Py_ssize_t
PyObjCRT_SizeOfType (const char *type)
{
	PyObjC_Assert(type != NULL, -1);

	Py_ssize_t itemSize;
	switch (*type) {
	case _C_VOID:    return 1; // More convenient than the correct value.
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
	case _C_LNG_LNG:  return sizeof(long long);
	case _C_ULNG_LNG: return sizeof(unsigned long long);
	case _C_UNICHAR:	return sizeof(UniChar);
	case _C_CHAR_AS_TEXT:	return sizeof(char);
	case _C_CHAR_AS_INT:	return sizeof(char);
	case _C_NSBOOL:		return sizeof(BOOL);

	case _C_PTR:
	case _C_CHARPTR:
#ifdef _C_ATOM
	case _C_ATOM:
#endif
		return sizeof(char*);
  
	case _C_ARY_B:
	{
		Py_ssize_t len = atoi(type+1);
		Py_ssize_t item_align;
		while (isdigit(*++type))
			;
		item_align = PyObjCRT_AlignedSize(type);
		if (item_align == -1) return -1;
		return len*item_align;
	}
	break; 

	case _C_STRUCT_B:
	{
		Py_ssize_t acc_size = 0;
		int have_align =  0;
		Py_ssize_t align;
		Py_ssize_t max_align = 0;

		/* This is an awfull hack... */
		/*   struct sockaddr is a generic type with several supported
		 *   specific types. Annoyingly enough not all of those have the
		 *   same size. 
		 *   This file has crude support for this scheme as its almost
		 *   impossible to implement this nicely using our C/Python
		 *   API.
		 */
		if (strncmp(type, 
			@encode(struct sockaddr), 
			sizeof(@encode(struct sockaddr)-1)) == 0) {

			return sizeof(struct sockaddr_in6);
		}

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
		Py_ssize_t max_size = 0;
		type++;
		/* Skip name part: */
		while (*type != _C_UNION_E && *type++ != '='); 

		/* Calculate size: */
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
	case _C_BYREF:
	case _C_ONEWAY:
		return PyObjCRT_SizeOfType(type+1);

	case _C_BFLD:
		{
			int i = strtol(type+1, NULL, 10);
			return (i+7)/8;
		}
		break;

	case _C_UNDEF:
		return sizeof(void*);

	default:
		PyErr_Format(PyObjCExc_InternalError, 
			"PyObjCRT_SizeOfType: Unhandled type '0x%x', %s", 
			*type, type);
		return -1;
	}
}

PyObject *
pythonify_c_array_nullterminated(const char* type, void* datum, BOOL alreadyRetained, BOOL alreadyCFRetained)
{
	PyObjC_Assert(type != NULL, NULL);
	PyObjC_Assert(datum != NULL, NULL);

	Py_ssize_t count = 0;
	Py_ssize_t sizeofitem = PyObjCRT_SizeOfType (type);
	unsigned char* curdatum = datum;

	type = PyObjCRT_SkipTypeQualifiers(type);
	switch (*type) {
	case _C_CHARPTR:
		while (*(char**)curdatum != NULL) {
			count ++;
			curdatum += sizeofitem;
		}
		break;

	case _C_ID:
		while (*(id*)curdatum != NULL) {
			count ++;
			curdatum += sizeofitem;
		}
		break;

	case _C_PTR:
		while (*(void**)curdatum != NULL) {
			count ++;
			curdatum += sizeofitem;
		}
		break;

	case _C_UCHR:
		while (*(unsigned char*)curdatum != 0) {
			count ++;
			curdatum += sizeofitem;
		}
		break;

	case _C_VOID:
	case _C_CHR:
		return PyBytes_FromString((char*)curdatum);
		break;

	case _C_CHAR_AS_TEXT:
		return PyBytes_FromString((char*)curdatum);
		break;

	case _C_USHT:
		while (*(unsigned short*)curdatum != 0) {
			count ++;
			curdatum += sizeofitem;
		}
		break;
	case _C_SHT:
		while (*(short*)curdatum != 0) {
			count ++;
			curdatum += sizeofitem;
		}
		break;

	case _C_UINT:
		while (*(unsigned int*)curdatum != 0) {
			count ++;
			curdatum += sizeofitem;
		}
		break;
	case _C_INT:
		while (*(int*)curdatum != 0) {
			count ++;
			curdatum += sizeofitem;
		}
		break;

	case _C_ULNG:
		while (*(unsigned long*)curdatum != 0) {
			count ++;
			curdatum += sizeofitem;
		}
		break;
	case _C_LNG:
		while (*(long*)curdatum != 0) {
			count ++;
			curdatum += sizeofitem;
		}
		break;

	case _C_ULNG_LNG:
		while (*(unsigned long long*)curdatum != 0) {
			count ++;
			curdatum += sizeofitem;
		}
		break;
	case _C_LNG_LNG:
		while (*(long long*)curdatum != 0) {
			count ++;
			curdatum += sizeofitem;
		}
		break;

	case _C_UNICHAR:
		while (*(UniChar*)curdatum != 0) {
			count ++;
			curdatum += sizeofitem;
		}
		break;

	case _C_CHAR_AS_INT:
		while (*(char*)curdatum != 0) {
			count ++;
			curdatum += sizeofitem;
		}
		break;

	
	default:
		PyErr_Format(PyExc_TypeError,
			"Cannot deal with NULL-terminated array of %s",
			type);
		return NULL;
	}
	if (*type == _C_UNICHAR) {
		return PyUnicode_FromUnicode((Py_UNICODE*)datum, count);
	}

	return  PyObjC_CArrayToPython2(type, datum, count, alreadyRetained, alreadyCFRetained);
}



/*#F Returns a tuple of objects representing the content of a C array
of type @var{type} pointed by @var{datum}. */
static PyObject *
pythonify_c_array (const char *type, void *datum)
{
	PyObjC_Assert(type != NULL, NULL);
	PyObjC_Assert(datum != NULL, NULL);

	PyObject *ret;
	Py_ssize_t nitems, itemidx, sizeofitem;
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
	PyObjC_Assert(type != NULL, NULL);
	PyObjC_Assert(datum != NULL, NULL);

	PyObject *ret;
	Py_ssize_t offset, itemidx;
	const char *item;
	int have_align = 0;
	Py_ssize_t align;
	int haveTuple;
	const char* type_start = type;
	const char* type_end = PyObjCRT_SkipTypeSpec(type);
	const char* type_real_start = type;
	Py_ssize_t type_real_length = type_end - type_start;

	/* Hacked up support for socket addresses */
	if (strncmp(type, @encode(struct sockaddr), sizeof(@encode(struct sockaddr)-1)) == 0) {
		return PyObjC_SockAddrToPython(datum);
	}

	if (IS_FSREF(type)) {
		return PyObjC_decode_fsref(datum);
	}

	if (IS_FSSPEC(type)) {
		return PyObjC_decode_fsspec(datum);
	}

	/* Skip back over digits at end of type in function prototypes */
	while (type_real_length > 0 && isdigit(type_start[type_real_length-1])) {
		type_real_length --;
	}

	/* The compiler adds useless digits at the end of the signature */
	while (type_end != type_start+1 && type_end[-1] != _C_STRUCT_E) {
		type_end--;
	}

	while (*type != _C_STRUCT_E && *type++ != '=') {
		/* skip "<name>=" */
	}

	haveTuple = 0;
	const char* oc_typestr = NULL;
	ret = PyObjC_CreateRegisteredStruct(type_start, 
			type_end-type_start, &oc_typestr);
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

		item = type;
	} else {
		item = type;

		if (oc_typestr != NULL) {
			item = oc_typestr + 1;
			while (*item && *item != '=') {
				item++;
			}
			if (*item) {
				item++;
			}
		}
	}


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

	if (haveTuple) {
		PyObject *converted;
		converted = [OC_PythonObject __pythonifyStruct:ret withType:type_real_start length:type_real_length];
		Py_DECREF(ret);
		return converted;
	} else {
		return ret;
	}
}

int 
depythonify_c_return_array_count(const char* rettype, Py_ssize_t count, PyObject* arg, void* resp, BOOL already_retained, BOOL already_cfretained)
{
	PyObjC_Assert(rettype != NULL, -1);
	PyObjC_Assert(arg != NULL, -1);
	PyObjC_Assert(resp != NULL, -1);

	/* Use an NSMutableData object to store the bytes, that way we can autorelease the data because we
	 * cannot free it otherwise.
	 */
	PyObject* seq = PySequence_Fast(arg, "Sequence required");
	if (seq == NULL) {
		return -1;
	}
	if (count == -1) {
		count = PySequence_Fast_GET_SIZE(seq);
	}

	NSMutableData* data = [NSMutableData dataWithLength:count * PyObjCRT_SizeOfType(rettype)];
	*(void**)resp = [data mutableBytes];
	int r = depythonify_c_array_count(rettype, count, YES, seq, [data mutableBytes], already_retained, already_cfretained);
	Py_DECREF(seq);

	return r;
}


int 
depythonify_c_return_array_nullterminated(const char* rettype, PyObject* arg, void* resp, BOOL already_retained, BOOL already_cfretained)
{
	PyObjC_Assert(rettype != NULL, -1);
	PyObjC_Assert(arg != NULL, -1);
	PyObjC_Assert(resp != NULL, -1);

	/* Use an NSMutableData object to store the bytes, that way we can autorelease the data because we
	 * cannot free it otherwise.
	 */
	if (*rettype == _C_CHR || *rettype == _C_CHAR_AS_TEXT || *rettype == _C_VOID) {
		if (PyBytes_Check(arg)) {
			NSMutableData* data = [NSMutableData dataWithBytes: PyBytes_AsString(arg)
						     length: PyBytes_Size(arg)];
			*(void**)resp = [data mutableBytes];
			return 0;
#ifdef PyByteArray_Check
		} else if (PyByteArray_Check(arg)) {
			NSMutableData* data = [NSMutableData dataWithBytes: PyByteArray_AsString(arg)
						     length: PyByteArray_Size(arg)];
			*(void**)resp = [data mutableBytes];
			return 0;
#endif
		}
	}


	PyObject* seq = PySequence_Fast(arg, "Sequence required");
	if (seq == NULL) {
		return -1;
	}

	Py_ssize_t count = PySequence_Fast_GET_SIZE(seq);

	/* The data is 0-filled, which means we won't have to add the terminated ourselves */
	NSMutableData* data = [NSMutableData dataWithLength:(count + 1) * PyObjCRT_SizeOfType(rettype)];
	*(void**)resp = [data mutableBytes];
	int result =  depythonify_c_array_count(rettype, count, YES, seq, [data mutableBytes], already_retained, already_cfretained);
	Py_DECREF(seq);
	return result;
}


int 
depythonify_c_array_count(const char* type, Py_ssize_t nitems, BOOL strict, PyObject* value, void* datum, BOOL already_retained, BOOL already_cfretained)
{
	PyObjC_Assert(type != NULL, -1);
	PyObjC_Assert(value != NULL, -1);
	PyObjC_Assert(datum != NULL, -1);

	Py_ssize_t itemidx, sizeofitem;
	unsigned char* curdatum;
	PyObject* seq;

	sizeofitem = PyObjCRT_AlignedSize (type);
	if (sizeofitem == -1) {
		PyErr_Format(PyExc_ValueError, 
			"cannot depythonify array of unknown type");
		return -1;
	}

	if (sizeofitem == 1 && PyBytes_Check(value)) {
		/* Special casing for strings */
		if (strict) {
			if (PyBytes_Size(value) != nitems) {
				PyErr_Format(PyExc_ValueError,
					"depythonifying array of %"PY_FORMAT_SIZE_T"d items, got one of %"PY_FORMAT_SIZE_T"d",
					nitems, PyBytes_Size(value));
				return -1;
			}
		} else {
			if (PyBytes_Size(value) < nitems) {
				PyErr_Format(PyExc_ValueError,
					"depythonifying array of %"PY_FORMAT_SIZE_T"d items, got one of %"PY_FORMAT_SIZE_T"d",
					nitems, PyBytes_Size(value));
				return -1;
			}
		}

		memcpy(datum, PyBytes_AS_STRING(value), nitems);
		return 0;
	}

	seq = PySequence_Fast(value, "depythonifying array, got no sequence");
	if (seq == NULL) {
		return -1;
	}

	if (strict) {
		if (PySequence_Fast_GET_SIZE(seq) != nitems) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying array of %"PY_FORMAT_SIZE_T"d items, got one of %"PY_FORMAT_SIZE_T"d",
				nitems, PySequence_Fast_GET_SIZE(seq));
			Py_DECREF(seq);
			return -1;
		}
	} else {
		if (PySequence_Fast_GET_SIZE(seq) < nitems) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying array of %"PY_FORMAT_SIZE_T"d items, got one of %"PY_FORMAT_SIZE_T"d",
				nitems, PySequence_Fast_GET_SIZE(seq));
			Py_DECREF(seq);
			return -1;
		}
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

		if (already_retained) { 
			[*(NSObject**)curdatum retain];

		} else if (already_cfretained) {
			CFRetain(*(NSObject**)curdatum);

		}
	  
		curdatum += sizeofitem;
	}

	if (*type == _C_CHARPTR) {
		/* We're depythonifying a list of strings, make sure the originals stay 
		 * around long enough.
		 */
		[[[OC_PythonObject alloc] initWithObject:seq] autorelease];
	}
	Py_DECREF(seq);
	return 0;
}

Py_ssize_t 
c_array_nullterminated_size(PyObject* object, PyObject** seq)
{
	PyObjC_Assert(object != NULL, -1);
	PyObjC_Assert(seq != NULL, -1);

	*seq = PySequence_Fast(object, "depythonifying array, got no sequence");
	if (*seq == NULL) {
		return -1;
	}

	return PySequence_Fast_GET_SIZE(*seq) + 1;
}

int 
depythonify_c_array_nullterminated(const char* type, Py_ssize_t count, PyObject* value, void* datum, BOOL already_retained, BOOL already_cfretained)
{
	PyObjC_Assert(type != NULL, -1);
	PyObjC_Assert(value != NULL, -1);
	PyObjC_Assert(datum != NULL, -1);

	/* XXX: we can do better than this: just clear the last item */
	/* Clear memory: */
	memset(datum, 0, count * PyObjCRT_SizeOfType(type));

	if (count == 1) {
		return 0;
	}

	/* Then copy the actual values */
	return depythonify_c_array_count(type, count-1, YES, value, datum, already_retained, already_cfretained);
}

/*#F Extracts the elements from the tuple @var{arg} and fills a C array
of type @var{type} pointed by @var{datum}. Returns an error message, or
NULL on success. */
static int
depythonify_c_array (const char *type, PyObject *arg, void *datum)
{
	PyObjC_Assert(type != NULL, -1);
	PyObjC_Assert(arg != NULL, -1);
	PyObjC_Assert(datum != NULL, -1);

	Py_ssize_t nitems, itemidx, sizeofitem;
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
		PyErr_Format(PyExc_ValueError,
			"depythonifying array of %"PY_FORMAT_SIZE_T"d items, got one of %"PY_FORMAT_SIZE_T"d",
			nitems, PySequence_Fast_GET_SIZE(seq));
		Py_DECREF(seq);
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
	PyObjC_Assert(types != NULL, -1);
	PyObjC_Assert(arg != NULL, -1);
	PyObjC_Assert(datum != NULL, -1);

	Py_ssize_t nitems, offset, itemidx;
	int have_align = 0;
	Py_ssize_t align;
	const char *type;
	PyObject* seq;

	/* Hacked in support for sockaddr structs */
	if (strncmp(types, @encode(struct sockaddr), sizeof(@encode(struct sockaddr)-1)) == 0) {
		return PyObjC_SockAddrFromPython(arg, datum);
	}

	if (IS_FSREF(types)) {
		if (PyObjC_encode_fsref(arg, datum) == 0) {
			return 0;
		}
		PyErr_Clear();
	}
	if (IS_FSSPEC(types)) {
		if (PyObjC_encode_fsspec(arg, datum) == 0) {
			return 0;
		}
		PyErr_Clear();
	}

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
			"depythonifying struct of %"PY_FORMAT_SIZE_T"d members, got tuple of %"PY_FORMAT_SIZE_T"d",
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
	PyObjC_Assert(type != NULL, NULL);
	PyObjC_Assert(datum != NULL, NULL);

	PyObject *retobject = NULL;

	type = PyObjCRT_SkipTypeQualifiers (type);

	switch (*type) {
	case _C_UNICHAR:
		{
			Py_UNICODE	c  = (Py_UNICODE)(*(UniChar*)datum);
			retobject = PyUnicode_FromUnicode(&c, 1);
		}
		break;

	case _C_CHAR_AS_TEXT:
		retobject = PyBytes_FromStringAndSize((char*)datum, 1);
		break;

	case _C_CHR:
	case _C_CHAR_AS_INT:
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
			retobject = (PyObject*)PyBytes_FromString(cp);
		}
		break;
	}

#ifdef _C_BOOL
	case _C_BOOL:
		retobject = (PyObject *) PyBool_FromLong (*(bool*) datum);
		break;
#endif

	case _C_NSBOOL:
		retobject = (PyObject *) PyBool_FromLong (*(BOOL*) datum);
		break;

	case _C_INT:
		retobject = (PyObject *) PyInt_FromLong (*(int*) datum);
		break;

	case _C_UINT:
#if __LP64__
		retobject = (PyObject*)PyInt_FromLong (
			*(unsigned int *) datum);

#else
		if (*(unsigned int*)datum > LONG_MAX) {
			retobject = (PyObject*)PyLong_FromUnsignedLongLong(
				*(unsigned int*)datum);
		} else {
			retobject = (PyObject*)PyInt_FromLong (
				*(unsigned int *) datum);
		}
#endif
		break;

	case _C_SHT:
		retobject = (PyObject *) PyInt_FromLong (*(short *) datum);
		break;

	case _C_USHT:
		retobject = (PyObject *) PyInt_FromLong (
			*(unsigned short *) datum);
		break;

	case _C_LNG_LNG: 
#ifndef __LP64__ /* else: fall-through to _C_LNG case */
		retobject = (PyObject*)PyLong_FromLongLong(*(long long*)datum);
		break;
#endif

	case _C_LNG:
		retobject = (PyObject *) PyInt_FromLong(*(long *) datum);
		break;

	case _C_ULNG_LNG:
#ifndef __LP64__ /* else: fallthrough to the ULNG case */
		retobject = (PyObject*)PyLong_FromUnsignedLongLong(
				*(unsigned long long*)datum);
		break;
#endif

	case _C_ULNG:
#if PY_MAJOR_VERSION == 2
		if (*(unsigned long*)datum > LONG_MAX) {
			retobject = (PyObject*)PyLong_FromUnsignedLongLong(
				*(unsigned long*)datum);
		} else {
			retobject = (PyObject*)PyInt_FromLong (
				*(unsigned long*) datum);
		}
#else
		retobject = PyLong_FromUnsignedLong(*(unsigned long*)datum);
#endif
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
			retobject = PyText_FromString(sel_getName(*(SEL*)datum)); 
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
		if (type[1] == _C_VOID) {
			/* A void*. These are treated like unsigned integers. */
			retobject = (PyObject*)PyLong_FromUnsignedLongLong(
				*(unsigned long*)datum);

		} else if (*(void**)datum == NULL) {
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
		Py_ssize_t size = PyObjCRT_SizeOfType (type);
		if (size == -1) return NULL;
		retobject = PyBytes_FromStringAndSize ((void*)datum, size);
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


Py_ssize_t 
PyObjCRT_SizeOfReturnType(const char* type)
{
	PyObjC_Assert(type != NULL, -1);

#if 1 /* def __ppc__ */
	switch(*type) {
	case _C_CHR:
	case _C_BOOL:
	case _C_UCHR:
	case _C_SHT:
	case _C_USHT:
	case _C_UNICHAR:
	case _C_CHAR_AS_TEXT:
	case _C_CHAR_AS_INT:
	case _C_NSBOOL:
		return sizeof(long);
	default:
		return PyObjCRT_SizeOfType(type);
	}
#else
		return PyObjCRT_SizeOfType(type);
#endif
}

/*
* Convert a python value to a basic C unsigned integer value.
*/
static int
depythonify_unsigned_int_value(
		PyObject* argument, char* descr,
		unsigned long long* out, unsigned long long max)
{
	PyObjC_Assert(argument != NULL, -1);
	PyObjC_Assert(descr != NULL, -1);
	PyObjC_Assert(out != NULL, -1);

#if PY_MAJOR_VERSION == 2
	if (PyInt_Check (argument)) {
		long temp = PyInt_AsLong(argument);
		if (PyErr_Occurred()) {
			return -1;
		}
		if (temp < 0) {
			if (PyErr_WarnEx(
				PyExc_DeprecationWarning, 
				"converting negative value to unsigned integer",
				1) < 0) {

				return -1;
			}
		}
		if ((unsigned long long)temp > max) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude (max %llu, value %llu)", descr,
					Py_TYPE(argument)->tp_name,
					max, temp);
			return -1;
		}
		*out = temp;
		return 0;

	} else 
#endif
	if (PyLong_Check(argument)) {
		*out = PyLong_AsUnsignedLongLong(argument);
		if (*out == (unsigned long long)-1 && PyErr_Occurred()) {
			PyErr_Clear();
			
			*out = (unsigned long long)PyLong_AsLongLong(argument);
			if (*out == (unsigned long long)-1 && PyErr_Occurred()) {
				PyErr_Format(PyExc_ValueError,
					"depythonifying '%s', got '%s' of "
					"wrong magnitude (max %llu, value %llu)", 
					descr,
					Py_TYPE(argument)->tp_name,
					max, *out);
				return -1;
			}

			if ((long long)*out < 0) {
				if (PyErr_WarnEx(
					PyExc_DeprecationWarning, 
					"converting negative value to unsigned integer",
					1) < 0) {

					return -1;
				}
			}
		}

		if (*out > max) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude (max %llu, value %llu)", descr,
				Py_TYPE(argument)->tp_name,
				max, *out);
			return -1;
		}
		return 0;

	} else {
		PyObject* tmp;

		if (
#if PY_MAJOR_VERSION == 2
			PyString_Check(argument) || 
#else
			PyBytes_Check(argument) || 
#endif
#ifdef PyByteArray_Check
			PyByteArray_Check(argument) || 
#endif
			PyUnicode_Check(argument)) {

			PyErr_Format(PyExc_ValueError,
				"depythonifying '%s', got '%s'",
					descr,
					Py_TYPE(argument)->tp_name);
			return -1;
		}

		tmp = PyNumber_Long(argument);
		if (tmp != NULL) {
			*out = PyLong_AsUnsignedLongLong(tmp);
			if (*out == (unsigned long long)-1 && PyErr_Occurred()) {
				PyErr_Clear();

				*out = PyLong_AsLong(tmp);
				if (*out == (unsigned long long)-1 && PyErr_Occurred()) {
					Py_DECREF(tmp);
					return -1;
				}
				if ((long long)*out < 0) {
					if (PyErr_WarnEx(
						PyExc_DeprecationWarning, 
						"converting negative value to unsigned integer",
						1) < 0) {
						Py_DECREF(tmp);

						return -1;
					}
				}
			}
			Py_DECREF(tmp);

			if (*out <= max) {
				return 0;
			}
		}

		PyErr_Format(PyExc_ValueError,
			"depythonifying '%s', got '%s'",
				descr,
				Py_TYPE(argument)->tp_name);
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
	PyObjC_Assert(argument != NULL, -1);
	PyObjC_Assert(descr != NULL, -1);
	PyObjC_Assert(out != NULL, -1);

#if PY_MAJOR_VERSION == 2
	if (PyInt_Check (argument)) {
		*out = (long long)PyInt_AsLong(argument);
		if (PyErr_Occurred()) {
			return -1;
		}
		if (*out < min || *out > max) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					Py_TYPE(argument)->tp_name);
			return -1;
		}
		return 0;

	} else 
#endif
	if (PyLong_Check(argument)) {
		*out = PyLong_AsLongLong(argument);
		if (PyErr_Occurred()) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					Py_TYPE(argument)->tp_name);
			return -1;
		}

		if (*out < min || *out > max) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying '%s', got '%s' of "
				"wrong magnitude", descr,
					Py_TYPE(argument)->tp_name);
			return -1;
		}
		return 0;

	} else {
		PyObject* tmp;

		if (
#if PY_MAJOR_VERSION == 2
			PyString_Check(argument) || 
#else
			PyBytes_Check(argument) || 
#endif
#ifdef PyByteArray_Check
			PyByteArray_Check(argument) || 
#endif
			PyUnicode_Check(argument)) {

			PyErr_Format(PyExc_ValueError,
				"depythonifying '%s', got '%s' of %"PY_FORMAT_SIZE_T"d",
					descr,
					Py_TYPE(argument)->tp_name,
					PyObject_Size(argument));
			return -1;
		}

		
		tmp = PyNumber_Long(argument);
		if (tmp != NULL) {
			*out = PyLong_AsLongLong(tmp);
			Py_DECREF(tmp);

			if (PyErr_Occurred()) {
				return -1;
			}

			if (*out >= min && *out <= max) {
				return 0;
			}
		}

		PyErr_Format(PyExc_ValueError,
			"depythonifying '%s', got '%s'",
				descr,
				Py_TYPE(argument)->tp_name);
		return -1;
	}
}

int depythonify_c_return_value(
const char* type, PyObject* argument, void* datum)
{
	PyObjC_Assert(type != NULL, -1);
	PyObjC_Assert(argument != NULL, -1);
	PyObjC_Assert(datum != NULL, -1);

#ifdef __ppc__
	long long temp;
	unsigned long long utemp;
	int       r;

	/* Small integers are promoted to integers when returning them */
	switch (*type) {
#ifdef _C_BOOL
	case _C_BOOL:
	case _C_NSBOOL:
		if (PyObject_IsTrue(argument)) {
			*(int*) datum = YES;
		} else {
			*(int*) datum = NO;
		}
		return 0;

#endif
	case _C_CHAR_AS_INT:
		r = depythonify_signed_int_value(argument, "char",
			&temp, CHAR_MIN, CHAR_MAX);
		if (r == 0) {
			*(int*)datum = temp;
		}
		return r;
	
	case _C_CHAR_AS_TEXT:
		if (PyBytes_Check(argument) && PyBytes_Size(argument) == 1) {
			*(int*) datum = PyBytes_AsString (argument)[0];
			return 0;
#ifdef PyByteArray_Check
		} else if (PyByteArray_Check(argument) && PyByteArray_Size(argument) == 1) {
			*(int*) datum = PyByteArray_AsString (argument)[0];
			return 0;
#endif
		} else {
			PyErr_Format(PyExc_ValueError,
				"Expecting byte string of length 1, got '%s'",
				Py_TYPE(argument)->tp_name);
			return -1;
		}
		break;

	case _C_CHR: 
		if (PyBytes_Check(argument) && PyBytes_Size(argument) == 1) {
			*(int*) datum = PyBytes_AsString (argument)[0];
			return 0;
#ifdef PyByteArray_Check
		} else if (PyByteArray_Check(argument) && PyByteArray_Size(argument) == 1) {
			*(int*) datum = PyByteArray_AsString (argument)[0];
			return 0;
#endif
		}

		r = depythonify_signed_int_value(argument, "char",
			&temp, CHAR_MIN, CHAR_MAX);
		if (r == 0) {
			*(int*)datum = temp;
		}
		return r;

	case _C_UNICHAR:
		if (PyUnicode_Check(argument) && PyUnicode_GetSize(argument) == 1) {
			*(int*)datum = (int)(*PyUnicode_AsUnicode(argument));
			return 0;

#if PY_MAJOR_VERSION == 2
		} else if (PyString_Check(argument)) {
			PyObject* u = PyUnicode_FromObject(argument);
			if (u == NULL) {
				return -1;
			}
			if (PyUnicode_Check(u) && PyUnicode_GetSize(u) == 1) {
				*(int*)datum = (int)(*PyUnicode_AsUnicode(u));
				Py_DECREF(u);
				return 0;
			} 
			Py_DECREF(u);
#endif
		}
		PyErr_Format(PyExc_ValueError, "Expecting unicode string of length 1, got a '%s'",
				Py_TYPE(argument)->tp_name);
		return -1;

	case _C_UCHR:
		if (PyBytes_Check(argument) && PyBytes_Size(argument) == 1) {
			*(unsigned int*) datum = 
				PyBytes_AsString (argument)[0];
			return 0;
		}
		r = depythonify_unsigned_int_value(argument, "unsigned char",
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
	PyObjC_Assert(type != NULL, NULL);
	PyObjC_Assert(datum != NULL, NULL);

#ifdef __ppc__
	/*
 	 * On PowerPC short and char return values are returned
 	 * as full-size ints.
	 */
	static  const char intType[] = { _C_INT, 0 };
	static  const char uintType[] = { _C_UINT, 0 };

	switch(*type) {
	case _C_BOOL:
	case _C_NSBOOL:
		return PyBool_FromLong(*(int*)datum);

	case _C_CHR: 
	case _C_CHAR_AS_INT: 
	case _C_SHT:
		return pythonify_c_value(intType, datum);
	case _C_UCHR: case _C_USHT:
		return pythonify_c_value(uintType, datum);

	case _C_CHAR_AS_TEXT:
		{
			char ch = *(int*)datum;
			return PyBytes_FromStringAndSize(&ch, 1);
		}

	case _C_UNICHAR:
		{
			Py_UNICODE ch = *(int*)datum;
			return PyUnicode_FromUnicode(&ch, 1);
		}

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
	PyObjC_Assert(type != NULL, -1);
	PyObjC_Assert(argument != NULL, -1);
	PyObjC_Assert(datum != NULL, -1);

	if (argument == NULL) abort();

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

		if (PyBytes_Check(argument)) {
			*(char**)datum = PyBytes_AsString(argument);
			if (*(char**)datum == NULL) {
				return -1;
			}

#ifdef PyByteArray_Check
		} else if (PyByteArray_Check(argument)) {
			*(char**)datum = PyByteArray_AsString(argument);
			if (*(char**)datum == NULL) {
				return -1;
			}
#endif
		} else if (argument == Py_None) {
			*(char**)datum = NULL;

		} else {
			PyErr_Format(PyExc_ValueError,
				"depythonifying 'charptr', got '%s'",
					Py_TYPE(argument)->tp_name);
			return -1;
		} 
		break;

	case _C_CHR:
		if (PyBytes_Check(argument) && PyBytes_Size(argument) == 1) {
			*(char*) datum = PyBytes_AsString (argument)[0];
			return 0;
#ifdef PyByteArray_Check
		} else if (PyByteArray_Check(argument) && PyByteArray_Size(argument) == 1) {
			*(char*) datum = PyByteArray_AsString (argument)[0];
			return 0;
#endif
		}

		r = depythonify_signed_int_value(argument, "char",
			&temp, CHAR_MIN, CHAR_MAX);
		if (r == 0) {
			*(char*)datum = temp;
		}
		return r;

	case _C_CHAR_AS_INT:
		r = depythonify_signed_int_value(argument, "char",
			&temp, CHAR_MIN, CHAR_MAX);
		if (r == 0) {
			*(char*)datum = temp;
		}
		return r;

	case _C_CHAR_AS_TEXT:

		if (PyBytes_Check(argument) && PyBytes_Size(argument) == 1) {
			*(char*) datum = PyBytes_AsString (argument)[0];
			return 0;
#ifdef PyByteArray_Check
		} else if (PyByteArray_Check(argument) && PyByteArray_Size(argument) == 1) {
			*(char*) datum = PyByteArray_AsString (argument)[0];
			return 0;
#endif
		} else {
			PyErr_Format(PyExc_ValueError,
					"Expecting byte string of length 1, got a '%s'",
					Py_TYPE(argument)->tp_name);
			return -1;
		}

	case _C_UCHR:
		if (PyBytes_Check(argument) && PyBytes_Size(argument) == 1) {
			*(unsigned char*) datum = 
				PyBytes_AsString (argument)[0];
			return 0;
#ifdef PyByteArray_Check
		} else if (PyByteArray_Check(argument) && PyByteArray_Size(argument) == 1) {
			*(unsigned char*) datum = PyByteArray_AsString (argument)[0];
			return 0;
#endif
		}
		r = depythonify_unsigned_int_value(argument, "unsigned char",
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

	case _C_NSBOOL: 
		*(BOOL*)datum = PyObject_IsTrue(argument);
		return 0;

	case _C_UNICHAR:
		if (PyUnicode_Check(argument) && PyUnicode_GetSize(argument) == 1) {
			*(UniChar*)datum = (UniChar)(*PyUnicode_AsUnicode(argument));
			return 0;
#if PY_MAJOR_VERSION == 2
		} else if (PyString_Check(argument)) {
			PyObject* u = PyUnicode_FromObject(argument);
			if (u == NULL) {
				return -1;
			}
			if (PyUnicode_Check(u) && PyUnicode_GetSize(u) == 1) {
				*(UniChar*)datum = (UniChar)(*PyUnicode_AsUnicode(u));
				Py_DECREF(u);
				return 0;
			} 
			Py_DECREF(u);
#endif
		}
		PyErr_Format(PyExc_ValueError, "Expecting unicode string of length 1, got a '%s'",
				Py_TYPE(argument)->tp_name);
		return -1;

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

	case _C_LNG_LNG:
		r = depythonify_signed_int_value(argument, "long long",
			&temp, LLONG_MIN, LLONG_MAX);
		if (r == 0) {
			*(long long*)datum = temp;
		}
		return r;

	case _C_ULNG_LNG:
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

		} else if (PyType_Check(argument) && PyType_IsSubtype((PyTypeObject*)argument, &PyObjCClass_Type)) {
			*(Class*) datum = PyObjCClass_GetClass(PyObjCClass_ClassForMetaClass(argument));

		} else {
			PyErr_Format(PyExc_ValueError,
				"depythonifying 'Class', got '%s'",
					Py_TYPE(argument)->tp_name);
			return -1;
		}
		break;

	case _C_SEL:
		if (argument == Py_None) {
			*(SEL*)datum = NULL;
		} else if (PyObjCSelector_Check (argument)) {
			*(SEL *) datum = PyObjCSelector_GetSelector(argument); 
		} else if (PyUnicode_Check(argument)) {
			PyObject* bytes = PyUnicode_AsEncodedString(argument, NULL, NULL);
			if (bytes == NULL) {
				return -1;
			}
			char *selname = PyBytes_AsString (bytes);
			SEL sel;

			if (*selname == '\0') {
				*(SEL*)datum = NULL;
				Py_DECREF(bytes);
			} else {
				sel = sel_getUid (selname);
				Py_DECREF(bytes);

				if (sel)  {
					*(SEL*) datum = sel;
				} else {
					PyErr_Format(PyExc_ValueError,
						"depythonifying 'SEL', cannot "
						"register string with runtime");
					return -1;
				}
			}

		} else if (PyBytes_Check(argument)) {
			char *selname = PyBytes_AsString (argument);
			SEL sel;

			if (*selname == '\0') {
				*(SEL*)datum = NULL;
			} else {
				sel = sel_getUid (selname);

				if (sel)  {
					*(SEL*) datum = sel;
				} else {
					PyErr_Format(PyExc_ValueError,
						"depythonifying 'SEL', cannot "
						"register string with runtime");
					return -1;
				}
			}
#ifdef PyByteArray_Check
		} else if (PyByteArray_Check(argument)) {
			char *selname = PyByteArray_AsString (argument);
			SEL sel;

			if (*selname == '\0') {
				*(SEL*)datum = NULL;
			} else {
				sel = sel_getUid (selname);

				if (sel)  {
					*(SEL*) datum = sel;
				} else {
					PyErr_Format(PyExc_ValueError,
						"depythonifying 'SEL', cannot "
						"register string with runtime");
					return -1;
				}
			}
#endif
		} else {
			PyErr_Format(PyExc_ValueError,
				"depythonifying 'SEL', got '%s'",
					Py_TYPE(argument)->tp_name);
			return -1;
		}
		break;


	case _C_PTR:
		if (argument == Py_None) {
			*(void**)datum = NULL;
			return 0;
		} 
		if (type[1] == _C_VOID) {
			r = depythonify_unsigned_int_value(argument, 
				"unsigned long",
				&utemp, ULONG_MAX);
			if (r == 0) {
				*(void**)datum = (void*)(unsigned long)utemp;
			}
			return r;

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
						Py_TYPE(argument)->tp_name);
				return -1;
			}
		}
		break;

	case _C_FLT:
		if (PyFloat_Check (argument)) {
			*(float *) datum = (float)PyFloat_AsDouble (argument);
#if PY_MAJOR_VERSION == 2
		} else if (PyInt_Check (argument)) {
			*(float *) datum = (float) PyInt_AsLong (argument);
#endif
		} else if (PyLong_Check (argument)) {
			*(float*) datum = (float) PyLong_AsDouble(argument);
			if (*(float*)datum == -1 && PyErr_Occurred()) {
				return -1;
			}
		} else if (
#if PY_MAJOR_VERSION == 2
				PyString_Check(argument) || 
#else
				PyBytes_Check(argument) || 
#ifdef PyByteArray_Check
				PyByteArray_Check(argument) || 
#endif
#endif
				PyUnicode_Check(argument)) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying 'float', got '%s'",
					Py_TYPE(argument)->tp_name);
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
					Py_TYPE(argument)->tp_name);
			return -1;
		}
		break;

	case _C_DBL:
		if (PyFloat_Check (argument)) {
			*(double *) datum = PyFloat_AsDouble (argument);
#if PY_MAJOR_VERSION == 2
		} else if (PyInt_Check (argument)) {
			*(double *) datum = (double) PyInt_AsLong (argument);
#endif
		} else if (PyLong_Check (argument)) {
			*(double *) datum = PyLong_AsDouble (argument);
			if (*(double*)datum == -1 && PyErr_Occurred()) {
				return -1;
			}
		} else if (
#if PY_MAJOR_VERSION == 2
				PyString_Check(argument) || 
#else
				PyBytes_Check(argument) || 
#endif
#ifdef PyByteArray_Check
				PyByteArray_Check(argument) || 
#endif
				PyUnicode_Check(argument)) {
			PyErr_Format(PyExc_ValueError,
				"depythonifying 'float', got '%s'",
					Py_TYPE(argument)->tp_name);
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
					Py_TYPE(argument)->tp_name);
			return -1;
		}
		break;

	case _C_UNION_B:
		if (PyBytes_Check (argument)) {
			Py_ssize_t expected_size = PyObjCRT_SizeOfType (type);

			if (expected_size == -1) {
				PyErr_Format(PyExc_ValueError,
					"depythonifying 'union' of "
					"unknown size");
				return -1;
			} else if (expected_size != PyBytes_Size (argument)) {
				PyErr_Format(PyExc_ValueError,
					"depythonifying 'union' of size %"PY_FORMAT_SIZE_T"d, "
					"got byte string of %"PY_FORMAT_SIZE_T"d",
						   expected_size, 
						   PyBytes_Size (argument));
				return -1;
			} else {
				memcpy ((void *) datum, 
					PyBytes_AS_STRING (argument), 
				expected_size);
			}
		} else {
			PyErr_Format(PyExc_ValueError,
				"depythonifying 'union', got '%s'",
					Py_TYPE(argument)->tp_name);
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

const char* 
PyObjCRT_RemoveFieldNames(char* buf, const char* type)
{
	PyObjC_Assert(buf != NULL, NULL);
	PyObjC_Assert(type != NULL, NULL);

	const char* end;
	if (*type == '"') {
		type++;
		while (*type++ != '"') {}
	}
	end = PyObjCRT_SkipTypeQualifiers(type);
	if (end == NULL) {
		return NULL;
	}
	switch (*end) {
	case _C_STRUCT_B:
		/* copy struct header */
		while (*end && *end != '=' && *end != _C_STRUCT_E) {
			end++;
		}
		if (*end == '\0') {
			PyErr_SetString(PyExc_ValueError, "Bad type string");
			return NULL;
		}
		if (*end == _C_STRUCT_E) {
			end ++;
			memcpy(buf, type, end-type);
			buf[end-type] = '\0';
			return end;
		}
		end++;
		memcpy(buf, type, end-type);
		buf += end - type;
		type = end;

		/* RemoveFieldNames until reaching end of struct */
		while (*type != _C_STRUCT_E) {
			end = PyObjCRT_RemoveFieldNames(buf, type);
			if (end == NULL) return NULL;
			buf += strlen(buf);
			type = end;
		}
		buf[0] = _C_STRUCT_E;
		buf[1] = '\0';
		return type+1;

	case _C_ARY_B:
		/* copy array header */
		end ++;
		while(isdigit(*end)) { end++; }

		memcpy(buf, type, end-type);
		buf += end - type;
		type = end;
		if (*type == _C_ARY_E) {
			buf[0] = _C_ARY_E;
			buf[1] = '\0';
			return type;
		}

		/* RemoveFieldName until reaching end of array */
		end = PyObjCRT_RemoveFieldNames(buf, type);
		if (end == NULL) return NULL;

		if (*end != _C_ARY_E) {
			PyErr_SetString(PyExc_ValueError, "bad type string");
			return NULL;
		}

		buf += strlen(buf);
		/*type += end - type;*/
		buf[0] = _C_ARY_E;
		buf[1] = '\0';
		return end + 1;
		break;

	default:
		end = PyObjCRT_SkipTypeSpec(end);
		if (end == NULL) return NULL;

		memcpy(buf, type, end-type);
		buf[end-type] = '\0';
		return end;
	}
}


PyObject* PyObjCObject_NewTransient(id objc_object, int* cookie)
{
	return [(NSObject*)objc_object __pyobjc_PythonTransient__:cookie];
}

void PyObjCObject_ReleaseTransient(PyObject* proxy, int cookie)
{
	if (cookie && Py_REFCNT(proxy) != 1) {
		CFRetain(PyObjCObject_GetObject(proxy));
		((PyObjCObject*)proxy)-> flags &= ~PyObjCObject_kSHOULD_NOT_RELEASE;
	}
	Py_DECREF(proxy);
}

BOOL PyObjC_signatures_compatible(const char* type1, const char* type2)
{
	/* Ignore type modifiers */
	type1 = PyObjCRT_SkipTypeQualifiers(type1);
	type2 = PyObjCRT_SkipTypeQualifiers(type2);

	if (*type1 == _C_ARY_B) {
		if (type2[0] == _C_PTR) {
			type1++;
			while (isdigit(*type1)) type1++;
			return PyObjC_signatures_compatible(type1, type2+1);
		} else if (type2[0] == _C_ARY_B) {
			type1++;
			while (isdigit(*type1)) type1++;
			type2++;
			while (isdigit(*type2)) type2++;
			return PyObjC_signatures_compatible(type1, type2);
		}
		return NO;
	}


	if (PyObjCRT_SizeOfType(type1) != PyObjCRT_SizeOfType(type2)) {
		return NO;
	}
	switch (*type1) {
	case _C_FLT: case _C_DBL: 
		switch (*type2) {
		case _C_FLT: case _C_DBL: 
			return YES;
	 	default:     
			return NO;
		}

	case _C_ID:
		if (*type2 == _C_ID) {
			return YES;
		}
		if (type2[0] == _C_PTR && type2[1] == _C_VOID) {
			return YES;
		}
		return NO;

	case _C_CHARPTR:
		if (*type2 == _C_CHARPTR) {
			return YES;
		} else if (*type2 == _C_PTR) {
			return PyObjC_signatures_compatible("c", type2+1);
		} else {
			return NO;
		}
	
	case _C_PTR:
		if (type1[1] == _C_VOID && type2[0] == _C_ID) {
			return YES;
		}
		if (*type2 == _C_CHARPTR) {
			return PyObjC_signatures_compatible(type1+1, "c");
		}
		if (*type2 != _C_PTR) {
			return NO;
		}
		if (type1[1] == _C_VOID || type2[1] == _C_VOID) {
			return YES;
		}
		return PyObjC_signatures_compatible(type1+1, type2+1);

	
	default:
		switch (*type2) {
		case _C_ID: case _C_PTR: return NO;
		case _C_FLT: case _C_DBL: return NO;
		default: return YES;
		}
	}
}
