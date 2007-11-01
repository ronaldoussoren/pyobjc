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

#if MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_3
#import  <Foundation/NSKeyValueObserving.h>
#endif

#import "OC_PythonUnicode.h"
#import "OC_PythonString.h"

extern NSString * const NSUnknownKeyException; /* Radar #3336042 */

PyObject *OC_PythonObject_DepythonifyTable = NULL;
PyObject *OC_PythonObject_PythonifyStructTable = NULL;

@implementation OC_PythonObject
+ (int)wrapPyObject:(PyObject *)argument toId:(id *)datum
{
	int r;
	id rval;
	PyObject *anObject;
	 
	if (unlikely(argument == Py_None)) {
		rval = nil;
		r = 0;
		goto end;
	}

	rval = PyObjC_FindObjCProxy(argument);
	if (unlikely(rval != nil)) { 
		[[rval retain] autorelease];
		r = 0; 
		goto end; 
	}
	
	if (likely(PyObjCObject_Check (argument))) {
		rval = PyObjCObject_GetObject(argument);
		r = 0;
		goto end;
	} else if (unlikely(PyObjCClass_Check(argument))) {
		rval = (id)PyObjCClass_GetClass(argument);
		r = 0;
		goto end;
	}    

	anObject = PyObject_GetAttrString(argument, "__pyobjc_object__");
	if (unlikely(anObject)) {
		if (anObject != argument) {
			r = [self wrapPyObject:anObject toId:datum];
			Py_DECREF(anObject);
			return r;
		} else {
			Py_DECREF(anObject);
		}
	}
	PyErr_Clear();
 
	if (PyUnicode_Check(argument)) {
		rval = [OC_PythonUnicode
			newWithPythonObject:argument];
		if (rval) {
			PyObjC_RegisterObjCProxy(argument, rval);
			r = 0;
		} else {
			r = -1;
		}
	} else if (PyBool_Check(argument)) {
		rval = [NSNumber 
			numberWithBool:PyInt_AS_LONG (argument)];
		r = 0;
	} else if (PyInt_Check (argument)) {
		rval = [NSNumber 
			numberWithLong:PyInt_AS_LONG (argument)];
		r = 0;
	} else if (PyFloat_Check (argument)) {
		rval = [NSNumber 
			numberWithDouble:PyFloat_AS_DOUBLE (argument)];
		r = 0;
	} else if (PyLong_Check(argument)) {
		rval = [NSNumber 
			numberWithLongLong:PyLong_AsLongLong(argument)];
		if (PyErr_Occurred()) {
			/* Probably overflow */
			rval = nil;
			r = -1;
		} else {
			r = 0;
		}
	} else if (PyList_Check(argument) || PyTuple_Check(argument)) {
		rval = [OC_PythonArray 
			newWithPythonObject:argument];
		PyObjC_RegisterObjCProxy(argument, rval);
		r = 0;
	} else if (PyDict_Check(argument)) {
		rval = [OC_PythonDictionary 
			newWithPythonObject:argument];
		PyObjC_RegisterObjCProxy(argument, rval);
		r = 0;
	} else if (PyString_Check(argument)) {
		r = 0;
		if (PyObjC_StrBridgeEnabled == 0) {
			if (PyErr_Warn(PyObjCStrBridgeWarning, "use unicode(str, encoding) for NSString")) {
				r = -1;
				rval = nil;
			}
		}
		if (r == 0) {
			rval = [OC_PythonString
				newWithPythonObject:argument];
			if (rval) {
				PyObjC_RegisterObjCProxy(argument, rval);
				r = 0;
			} else {
				r = -1;
			}
		}
	} else if (PyObject_CheckReadBuffer(argument)) {
		rval = [OC_PythonData
			newWithPythonObject:argument];
		if (rval) {
			PyObjC_RegisterObjCProxy(argument, rval);
			r = 0;
		} else {
			r = -1;
		}
	} else if ((rval = PyObjC_CFTypeToID(argument))) {
		// unwrapped cf
		r = 0;
	} else {
		PyObjC_DURING
			rval = [OC_PythonObject 
				newWithCoercedObject:argument];

			r = 0;

		PyObjC_HANDLER
			PyObjCErr_FromObjC(localException);
			rval = nil;
			r = -1;

		PyObjC_ENDHANDLER
	}

end:
	*datum = rval;
	return r;
}

+ newWithObject:(PyObject *) obj
{
	id instance;
	if (likely(PyObjCObject_Check(obj))) {
		instance = PyObjCObject_GetObject(obj);
	} else {
		instance = [[self alloc] initWithObject:obj];
		[instance autorelease];
	}
	return instance;
}

+ newWithCoercedObject:(PyObject *)obj
{
	id instance;
	PyObjC_BEGIN_WITH_GIL
		if (PyObjCObject_Check(obj)) {
			instance = PyObjCObject_GetObject(obj);
			PyObjC_GIL_RETURN(instance);
		}
		if(PyObjCFormalProtocol_Check(obj)) {
			instance = PyObjCFormalProtocol_GetProtocol(obj);
			PyObjC_GIL_RETURN(instance);
		}
		if (OC_PythonObject_DepythonifyTable != NULL &&
			PyList_Check(OC_PythonObject_DepythonifyTable)) {
			int i;
			for (i=0; i<PyList_GET_SIZE(OC_PythonObject_DepythonifyTable); i++) {
				PyObject *tpl = PyList_GET_ITEM(OC_PythonObject_DepythonifyTable, i);
				PyObject *cls;
				if (!PyTuple_Check(tpl)) continue;

				cls = PyTuple_GET_ITEM(tpl, 0);
				if (PyObject_IsInstance(obj, cls)) {
					PyObject *fn;
					PyObject *res;
					int err;
					fn = PyTuple_GET_ITEM(tpl, 1);
					res = PyObject_CallFunctionObjArgs(fn, obj, NULL);
					if (res == NULL) {
						PyObjC_GIL_FORWARD_EXC();
					}
					if (PyObject_IsInstance(res, cls)) {
						Py_DECREF(res);
						continue;
					}
					err = depythonify_c_value (@encode(id), res, &instance);
					Py_DECREF(res);
					if (err == -1) {
						PyObjC_GIL_FORWARD_EXC();
					} else {
						PyObjC_GIL_RETURN(instance);
					}
				}
			}
		}

		/* Check if the object is "sequence-like" */
		instance = [OC_PythonArray depythonifyObject:obj];
		if (instance != nil) {
			PyObjC_GIL_RETURN(instance);
		} 
		if (PyErr_Occurred()) {
			PyObjC_GIL_FORWARD_EXC();
		}

		/* Check if the object is "mapping-like" */
		instance = [OC_PythonDictionary depythonifyObject:obj];
		if (instance != nil) {
			PyObjC_GIL_RETURN(instance);
		} 
		if (PyErr_Occurred()) {
			PyObjC_GIL_FORWARD_EXC();
		}

		/* If all else fails use the generic proxy */
		instance = [[self alloc] initWithObject:obj];
	PyObjC_END_WITH_GIL
	[instance autorelease];
	return instance;
}

+ depythonifyTable
{
	PyObjC_BEGIN_WITH_GIL
		if (OC_PythonObject_DepythonifyTable == NULL) {
			OC_PythonObject_DepythonifyTable = PyList_New(0);
		}
		id rval;
		int err = depythonify_c_value(@encode(id), OC_PythonObject_DepythonifyTable, &rval);
		if (err == -1) {
			PyObjC_GIL_FORWARD_EXC();
		}
		PyObjC_GIL_RETURN(rval);
	PyObjC_END_WITH_GIL
}

+ pythonifyStructTable
{
	PyObjC_BEGIN_WITH_GIL
		if (OC_PythonObject_PythonifyStructTable == NULL) {
			OC_PythonObject_PythonifyStructTable = PyDict_New();
		}
		id rval;
		int err = depythonify_c_value(@encode(id), OC_PythonObject_PythonifyStructTable, &rval);
		if (err == -1) {
			PyObjC_GIL_FORWARD_EXC();
		}
		PyObjC_GIL_RETURN(rval);
	PyObjC_END_WITH_GIL
}

+ (PyObject *)__pythonifyStruct:(PyObject*)obj withType:(const char *)type length:(Py_ssize_t)length
{
	if (OC_PythonObject_PythonifyStructTable == NULL) {
		Py_INCREF(obj);
		return obj;
	}
	PyObject *typeString = PyString_FromStringAndSize(type, length);
	if (type == NULL) {
		return NULL;
	}
	PyObject *convert = PyDict_GetItem(OC_PythonObject_PythonifyStructTable, typeString);
	Py_DECREF(typeString);
	if (convert == NULL) {
		Py_INCREF(obj);
		return obj;
	}
	return PyObject_CallFunctionObjArgs(convert, obj, NULL);
}

- initWithObject:(PyObject *) obj
{
	PyObjC_BEGIN_WITH_GIL
		if (pyObject) {
			PyObjC_UnregisterObjCProxy(pyObject, self);
		}
		PyObjC_RegisterObjCProxy(obj, self);
		Py_XINCREF(obj);
		Py_XDECREF(pyObject);
		pyObject = obj;
		PyObjC_GIL_RETURN(self);
	PyObjC_END_WITH_GIL
}

-(void)release
{
	/* See comment in OC_PythonUnicode */
	PyObjC_BEGIN_WITH_GIL
		[super release];
	PyObjC_END_WITH_GIL
}
        


- (void)dealloc
{
	PyObjC_BEGIN_WITH_GIL
		PyObjC_UnregisterObjCProxy(pyObject, self);
		Py_XDECREF(pyObject);

	PyObjC_END_WITH_GIL

	[super dealloc];
}

/* Undocumented method used by NSLog, this seems to work. */
- (NSString*) _copyDescription
{
	return [[self description] copy];
}

- (NSString*) description
{
	PyObject *repr;

	if (pyObject == NULL) return @"no python object";
	
	PyObjC_BEGIN_WITH_GIL

		repr = PyObject_Repr (pyObject);
		if (repr) {
			int err;
			NSString* result;
			PyObject *urepr = PyUnicode_FromEncodedObject(
				repr,
				NULL,
				"replace");
			Py_DECREF(repr);
			if (urepr == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}
			err = depythonify_c_value (@encode(id), urepr, &result);
			Py_DECREF (urepr);
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
				self, sel_getName(aSelector)];
}


/*#F Check the argument count of the method/function @var{pymethod},
  returning the method itself if it matches @var{argcount}, NULL
  otherwise. */
static inline PyObject *
check_argcount (PyObject *pymethod, Py_ssize_t argcount)
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
	Py_ssize_t   len;
	char         pymeth_name[256];
	Py_ssize_t   argcount;
	PyObject*    pymethod;
	const char*  p;
	PyObject*    result;

	if (!aSelector) {
		[NSException raise:NSInvalidArgumentException
			     format:@"nil selector"];
	}

	meth_name = sel_getName(aSelector);
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

	result =  check_argcount(pymethod, argcount);
	if (result == NULL) {
		Py_DECREF(pymethod);
	}
	return result;
}


- (BOOL) respondsToSelector:(SEL) aSelector
{
	PyObject *m;
	Method* methods;
	unsigned int method_count;
	unsigned int i;
	void* cookie;

	/*
	 * We cannot rely on NSProxy, it doesn't implement most of the
	 * NSObject interface anyway.
	 */

	cookie = NULL;
	methods = class_copyMethodList(object_getClass(self),
			&method_count);
	if (methods == NULL) {
		return NO;
	}

	for (i = 0 ;i < method_count; i++) {
		if (sel_isEqual(
				method_getName(methods[i]), aSelector)) {
			free(methods);
			return YES;
		}
	}
	free(methods);

	PyObjC_BEGIN_WITH_GIL
		m = get_method_for_selector(pyObject, aSelector);

		if (m) {
			Py_DECREF(m);
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

	char*    	   encoding;
	PyObject*          pymethod;
	PyCodeObject*      func_code;
	Py_ssize_t         argcount;
	Class		   cls;
	Method		   m;

	cls = object_getClass(self);
	m = class_getInstanceMethod(cls, sel);
	if (m) {
		/* A real Objective-C method */
		return [NSMethodSignature 
		    signatureWithObjCTypes:method_getTypeEncoding(m)];
	}

	PyObjC_BEGIN_WITH_GIL

		pymethod = get_method_for_selector(pyObject, sel);
		if (!pymethod) {
			PyErr_Clear();
			PyGILState_Release(_GILState); 
			[NSException raise:NSInvalidArgumentException 
				format:@"Class %s: no such selector: %s", 
				object_getClassName(self), sel_getName(sel)];
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
		Py_DECREF(pymethod);

		encoding = alloca(argcount+4);
		memset(encoding, '@', argcount+3);
		encoding[argcount+3] = '\0';
		encoding[2] = ':';
	
	PyObjC_END_WITH_GIL

	return [NSMethodSignature signatureWithObjCTypes:encoding];
}

- (BOOL) _forwardNative:(NSInvocation*) invocation
{
	/* XXX: This should use libffi to call call native methods of this
	 *      class. The implementation below works good enough for
	 *      now...
	 */
	SEL aSelector = [invocation selector];

	if (sel_isEqual(aSelector, @selector(description))) {
		id res = [self description];
		[invocation setReturnValue:&res];

		return YES;

	} else if (sel_isEqual(aSelector, @selector(_copyDescription))) {
		id res = [self _copyDescription];
		[invocation setReturnValue:&res];

		return YES;

	} else if (sel_isEqual(aSelector, @selector(respondsToSelector:))){
		SEL	sel;
		BOOL	b;

		[invocation getArgument:&sel atIndex:2];

		b = [self respondsToSelector: sel];
		[invocation setReturnValue:&b];

		return YES;
	}

	return NO;
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
	Py_ssize_t	   retsize;
	char*              retbuffer;

	if ([self _forwardNative:invocation]) {
		return;
	}

	PyObjC_BEGIN_WITH_GIL

		retsize = PyObjCRT_SizeOfType (rettype);
		if (retsize == -1) {
			PyObjC_GIL_FORWARD_EXC();
		}
	
		retbuffer = alloca(retsize);
  
		pymethod = get_method_for_selector(pyObject, aSelector);

		if (!pymethod) {
			PyGILState_Release(_GILState);
			[self doesNotRecognizeSelector:aSelector];
			return;
		}
 
		argcount = [msign numberOfArguments];
		args = PyTuple_New(argcount-2);
		if (args == NULL) {
			Py_DECREF(pymethod);
			PyObjC_GIL_FORWARD_EXC();
		}
		for (i=2; i< argcount; i++) {
			const char *argtype;
			char *argbuffer;
			Py_ssize_t  argsize;
			PyObject *pyarg;

			argtype = [msign getArgumentTypeAtIndex:i];

			/* What if argtype is a pointer? */

			argsize = PyObjCRT_SizeOfType(argtype);
			if (argsize == -1) {
				Py_DECREF(args);
				Py_DECREF(pymethod);
				PyObjC_GIL_FORWARD_EXC();
			}
			argbuffer = alloca (argsize);

			PyObjC_DURING
				[invocation getArgument:argbuffer atIndex:i];

			PyObjC_HANDLER
				PyGILState_Release(_GILState);
				[localException raise];

			PyObjC_ENDHANDLER

			pyarg = pythonify_c_value (argtype, argbuffer);
			if (pyarg == NULL) {
				Py_DECREF(args);
				Py_DECREF(pymethod);
				PyObjC_GIL_FORWARD_EXC();
			}

			PyTuple_SET_ITEM (args, i-2, pyarg);
		}
		result = PyObject_CallObject(pymethod, args);
		Py_DECREF(args); args = NULL;
		Py_DECREF(pymethod); pymethod = NULL;

		if (result == NULL) {
			PyObjC_GIL_FORWARD_EXC();
			return;
		}

		err = depythonify_c_value (rettype, result, retbuffer);
		Py_DECREF(result);
		if (err == -1) {
			PyObjC_GIL_FORWARD_EXC();
		} else {
			PyObjC_DURING
				[invocation setReturnValue:retbuffer];

			PyObjC_HANDLER
				PyGILState_Release(_GILState);
				[localException raise];
			PyObjC_ENDHANDLER
		}
	
	PyObjC_END_WITH_GIL
}


- (PyObject *)  pyObject
{
	return pyObject;
}

- (PyObject *)  __pyobjc_PythonObject__
{
	PyObjC_BEGIN_WITH_GIL
	Py_INCREF(pyObject);
	PyObjC_GIL_RETURN(pyObject);
	PyObjC_END_WITH_GIL
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
- (void)takeValue: value forKey: (NSString*) key
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
- (void)takeValue: value forKeyPath: (NSString*)keyPath
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

#if MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_3
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

/* NSObject protocol */
- (unsigned)hash
{
    PyObjC_BEGIN_WITH_GIL
        int rval;
        rval = PyObject_Hash([self pyObject]);
        if (rval == -1) {
            PyErr_Clear();
            rval = (int)[self pyObject];
        }
        PyObjC_GIL_RETURN((unsigned)rval);
    PyObjC_END_WITH_GIL
}

- (BOOL)isEqual:(id)anObject
{
    if (anObject == nil) {
        return NO;
    } else if (self == anObject) {
        return YES;
    }
    PyObjC_BEGIN_WITH_GIL
        PyObject *otherPyObject = PyObjC_IdToPython(anObject);
        if (otherPyObject == NULL) {
            PyErr_Clear();
            PyObjC_GIL_RETURN(NO);
        }
        if (otherPyObject == [self pyObject]) {
            PyObjC_GIL_RETURN(YES);
        }
        switch (PyObject_RichCompareBool([self pyObject], otherPyObject, Py_EQ)) {
            case -1:
                PyErr_Clear();
            case 0:
                PyObjC_GIL_RETURN(NO);
                break;
            default:
                PyObjC_GIL_RETURN(YES);
        }
    PyObjC_END_WITH_GIL
}

/* NSObject methods */
- (NSComparisonResult)compare:(id)other
{
    if (other == nil) {
        [NSException raise: NSInvalidArgumentException
                    format: @"nil argument"];
    } else if (self == other) {
        return NSOrderedSame;
    }
    PyObjC_BEGIN_WITH_GIL
        PyObject *otherPyObject = PyObjC_IdToPython(other);
        if (otherPyObject == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }
        if (otherPyObject == [self pyObject]) {
            PyObjC_GIL_RETURN(NSOrderedSame);
        }
        int r;
        if (PyObject_Cmp([self pyObject], otherPyObject, &r) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
        NSComparisonResult rval;
        switch (r) {
            case -1:
                rval = NSOrderedAscending;
                break;
            case 0:
                rval = NSOrderedSame;
                break;
            default:
                rval = NSOrderedDescending;
        }
        PyObjC_GIL_RETURN(rval);
    PyObjC_END_WITH_GIL
}

- (void)encodeWithCoder:(NSCoder*)coder
{
	/* 
	 * Forcefully disable coding for now, to avoid generating invalid
	 * encoded streams.
	 */
	[NSException raise:NSInvalidArgumentException format:@"PyObjC: Encoding python objects of type %s is not supported", [self pyObject]->ob_type->tp_name, coder];
}

- initWithCoder:(NSCoder*)coder
{
	[NSException raise:NSInvalidArgumentException format:@"PyObjC: Decoding python objects is not supported", coder];
	return nil;
}

/* NOTE: NSProxy does not implement isKindOfClass on Leopard, therefore we 
 * have to provide it ourself.
 *
 * Luckily that's kind of easy, we know the entiry class hierarcy and also
 * know there are no subclasses.
 */
- (BOOL)isKindOfClass:(Class)aClass
{
	if (aClass == [NSProxy class] || aClass == [OC_PythonObject class]) {
		return YES;
	} 
	return NO;
}

@end /* OC_PythonObject class implementation */
