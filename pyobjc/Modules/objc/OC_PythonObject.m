/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: OC_PythonObject.m,v
 * Revision: 1.23
 * Date: 1998/08/18 15:35:52
 *
 * Created Wed Sep  4 19:57:44 1996.
 */

#include "pyobjc.h"
#include "objc_support.h"
#include "compile.h"

#include <stdarg.h>

#import  <Foundation/NSObject.h>  
#import  <Foundation/NSMethodSignature.h>
#import  <Foundation/NSInvocation.h>

@implementation OC_PythonObject

+ newWithObject:(PyObject *) obj
{
	if (ObjCObject_Check (obj)) {
		id objc_obj = ObjCObject_GetObject(obj);
		return objc_obj;
	} else {
		id instance = [[self alloc] initWithObject:obj];
		[instance autorelease];
		return instance;
	}
}

- initWithObject:(PyObject *) obj
{
	Py_XDECREF(pyObject);
	pyObject = obj;
	Py_XINCREF(obj);

	return self;
}

- (void)dealloc
{
	Py_XDECREF(pyObject);
	[super dealloc];
}

- (NSString *) description
{
	PyObject *repr = PyObject_Repr (pyObject);
	if (repr) {
		int err;
		NSString* result;

		err = depythonify_c_value ("@", repr, &result);
		Py_DECREF (repr);
		if (err == -1) {
			ObjCErr_ToObjC();		
			return @"a python object";
		}
		return result;
	} else {
		PyErr_Clear();
		return [super description];
	}
}
  
- (void) doesNotRecognizeSelector:(SEL) aSelector
{
	[NSException raise:NSInvalidArgumentException
		     format:@"%@ does not recognize -%s",
		     	self, SELNAME(aSelector)];
}


/*#F Check the argument count of the method/function @var{pymethod},
  returning the method itself if it matches @var{argcount}, NULL
  otherwise. */
static inline PyObject *
check_argcount (PyObject *pymethod, unsigned int argcount)
{
	PyCodeObject *func_code;

	if (!pymethod) {
		return NULL;
	}
	if (PyFunction_Check(pymethod)) {
		func_code = (PyCodeObject *)PyFunction_GetCode(
			PyMethod_Function (pymethod));
		if (argcount == func_code->co_argcount - 1) {
			return pymethod;
		}
	} else if (PyMethod_Check(pymethod)) {
        	func_code = (PyCodeObject *)PyFunction_GetCode(pymethod);
		if (argcount == func_code->co_argcount) {
			return pymethod;
		}
	} 
	return NULL;
}


/*#F If the Python object @var{obj} implements a method whose name matches
  the Objective-C selector @var{aSelector} and accepts the correct number
  of arguments, return that method, otherwise NULL. */
static PyObject*
get_method_for_selector(PyObject *obj, SEL aSelector)
{
	const char*  meth_name;
	int          len;
	char*        pymeth_name;
	unsigned int argcount;
	PyObject*    pymethod;
	const char*  p;

	if (!aSelector) {
		[NSException raise:NSInvalidArgumentException
			     format:@"nil selector"];
	}

	meth_name = SELNAME(aSelector);
	len = strlen(meth_name);
      
	for (argcount=0, p=meth_name; *p; p++) {
		if (*p == ':') {
			argcount++;
		}
	}
  
	pymeth_name = alloca(PYTHONIFIED_LENGTH(meth_name, len, argcount));
	pythonify_objc_message(meth_name, pymeth_name);

	pymethod = PyObject_GetAttrString(obj, pymeth_name);
	return check_argcount(pymethod, argcount);
}


- (BOOL) respondsToSelector:(SEL) aSelector
{
	PyObject *m;

	if ([super respondsToSelector:aSelector]) {
		return YES;
	} 
    
	m = get_method_for_selector(pyObject, aSelector);

	if (m) {
        	return YES;
	} else {
		PyErr_Clear();
		return NO;
	}
}


- (NSMethodSignature *) methodSignatureForSelector:(SEL) sel
{
	/* We can't call our superclass implementation, NSProxy just raises
	 * and exception.
	 */

	char*        	   encoding;
	PyObject*          pymethod;
	PyCodeObject*      func_code;
	int                argcount;

	encoding = (char*)get_selector_encoding (self, sel);
	if (encoding) {
		/* A real Objective-C method */
		return [NSMethodSignature signatureWithObjCTypes:encoding];
	}

	pymethod = get_method_for_selector(pyObject, sel);
	if (!pymethod) {
		PyErr_Clear();
		[NSException raise:NSInvalidArgumentException 
			format:@"No such selector: %s", SELNAME(sel)];
	}


	if (PyMethod_Check (pymethod)) {
		func_code = (PyCodeObject *) PyFunction_GetCode(
			PyMethod_Function (pymethod));
		argcount = func_code->co_argcount-1;
	} else {
		func_code = (PyCodeObject *) PyFunction_GetCode(
			pymethod);
		  argcount = func_code->co_argcount;
	}

	encoding = alloca(argcount+3);
	memset(encoding, '@', argcount+2);
	encoding[argcount+2] = '\0';
	encoding[2] = ':';
	return [NSMethodSignature signatureWithObjCTypes:encoding];
}

/*
 * XXX: Should make sure that this is consistant with forwardInvocation for
 *      ObjCObject_Type
 * XXX: There is no testsuite for this code!
 */
- (void) forwardInvocation:(NSInvocation *) invocation
{
	/* XXX: Needs cleanup */
	NSMethodSignature* msign = [invocation methodSignature];
	SEL                aSelector = [invocation selector];
	PyObject*          pymethod;
	PyObject*          result;
	const char*        rettype = [msign methodReturnType];
	int		   err;
	PyObject*          args = NULL;
	unsigned int       i;
	unsigned int       argcount;      
	PyCodeObject*      func_code;
	int		   retsize = objc_sizeof_type (rettype);
	char*              retbuffer;

	if (retsize == -1) {
		ObjCErr_ToObjC();
	}
	
	retbuffer = alloca(retsize);
  
	pymethod = get_method_for_selector(pyObject, aSelector);

	if (!pymethod) {
		/* The method does not exist. We cannot forward this to our 
		 * super because NSProxy doesn't implement forwardInvocation. 
		 */
		PyErr_Clear();
		[self doesNotRecognizeSelector:aSelector];
		return;
	}
 
	argcount = [msign numberOfArguments];
	args = PyTuple_New(argcount);
	if (args == NULL) {
		ObjCErr_ToObjC();
	}
	for (i=2; i< argcount; i++) {
		const char *argtype;
		char *argbuffer;
		int  argsize;
		PyObject *pyarg;

		argtype = [msign getArgumentTypeAtIndex:i];

		/* What if argtype is a pointer? */

		argsize = objc_sizeof_type(argtype);
		if (argsize == -1) {
			ObjCErr_ToObjC();
		}
		argbuffer = alloca (argsize);
		[invocation getArgument:argbuffer atIndex:i];
		pyarg = pythonify_c_value (argtype, argbuffer);
		if (pyarg == NULL) {
			Py_DECREF(args);
			ObjCErr_ToObjC();
			return;
		}

		PyTuple_SET_ITEM (args, i-2, pyarg);
	}
	result = PyObject_CallObject(pymethod, args);
	Py_DECREF(args);

	if (result == NULL) {
		ObjCErr_ToObjC();
	}

	err = depythonify_c_value (rettype, result, retbuffer);
	if (err == -1) {
		ObjCErr_ToObjC();
	} else {
		[invocation setReturnValue:retbuffer];
	}
}


- (PyObject *)  pyObject
{
	return pyObject;
}

- (PyObject *)  __pyobjc_PythonObject__
{
	Py_INCREF(pyObject);
	return pyObject;
}

@end /* OC_PythonObject class implementation */
