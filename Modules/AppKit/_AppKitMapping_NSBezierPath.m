/*
 * NSBezierPath mappings for special methods:
 * - appendBezierPathWithGlyphs:count:inFont:  [call, imp]
 * - appendBezierPathWithPoints:count:	       [call, imp]
 * - elementAtIndex:associatedPoints:	       [call, imp]
 * - setAssociatedPoints:atIndex:	       [call]
 * - setLineDash:count:phase:		       [call, imp]
 *
 * Not supported:
 * - getLineDash:count:phase:
 *   The documentation is too vague, I wouldn't know how I can determine the
 *   required size for the pattern buffer.
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

static PyObject* call_NSBezierPath_appendBezierPathWithGlyphs_count_inFont_(
		PyObject* method __attribute__((__unused__)), 
		PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	PyObject* glyphList;
	PyObject* seq;
	NSGlyph* glyphs;
	int count;
	id fontObj;
	int i;
	
	if  (PyArg_ParseTuple(arguments, "OiO&", &glyphList, &count, 
			PyObjCObject_Convert, &fontObj) < 0) {
		return NULL;
	}

	seq = PySequence_Fast(glyphList, "glyphs must be a sequence");
	if (count > PySequence_Fast_GET_SIZE(seq)) {
		Py_DECREF(seq);
		PyErr_SetString(PyExc_ValueError, "Count larger than sequence");
		return NULL;
	}

	glyphs = malloc (sizeof(NSGlyph) * count);
	if (glyphs == NULL) {
		Py_DECREF(seq);
		PyErr_NoMemory();
		return NULL;
	}

	for (i = 0; i < count; i++) {
		int err;

		err = PyObjC_PythonToObjC(@encode(NSGlyph), 
			PySequence_Fast_GET_ITEM(seq, i),
			glyphs + i);
		if (err == -1) {
			Py_DECREF(seq);
			free(glyphs);
			return NULL;
		}
	} 

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCClass_GetClass((PyObject*)(self->ob_type)),
			PyObjCObject_GetObject(self));


		(void)objc_msgSendSuper(&super,
			@selector(appendBezierPathWithGlyphs:count:inFont:),
			glyphs,
			count,
			fontObj);

		free(glyphs);
		result = Py_None;
		Py_INCREF(result);
	NS_HANDLER
		free(glyphs);
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static PyObject* call_NSBezierPath_appendBezierPathWithPoints_count_(
		PyObject* method __attribute__((__unused__)), 
		PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	PyObject* pointList;
	PyObject* seq;
	NSPoint* points;
	int count;
	int i;
	
	if  (PyArg_ParseTuple(arguments, "OiO&", &pointList, &count) < 0) {
		return NULL;
	}

	seq = PySequence_Fast(pointList, "points must be a sequence");
	if (count > PySequence_Fast_GET_SIZE(seq)) {
		Py_DECREF(seq);
		PyErr_SetString(PyExc_ValueError, "Count larger than sequence");
		return NULL;
	}

	points = malloc (sizeof(NSPoint) * count);
	if (points == NULL) {
		Py_DECREF(seq);
		PyErr_NoMemory();
		return NULL;
	}

	for (i = 0; i < count; i++) {
		int err;

		err = PyObjC_PythonToObjC(@encode(NSPoint), 
			PySequence_Fast_GET_ITEM(seq, i),
			points + i);
		if (err == -1) {
			Py_DECREF(seq);
			free(points);
			return NULL;
		}
	} 

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCClass_GetClass((PyObject*)(self->ob_type)),
			PyObjCObject_GetObject(self));


		(void)objc_msgSendSuper(&super,
			@selector(appendBezierPathWithPoints:count:inFont:),
			points,
			count);

		free(points);
		result = Py_None;
		Py_INCREF(result);
	NS_HANDLER
		free(points);
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static PyObject* call_NSBezierPath_elementAtIndex_associatedPoints_(
		PyObject* method __attribute__((__unused__)), 
		PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	int    idx;
	int    pointCount;
	NSPoint points[3];
	NSBezierPathElement res;
	int i;
	
	if  (PyArg_ParseTuple(arguments, "i", &idx) < 0) {
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCClass_GetClass((PyObject*)(self->ob_type)),
			PyObjCObject_GetObject(self));


		res = (NSBezierPathElement)objc_msgSendSuper(&super,
			@selector(elementAtIndex:associatedPoints:),
			idx,
			points);

	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	switch (res) {
	case NSMoveToBezierPathElement: pointCount = 1; break;
	case NSLineToBezierPathElement: pointCount = 1; break;
	case NSCurveToBezierPathElement: pointCount = 3; break;
	case NSClosePathBezierPathElement: pointCount = 0; break;
	default:
		PyErr_SetString(PyExc_ValueError, 
			"ObjC returned illegal value");
		return NULL;
	}

	result = PyTuple_New(2);
	if (result == NULL) return NULL;

	PyTuple_SET_ITEM(result, 0,
		PyObjC_ObjCToPython(@encode(NSBezierPathElement), &res));
	if (PyTuple_GET_ITEM(result, 0) == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	PyTuple_SET_ITEM(result, 1, PyTuple_New(pointCount));
	if (PyTuple_GET_ITEM(result, 1) == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	for (i = 0; i < pointCount; i++) {
		PyTuple_SET_ITEM(PyTuple_GET_ITEM(result, 1), i,
			PyObjC_ObjCToPython(@encode(NSPoint), &points[i]));
		if (PyErr_Occurred()) {
			Py_DECREF(result);
			return NULL;
		}
	}

	return result;
}

static PyObject* call_NSBezierPath_setAssociatedPoints_atIndex_(
		PyObject* method __attribute__((__unused__)), 
		PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	int    idx;
	NSPoint points[3];
	PyObject* pointList;
	PyObject* seq;
	int i, len;
	
	if  (PyArg_ParseTuple(arguments, "Oi", &pointList, &idx) < 0) {
		return NULL;
	}

	memset(points, 0, sizeof(points));

	seq = PySequence_Fast(pointList, "points is not a sequence");
	if (seq == NULL) {
		return NULL;
	}

	len = PySequence_Fast_GET_SIZE(seq);
	if (len > 3) {
		Py_DECREF(seq);
		PyErr_SetString(PyExc_ValueError, "Need at most 3 elements");
		return NULL;
	}

	for (i = 0; i < len; i++) {
		int err = PyObjC_PythonToObjC(@encode(NSPoint), 
			PySequence_Fast_GET_ITEM(seq, i), points + i);
		if (err == -1) {
			return NULL;
		}
	}

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCClass_GetClass((PyObject*)(self->ob_type)),
			PyObjCObject_GetObject(self));


		(void)objc_msgSendSuper(&super,
			@selector(setAssociatedPoints:atIndex:),
			points,
			idx);

		result = Py_None;
		Py_INCREF(result);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static PyObject* call_NSBezierPath_setLineDash_count_phase_(
		PyObject* method __attribute__((__unused__)), 
		PyObject* self, PyObject* arguments)
{
	PyObject* result;
	PyObject* seq;
	struct objc_super super;
	PyObject* patternList;
	float* pattern;
	int count, len, i;
	float phase;

	
	if  (PyArg_ParseTuple(arguments, "Oif", &patternList, &count, &phase) < 0) {
		return NULL;
	}

	seq = PySequence_Fast(patternList, "pattern is not a sequence");
	if (seq == NULL) {
		return NULL;
	}

	len = PySequence_Fast_GET_SIZE(seq);
	if (len < count) {
		Py_DECREF(seq);
		PyErr_SetString(PyExc_ValueError, "Count is larger than list");
		return NULL;
	}

	pattern = malloc(count * sizeof(float));
	if (pattern == NULL) {
		Py_DECREF(seq);
		PyErr_NoMemory();
		return NULL;
	}

	for (i = 0; i < len; i++) {
		int err = PyObjC_PythonToObjC(@encode(float), 
			PySequence_Fast_GET_ITEM(seq, i), pattern + i);
		if (err == -1) {
			return NULL;
		}
	}

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCClass_GetClass((PyObject*)(self->ob_type)),
			PyObjCObject_GetObject(self));


		objc_msgSendSuper(&super,
			@selector(setLineDash:count:phase:),
			pattern, count, phase);

		result = Py_None;
		Py_INCREF(result);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}




static void imp_NSBezierPath_appendBezierPathWithGlyphs_count_inFont_(id self, SEL sel, NSGlyph* glyphs, int count, NSFont* font)
{
	PyObject* result;
	PyObject* arglist;
	PyObject* v;
	int i;

	arglist = PyTuple_New(4);
	if (arglist == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	v = PyObjC_IdToPython(self);
	if (self == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	PyTuple_SET_ITEM(arglist, 0, v);

	v = PyTuple_New(count);
	if (v == NULL) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	for (i = 0; i < count; i++) {
		PyTuple_SET_ITEM(v, i, 
			PyObjC_ObjCToPython(@encode(NSGlyph), glyphs+i));
	}
	if (PyErr_Occurred()) {
		Py_DECREF(v);
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	PyTuple_SET_ITEM(arglist, 1, v);

	v = PyInt_FromLong(count);
	if (v == NULL) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	PyTuple_SET_ITEM(arglist, 2, v);

	v = PyObjC_ObjCToPython(@encode(NSFont*), &font);
	if (v == NULL) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	PyTuple_SET_ITEM(arglist, 3, v);

	result = PyObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	Py_DECREF(result);
}

static void imp_NSBezierPath_appendBezierPathWithPoints_count_(id self, SEL sel, NSPoint* points, int count)
{
	PyObject* result;
	PyObject* arglist;
	PyObject* v;
	int i;

	arglist = PyTuple_New(3);
	if (arglist == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	v = PyObjC_IdToPython(self);
	if (self == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	v = PyTuple_New(count);
	if (v == NULL) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	for (i = 0; i < count; i++) {
		PyTuple_SET_ITEM(v, i, 
			PyObjC_ObjCToPython(@encode(NSPoint), points+i));
	}
	if (PyErr_Occurred()) {
		Py_DECREF(v);
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}


	PyTuple_SET_ITEM(arglist, 1, v);

	v = PyInt_FromLong(count);
	if (v == NULL) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	PyTuple_SET_ITEM(arglist, 2, v);


	result = PyObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	Py_DECREF(result);
}

static NSBezierPathElement imp_NSBezierPath_elementAtIndex_associatedPoints_(id self, SEL sel, int idx, NSPoint* points)
{
	PyObject* result;
	PyObject* seq;
	PyObject* arglist;
	PyObject* v;
	NSBezierPathElement res;
	int err;
	int pointCount;
	int i;

	arglist = PyTuple_New(2);
	if (arglist == NULL) {
		PyObjCErr_ToObjC();
		return 0;
	}

	v = PyObjC_IdToPython(self);
	if (v == NULL) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return 0;
	}
	PyTuple_SET_ITEM(arglist, 0, v);


	v = PyInt_FromLong(idx);
	if (v == NULL) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return 0;
	}

	PyTuple_SET_ITEM(arglist, 1, v);

	result = PyObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return 0;
	}

	seq = PySequence_Fast(result, "should return tuple of lenght 2");
	Py_DECREF(result);
	if (seq == NULL) {
		PyObjCErr_ToObjC();
		return 0;
	}

	if (PySequence_Fast_GET_SIZE(seq) != 2) {
		PyErr_SetString(PyExc_ValueError, 
			"should return tuple of lenght 2");
		Py_DECREF(seq);
		PyObjCErr_ToObjC();
		return 0;
	}

	v = PySequence_Fast_GET_ITEM(seq, 0);

	err = PyObjC_PythonToObjC(@encode(NSBezierPathElement), v, &res);
	if (err == -1) {
		Py_DECREF(seq);
		PyObjCErr_ToObjC();
		return 0;
	}

	v = PySequence_Fast(PySequence_Fast_GET_ITEM(seq, 1),
		"result[1] should be a sequence");
	if (v == NULL) {
		Py_DECREF(seq);
		PyObjCErr_ToObjC();
		return 0;
	}

	switch (res) {
	case NSMoveToBezierPathElement: pointCount = 1; break;
	case NSLineToBezierPathElement: pointCount = 1; break;
	case NSCurveToBezierPathElement: pointCount = 3; break;
	case NSClosePathBezierPathElement: pointCount = 0; break;
	default:
		PyErr_SetString(PyExc_ValueError, 
			"Return[0] should be NS{*}PathElement");
		PyObjCErr_ToObjC();
		return 0;
	}

	if (PySequence_Fast_GET_SIZE(v) != pointCount) {
		PyErr_SetString(PyExc_ValueError,
			"wrong number of points");
		PyObjCErr_ToObjC();
		return 0;
	}

	for (i = 0; i < pointCount; i++) {
		err = PyObjC_PythonToObjC(@encode(NSPoint),
			PySequence_Fast_GET_ITEM(v, i),
			points + i);
		if (err == -1) {
			Py_DECREF(v);
			Py_DECREF(seq);
			PyObjCErr_ToObjC();
			return 0;
		}
	}

	Py_DECREF(v);
	Py_DECREF(seq);

	return res;
}

#define U(x) x __attribute__((__unused__))
static void imp_NSBezierPath_setAssociatedPoints_atIndex_(U(id self), U(SEL sel), U(NSPoint* points), U(int idx))
{
	PyErr_SetString(PyExc_RuntimeError,
		"NSBezierPath -setAssociatedPoints:atIndex: -> Python implementation not supported");
	PyObjCErr_ToObjC();
	return;
}
#undef U

static void imp_NSBezierPath_setLineDash_count_phase_(id self, SEL sel, float* pattern, int count, float phase)
{
	PyObject* result;
	PyObject* arglist;
	PyObject* v;
	int i;

	arglist = PyTuple_New(4);
	if (arglist == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	v = PyObjC_IdToPython(self);
	if (v == NULL) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	PyTuple_SET_ITEM(arglist, 0, v);

	v = PyTuple_New(count);
	if (v == NULL) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	for (i = 0; i < count; i++) {
		PyTuple_SET_ITEM(v, i, 
			PyObjC_ObjCToPython(@encode(float), pattern+i));
	}
	if (PyErr_Occurred()) {
		Py_DECREF(v);
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}


	PyTuple_SET_ITEM(arglist, 1, v);

	v = PyInt_FromLong(count);
	if (v == NULL) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	PyTuple_SET_ITEM(arglist, 2, v);

	v = PyFloat_FromDouble(phase);
	if (v == NULL) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	PyTuple_SET_ITEM(arglist, 3, v);

	result = PyObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	Py_DECREF(result);
}


int _pyobjc_install_NSBezierPath(void)
{
	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSBezierPath"), 
		@selector(appendBezierPathWithGlyphs:count:inFont:),
		call_NSBezierPath_appendBezierPathWithGlyphs_count_inFont_,
		(IMP)imp_NSBezierPath_appendBezierPathWithGlyphs_count_inFont_) < 0 ) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSBezierPath"), 
		@selector(appendBezierPathWithPoints:count:),
		call_NSBezierPath_appendBezierPathWithPoints_count_,
		(IMP)imp_NSBezierPath_appendBezierPathWithPoints_count_) < 0 ) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSBezierPath"), 
		@selector(elementAtIndex:associatedPoints:),
		call_NSBezierPath_elementAtIndex_associatedPoints_,
		(IMP)imp_NSBezierPath_elementAtIndex_associatedPoints_) < 0 ) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSBezierPath"), 
		@selector(setAssociatedPoints:atIndex:),
		call_NSBezierPath_setAssociatedPoints_atIndex_,
		(IMP)imp_NSBezierPath_setAssociatedPoints_atIndex_) < 0 ) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSBezierPath"), 
		@selector(setLineDash:count:phase:),
		call_NSBezierPath_setLineDash_count_phase_,
		(IMP)imp_NSBezierPath_setLineDash_count_phase_) < 0 ) {

		return -1;
	}

	return 0;
}
