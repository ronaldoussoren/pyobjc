#include "pyobjc.h"


static PyObject* mapTypes = NULL;


@implementation OC_PythonSet

+ (instancetype)depythonifyObject:(PyObject*)object
{
	Py_ssize_t i, len;
	
	if (mapTypes == NULL) return NULL;

	len = PyList_GET_SIZE(mapTypes);

	for (i = 0; i < len; i++) {
		PyObject* tp = PyList_GET_ITEM(mapTypes, i);
		int r = PyObject_IsInstance(object, tp);
		if (r == -1) {
			return NULL;
		}

		if (!r) continue;

		/* Instance of this type should be pythonifyed as a sequence */
		return [OC_PythonSet setWithPythonObject:object];
	}

	return NULL;
}

+ (id)depythonifyTable
{
	NSObject* result; 

	PyObjC_BEGIN_WITH_GIL

		if (mapTypes == NULL) {
			mapTypes = PyList_New(0);
			if (mapTypes == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}
		result = PyObjC_PythonToId(mapTypes);
		if (result == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

	PyObjC_END_WITH_GIL

	return result;
}

+ (instancetype)setWithPythonObject:(PyObject*)v
{
	OC_PythonSet* res;

	res = [[OC_PythonSet alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}

- (id)initWithPythonObject:(PyObject*)v
{
	self = [super init];
	if (unlikely(self == nil)) return nil;

	Py_INCREF(v);
	Py_XDECREF(value);
	value = v;
	return self;
}

-(PyObject*)__pyobjc_PythonObject__
{
	Py_INCREF(value);
	return value;
}

-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
	*cookie = 0;
	Py_INCREF(value);
	return value;
}

-(BOOL)supportsWeakPointers { return YES; }

-(oneway void)release
{
	/* See comment in OC_PythonUnicode */
	PyObjC_BEGIN_WITH_GIL
		[super release];
	PyObjC_END_WITH_GIL
}

-(void)dealloc
{
	PyObjC_BEGIN_WITH_GIL
		PyObjC_UnregisterObjCProxy(value, self);
		Py_XDECREF(value);

	PyObjC_END_WITH_GIL

	[super dealloc];
}


/* NSCoding support */

-(Class)classForCoder
{
	return [OC_PythonSet class];
}


- (void)encodeWithCoder:(NSCoder*)coder
{
	PyObjC_encodeWithCoder(value, coder);
}


/* 
 * Helper method for initWithCoder, needed to deal with
 * recursive objects (e.g. o.value = o)
 */
-(void)pyobjcSetValue:(NSObject*)other
{
	PyObjC_BEGIN_WITH_GIL
		PyObject* v = PyObjC_IdToPython(other);
		Py_XDECREF(value);
		value = v;
	PyObjC_END_WITH_GIL
}

- (id)initWithCoder:(NSCoder*)coder
{
	if (PyObjC_Decoder != NULL) {
		PyObjC_BEGIN_WITH_GIL
			PyObject* cdr = PyObjC_IdToPython(coder);
			if (cdr == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}

			PyObject* setValue;
			PyObject* selfAsPython = PyObjCObject_New(self, 0, YES);
			setValue = PyObject_GetAttrString(selfAsPython, "pyobjcSetValue_");

			PyObject* v = PyObject_CallFunction(PyObjC_Decoder, "OO", cdr, setValue);
			Py_DECREF(cdr);
			Py_DECREF(setValue);
			Py_DECREF(selfAsPython);

			if (v == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}

			Py_XDECREF(value);
			value = v;

			NSObject* proxy = PyObjC_FindObjCProxy(value);
			if (proxy == NULL) {
				PyObjC_RegisterObjCProxy(value, self);
			} else {
				[self release];
				[proxy retain];
				self = (OC_PythonSet*)proxy;
			}


		PyObjC_END_WITH_GIL

		return self;

	} else {
		[NSException raise:NSInvalidArgumentException
				format:@"decoding Python objects is not supported"];
		return nil;

	}
}


/*
 * Implementation of the NSMutableSet interface
 */
-(id)copyWithZone:(NSZone*)zone
{
	(void)zone;
	if (PyObjC_CopyFunc != NULL) {
		PyObjC_BEGIN_WITH_GIL
			PyObject* tmp = PyObject_CallFunction(PyObjC_CopyFunc, "O", value);
			if (tmp == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}

			NSObject* result = PyObjC_PythonToId(tmp);
			Py_DECREF(tmp);
			if (PyErr_Occurred()) {
				PyObjC_GIL_FORWARD_EXC();
			}

			[result retain];
			PyObjC_GIL_RETURN(result);

		PyObjC_END_WITH_GIL

	} else {
		[NSException raise:NSInvalidArgumentException 
		            format:@"cannot copy python set"];
		return nil;
	}
}

-(id)mutableCopyWithZone:(NSZone*)zone
{
	(void)zone;
	PyObjC_BEGIN_WITH_GIL

		PyObject* tmp = PySet_New(value);
		if (tmp == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		NSObject* result = PyObjC_PythonToId(tmp);
		Py_DECREF(tmp);
		if (PyErr_Occurred()) {
			PyObjC_GIL_FORWARD_EXC();
		}
		
		[result retain];
		PyObjC_GIL_RETURN(result);

	PyObjC_END_WITH_GIL
}

-(NSArray*)allObjects
{
	PyObjC_BEGIN_WITH_GIL
		PyObject* tmp = PySequence_List(value);
		if (tmp == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		NSArray* result = (NSArray*)PyObjC_PythonToId(tmp);
		Py_DECREF(tmp);
		if (PyErr_Occurred()) {
			PyObjC_GIL_FORWARD_EXC();
		}

		PyObjC_GIL_RETURN(result);

	PyObjC_END_WITH_GIL
}

-(NSObject*)anyObject
{
	PyObjC_BEGIN_WITH_GIL
		if (PySet_Size(value) == 0) {
			PyObjC_GIL_RETURN(nil);
		}

		PyObject* tmp = PyObject_GetIter(value);
		if (tmp == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		PyObject* v = PyIter_Next(tmp);
		Py_DECREF(tmp);
		if (v == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}
		
		NSObject* result = PyObjC_PythonToId(v);
		Py_DECREF(v);
		if (PyErr_Occurred()) {
			PyObjC_GIL_FORWARD_EXC();
		}
		
		PyObjC_GIL_RETURN(result);

	PyObjC_END_WITH_GIL
}

-(BOOL)containsObject:(id)anObject
{
	PyObjC_BEGIN_WITH_GIL
		PyObject* tmp = PyObjC_IdToPython(anObject);
		if (tmp == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		int r = PySequence_Contains(value, tmp);
		Py_DECREF(tmp);
		if (r == -1) {
			PyObjC_GIL_FORWARD_EXC();
		}


		if (r) {
			PyObjC_GIL_RETURN(YES);
		} else {
			PyObjC_GIL_RETURN(NO);
		}
	PyObjC_END_WITH_GIL
}

-(NSUInteger)count
{
	PyObjC_BEGIN_WITH_GIL
		Py_ssize_t result = PySequence_Size(value);
		if (result == -1) {
			PyObjC_GIL_FORWARD_EXC();
		}

		PyObjC_GIL_RETURN((NSUInteger)result);
	PyObjC_END_WITH_GIL
}

-(NSEnumerator*)objectEnumerator
{
	PyObjC_BEGIN_WITH_GIL
		PyObject* tmp = PyObject_GetIter(value);
		if (tmp == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		NSEnumerator* result = [OC_PythonEnumerator enumeratorWithPythonObject:tmp];
		Py_DECREF(tmp);

		PyObjC_GIL_RETURN(result);

	PyObjC_END_WITH_GIL
}

/* It seems impossible to create an efficient implementation of this method,
 * iteration is basicly the only way to fetch the requested object
 *
 * XXX: this means we should implement more of NS(Mutable)Set interface,
 * that's a lot more efficient than iterating over and over again.
 *
 */
-(id)member:(id)anObject
{
	PyObjC_BEGIN_WITH_GIL
		PyObject* tmpMember = PyObjC_IdToPython(anObject);
		if (tmpMember == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		int r = PySequence_Contains(value, tmpMember);
		if (r == -1) {
			Py_DECREF(tmpMember);
			PyObjC_GIL_FORWARD_EXC();
		}

		if (!r) {
			Py_DECREF(tmpMember);
			PyObjC_GIL_RETURN(nil);
		}


		/* This sucks, we have to iterate over the contents of the
		 * set to find the object we need...
		 */
		PyObject* tmp = PyObject_GetIter(value);
		if (tmp == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		PyObject* v;
		
		while ((v = PyIter_Next(tmp)) != NULL) {
			r = PyObject_RichCompareBool(v, tmpMember, Py_EQ);
			if (r == -1) {
				Py_DECREF(tmp);
				Py_DECREF(tmpMember);
				PyObjC_GIL_FORWARD_EXC();
			}

			if (r) {
				/* Found the object */
				Py_DECREF(tmp);
				Py_DECREF(tmpMember);

				NSObject* result = PyObjC_PythonToId(v);
				if (PyErr_Occurred()) {
					PyObjC_GIL_FORWARD_EXC();
				}
				PyObjC_GIL_RETURN(result);
			}
		}

		Py_DECREF(tmp);
		Py_DECREF(tmpMember);
		PyObjC_GIL_RETURN(nil);


	PyObjC_END_WITH_GIL
}

-(void)removeAllObjects
{
	PyObjC_BEGIN_WITH_GIL
		if (PyFrozenSet_CheckExact(value)) {
			PyErr_SetString(PyExc_TypeError,
				"Cannot mutate a frozenstring");
			PyObjC_GIL_FORWARD_EXC();
		}

		if (PyAnySet_Check(value)) {
			int r = PySet_Clear(value);\
			if (r == -1) {
				PyObjC_GIL_FORWARD_EXC();
			}
		} else {
			/* Assume an object that conforms to 
			 * the set interface 
			 */
			 PyObject* r;
			 
			 r = PyObject_CallMethod(value, "clear", NULL);
			 if (r == NULL) {
				 PyObjC_GIL_FORWARD_EXC();
			 }
			 Py_DECREF(r);
		}
	PyObjC_END_WITH_GIL
}

-(void)removeObject:(id)anObject
{
	PyObjC_BEGIN_WITH_GIL
		PyObject* tmp = PyObjC_IdToPython(anObject);
		if (tmp == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		} 

		if (PyFrozenSet_CheckExact(value)) {
			PyErr_SetString(PyExc_TypeError,
				"Cannot mutate a frozenstring");
			PyObjC_GIL_FORWARD_EXC();
		}

		if (PyAnySet_Check(value)) {
			int r = PySet_Discard(value, tmp);
			Py_DECREF(tmp);
			if (r == -1) {
				PyObjC_GIL_FORWARD_EXC();
			}

		} else {
			 PyObject* r;
			 
			 r = PyObject_CallMethod(value, "discard", "O", tmp);
			 Py_DECREF(tmp);
			 if (r == NULL) {
				 PyObjC_GIL_FORWARD_EXC();
			 }
			 Py_DECREF(r);
		}

	PyObjC_END_WITH_GIL
}

-(void)addObject:(id)anObject
{
	PyObjC_BEGIN_WITH_GIL
		PyObject* tmp = PyObjC_IdToPython(anObject);
		if (tmp == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		} 

		if (PyFrozenSet_CheckExact(value)) {
			PyErr_SetString(PyExc_TypeError,
				"Cannot mutate a frozenstring");
			PyObjC_GIL_FORWARD_EXC();
		}

		if (PyAnySet_Check(value)) {
			int r = PySet_Add(value, tmp);
			Py_DECREF(tmp);
			if (r == -1) {
				PyObjC_GIL_FORWARD_EXC();
			}

		} else {
			 PyObject* r;
			 
			 r = PyObject_CallMethod(value, "add", "O", tmp);
			 Py_DECREF(tmp);
			 if (r == NULL) {
				 PyObjC_GIL_FORWARD_EXC();
			 }
			 Py_DECREF(r);
		}
		
	PyObjC_END_WITH_GIL
}

@end
