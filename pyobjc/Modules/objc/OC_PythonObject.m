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

PyObject *OC_PythonObject_DepythonifyTable = NULL;
PyObject *OC_PythonObject_PythonifyStructTable = NULL;

#if 0
static void
nsmaptable_python_retain(NSMapTable *table __attribute__((__unused__)), const void *datum) {
	Py_INCREF((PyObject *)datum);
}

static void
nsmaptable_python_release(NSMapTable *table __attribute__((__unused__)), void *datum) {
	Py_DECREF((PyObject *)datum);
}

static void
nsmaptable_objc_retain(NSMapTable *table __attribute__((__unused__)), const void *datum) {
	[(id)datum retain];
}

static void
nsmaptable_objc_release(NSMapTable *table __attribute__((__unused__)), void *datum) {
	[(id)datum release];
}

NSMapTableKeyCallBacks PyObjC_ObjectToIdTable_KeyCallBacks = {
	NULL, // use pointer value for hash
	NULL, // use pointer value for equality
	&nsmaptable_python_retain,
	&nsmaptable_python_release,
	NULL, // generic description
	NULL // not a key
};

NSMapTableValueCallBacks PyObjC_ObjectToIdTable_ValueCallBacks = {
	&nsmaptable_objc_retain,
	&nsmaptable_objc_release,
	NULL  // generic description
};

NSMapTable *PyObjC_ObjectToIdTable = NULL;
#endif

@implementation OC_PythonObject
+ (int)wrapPyObject:(PyObject *)argument toId:(id *)datum
{
	int r;
	id rval;
	 
	if (argument == Py_None) {
		rval = nil;
		r = 0;
		goto end;
	}
#if 0
	if (!PyObjC_ObjectToIdTable) {
		PyObjC_ObjectToIdTable = NSCreateMapTable(PyObjC_ObjectToIdTable_KeyCallBacks, PyObjC_ObjectToIdTable_ValueCallBacks, 1024);
	}
	if ((*datum = (id)NSMapGet(PyObjC_ObjectToIdTable, argument))) {
		// key found
		return 0;
	}
#endif
	
	if (PyObjCClass_Check (argument)) {
		rval = (id)PyObjCClass_GetClass(argument);
		r = 0;
	} else if (PyObjCObject_Check (argument)) {
		rval = PyObjCObject_GetObject(argument);
		r = 0;
	} else if (PyObjCUnicode_Check(argument)) {
		rval = PyObjCUnicode_Extract(argument);
		r = 0;
	} else if (PyUnicode_Check(argument)) {
#ifdef PyObjC_UNICODE_FAST_PATH
		rval = [NSString stringWithCharacters:(const unichar *)PyUnicode_AS_UNICODE(argument) length:(unsigned)PyUnicode_GET_SIZE(argument)];
        r = 0;
#else
		PyObject* utf8 = PyUnicode_AsUTF8String(argument);
		if (utf8) {
			rval = [NSString 
				stringWithUTF8String:
					PyString_AS_STRING(utf8)];
			Py_DECREF(utf8);
			r = 0;
		} else {
			PyErr_Format(PyExc_ValueError,
				"depythonifying 'id', failed "
				"to encode unicode string to UTF8");
			rval = nil;
			r = -1;
		}
#endif
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
		/* XXX: What if the value doesn't fit into a 
		 * 'long long' 
		 */
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
		r = 0;
	} else if (PyDict_Check(argument)) {
		rval = [OC_PythonDictionary 
			newWithPythonObject:argument];
		r = 0;
#ifdef MACOSX
	} else if ((rval = PyObjC_CFTypeToID(argument))) {
		// unwrapped cf
		r = 0;
#endif /* MACOSX */
	} else {
		PyObject *anObject = PyObject_GetAttrString(argument, "__pyobjc_object__");
		if (anObject && anObject != argument) {
			return [self wrapPyObject:anObject toId:datum];
		}
		PyErr_Clear();
		NS_DURING
			rval = [OC_PythonObject 
				newWithCoercedObject:argument];
			r = 0;

		NS_HANDLER
			PyObjCErr_FromObjC(localException);
			rval = nil;
			r = -1;

		NS_ENDHANDLER
	}
#if 0
	NSMapInsert(PyObjC_ObjectToIdTable, (const void *)argument, (const void *)rval);
#endif
end:
	*datum = rval;
	return r;
}

+ newWithObject:(PyObject *) obj
{
	id instance;
	if (PyObjCObject_Check (obj)) {
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
		if (PyObjCObject_Check (obj)) {
			instance = PyObjCObject_GetObject(obj);
			PyObjC_GIL_RETURN(instance);
		}
		if (OC_PythonObject_DepythonifyTable != NULL &&
			PyList_Check(OC_PythonObject_DepythonifyTable)) {
			int i;
			for (i=0; i<PyList_GET_SIZE(OC_PythonObject_DepythonifyTable); i++) {
				PyObject *tpl = PyList_GET_ITEM(OC_PythonObject_DepythonifyTable, i);
				PyObject *cls = PyTuple_GET_ITEM(tpl, 0);
				if (!PyTuple_Check(tpl)) continue;
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

+ (PyObject *)__pythonifyStruct:(PyObject*)obj withType:(const char *)type length:(int)length
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
		Py_XINCREF(obj);
		Py_XDECREF(pyObject);
		pyObject = obj;
		PyObjC_GIL_RETURN(self);
	PyObjC_END_WITH_GIL
}

- (void)dealloc
{
	PyObjC_BEGIN_WITH_GIL
		Py_XDECREF(pyObject);

	PyObjC_END_WITH_GIL

	[super dealloc];
}

/* Undocumented method used by NSLog, this seems to work. */
- (NSString*) _copyDescription
{
	return [[self description] retain];
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
	struct objc_method_list* lst;
	void* cookie;

	/*
	 * We cannot rely on NSProxy, it doesn't implement most of the
	 * NSObject interface anyway.
	 */

	cookie = NULL;
	lst = PyObjCRT_NextMethodList(GETISA(self), &cookie);
	while (lst != NULL) {
		int i;

		for (i = 0; i < lst->method_count; i++) {
			if (PyObjCRT_SameSEL(
					lst->method_list[i].method_name, 
					aSelector)) {
				return YES;
			}
		}
		lst = PyObjCRT_NextMethodList(GETISA(self), &cookie);
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

- (BOOL) _forwardNative:(NSInvocation*) invocation
{
	/* XXX: This should use libffi to call call native methods of this
	 *      class. The implementation below works good enough for
	 *      now...
	 */
	SEL aSelector = [invocation selector];

	if (PyObjCRT_SameSEL(aSelector, @selector(description))) {
		id res = [self description];
		[invocation setReturnValue:&res];

		return YES;

	} else if (PyObjCRT_SameSEL(aSelector, @selector(_copyDescription))) {
		id res = [self _copyDescription];
		[invocation setReturnValue:&res];

		return YES;

	} else if (PyObjCRT_SameSEL(aSelector, @selector(respondsToSelector:))){
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
	int		   retsize;
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
