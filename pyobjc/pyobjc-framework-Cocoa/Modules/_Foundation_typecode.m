/*
 * Some code that deals with HFSTypeCodes. 
 *
 * Needed for backward compatiblity with earlier versions of PyObjC.
 */
#include "Python.h"



#include "pyobjc-api.h"

#include <Foundation/Foundation.h>

/* inline definition of PyMac_GetOSType pymactoolbox.h doesn't work in 64-bit mode */
extern int PyMac_GetOSType(PyObject *v, OSType *pr);
extern PyObject * PyMac_BuildOSType(OSType t);




PyDoc_STRVAR(objc_NSFileTypeForHFSTypeCode_doc,
	"NSString *NSFileTypeForHFSTypeCode(OSType hfsTypeCode);");
static PyObject* 
objc_NSFileTypeForHFSTypeCode(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static	char* keywords[] = { "hfsTypeCode", NULL };
	PyObject*  result;
	NSString*  oc_result;
	OSType hfsTypeCode;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
			"i:NSFileTypeForHFSTypeCode",
			keywords, &hfsTypeCode)) {
		PyErr_Clear();
		if (!PyArg_ParseTupleAndKeywords(args, kwds, 
				"O&:NSFileTypeForHFSTypeCode",
				keywords, PyMac_GetOSType, &hfsTypeCode)) {
			return NULL;
		}
	}
	
	PyObjC_DURING
		oc_result = NSFileTypeForHFSTypeCode(hfsTypeCode);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		oc_result = NULL;
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) return NULL;

	result = PyObjC_IdToPython(oc_result);
	return result;
}

PyDoc_STRVAR(objc_NSHFSTypeCodeFromFileType_doc,
		"OSType NSHFSTypeCodeFromFileType(NSString *fileType);");
static PyObject* 
objc_NSHFSTypeCodeFromFileType(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static	char* keywords[] = { "hfsTypeCode", NULL };
	NSString*  fileType;
	OSType hfsTypeCode;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
			"O&:NSHFSTypeCodeFromFileType",
			keywords, PyObjCObject_Convert, &fileType)) {
		return NULL;
	}
	
	PyObjC_DURING
		hfsTypeCode = NSHFSTypeCodeFromFileType(fileType);
	PyObjC_HANDLER
		hfsTypeCode = 0;
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) return NULL;

	return PyMac_BuildOSType(hfsTypeCode);
}

PyDoc_STRVAR(mod_doc, "");

static PyMethodDef mod_methods[] = {
	{ 
		"NSFileTypeForHFSTypeCode", 
		(PyCFunction)objc_NSFileTypeForHFSTypeCode, 
		METH_VARARGS|METH_KEYWORDS, 
		objc_NSFileTypeForHFSTypeCode_doc
	},
	{ 
		"NSHFSFTypeCodeFromFileType", 
		(PyCFunction)objc_NSHFSTypeCodeFromFileType, 
		METH_VARARGS|METH_KEYWORDS, 
		objc_NSHFSTypeCodeFromFileType_doc 
	},
	{ 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
	"_typecode",
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

PyObject* PyInit__typecode(void);

PyObject*
PyInit__typecode(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_typecode(void);

void
init_typecode(void)
#endif
{
	PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("_typecode", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) INITERROR();

	INITDONE();
}
