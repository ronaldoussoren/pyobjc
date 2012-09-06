#include <Python.h>
#include "pyobjc-api.h"

#import <ApplicationServices/ApplicationServices.h>


static PyObject*
m_CTFontCopyAvailableTables(PyObject* self __attribute__((__unused__)), 
		PyObject* args)
{
	PyObject* py_font;
	PyObject* py_options;
	CTFontRef font;
	CTFontTableOptions options;
	CFArrayRef ref;
	Py_ssize_t len, i;
	PyObject*  result;

	if (!PyArg_ParseTuple(args, "OO", &py_font, &py_options)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CTFontRef), py_font, &font) == -1) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CTFontTableOptions), py_options, &options) == -1) {
		return NULL;
	}

	PyObjC_DURING
		ref = CTFontCopyAvailableTables(font, options);

	PyObjC_HANDLER
		ref = NULL;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER;

	if (ref == NULL) {
		if (PyErr_Occurred()) {
			return NULL;
		}

		Py_INCREF(Py_None);
		return Py_None;
	}

	len = CFArrayGetCount(ref);
	result = PyTuple_New(len);
	if (result == NULL) {
		CFRelease(ref);
		return NULL;
	}

	for (i = 0; i < len; i++) {
		CTFontTableTag tag = (CTFontTableTag)(uintptr_t)CFArrayGetValueAtIndex(ref, i);
		PyTuple_SET_ITEM(result, i, PyInt_FromLong(tag));
		if (PyTuple_GET_ITEM(result, i) == NULL) {
			Py_DECREF(result);
			CFRelease(ref);
			return NULL;
		}
	}
	CFRelease(ref);
	return result;
}

static PyObject*
m_CTParagraphStyleGetTabStops(PyObject* self __attribute__((__unused__)),
		PyObject* args)
{
	PyObject* py_style;
	CTParagraphStyleRef style;
	CFArrayRef output = NULL;
	PyObject* result;
	bool b;

	if (!PyArg_ParseTuple(args, "O", &py_style)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CTParagraphStyleRef), py_style, &style) == -1) {
		return NULL;
	}

	PyObjC_DURING
		b = CTParagraphStyleGetValueForSpecifier(style, kCTParagraphStyleSpecifierTabStops,
				sizeof(CFArrayRef), &output);
	PyObjC_HANDLER
		b = 0;
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}


	if (!b) {
		return Py_BuildValue("OO", Py_False, Py_None);
	} 

	result = Py_BuildValue("NN", PyBool_FromLong(b), PyObjC_IdToPython((NSObject*)output));
	return result;
}

static PyObject*
m_CTParagraphStyleCreate(PyObject* self __attribute__((__unused__)),
		PyObject* args)
{
	PyObject* py_settings;
	PyObject* seq;
	PyObject* result;
	Py_ssize_t len, i;
	CFArrayRef aref = NULL;
	CTParagraphStyleSetting* settings;
	CTParagraphStyleRef style = NULL;

	if (!PyArg_ParseTuple(args, "O" Py_ARG_SIZE_T, &py_settings, &len)) {
		return NULL;
	}

	if (py_settings == Py_None) {
		/* Handle simple case */
		if (len != 0) {
			PyErr_SetString(PyExc_ValueError, "settings list is 'None', length is not 0");
			return NULL;
		}
		PyObjC_DURING
			style = CTParagraphStyleCreate(NULL, 0);

		PyObjC_HANDLER
			style = NULL;
			PyObjCErr_FromObjC(localException);
		PyObjC_ENDHANDLER

		if (PyErr_Occurred()) {
			return NULL;
		}
		if (style == NULL) {
			Py_INCREF(Py_None);
			return Py_None;
		}

		result = PyObjC_ObjCToPython(@encode(CTParagraphStyleRef), &style);
		CFRelease(style);
		return result;
	}

	seq = PySequence_Fast(py_settings, "need sequence of settings");
	if (seq == NULL) {
		return NULL;
	}

	if (PySequence_Fast_GET_SIZE(seq) < len) {
		PyErr_Format(PyExc_ValueError, "need sequence of at least %ld arguments",
				(long)len);
		Py_DECREF(seq);
		return NULL;
	}

	settings = malloc(sizeof(*settings) * len);
	if (settings == NULL) {
		Py_DECREF(seq);
		PyErr_NoMemory();
		return NULL;
	}

	for (i = 0; i < len; i++) {
		CTParagraphStyleSetting* cur = settings + i;
		PyObject* curPy = PySequence_Fast_GET_ITEM(seq, i);
		PyObject* s = PySequence_Fast(curPy, "CTParagraphStyleItem");
		int r;

		if (s == NULL) {
			Py_DECREF(seq);
			free(settings);
			return NULL;
		}
		if (PySequence_Fast_GET_SIZE(s) != 3) {
			PyErr_Format(PyExc_ValueError, "settings item has length %ld, not 3", (long)PySequence_Fast_GET_SIZE(s));
			Py_DECREF(seq);
			free(settings);
			return NULL;
		}

		r = PyObjC_PythonToObjC(@encode(CTParagraphStyleSpecifier), 
				PySequence_Fast_GET_ITEM(s, 0), &cur->spec);
		if (r == -1) {
			Py_DECREF(seq);
			free(settings);
			return NULL;
		}
		r = PyObjC_PythonToObjC(@encode(size_t), 
				PySequence_Fast_GET_ITEM(s, 1), &cur->valueSize);
		if (r == -1) {
			Py_DECREF(seq);
			free(settings);
			return NULL;
		}
		if (cur->spec == kCTParagraphStyleSpecifierTabStops) {
			/* Force the size to be correct, just in case */
			cur->valueSize = sizeof(CFArrayRef);

			if (aref != NULL) {
				PyErr_SetString(PyExc_ValueError,
					"Multiple kCTParagraphStyleSpecifierTabStops settings");
				r = -1;
			} else {

				r = PyObjC_PythonToObjC(@encode(CFArrayRef), 
					PySequence_Fast_GET_ITEM(s, 2), &aref);
				cur->value = &aref;
			}
		} else {
			const void* buf;
			Py_ssize_t buflen;

			r = PyObject_AsReadBuffer(
				PySequence_Fast_GET_ITEM(s, 2), &buf, &buflen);
			if (r != -1) {
				if (buflen != cur->valueSize) {
					PyErr_Format(PyExc_ValueError,
						"Got buffer of %ld bytes, need %ld bytes",
						(long)buflen, (long)cur->valueSize);
					r = -1;
				} else {
					cur->value = (void*)buf;
				}
			}
		}
		if (r == -1) {
			Py_DECREF(seq);
			free(settings);
			return NULL;
		}
	}

	CTParagraphStyleRef rv = NULL;

	PyObjC_DURING
		rv = CTParagraphStyleCreate(settings, len);

	PyObjC_HANDLER
		rv = NULL;
		PyObjCErr_FromObjC(localException);
	
	PyObjC_ENDHANDLER

	free(settings);
	
	if (PyErr_Occurred()) {
		if (rv) {
			CFRelease(rv);
		}
		return NULL;
	}

	if (rv == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	result = PyObjC_ObjCToPython(@encode(CTParagraphStyleRef), &rv);
	CFRelease(rv);
	return result;
}




static PyMethodDef mod_methods[] = {
	{
		"CTFontCopyAvailableTables",
		(PyCFunction)m_CTFontCopyAvailableTables,
		METH_VARARGS,
		NULL
	},
	{
		"CTParagraphStyleGetTabStops",
		(PyCFunction)m_CTParagraphStyleGetTabStops,
		METH_VARARGS,
		"CTParagraphStyleGetTabStops(style) -> (stop, ...)"
	},
	{
		"CTParagraphStyleCreate",
		(PyCFunction)m_CTParagraphStyleCreate,
		METH_VARARGS,
		NULL,
	},


	{ 0, 0, 0, }
};

PyObjC_MODULE_INIT(_manual)
{
	PyObject* m = PyObjC_MODULE_CREATE(_manual);
	if (m == NULL) PyObjC_INITERROR();

        if (PyObjC_ImportAPI(m) < 0) PyObjC_INITERROR();

	if (PyModule_AddIntConstant(m, "sizeof_CGFloat", sizeof(CGFloat)) < 0) PyObjC_INITERROR();
	if (PyModule_AddIntConstant(m, "sizeof_CTTextAlignment", sizeof(CTTextAlignment)) < 0) PyObjC_INITERROR();
	if (PyModule_AddIntConstant(m, "sizeof_CTLineBreakMode", sizeof(CTLineBreakMode)) < 0) PyObjC_INITERROR();
	if (PyModule_AddIntConstant(m, "sizeof_CTWritingDirection", sizeof(CTWritingDirection)) < 0) PyObjC_INITERROR();
	if (PyModule_AddIntConstant(m, "sizeof_id", sizeof(id)) < 0) PyObjC_INITERROR();

	PyObjC_INITDONE();
}
