/*
 * NSFont mappings for 'difficult' methods:
 *
 * -positionsForCompositeSequence:numberOfGlyphs:pointArray:    [call, imp]
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

static PyObject*
call_NSFont_positionsForCompositeSequence_numberOfGlyphs_pointArray_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	int numGlyphs;
	PyObject* glyphList;
	PyObject* seq;
	NSGlyph* glyphs;
	NSPoint* points;
	int i, len;

	if (PyArg_ParseTuple(arguments, "Oi", &glyphList, &numGlyphs) < 0) {
		return 0;
	}

	seq = PySequence_Fast(glyphList, "glyphList is not a sequence");
	if (seq == NULL) {
		return NULL;
	}
	
	len = PySequence_Fast_GET_SIZE(seq);
	if (len < numGlyphs) {
		PyErr_SetString(PyExc_ValueError, "Too few glyphs");
		Py_DECREF(seq);
		return NULL;
	}

	glyphs = malloc(sizeof(NSGlyph));
	if (glyphs == NULL) {
		Py_DECREF(seq);
		return NULL;
	}

	points = malloc(sizeof(NSPoint));
	if (glyphs == NULL) {
		free(glyphs);
		Py_DECREF(seq);
		return NULL;
	}

	for (i = 0; i < len; i++) {
		int r;

		r = PyObjC_PythonToObjC(@encode(NSGlyph), 
			PySequence_Fast_GET_ITEM(seq, i),
			glyphs + i);
		if (r == -1) {
			free(glyphs);
			Py_DECREF(seq);
			return NULL;
		}
	}
	Py_DECREF(seq);

	NS_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		len = (int)objc_msgSendSuper(&super,
			@selector(positionsForCompositeSequence:numberOfGlyphs:pointArray:),
			glyphs, numGlyphs, points);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		len = -1;
	NS_ENDHANDLER

	if (len == -1 && PyErr_Occurred()) {
		free(points);
		free(glyphs);
		return NULL;
	}

	free(glyphs);

	seq = PyTuple_New(len > 0? len: 0);
	if (seq == NULL) {
		free(points);
		return NULL;
	}

	for (i = 0; i < len; i++) {
		PyObject* v;

		v = PyObjC_ObjCToPython(@encode(NSPoint), points + i);
		if (v == NULL) {
			free(points);
			return NULL;
		}

		PyTuple_SET_ITEM(seq, i, v);
	}
	free(points);

	result = Py_BuildValue("(iO)", len, seq);
	Py_DECREF(seq);

	return result;
}

static int
imp_NSFont_positionsForCompositeSequence_numberOfGlyphs_pointArray_(
	id self, SEL sel, NSGlyph* glyphs, int numGlyphs, NSPoint* points)
{
	PyObject* args;
	PyObject* result;
	PyObject* seq;
	PyObject* v;
	int i;
	int retValue;

	args = PyTuple_New(3);
	if (args == NULL) {
		PyObjCErr_ToObjC();
		return -1;
	}
	
	v = PyObjC_IdToPython(self);
	if (v == NULL) {
		Py_DECREF(args);
		PyObjCErr_ToObjC();
		return -1;
	}

	PyTuple_SET_ITEM(args, 0, v);

	v = PyTuple_New(numGlyphs);
	if (v == NULL) {
		Py_DECREF(args);
		PyObjCErr_ToObjC();
		return -1;
	}
	PyTuple_SET_ITEM(args, 1, v);

	for (i = 0; i < numGlyphs; i++) {
		PyObject* t;

		t = PyObjC_ObjCToPython(@encode(NSGlyph), glyphs + i);
		if (t == NULL) {
			Py_DECREF(args);
			PyObjCErr_ToObjC();
			return -1;
		}
		PyTuple_SET_ITEM(v, i, t);
	}

	v = PyInt_FromLong(numGlyphs);
	if (v == NULL) {
		Py_DECREF(args);
		PyObjCErr_ToObjC();
		return -1;
	}

	PyTuple_SET_ITEM(args, 2, v);

	result = PyObjC_CallPython(self, sel, args);
	Py_DECREF(args);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return -1;
	}

	if (!PyTuple_Check(result)) {
		PyErr_SetString(PyExc_TypeError, 
			"Should return tuple (numPoints, points)");
		Py_DECREF(result);
		PyObjCErr_ToObjC();
		return -1;
	}

	if (PyObjC_PythonToObjC(
		@encode(int), PyTuple_GET_ITEM(result, 0), &retValue) < 0) {
		Py_DECREF(result);
		PyObjCErr_ToObjC();
		return -1;
	}

	seq = PySequence_Fast(PyTuple_GET_ITEM(result, 1),
		"Should return tuple (numPoints, points)");
	if (seq == NULL) {
		Py_DECREF(result);
		PyObjCErr_ToObjC();
		return -1;
	}

	if (PySequence_Fast_GET_SIZE(seq) < retValue) {
		PyErr_SetString(PyExc_ValueError, "Too few points returned");
		Py_DECREF(result);
		Py_DECREF(seq);
		PyObjCErr_ToObjC();
		return -1;
	}

	if (retValue > numGlyphs) {
		PyErr_SetString(PyExc_ValueError, "Too many points returned");
		Py_DECREF(result);
		Py_DECREF(seq);
		PyObjCErr_ToObjC();
		return -1;
	}


	for (i = 0; i < retValue; i++) {
		int r;

		r = PyObjC_PythonToObjC(@encode(NSPoint),
			PySequence_Fast_GET_ITEM(seq, i),
			points + i);
		if (r == -1) {
			Py_DECREF(result);
			Py_DECREF(seq);
			PyObjCErr_ToObjC();
			return -1;
		}
	}
	Py_DECREF(seq);
	Py_DECREF(result);

	return retValue;
}

static int 
_pyobjc_install_NSFont(void)
{
	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSFont"), 
		@selector(positionsForCompositeSequence:numberOfGlyphs:pointArray:),
		call_NSFont_positionsForCompositeSequence_numberOfGlyphs_pointArray_,
		(IMP)imp_NSFont_positionsForCompositeSequence_numberOfGlyphs_pointArray_) < 0 ) {

		return -1;
	}

	return 0;
}
