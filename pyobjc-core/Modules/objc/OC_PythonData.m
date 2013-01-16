#include "pyobjc.h"
#import "OC_PythonData.h"

@implementation OC_PythonData 

+ (OC_PythonData*)dataWithPythonObject:(PyObject*)v
{
	OC_PythonData* res;

	res = [[OC_PythonData alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}


- (OC_PythonData*)initWithPythonObject:(PyObject*)v
{
	self = [super init];
	if (unlikely(self == nil)) return nil;

	if (unlikely(PyObject_AsReadBuffer(v, &buffer, &buffer_len) == -1)) {
		[super dealloc];
		return nil;
	}
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

-(NSUInteger)length
{
	NSUInteger rval;
	
	PyObjC_BEGIN_WITH_GIL
		if (unlikely(PyObject_AsReadBuffer(value, &buffer, &buffer_len) == -1)) {
			PyErr_Clear();
			rval = 0;
		} else {
			if ((NSUInteger)buffer_len > NSUIntegerMax) {
				rval = NSUIntegerMax;
			} else {
				rval = buffer_len;
			}
		}
	PyObjC_END_WITH_GIL
	return rval;
}

-(const void *)bytes
{
	const void *rval;
	PyObjC_BEGIN_WITH_GIL
		if (unlikely(PyObject_AsReadBuffer(value, &buffer, &buffer_len) == -1)) {
			PyErr_Clear();
			rval = NULL;
		}
		rval = buffer;
	PyObjC_END_WITH_GIL
	return rval;
}

-(Class)classForCoder
{
	return [OC_PythonData class];
}


-(void)encodeWithCoder:(NSCoder*)coder
{

	PyObjC_BEGIN_WITH_GIL
		if (PyBytes_CheckExact(value)) {
			if (unlikely(PyObject_AsReadBuffer(value, &buffer, &buffer_len) == -1)) {
				PyObjC_GIL_FORWARD_EXC();
			}


			if ([coder allowsKeyedCoding]) {
				[coder encodeInt32:1 forKey:@"pytype"];
				[coder encodeBytes:buffer length:buffer_len forKey: @"pybytes"];

			} else {
				int v = 1;
				[coder encodeValueOfObjCType:@encode(int) at:&v];
				[coder encodeBytes:buffer length:buffer_len];
			}
			
		} else {
			if ([coder allowsKeyedCoding]) {
				[coder encodeInt32:2 forKey:@"pytype"];
			} else {
				int v = 2;
				[coder encodeValueOfObjCType:@encode(int) at:&v];
			}

			PyObjC_encodeWithCoder(value, coder);
		}
	PyObjC_END_WITH_GIL
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
	int v;
	
	if ([coder allowsKeyedCoding]) {

		v = [coder decodeInt32ForKey:@"pytype"];
	} else {
		[coder decodeValueOfObjCType:@encode(int) at:&v];
	}
	if (v == 1) {
		self = [super init];
		if (unlikely(self == nil)) return nil;

		const void *bytes;
		NSUInteger length;

		if ([coder allowsKeyedCoding]) {
			bytes = [coder decodeBytesForKey:@"pybytes" returnedLength:&length];
		} else {
			bytes = [coder decodeBytesWithReturnedLength:&length];
		}
		PyObjC_BEGIN_WITH_GIL
			value = PyBytes_FromStringAndSize(bytes, length);
			if (value == NULL) {
				[super dealloc];
				PyObjC_GIL_FORWARD_EXC();
			}
		PyObjC_END_WITH_GIL;
		return self;

	} else if (v == 2) {

		if (PyObjC_Decoder != NULL) {
			PyObjC_BEGIN_WITH_GIL
				PyObject* cdr = PyObjC_IdToPython(coder);
				if (cdr == NULL) {
					PyObjC_GIL_FORWARD_EXC();
				}

				PyObject* setValue;
				PyObject* selfAsPython = PyObjCObject_New(self, 0, YES);
				setValue = PyObject_GetAttrString(selfAsPython, "pyobjcSetValue_");

				PyObject* v2 = PyObject_CallFunction(PyObjC_Decoder, "OO", cdr, setValue);
				Py_DECREF(cdr);
				Py_DECREF(setValue);
				Py_DECREF(selfAsPython);

				if (v2 == NULL) {
					PyObjC_GIL_FORWARD_EXC();
				}

				Py_XDECREF(value);
				value = v2;

				NSObject* proxy = PyObjC_FindObjCProxy(value);
				if (proxy == NULL) {
					PyObjC_RegisterObjCProxy(value, self);
				} else {
					[self release];
					[proxy retain];
					self = (OC_PythonData*)proxy;
				}


			PyObjC_END_WITH_GIL

			return self;

		} else {
			[NSException raise:NSInvalidArgumentException
					format:@"decoding Python objects is not supported"];
			return nil;

		}

	} else {
		[NSException raise:NSInvalidArgumentException
				format:@"encoding Python objects is not supported"];
	}
	return self;
}


@end /* implementation OC_PythonData */
