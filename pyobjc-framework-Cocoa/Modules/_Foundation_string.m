/*
 * Special wrappers for NSString methods with 'difficult' arguments.
 *
 * -getCString:maxLength:range:remainingRange:	[call]
 * -getCString:maxLength:			[call]
 *
 */
#include <Python.h>
#include "pyobjc-api.h"

#include <Foundation/Foundation.h>


static PyObject*
call_NSString_getCString_maxLength_range_remainingRange_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* rangeObj;
	NSRange aRange;
	NSRange leftoverRange;
	char* buf;
	int maxLength;
	struct objc_super super;
	PyObject* res;

	if  (!PyArg_ParseTuple(arguments, "iO", &maxLength, &rangeObj)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(NSRange), rangeObj, &aRange) < 0) {
		return NULL;
	}

	buf = malloc(maxLength+1);
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		(void)objc_msgSendSuper(&super,
			@selector(getCString:maxLength:range:remainingRange:),
			buf, maxLength, aRange, &leftoverRange);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		free(buf);
		return NULL;
	}
	
	res = PyTuple_New(2);
	if (res == NULL) {
		free(buf);
		return NULL;
	}

	PyTuple_SET_ITEM(res, 0, PyString_FromString(buf));
	free(buf);
	if (PyErr_Occurred()) {
		Py_DECREF(res);
		free(buf);
		return NULL;
	}

	rangeObj = PyObjC_ObjCToPython(@encode(NSRange), &leftoverRange);
	if (rangeObj == NULL) {
		Py_DECREF(res);
		return NULL;
	}

	PyTuple_SET_ITEM(res, 1, rangeObj);
	return res;
}

static PyObject*
call_NSString_getCString_maxLength_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* buf;
	int maxLength;
	struct objc_super super;
	PyObject* res;

	if  (!PyArg_ParseTuple(arguments, "i", &maxLength)) {
		return NULL;
	}

	buf = malloc(maxLength+1);
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		(void)objc_msgSendSuper(&super,
			@selector(getCString:maxLength:),
			buf, maxLength);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		free(buf);
		return NULL;
	}
	
	res = PyString_FromString(buf);
	free(buf);
	if (res == NULL) {
		return NULL;
	}

	return res;
}

static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 } /* sentinel */
};

/* Python glue */
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
	"_string",
	NULL,
	0,
	mod_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit__string(void);

PyObject*
PyInit__string(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_string(void);

void
init_string(void)
#endif
{
	PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("_string", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	Class classNSString = objc_lookUpClass("NSString");
	if (classNSString == NULL) INITDONE();
	if (PyObjC_ImportAPI(m) == -1) INITERROR();


	if (PyObjC_RegisterMethodMapping(
		classNSString,
		@selector(getCString:maxLength:range:remainingRange:),
		call_NSString_getCString_maxLength_range_remainingRange_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		INITERROR();
	}

	if (PyObjC_RegisterMethodMapping(
		classNSString,
		@selector(getCString:maxLength:),
		call_NSString_getCString_maxLength_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		INITERROR();
	}

	INITDONE();
}
