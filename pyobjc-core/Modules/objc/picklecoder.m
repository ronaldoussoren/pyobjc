#include "pyobjc.h"

@implementation OC_PickleCoder

-(NSObject*)init
{
	self = [super init];
	if (!self) return nil;

	serialValues = keyedValues = NULL;

	serialValues = PyList_New(0);
	if (!serialValues) {
		[self release];
		return nil;
	}

	keyedValues = PyDict_New();
	if (!keyedValues) {
		[self release];
		return nil;
	}
	return self;
}

-(void)dealloc
{
	Py_DECREF(serialValues); serialValues = NULL;
	Py_DECREF(keyedValues); keyedValues = NULL;
	[super dealloc];
}

-(PyObject*)data
{
	return Py_BuildValue("OO", serialValues, keyedValues);
}

-(void)encodeArrayOfObjCType:(const char*)itemType count:(NSUInteger)count at:(const void*)address
{
}

-(void)encodeBool:(BOOL)value forKey:(NSString*)key
{
	//char typestr[2] = { _C_NSBOOL, 0 };
	//PyObject* item = pythonify_c_value(typestr, &value);
	//PyDict_SetItemString(keyedValues, key, item);
}

-(void)encodeBytes:(void*)address length:(NSUInteger)numBytes
{
	PyObject* value = PyString_FromStringAndSize(address, numBytes);
	PyList_Append(serialValues, value);
	Py_DECREF(value);
}

-(void)encodeBytes:(void*)address length:(NSUInteger)numBytes forKey:(NSString*)key
{
}

-(void)encodeDataObject:(NSData*)data
{
}

-(void)encodeDouble:(double)value forKey:(NSString*)key
{
}

-(void)encodeFloat:(float)value forKey:(NSString*)key
{
}

-(void)encodeInt32:(int32_t)value forKey:(NSString*)key
{
}

-(void)encodeInt64:(int64_t)value forKey:(NSString*)key
{
}

-(void)encodeInt:(int)value forKey:(NSString*)key
{
}

-(void)encodeInteger:(NSInteger)value forKey:(NSString*)key
{
}

-(void)encodeObject:(NSObject*)value
{
	PyObject* encoded = pythonify_c_value(@encode(NSObject*), value);
	PyList_Append(serialValues, encoded);
	Py_DECREF(encoded);
}


-(void)encodeObject:(NSObject*)value forKey:(NSString*)key
{
	/* XXX: research how this should be implemented */
}

- (void)encodeValueOfObjCType:(const char *)valueType at:(const void *)address
{
	PyObject* item = pythonify_c_value(valueType, address);
	PyList_Append(serialValues, item);
}

@end /* OC_PickleCoder */



@implementation OC_PickleDecoder

-(OC_PickleDecoder*)initWithData:(PyObject*)data
{
	self = [super init];
	if (!self) return nil;

	if (!PyTuple_Check(data) || PyTuple_GET_SIZE(data) != 2) {
		return nil;
	}

	serialValues = PyTuple_GET_ITEM(data, 0);
	Py_INCREF(serialValues);
	keyedValues = PyTuple_GET_ITEM(data, 0);
	Py_INCREF(keyedValues);
	return self;
}

-(void)dealloc
{
	Py_DECREF(serialValues); serialValues = NULL;
	Py_DECREF(keyedValues); keyedValues = NULL;
	[super dealloc];
}


@end /* OC_PickleDecoder */
