/*
 * NSFont mappings for 'difficult' methods:
 *
 * -positionsForCompositeSequence:numberOfGlyphs:pointArray:    [call, imp]
 * -fontWithName:matrix:
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

	if (!PyArg_ParseTuple(arguments, "Oi", &glyphList, &numGlyphs)) {
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

	result = PyObjC_CallPython(self, sel, args, NULL);
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


static PyObject*
call_NSFont_fontWithName_matrix_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	struct objc_super super;
	id  font;
	id  typeface;
	PyObject* pyFontMatrix;
	float _fontMatrix[6];
	float* volatile fontMatrix;
	PyObject* seq;
	int i, len;

	if (!PyArg_ParseTuple(arguments, "O&O", 
			PyObjCObject_Convert, &typeface, &pyFontMatrix)) {
		return 0;
	}

	if (pyFontMatrix == Py_None) {
		fontMatrix = NULL;

	} else {
		fontMatrix = _fontMatrix;

		seq = PySequence_Fast(pyFontMatrix, "fontMatrix is not a sequence");
		if (seq == NULL) {
			return NULL;
		}
		
		len = PySequence_Fast_GET_SIZE(seq);
		if (len != 6) {
			PyErr_SetString(PyExc_ValueError, "fontMatrix must be exactly 6 floats");
			Py_DECREF(seq);
			return NULL;
		}

		for (i = 0; i < len; i++) {
			int r;

			r = PyObjC_PythonToObjC(@encode(float), 
				PySequence_Fast_GET_ITEM(seq, i),
				fontMatrix + i);
			if (r == -1) {
				Py_DECREF(seq);
				return NULL;
			}
		}
		Py_DECREF(seq);
	}

	NS_DURING
		PyObjC_InitSuperCls(&super,
			PyObjCSelector_GetClass(method),
			PyObjCClass_GetClass(self));

		font = objc_msgSendSuper(&super,
			PyObjCSelector_GetSelector(method),
			typeface, fontMatrix);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		font = nil;
	NS_ENDHANDLER

	if (font == nil && PyErr_Occurred()) {
		return NULL;
	}

	return PyObjC_IdToPython(font);
}

static id
imp_NSFont_fontWithName_matrix_(
	Class self, SEL sel, NSString* typeface, const float* fontMatrix)
{
	PyObject* args;
	PyObject* result;
	PyObject* v;
	int i;
	id retValue;

	args = PyTuple_New(3);
	if (args == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	v = PyObjC_ObjCToPython(@encode(Class), &self);
	if (v == NULL) {
		Py_DECREF(args);
		PyObjCErr_ToObjC();
		return nil;
	}

	PyTuple_SET_ITEM(args, 0, v);

	v = PyObjC_IdToPython(typeface);
	if (v == NULL) {
		Py_DECREF(args);
		PyObjCErr_ToObjC();
		return nil;
	}

	PyTuple_SET_ITEM(args, 1, v);

	if (fontMatrix == NULL) {
		v = Py_None;
		Py_INCREF(Py_None);
	} else {
		v = PyTuple_New(6);
		if (v == NULL) {
			Py_DECREF(args);
			PyObjCErr_ToObjC();
			return nil;
		}
		for (i = 0; i < 6; i++) {
			PyObject* t = PyFloat_FromDouble(fontMatrix[i]);
			if (t == NULL) {
				Py_DECREF(v);
				Py_DECREF(args);
				PyObjCErr_ToObjC();
				return nil;
			}
			PyTuple_SET_ITEM(v, i, t);
		}
	}
	PyTuple_SET_ITEM(args, 2, v);

	result = PyObjC_CallPython(self, sel, args, NULL);
	Py_DECREF(args);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	retValue = PyObjC_PythonToId(result);
	Py_DECREF(result);
	if (retValue == nil && PyErr_Occurred()) {
		PyObjCErr_ToObjC();
		return nil;
	}

	return retValue;
}

static PyObject*
call_NSFont_matrix(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	struct objc_super super;
	PyObject* pyFontMatrix;
	float* fontMatrix;
	int i;

	if (!PyArg_ParseTuple(arguments, "")) {
		return 0;
	}

	NS_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		fontMatrix = (float*)objc_msgSendSuper(&super,
			PyObjCSelector_GetSelector(method));
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		fontMatrix = nil;
	NS_ENDHANDLER

	if (fontMatrix == nil && PyErr_Occurred()) {
		return NULL;
	}

	pyFontMatrix = PyTuple_New(6);
	if (pyFontMatrix == NULL) {
		return NULL;
	}
	for (i = 0; i < 6; i++) {
		PyObject* t = PyFloat_FromDouble(fontMatrix[i]);
		if (t == NULL) {
			Py_DECREF(pyFontMatrix);
		}
		PyTuple_SET_ITEM(pyFontMatrix, i, t);
	}

	return pyFontMatrix;
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

	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSFont"), 
		@selector(fontWithName:matrix:),
		call_NSFont_fontWithName_matrix_,
		(IMP)imp_NSFont_fontWithName_matrix_) < 0 ) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSFont"), 
		@selector(matrix),
		call_NSFont_matrix,
		(IMP)PyObjCUnsupportedMethod_IMP) < 0 ) {

		return -1;
	}

	return 0;
}
