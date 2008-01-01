#include <Python.h>
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>

static PyObject*
mod_CFNumberGetValue(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_number;
	CFNumberRef number;
	Py_ssize_t type;
	PyObject* py_buf = Py_None;
	union {
		SInt8	sint8;
		SInt16	sint16;
		SInt32	sint32;
		SInt64  sint64;
		Float32 float32;
		Float64 float64;
		char    charv;
		short   shortv;
		int     intv;
		long    longv;
		long long  longlongv;
		float  	floatv;
		double	doublev;
		CFIndex indexv;
	} buf;

	if (!PyArg_ParseTuple(args, "Oi|O", &py_number, &type, &py_buf)) {
		return NULL;
	}
	if (py_buf != Py_None) {
		PyErr_SetString(PyExc_ValueError, "Bad value for buffer");
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFNumberRef), py_number, &number) < 0) {
		return NULL;
	}

	Boolean rv = FALSE;
	PyObjC_DURING
		rv = CFNumberGetValue(number, type, &buf);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	if (rv) {
		PyObject* n;
		switch (type) {
		case kCFNumberSInt8Type:
			n = PyObjC_ObjCToPython(@encode(SInt8), &buf.sint8);
			break;

		case kCFNumberSInt16Type:
			n = PyObjC_ObjCToPython(@encode(SInt16), &buf.sint16);
			break;

		case kCFNumberSInt32Type:
			n = PyObjC_ObjCToPython(@encode(SInt32), &buf.sint32);
			break;

		case kCFNumberSInt64Type:
			n = PyObjC_ObjCToPython(@encode(SInt64), &buf.sint64);
			break;

		case kCFNumberFloat32Type:
			n = PyObjC_ObjCToPython(@encode(Float32), &buf.float32);
			break;

		case kCFNumberFloat64Type:
			n = PyObjC_ObjCToPython(@encode(Float64), &buf.float64);
			break;

		case kCFNumberCharType:
			n = PyObjC_ObjCToPython(@encode(char), &buf.charv);
			break;

		case kCFNumberShortType:
			n = PyObjC_ObjCToPython(@encode(short), &buf.shortv);
			break;

		case kCFNumberIntType:
			n = PyObjC_ObjCToPython(@encode(int), &buf.intv);
			break;

		case kCFNumberLongType:
			n = PyObjC_ObjCToPython(@encode(long), &buf.longv);
			break;

		case kCFNumberLongLongType:
			n = PyObjC_ObjCToPython(@encode(long long), &buf.longlongv);
			break;

		case kCFNumberFloatType:
			n = PyObjC_ObjCToPython(@encode(float), &buf.floatv);
			break;

		case kCFNumberDoubleType:
			n = PyObjC_ObjCToPython(@encode(double), &buf.doublev);
			break;

		case kCFNumberCFIndexType:
			n = PyObjC_ObjCToPython(@encode(CFIndex), &buf.indexv);
			break;

		default:
			PyErr_SetString(PyExc_ValueError, "number type");
			return NULL;
		}

		return Py_BuildValue("NN", PyBool_FromLong(1), n);

	} else {
		return Py_BuildValue("NO", PyBool_FromLong(0), Py_None);
	}
}



static PyMethodDef mod_methods[] = {
        {
		"CFNumberGetValue",
		(PyCFunction)mod_CFNumberGetValue,
		METH_VARARGS,
		NULL
	},
	{ 0, 0, 0, 0 } /* sentinel */
};

void init_CFNumber(void);
void init_CFNumber(void)
{
	PyObject* m = Py_InitModule4("_CFNumber", mod_methods, "", NULL,
	PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
}
