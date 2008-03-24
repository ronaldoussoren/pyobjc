/*
 * The implementation is not present yet, will add later 
 *
 * As the .h file says: the implementation should be correct and easy to
 * read, compactness of storage is not important.
 */
#include "pyobjc.h"

enum {
	ENC_NONE,
	ENC_BOOL,
	ENC_INT,
	ENC_LONG,
	ENC_FLOAT,
	ENC_STRING,
	ENC_UNICODE,
	ENC_TUPLE,
	ENC_LIST,
	ENC_INST,
};

static void encode_none(NSCoder* coder, PyObject* value __attribute__((__unused__)))
{
	[coder encodeInt32:ENC_NONE forKey:@"type"];
}

static PyObject* load_none(NSCoder* coder)
{
	Py_INCREF(Py_None);
	return Py_None;
}


static void save_bool(NSCoder* coder, PyObject* value)
{
	[coder encodeInt32:ENC_BOOL forKey:@"type"];
	if (PyObject_IsTrue(value)) {
		[coder encodeBool:YES forKey:@"value"];
	} else {
		[coder encodeBool:NO forKey:@"value"];
	}
}

static PyObject* load_bool(NSCoder* coder)
{
	BOOL v = [coder decodeBoolForKey:@"value"];
	return PyBool_FromLong(v);
}


static void save_int(NSCoder* coder, PyObject* value)
{
	int64_t v;
	[coder encodeInt32:ENC_INT forKey:@"type"];
	v = PyInt_AsLong(value);
	[coder encodeInt64:v forKey:@"value"];
}

static PyObject* load_int(NSCoder* coder)
{
	int64_t v = [coder decodeInt64ForKey:"@value"];
	return PyLong_FromLongLong(v);
}
	

static void save_long(NSCoder* coder, PyObject* value)
{
	int64_t v = PyLong_AsLongLong(value);
	if (!PyErr_Occurred()) {
		[coder encodeInt32:ENC_INT forKey:@"type"];
		[coder encodeInt64:v forKey:@"value"];
	} else {
		[coder encodeInt32:ENC_LONG forKey:@"type"];
		// ... encode stringified value
	}
}
	
	

int PyObjC_encode_object(NSCoder* coder, PyObject* object)
{
#if 0
	if (object == Py_None) {
		save_none(coder, object);
	} else if (PyBool_CheckExact(object)) {
		save_boolone(coder, object);
	} else if (PyInt_CheckExact(object)) {
		save_int(coder, object);
	} else if (PyLong_CheckExact(object)) {
		save_long(coder, object);
	} else if (PyFloat_CheckExact(object)) {
		save_float(coder, object);
	} else if (PyString_CheckExact(object)) {
		save_string(coder, object);
	} else if (PyUnicode_CheckExact(object)) {
		save_unicode(coder, object);
	} else if (PyList_CheckExact(object)) {
		save_list(coder, object);
	} else if (PyTuple_CheckExact(object)) {
		save_tuple(coder, object);
	} else if (PyInstance_Check(object)) {
		save_instance(coder, object)
	} else {
		save_reduce(coder, object);
	}
#endif
        /* 
	 * Forcefully disable coding for now, to avoid generating invalid
	 * encoded streams.
	 */
	[NSException 
		raise:NSInvalidArgumentException 
		format:@"PyObjC: Encoding python objects of type %s is not supported", object->ob_type->tp_name, coder];
	return -1;
}

PyObject* PyObjC_decode_object(NSCoder* coder)
{
#if 0
	int32_t tp = [coder decodeInt32ForKey:@"type"];
	switch (tp) {
	case ENC_NONE: return load_none(coder);
	case ENC_BOOL: return load_bool(coder);
	case ENC_INT: return load_int(coder);
	case ENC_LONG: return load_long(coder);
	case ENC_FLOAT: return load_float(coder);
	case ENC_STRING: return load_string(coder);
	case ENC_UNICODE: return load_unicode(coder);
	case ENC_TUPLE: return load_tuple(coder);
	case ENC_LIST: return load_list(coder);
	case ENC_INST: return load_int(coder);
	}
#endif

        [NSException 
		raise:NSInvalidArgumentException 
		format:@"PyObjC: Decoding python objects is not supported", coder];
	return nil;

}

