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

#if PY_MAJOR_VERSION == 2 && PY_MINOR_VERSION == 2 && PY_MICRO_VERSION == 0

    /* Python 2.2.0 contains incorrect definitions for PyMapping_DelItem
     * and PyMapping_DelItemString
     */
#   undef PyMapping_DelItem
#   undef PyMapping_DelItemString

#   define PyMapping_DelItem(O,K) PyDict_DelItem((O),(K))
#   define PyMapping_DelItemString(O,K) PyDict_DelItemString((O),(K))

#endif /* Python 2.2.0 */


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
		const char* error;
		NSString* result;

		error = depythonify_c_value ("@", repr, &result);
		Py_DECREF (repr);
		if (error) {
			NSLog(@"PyObjC: `repr` failed to depythonify: %s",
				error);
			return @"a python object";
		}
		return result;
	} else {
		PyErr_Clear();
		return [super description];
	}
}
  
#define RETURN_RESULT(result) 						\
	do {								\
		if (result)                                             \
		{                                                       \
			OC_PythonObject *ret = [[self class] 		\
					newWithObject:result];		\
			Py_DECREF (result);				\
			return ret;					\
		} else {						\
			PySys_WriteStderr("Error in Python call from ObjC:\n");\
			PyErr_Print();                                  \
			return nil;					\
		}							\
	} while (0)

- (void) doesNotRecognizeSelector:(SEL) aSelector
{
	/* FIXME: Just raise the appropriate Foundation exception */
	ObjCErr_Set(ObjCExc_error, "%s does not recognize -%s",
		[[super description] cString], SELNAME(aSelector));
	ObjCErr_ToObjC();
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
    
	m = get_method_for_selector([self pyObject], aSelector);

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

	pymethod = get_method_for_selector([self pyObject], sel);
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

- (void) forwardInvocation:(NSInvocation *) invocation
{
	NSMethodSignature* msign = [invocation methodSignature];
	SEL                aSelector = [invocation selector];
	PyObject*          pymethod;
	PyObject*          result;
	const char*        rettype = [msign methodReturnType];
	char*              retbuffer = alloca(objc_sizeof_type (rettype));
	const char*        error;
	PyObject*          args = NULL;
	unsigned int       i;
	unsigned int       argcount;      
	PyCodeObject*      func_code;
  
	pymethod = get_method_for_selector([self pyObject], aSelector);

	if (!pymethod) {
		/* The method does not exist. We cannot forward this to our 
		 * super because NSProxy doesn't implement forwardInvocation. 
		 */
		PyErr_Clear();
		[self doesNotRecognizeSelector:aSelector];
		return;
	}
  
	if (PyMethod_Check(pymethod)) {
		func_code = (PyCodeObject *)PyFunction_GetCode(
			PyMethod_Function(pymethod));
		argcount = func_code->co_argcount-1;
	} else {
		func_code = (PyCodeObject *)PyFunction_GetCode (
			pymethod);
		argcount = func_code->co_argcount;
	}

	args = PyTuple_New(argcount);
	if (args == NULL) {
		ObjCErr_ToObjC();
	}
	for (i=argcount+1; i>1; i--) {
		const char *argtype;
		char *argbuffer;
		PyObject *pyarg;

#ifdef NOTOSX /* XXX: This should be abstracted into a macro/function */
		argtype = [msign argumentInfoAtIndex:i].type;
#else
		argtype = [msign getArgumentTypeAtIndex:i];
#endif
		argbuffer = alloca (objc_sizeof_type (argtype));
		[invocation getArgument:argbuffer atIndex:i];
		pyarg = pythonify_c_value (argtype, argbuffer);

		PyTuple_SET_ITEM (args, i-2, pyarg);
	}
	result = PyObject_CallObject(pymethod, args);
	Py_DECREF(args);

	if (result == NULL) {
		ObjCErr_ToObjC();
	}

	error = depythonify_c_value (rettype, result, retbuffer);
	if (error) {
		NSLog(@"PyObjC: error depythonifying return value of %s: %s\n", SELNAME(aSelector), error);
		/* XXX: Throw ObjC exception */
		abort();
	} else {
		[invocation setReturnValue:retbuffer];
	}
}


/************************ NUMBER PROTOCOL ***********************************/

- (int) numberCheck
{
	return PyNumber_Check([self pyObject]);
}

- (id <PythonObject>) numberAdd:(id <PythonObject>) o2
{
	PyObject *pyo1 = [self pyObject];
	PyObject *pyo2 = [o2 pyObject];
	PyObject *result = PyNumber_Add(pyo1, pyo2);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberSubtract:(id <PythonObject>) o2
{
	PyObject *pyo1 = [self pyObject];
	PyObject *pyo2 = [o2 pyObject];
	PyObject *result = PyNumber_Subtract(pyo1, pyo2);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberMultiply:(id <PythonObject>) o2
{
	PyObject *pyo1 = [self pyObject];
	PyObject *pyo2 = [o2 pyObject];
	PyObject *result = PyNumber_Multiply(pyo1, pyo2);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberDivide:(id <PythonObject>) o2
{
	PyObject *pyo1 = [self pyObject];
	PyObject *pyo2 = [o2 pyObject];
	PyObject *result = PyNumber_Divide(pyo1, pyo2);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberRemainder:(id <PythonObject>) o2
{
	PyObject *pyo1 = [self pyObject];
	PyObject *pyo2 = [o2 pyObject];
	PyObject *result = PyNumber_Remainder(pyo1, pyo2);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberDivmod:(id <PythonObject>) o2
{
	PyObject *pyo1 = [self pyObject];
	PyObject *pyo2 = [o2 pyObject];
	PyObject *result = PyNumber_Divmod(pyo1, pyo2);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberPower:(id <PythonObject>) o2
                                 :(id <PythonObject>) o3
{
	PyObject *pyo1 = [self pyObject];
	PyObject *pyo2 = [o2 pyObject];
	PyObject *pyo3 = [o3 pyObject];
	PyObject *result = PyNumber_Power(pyo1, pyo2, pyo3);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberNegative
{
	PyObject *pyo = [self pyObject];
	PyObject *result = PyNumber_Negative(pyo);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberPositive
{
	PyObject *pyo = [self pyObject];
	PyObject *result = PyNumber_Positive(pyo);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberAbsolute
{
	PyObject *pyo = [self pyObject];
	PyObject *result = PyNumber_Absolute(pyo);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberInvert
{
	PyObject *pyo = [self pyObject];
	PyObject *result = PyNumber_Invert(pyo);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberLshift:(id <PythonObject>) o2
{
	PyObject *pyo1 = [self pyObject];
	PyObject *pyo2 = [o2 pyObject];
	PyObject *result = PyNumber_Lshift(pyo1, pyo2);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberRshift:(id <PythonObject>) o2
{
	PyObject *pyo1 = [self pyObject];
	PyObject *pyo2 = [o2 pyObject];
	PyObject *result = PyNumber_Rshift(pyo1, pyo2);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberAnd:(id <PythonObject>) o2
{
	PyObject *pyo1 = [self pyObject];
	PyObject *pyo2 = [o2 pyObject];
	PyObject *result = PyNumber_And(pyo1, pyo2);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberXor:(id <PythonObject>) o2
{
	PyObject *pyo1 = [self pyObject];
	PyObject *pyo2 = [o2 pyObject];
	PyObject *result = PyNumber_Xor(pyo1, pyo2);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberOr:(id <PythonObject>) o2
{
	PyObject *pyo1 = [self pyObject];
	PyObject *pyo2 = [o2 pyObject];
	PyObject *result = PyNumber_Or(pyo1, pyo2);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberInt
{
	PyObject *pyo = [self pyObject];
	PyObject *result = PyNumber_Int(pyo);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberLong
{
	PyObject *pyo = [self pyObject];
	PyObject *result = PyNumber_Long(pyo);

	RETURN_RESULT(result);
}

- (id <PythonObject>) numberFloat
{
	PyObject *pyo = [self pyObject];
	PyObject *result = PyNumber_Float(pyo);

	RETURN_RESULT(result);
}

/************************ SEQUENCE PROTOCOL ********************************/

- (int) sequenceCheck
{
	return PySequence_Check([self pyObject]);
}

- (int) sequenceLength
{
	return PySequence_Length([self pyObject]);
}

- (id <PythonObject>) sequenceConcat:(id <PythonObject>) o2
{
	PyObject *pyo1 = [self pyObject];
	PyObject *pyo2 = [o2 pyObject];
	PyObject *result = PySequence_Concat(pyo1, pyo2);

	RETURN_RESULT(result);
}

- (id <PythonObject>) sequenceRepeat:(int) count
{
	PyObject *pyo = [self pyObject];
	PyObject *result = PySequence_Repeat(pyo, count);

	RETURN_RESULT(result);
}

- (id <PythonObject>) sequenceGetItem:(int) count
{
	PyObject *pyo = [self pyObject];
	PyObject *result = PySequence_GetItem(pyo, count);

	RETURN_RESULT(result);
}
  
- (id <PythonObject>) sequenceGetSliceFrom:(int) i1 to:(int) i2
{
	PyObject *pyo = [self pyObject];
	PyObject *result = PySequence_GetSlice(pyo, i1, i2);

	RETURN_RESULT(result);
}

- (int) sequenceSetItem:(int) i value:(id <PythonObject>) v
{
	PyObject *pyo = [self pyObject];
	PyObject *pyv = [v pyObject];

	return PySequence_SetItem(pyo, i, pyv);
}

- (int) sequenceDelItem:(int) i
{
	PyObject *pyo = [self pyObject];

	return PySequence_DelItem(pyo, i);
}

- (int) sequenceSetSliceFrom:(int) i1
                          to:(int) i2
                       value:(id <PythonObject>) v
{
	PyObject *pyo = [self pyObject];
	PyObject *pyv = [v pyObject];

	return PySequence_SetSlice(pyo, i1, i2, pyv);
}

- (int) sequenceDelSliceFrom:(int) i1
                          to:(int) i2
{
	PyObject *pyo = [self pyObject];

	return PySequence_DelSlice(pyo, i1, i2);
}

- (id <PythonObject>) sequenceTuple
{
	PyObject *pyo = [self pyObject];
	PyObject *result = PySequence_Tuple(pyo);

	RETURN_RESULT(result);
}

- (id <PythonObject>) sequenceList
{
	PyObject *pyo = [self pyObject];
	PyObject *result = PySequence_List(pyo);

	RETURN_RESULT(result);
}

- (int) sequenceCount:(id <PythonObject>) value
{
	PyObject *pyo = [self pyObject];
	PyObject *pyv = [value pyObject];

	return PySequence_Count(pyo, pyv);
}

- (int) sequenceIn:(id <PythonObject>) value
{
	PyObject *pyo = [self pyObject];
	PyObject *pyv = [value pyObject];

	return PySequence_In(pyo, pyv);
}

- (int) sequenceIndex:(id <PythonObject>) value
{
	PyObject *pyo = [self pyObject];
	PyObject *pyv = [value pyObject];

	return PySequence_Index(pyo, pyv);
}

/************************* CALLING PROTOCOL ********************************/

- (int) callableCheck
{
	return PyCallable_Check([self pyObject]);
}

- (id <PythonObject>) callableCall:(id <PythonObject>) args
{
	PyObject *pyo = [self pyObject];
	PyObject *pyargs = [args pyObject];
	PyObject *result = PyObject_CallObject(pyo, pyargs);

	RETURN_RESULT(result);
}

- (id <PythonObject>) callableCallFunction:(char *) format, ...
{
	va_list va;
	PyObject *args;
	PyObject *result;

	va_start(va, format);

	if (format) {
		args = Py_VaBuildValue (format, va);
	} else {
		args = PyTuple_New(0);
	}

	va_end(va);

	if (!args) {
		return nil;
	}

	if (!PyTuple_Check(args)) {
		PyObject *a = PyTuple_New(1);

		if (!a) {
			return nil;
		}
		PyTuple_SET_ITEM(a, 0, args);
		args = a;
	}

	result = PyObject_CallObject([self pyObject], args);
	Py_DECREF(args);
	RETURN_RESULT(result);
}


- (id <PythonObject>) callableCallMethod:(char *) m
                                withArgs:(char *) format, ...
{
	va_list va;
	PyObject *args;
	PyObject *method;
	PyObject *result;

	method = PyObject_GetAttrString([self pyObject], m);
	if (!method) {
	      PyErr_SetString(PyExc_AttributeError, m);
	      return nil;
	} else if (!PyCallable_Check(method)) {
		PyErr_SetString(PyExc_TypeError,
			"call of non-callable attribute");
	      return nil;
	}
  
	va_start(va, format);
	if (format) {
		args = Py_VaBuildValue(format, va);
	} else {
		args = PyTuple_New(0);
	}

	va_end(va);
  
	if (!args) return nil;

	if (!PyTuple_Check(args)) {
		PyObject *a = PyTuple_New(1);

		if (!a) return nil;
		PyTuple_SET_ITEM(a, 0, args);
		args = a;
	}

	result = PyObject_CallObject(method, args);
	Py_DECREF(args);
	RETURN_RESULT(result);
}


/************************  MAPPING PROTOCOL *****************************/

- (int) mappingCheck
{
	return PyMapping_Check([self pyObject]);
}

- (int) mappingLength
{
	return PyMapping_Length([self pyObject]);
}

- (int) mappingDelItemCString:(char *) key
{
	return PyMapping_DelItemString([self pyObject], key);
}

- (int) mappingDelItemString:(NSString *) key
{
	return PyMapping_DelItemString(
		[self pyObject], (char *) [key cString]);
}

- (int) mappingDelItem:(id <PythonObject>) key
{
	return PyMapping_DelItem([self pyObject], [key pyObject]);
}

- (int) mappingHasKeyCString:(char *) key
{
	return PyMapping_HasKeyString([self pyObject], key);
}

- (int) mappingHasKeyString:(NSString *) key
{
	return PyMapping_HasKeyString([self pyObject], (char *) [key cString]);
}

- (int) mappingHasKey:(id <PythonObject>) key
{
	return PyMapping_HasKey([self pyObject], [key pyObject]);
}

- (id <PythonObject>) mappingKeys
{
	PyObject *pykeys = PyMapping_Keys([self pyObject]);
	RETURN_RESULT(pykeys);
}

- (id <PythonObject>) mappingItems
{
	PyObject *pyitems = PyMapping_Items([self pyObject]);
	RETURN_RESULT(pyitems);
}

- (id <PythonObject>) mappingValues
{
	PyObject *pyvalues = PyMapping_Values([self pyObject]);
	RETURN_RESULT(pyvalues);
}

- (id <PythonObject>) mappingGetItemCString:(char *) key
{
	PyObject *r= PyMapping_GetItemString([self pyObject], key);
	RETURN_RESULT(r);
}

- (id <PythonObject>) mappingGetItemString:(NSString *) key
{
	PyObject *r = PyMapping_GetItemString(
		[self pyObject], (char *) [key cString]);
	RETURN_RESULT(r);
}

- (int) mappingSetItemCString:(char *) key value:(id <PythonObject>) value
{
	return PyMapping_SetItemString([self pyObject], key, [value pyObject]);
}

- (int) mappingSetItemString:(NSString *) key value:(id <PythonObject>) value
{
	return PyMapping_SetItemString([self pyObject],
			 (char *) [key cString], [value pyObject]);
}


/*********************** PYTHON OBJECT PROTOCOL *****************************/

- (PyObject *) pyObject
{
	return pyObject;
}

- (int) print:(FILE *) fp flags:(int) flags
{
	return PyObject_Print([self pyObject], fp, flags);
}

- (int) hasAttrCString:(char *) attr_name
{
	return PyObject_HasAttrString([self pyObject], attr_name);
}

- (int) hasAttrString:(NSString *) attr_name
{
	return PyObject_HasAttrString([self pyObject], 
		(char *) [attr_name cString]);
}

- (id <PythonObject>) getAttrCString:(char *) attr_name
{
	PyObject *r = PyObject_GetAttrString([self pyObject], attr_name);
	RETURN_RESULT(r);
}

- (id <PythonObject>) getAttrString:(NSString *) attr_name
{
	PyObject *r = PyObject_GetAttrString(
		[self pyObject], (char *) [attr_name cString]);
	RETURN_RESULT(r);
}

- (int) hasAttr:(id <PythonObject>) attr_name
{
	return PyObject_HasAttr([self pyObject], [attr_name pyObject]);
}

- (id <PythonObject>) getAttr:(id <PythonObject>) attr_name
{
	PyObject *r = PyObject_GetAttr([self pyObject], [attr_name pyObject]);
	RETURN_RESULT(r);
}

- (int) setAttrCString:(char *) attr_name value:(id <PythonObject>) value
{
	return PyObject_SetAttrString(
		[self pyObject], attr_name, [value pyObject]);
}

- (int) setAttrString:(NSString *) attr_name value:(id <PythonObject>) value
{
	return PyObject_SetAttrString(
		[self pyObject], (char *)[attr_name cString], [value pyObject]);
}

- (int) setAttr:(id <PythonObject>) attr_name value:(id <PythonObject>) value
{
	return PyObject_SetAttr(
		[self pyObject], [attr_name pyObject], [value pyObject]);
}

- (int) delAttrCString:(char *) attr_name
{
	return PyObject_DelAttrString([self pyObject], attr_name);
}

- (int) delAttrString:(NSString *) attr_name
{
	return PyObject_DelAttrString(
		[self pyObject], (char *)[attr_name cString]);
}

- (int) delAttr:(id <PythonObject>) attr_name
{
	return PyObject_DelAttr([self pyObject], [attr_name pyObject]);
}

- (int) cmp:(id <PythonObject>) o2 result:(int *) result
{
	return PyObject_Cmp([self pyObject], [o2 pyObject], result);
}

- (int) compare:(id <PythonObject>) o2
{
	return PyObject_Compare([self pyObject], [o2 pyObject]);
}

- (id <PythonObject>) repr
{
	PyObject* r = PyObject_Repr([self pyObject]);
	RETURN_RESULT(r);
}

- (id <PythonObject>) str
{
	PyObject* r = PyObject_Str([self pyObject]);
	RETURN_RESULT(r);
}

- (unsigned int) hash
{
	return PyObject_Hash([self pyObject]);
}

- (int) isTrue
{
	return PyObject_IsTrue([self pyObject]);
}

- (id <PythonObject>) type
{
	PyObject* r = PyObject_Type([self pyObject]);
	RETURN_RESULT(r);
}

- (unsigned int) length
{
	int len = PyObject_Length([self pyObject]);

	if (PyErr_Occurred()) {
		ObjCErr_ToObjC();
	}

	return len;
}

- (unsigned int) count
{
	return [self length];
}

- (id <PythonObject>) getItem:(id <PythonObject>) key
{
	PyObject* r = PyObject_GetItem([self pyObject], [key pyObject]);
	RETURN_RESULT(r);
}

- (int) setItem:(id <PythonObject>) key value:(id <PythonObject>) v
{
	return PyObject_SetItem([self pyObject], [key pyObject], [v pyObject]);
}

- (int) delItem:(id <PythonObject>) key
{
	return PyObject_DelItem([self pyObject], [key pyObject]);
}

@end /* OC_PythonObject class implementation */
