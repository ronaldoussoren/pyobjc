/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 * Copyright 2002, 2003 Ronald Oussoren, Jack Jansen
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
#include "compile.h" /* From Python */

#include <stdarg.h>

#import  <Foundation/NSObject.h>  
#import  <Foundation/NSMethodSignature.h>
#import  <Foundation/NSInvocation.h>
#import  <Foundation/NSString.h>
#import  <Foundation/NSDictionary.h>
#import  <Foundation/NSEnumerator.h>

#if defined(MACOSX) && MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_3
#import  <Foundation/NSKeyValueObserving.h>
#endif

extern NSString* NSUnknownKeyException; /* Radar #3336042 */

@implementation OC_PythonObject
+ newWithObject:(PyObject *) obj
{
	if (PyObjCObject_Check (obj)) {
		id objc_obj = PyObjCObject_GetObject(obj);
		return objc_obj;
	} else {
		id instance = [[self alloc] initWithObject:obj];
		[instance autorelease];
		return instance;
	}
}

- initWithObject:(PyObject *) obj
{
	Py_XINCREF(obj);
	Py_XDECREF(pyObject);
	pyObject = obj;
	return self;
}

- (void)dealloc
{
	PyObjC_BEGIN_WITH_GIL
		Py_XDECREF(pyObject);

	PyObjC_END_WITH_GIL

	[super dealloc];
}

- (NSString *) description
{
	PyObject *repr;

	if (pyObject == NULL) return @"no python object";
	
	PyObjC_BEGIN_WITH_GIL

		repr = PyObject_Repr (pyObject);
		if (repr) {
			int err;
			NSString* result;

			err = depythonify_c_value ("@", repr, &result);
			Py_DECREF (repr);
			if (err == -1) {
				PyObjC_GIL_FORWARD_EXC();
			}
			PyObjC_GIL_RETURN(result);
		} else {
			PyObjC_GIL_FORWARD_EXC();
		}

	PyObjC_END_WITH_GIL
	
	/* not reached */
	return @"a python object";
}
  
- (void) doesNotRecognizeSelector:(SEL) aSelector
{
	[NSException raise:NSInvalidArgumentException
				format:@"%@ does not recognize -%s",
				self, PyObjCRT_SELName(aSelector)];
}


/*#F Check the argument count of the method/function @var{pymethod},
  returning the method itself if it matches @var{argcount}, NULL
  otherwise. */
static inline PyObject *
check_argcount (PyObject *pymethod, int argcount)
{
	PyCodeObject *func_code;

	if (PyFunction_Check(pymethod)) {
        	func_code = (PyCodeObject *)PyFunction_GetCode(pymethod);
		if (argcount == func_code->co_argcount) {
			return pymethod;
		}
	} else if (PyMethod_Check(pymethod)) {
		func_code = (PyCodeObject *)PyFunction_GetCode(
			PyMethod_Function (pymethod));
		if (argcount == func_code->co_argcount - 1) {
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
	char         pymeth_name[256];
	unsigned int argcount;
	PyObject*    pymethod;
	const char*  p;

	if (!aSelector) {
		[NSException raise:NSInvalidArgumentException
			     format:@"nil selector"];
	}

	meth_name = PyObjCRT_SELName(aSelector);
	len = strlen(meth_name);
      
	for (argcount=0, p=meth_name; *p; p++) {
		if (*p == ':') {
			argcount++;
		}
	}
  
	pymethod = PyObject_GetAttrString(obj, 
			PyObjC_SELToPythonName(
				aSelector, pymeth_name, sizeof(pymeth_name)));
	if (pymethod == NULL) {
		return NULL;	
	}

	return check_argcount(pymethod, argcount);
}


- (BOOL) respondsToSelector:(SEL) aSelector
{
	PyObject *m;

	if ([super respondsToSelector:aSelector]) {
		return YES;
	} 

	PyObjC_BEGIN_WITH_GIL
		m = get_method_for_selector(pyObject, aSelector);

		if (m) {
			PyObjC_GIL_RETURN(YES);
		} else {
			PyErr_Clear();
			PyObjC_GIL_RETURN(NO);
		}
	
	PyObjC_END_WITH_GIL
}


- (NSMethodSignature *) methodSignatureForSelector:(SEL) sel
{
	/* We can't call our superclass implementation, NSProxy just raises
	 * an exception.
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

	PyObjC_BEGIN_WITH_GIL

		pymethod = get_method_for_selector(pyObject, sel);
		if (!pymethod) {
			PyErr_Clear();
			PyGILState_Release(_GILState); // XXX: FIXME
			[NSException raise:NSInvalidArgumentException 
				format:@"Class %s: no such selector: %s", 
				GETISA(self)->name, PyObjCRT_SELName(sel)];
		}


		if (PyMethod_Check(pymethod)) {
			func_code = (PyCodeObject*) PyFunction_GetCode(
				PyMethod_Function (pymethod));
			argcount = func_code->co_argcount-1;

		} else {
			func_code = (PyCodeObject*) PyFunction_GetCode(
				pymethod);
			argcount = func_code->co_argcount;
		}

		encoding = alloca(argcount+4);
		memset(encoding, '@', argcount+3);
		encoding[argcount+3] = '\0';
		encoding[2] = ':';
	
	PyObjC_END_WITH_GIL

	return [NSMethodSignature signatureWithObjCTypes:encoding];
}

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
	volatile unsigned int       i;
	unsigned int       argcount;      
	int		   retsize;
	char*              retbuffer;

	PyObjC_BEGIN_WITH_GIL

		retsize = PyObjCRT_SizeOfType (rettype);
		if (retsize == -1) {
			PyObjC_GIL_FORWARD_EXC();
		}
	
		retbuffer = alloca(retsize);
  
		pymethod = get_method_for_selector(pyObject, aSelector);

		if (!pymethod) {
			/* The method does not exist. We cannot forward this 
			 * to our * super because NSProxy doesn't implement 
			 * forwardInvocation. 
			 */
			PyErr_Clear();

			if (aSelector == @selector(description)) {
				NS_DURING
					id res = [self description];
					[invocation setReturnValue:&res];

				NS_HANDLER
					PyGILState_Release(_GILState); // FIXME
					[localException raise];

				NS_ENDHANDLER

				PyObjC_GIL_RETURNVOID;
			}
			PyGILState_Release(_GILState); // FIXME
			[self doesNotRecognizeSelector:aSelector];
			return;
		}
 
		argcount = [msign numberOfArguments];
		args = PyTuple_New(argcount-2);
		if (args == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}
		for (i=2; i< argcount; i++) {
			const char *argtype;
			char *argbuffer;
			int  argsize;
			PyObject *pyarg;

			argtype = [msign getArgumentTypeAtIndex:i];

			/* What if argtype is a pointer? */

			argsize = PyObjCRT_SizeOfType(argtype);
			if (argsize == -1) {
				PyObjC_GIL_FORWARD_EXC();
			}
			argbuffer = alloca (argsize);

			NS_DURING
				[invocation getArgument:argbuffer atIndex:i];

			NS_HANDLER
				PyGILState_Release(_GILState); // FIXME
				[localException raise];

			NS_ENDHANDLER

			pyarg = pythonify_c_value (argtype, argbuffer);
			if (pyarg == NULL) {
				Py_DECREF(args);
				PyObjC_GIL_FORWARD_EXC();
			}

			PyTuple_SET_ITEM (args, i-2, pyarg);
		}
		result = PyObject_CallObject(pymethod, args);
		Py_DECREF(args);

		if (result == NULL) {
			PyObjC_GIL_FORWARD_EXC();
			return;
		}

		err = depythonify_c_value (rettype, result, retbuffer);
		if (err == -1) {
			PyObjC_GIL_FORWARD_EXC();
		} else {
			NS_DURING
				[invocation setReturnValue:retbuffer];

			NS_HANDLER
				PyGILState_Release(_GILState); // FIXME
				[localException raise];
			NS_ENDHANDLER
		}
	
	PyObjC_END_WITH_GIL
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


/*
 * Implementation for Key-Value Coding.
 *
 * Because this is a subclass of NSProxy we must implement all of the protocol,
 * and cannot rely on the implementation in our superclass. 
 *
 */

+ (BOOL)useStoredAccessor
{
 	return YES;
}

+ (BOOL)accessInstanceVariablesDirectly;
{
	return YES;
}


static PyObject*
getModuleFunction(char* modname, char* funcname)
{
	PyObject* func;
	PyObject* name;
	PyObject* mod;

	name = PyString_FromString(modname);
	if (name == NULL) {
		return NULL;
	}

	mod = PyImport_Import(name);
	if (mod == NULL) {
		Py_DECREF(name);
		return NULL;
	}
	func = PyObject_GetAttrString(mod, funcname);
	if (func == NULL) {
		Py_DECREF(name);
		Py_DECREF(mod);
		return NULL;
	}
	Py_DECREF(name);
	Py_DECREF(mod);

	return func;
}

/*
 *  Call PyObjCTools.KeyValueCoding.getKey to get the value for a key
 */
- valueForKey:(NSString*) key;
{
static  PyObject* getKeyFunc = NULL;

	PyObject* keyName;
	PyObject* val;
	id res = nil;

	PyObjC_BEGIN_WITH_GIL

		if (getKeyFunc == NULL) {
			getKeyFunc = getModuleFunction(
				"PyObjCTools.KeyValueCoding",
				"getKey");
			if (getKeyFunc == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}

		keyName = PyObjC_IdToPython(key);
		if (keyName == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		val = PyObject_CallFunction(getKeyFunc, "OO", pyObject, keyName);
		Py_DECREF(keyName);
		if (val == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		if (depythonify_c_value(@encode(id), val, &res) < 0) {
			Py_DECREF(val);
			PyObjC_GIL_FORWARD_EXC();
		}
		Py_DECREF(val);
	
	PyObjC_END_WITH_GIL

	return res;
}

- storedValueForKey: (NSString*) key;
{
	return [self valueForKey: key];
}


/* Calls PyObjCTools.KeyValueCoding.setKey to set the key */

/* This is the 10.2 flavour of this method, deprecated in 10.3 */
- (void)takeValue: value forKey: key
{
	[self setValue: value forKey: key];
}

- (void)setValue: value forKey: (NSString*) key;
{
static  PyObject* setKeyFunc = NULL;

	PyObject* keyName;
	PyObject* pyValue;
	PyObject* val;

	PyObjC_BEGIN_WITH_GIL

		if (setKeyFunc == NULL) {
			setKeyFunc = getModuleFunction(
				"PyObjCTools.KeyValueCoding",
				"setKey");
			if (setKeyFunc == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}

		keyName = PyObjC_IdToPython(key);
		if (keyName == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		pyValue = PyObjC_IdToPython(value);
		if (pyValue == NULL) {
			Py_DECREF(keyName);
			PyObjC_GIL_FORWARD_EXC();
		}

		val = PyObject_CallFunction(setKeyFunc, "OOO", 
				pyObject, keyName, pyValue);
		Py_DECREF(keyName);
		Py_DECREF(pyValue);
		if (val == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		Py_DECREF(val);

	PyObjC_END_WITH_GIL
}

- (void)takeStoredValue: value forKey: (NSString*) key;
{
	[self takeValue: value forKey: key];
}

- (NSDictionary*) valuesForKeys: (NSArray*)keys;
{
	NSMutableDictionary* result;
	NSEnumerator* enumerator;
	id aKey, aValue;

	enumerator = [keys objectEnumerator];
	result = [NSMutableDictionary dictionary];

	while ((aKey = [enumerator nextObject]) != NULL) {
		aValue = [self valueForKey: aKey];
		[result setObject: aValue forKey: aKey];
	}

	return result;
}

- valueForKeyPath: (NSString*) keyPath;
{
	NSArray* elems = [keyPath componentsSeparatedByString:@"."];
	NSEnumerator* enumerator = [elems objectEnumerator];
	id aKey;
	id target;

	target = self;
	while ((aKey = [enumerator nextObject]) != NULL) {
		target = [target valueForKey: aKey];
	}

	return target;
}

/* takeValue:forKeyPath: was deprecated in 10.3, and is the right way on 10.2 */
- (void)takeValue: value forKeyPath: keyPath
{
	[self setValue: value forKeyPath: keyPath];
}
	
- (void)setValue: value forKeyPath: (NSString*) keyPath;
{
	NSArray* elems = [keyPath componentsSeparatedByString:@"."];
	id target;
	int len;
	int i;

	len = [elems count];
	target = self;
	for (i = 0; i < len-1; i++) {
		target = [target valueForKey: [elems objectAtIndex: i]];
	}

	[target takeValue: value forKey: [elems objectAtIndex: len-1]];
}

- (void)takeValuesFromDictionary: (NSDictionary*) aDictionary
{
	[self setValuesForKeysWithDictionary: aDictionary];
}

- (void)setValuesForKeysWithDictionary: (NSDictionary*) aDictionary;
{
	NSEnumerator* enumerator = [aDictionary keyEnumerator];
	id aKey;
	id aValue;

	while ((aKey = [enumerator nextObject]) != NULL) {
		aValue = [aDictionary objectForKey: aKey];
		[self takeValue: aValue forKey: aKey];
	}
}

- (void)unableToSetNilForKey: (NSString*) key;
{
	[NSException 
		raise: NSUnknownKeyException 
		format: @"cannot set Nil for key: %@", key];
}

- (void)handleQueryWithUnboundKey: (NSString*) key;
{
	[self valueForUndefinedKey: key];
}

- (void)valueForUndefinedKey: (NSString*)key;
{
	[NSException 
		raise: NSUnknownKeyException
		format: @"query for unknown key: %@", key];
}

- (void)handleTakeValue: value forUnboundKey: (NSString*) key;
{
	[self setValue: value forUndefinedKey: key];
}

- (void)setValue: value forUndefinedKey: (NSString*) key;
{
	[NSException 
		raise: NSUnknownKeyException 
		format: @"setting unknown key: %@ to <%@>", key, value];
}

#if defined(MACOSX) && MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_3
- (void)addObserver:(NSObject *)observer forKeyPath:(NSString *)keyPath options:(NSKeyValueObservingOptions)options context:(void *)context;
{
    NSLog(@"*** Ignoring *** %@ for '%@' (of %@ with %#x in %p).\n", NSStringFromSelector(_cmd), keyPath, observer, options, context);
    return;
}
- (void)removeObserver:(NSObject *)observer forKeyPath:(NSString *)keyPath;
{
    NSLog(@"*** Ignoring *** %@ for '%@' (of %@).", NSStringFromSelector(_cmd), keyPath, observer);
}
#endif

@end /* OC_PythonObject class implementation */
