static inline int convert_NSAffineTransformStruct(PyObject* object, void* pvar)
{
	int err;

	err = ObjC_PythonToObjC(@encode(NSAffineTransformStruct), object, pvar);
	if (err == -1) {
		return 0;
	}
	return 1;
}
static inline int convert_NSRect(PyObject* object, void* pvar)
{
	int err;

	err = ObjC_PythonToObjC(@encode(NSRect), object, pvar);
	if (err == -1) {
		return 0;
	}
	return 1;
}
static inline int convert_NSPoint(PyObject* object, void* pvar)
{
	int err;

	err = ObjC_PythonToObjC(@encode(NSPoint), object, pvar);
	if (err == -1) {
		return 0;
	}
	return 1;
}
/*
 * This is a generated file.
 */

typedef void* PYOBJC_VOIDPTR;

static inline int convert_BOOL(PyObject* object, void* pvar)
{
    BOOL* pbool = (BOOL*)pvar;

    if (PyObject_IsTrue(object)) {
        *pbool = YES;
    } else {
        *pbool = NO;
    }

    return 1;
}


static inline int convert_char(PyObject* object, void* pvar)
{
	char* pchar = (char*)pvar;

	if (!PyString_Check(object)) {
		PyErr_SetString(PyExc_TypeError, "Expecting string of len 1");
		return 0;
	}

	if (PyString_Size(object) != 1) {
		PyErr_SetString(PyExc_TypeError, "Expecting string of len 1");
		return 0;
	}

	*pchar = *PyString_AsString(object);
	return 1;
}

static inline int convert_id(PyObject* object, void* pvar)
{
	id* pid = (id*)pvar;

	*pid = ObjC_PythonToId(object);

        if (PyErr_Occurred()) {
            return 0;
        } 
        return 1;
}

static inline int convert_SEL(PyObject* object, void* pvar)
{
	if (!PyString_Check(object)) {
		PyErr_SetString(PyExc_TypeError, "Excpected string");
		return 0;
	}

	*(SEL*)pvar = SELUID(PyString_AsString(object));
	return 1;
}

static inline int convert_Class(PyObject* object, void* pvar)
{
	if (!PyObjCClass_Check(object)) {
		PyErr_SetString(PyExc_TypeError, "Excpected objective-C class");
		return 0;
	}

	*(Class*)pvar = PyObjCClass_GetClass(object);
	if (*(Class*)pvar == NULL) return 0;
	return 1;
}

/* void NSUpdateDynamicServices(void); */
PyObject* objc_NSUpdateDynamicServices(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSUpdateDynamicServices", keywords) < 0) return NULL;
	NS_DURING
		NSUpdateDynamicServices(
);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* BOOL NSPlanarFromDepth (NSWindowDepth depth); */
PyObject* objc_NSPlanarFromDepth(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "depth", NULL };
	PyObject* result;
	BOOL objc_result;
	NSWindowDepth objc_depth;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "i:NSPlanarFromDepth", keywords, &objc_depth) < 0) return NULL;
	NS_DURING
		objc_result = NSPlanarFromDepth(
objc_depth);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* int NSBitsPerSampleFromDepth (NSWindowDepth depth); */
PyObject* objc_NSBitsPerSampleFromDepth(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "depth", NULL };
	PyObject* result;
	int objc_result;
	NSWindowDepth objc_depth;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "i:NSBitsPerSampleFromDepth", keywords, &objc_depth) < 0) return NULL;
	NS_DURING
		objc_result = NSBitsPerSampleFromDepth(
objc_depth);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* int NSBitsPerPixelFromDepth (NSWindowDepth depth); */
PyObject* objc_NSBitsPerPixelFromDepth(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "depth", NULL };
	PyObject* result;
	int objc_result;
	NSWindowDepth objc_depth;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "i:NSBitsPerPixelFromDepth", keywords, &objc_depth) < 0) return NULL;
	NS_DURING
		objc_result = NSBitsPerPixelFromDepth(
objc_depth);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* void NSRectFill(NSRect aRect); */
PyObject* objc_NSRectFill(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", NULL };
	PyObject* result;
	NSRect objc_aRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSRectFill", keywords, convert_NSRect, &objc_aRect) < 0) return NULL;
	NS_DURING
		NSRectFill(
objc_aRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSRectFillUsingOperation(NSRect aRect, NSCompositingOperation op); */
PyObject* objc_NSRectFillUsingOperation(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "op", NULL };
	PyObject* result;
	NSRect objc_aRect;
	NSCompositingOperation objc_op;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&i:NSRectFillUsingOperation", keywords, convert_NSRect, &objc_aRect, &objc_op) < 0) return NULL;
	NS_DURING
		NSRectFillUsingOperation(
objc_aRect, objc_op);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSFrameRect(NSRect aRect); */
PyObject* objc_NSFrameRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", NULL };
	PyObject* result;
	NSRect objc_aRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSFrameRect", keywords, convert_NSRect, &objc_aRect) < 0) return NULL;
	NS_DURING
		NSFrameRect(
objc_aRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSFrameRectWithWidth(NSRect aRect, float frameWidth); */
PyObject* objc_NSFrameRectWithWidth(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "frameWidth", NULL };
	PyObject* result;
	NSRect objc_aRect;
	float objc_frameWidth;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&f:NSFrameRectWithWidth", keywords, convert_NSRect, &objc_aRect, &objc_frameWidth) < 0) return NULL;
	NS_DURING
		NSFrameRectWithWidth(
objc_aRect, objc_frameWidth);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSFrameRectWithWidthUsingOperation(NSRect aRect, float frameWidth, NSCompositingOperation op); */
PyObject* objc_NSFrameRectWithWidthUsingOperation(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "frameWidth", "op", NULL };
	PyObject* result;
	NSRect objc_aRect;
	float objc_frameWidth;
	NSCompositingOperation objc_op;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&fi:NSFrameRectWithWidthUsingOperation", keywords, convert_NSRect, &objc_aRect, &objc_frameWidth, &objc_op) < 0) return NULL;
	NS_DURING
		NSFrameRectWithWidthUsingOperation(
objc_aRect, objc_frameWidth, objc_op);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSRectClip(NSRect aRect); */
PyObject* objc_NSRectClip(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", NULL };
	PyObject* result;
	NSRect objc_aRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSRectClip", keywords, convert_NSRect, &objc_aRect) < 0) return NULL;
	NS_DURING
		NSRectClip(
objc_aRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSDrawGrayBezel(NSRect aRect, NSRect clipRect); */
PyObject* objc_NSDrawGrayBezel(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "clipRect", NULL };
	PyObject* result;
	NSRect objc_aRect;
	NSRect objc_clipRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSDrawGrayBezel", keywords, convert_NSRect, &objc_aRect, convert_NSRect, &objc_clipRect) < 0) return NULL;
	NS_DURING
		NSDrawGrayBezel(
objc_aRect, objc_clipRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSDrawGroove(NSRect aRect, NSRect clipRect); */
PyObject* objc_NSDrawGroove(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "clipRect", NULL };
	PyObject* result;
	NSRect objc_aRect;
	NSRect objc_clipRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSDrawGroove", keywords, convert_NSRect, &objc_aRect, convert_NSRect, &objc_clipRect) < 0) return NULL;
	NS_DURING
		NSDrawGroove(
objc_aRect, objc_clipRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSDrawWhiteBezel(NSRect aRect, NSRect clipRect); */
PyObject* objc_NSDrawWhiteBezel(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "clipRect", NULL };
	PyObject* result;
	NSRect objc_aRect;
	NSRect objc_clipRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSDrawWhiteBezel", keywords, convert_NSRect, &objc_aRect, convert_NSRect, &objc_clipRect) < 0) return NULL;
	NS_DURING
		NSDrawWhiteBezel(
objc_aRect, objc_clipRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSDrawButton(NSRect aRect, NSRect clipRect); */
PyObject* objc_NSDrawButton(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "clipRect", NULL };
	PyObject* result;
	NSRect objc_aRect;
	NSRect objc_clipRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSDrawButton", keywords, convert_NSRect, &objc_aRect, convert_NSRect, &objc_clipRect) < 0) return NULL;
	NS_DURING
		NSDrawButton(
objc_aRect, objc_clipRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSEraseRect(NSRect aRect); */
PyObject* objc_NSEraseRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", NULL };
	PyObject* result;
	NSRect objc_aRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSEraseRect", keywords, convert_NSRect, &objc_aRect) < 0) return NULL;
	NS_DURING
		NSEraseRect(
objc_aRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}

#if 0 /* This doesn't link ??? */
/* void NSCopyBitmapFromGState(int srcGState, NSRect srcRect, NSRect destRect); */
PyObject* objc_NSCopyBitmapFromGState(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "srcGState", "srcRect", "destRect", NULL };
	PyObject* result;
	int objc_srcGState;
	NSRect objc_srcRect;
	NSRect objc_destRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "iO&O&:NSCopyBitmapFromGState", keywords, &objc_srcGState, convert_NSRect, &objc_srcRect, convert_NSRect, &objc_destRect) < 0) return NULL;
	NS_DURING
		NSCopyBitmapFromGState(
objc_srcGState, objc_srcRect, objc_destRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
#endif
/* void NSCopyBits(int srcGState, NSRect srcRect, NSPoint destPoint); */
PyObject* objc_NSCopyBits(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "srcGState", "srcRect", "destPoint", NULL };
	PyObject* result;
	int objc_srcGState;
	NSRect objc_srcRect;
	NSPoint objc_destPoint;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "iO&O&:NSCopyBits", keywords, &objc_srcGState, convert_NSRect, &objc_srcRect, convert_NSPoint, &objc_destPoint) < 0) return NULL;
	NS_DURING
		NSCopyBits(
objc_srcGState, objc_srcRect, objc_destPoint);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSHighlightRect(NSRect aRect); */
PyObject* objc_NSHighlightRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", NULL };
	PyObject* result;
	NSRect objc_aRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSHighlightRect", keywords, convert_NSRect, &objc_aRect) < 0) return NULL;
	NS_DURING
		NSHighlightRect(
objc_aRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSBeep(void); */
PyObject* objc_NSBeep(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSBeep", keywords) < 0) return NULL;
	NS_DURING
		NSBeep(
);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSDrawDarkBezel(NSRect aRect, NSRect clipRect); */
PyObject* objc_NSDrawDarkBezel(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "clipRect", NULL };
	PyObject* result;
	NSRect objc_aRect;
	NSRect objc_clipRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSDrawDarkBezel", keywords, convert_NSRect, &objc_aRect, convert_NSRect, &objc_clipRect) < 0) return NULL;
	NS_DURING
		NSDrawDarkBezel(
objc_aRect, objc_clipRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSDrawLightBezel(NSRect aRect, NSRect clipRect); */
PyObject* objc_NSDrawLightBezel(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "clipRect", NULL };
	PyObject* result;
	NSRect objc_aRect;
	NSRect objc_clipRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSDrawLightBezel", keywords, convert_NSRect, &objc_aRect, convert_NSRect, &objc_clipRect) < 0) return NULL;
	NS_DURING
		NSDrawLightBezel(
objc_aRect, objc_clipRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSDottedFrameRect(NSRect aRect); */
PyObject* objc_NSDottedFrameRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", NULL };
	PyObject* result;
	NSRect objc_aRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSDottedFrameRect", keywords, convert_NSRect, &objc_aRect) < 0) return NULL;
	NS_DURING
		NSDottedFrameRect(
objc_aRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSDrawWindowBackground(NSRect aRect); */
PyObject* objc_NSDrawWindowBackground(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", NULL };
	PyObject* result;
	NSRect objc_aRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSDrawWindowBackground", keywords, convert_NSRect, &objc_aRect) < 0) return NULL;
	NS_DURING
		NSDrawWindowBackground(
objc_aRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSSetFocusRingStyle(NSFocusRingPlacement placement); */
PyObject* objc_NSSetFocusRingStyle(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "placement", NULL };
	PyObject* result;
	NSFocusRingPlacement objc_placement;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "i:NSSetFocusRingStyle", keywords, &objc_placement) < 0) return NULL;
	NS_DURING
		NSSetFocusRingStyle(
objc_placement);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSReleaseAlertPanel(id panel); */
PyObject* objc_NSReleaseAlertPanel(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "panel", NULL };
	PyObject* result;
	id objc_panel;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSReleaseAlertPanel", keywords, convert_id, &objc_panel) < 0) return NULL;
	NS_DURING
		NSReleaseAlertPanel(
objc_panel);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}

#if 0
	{ "NSCopyBitmapFromGState", (PyCFunction)objc_NSCopyBitmapFromGState, METH_VARARGS|METH_KEYWORDS, "void NSCopyBitmapFromGState(int srcGState, NSRect srcRect, NSRect destRect);" }, 
#endif

#define METHOD_TABLE_ENTRIES \
	{ "NSUpdateDynamicServices", (PyCFunction)objc_NSUpdateDynamicServices, METH_VARARGS|METH_KEYWORDS, "void NSUpdateDynamicServices(void);" }, \
	{ "NSPlanarFromDepth", (PyCFunction)objc_NSPlanarFromDepth, METH_VARARGS|METH_KEYWORDS, "BOOL NSPlanarFromDepth (NSWindowDepth depth);" }, \
	{ "NSBitsPerSampleFromDepth", (PyCFunction)objc_NSBitsPerSampleFromDepth, METH_VARARGS|METH_KEYWORDS, "int NSBitsPerSampleFromDepth (NSWindowDepth depth);" }, \
	{ "NSBitsPerPixelFromDepth", (PyCFunction)objc_NSBitsPerPixelFromDepth, METH_VARARGS|METH_KEYWORDS, "int NSBitsPerPixelFromDepth (NSWindowDepth depth);" }, \
	{ "NSRectFill", (PyCFunction)objc_NSRectFill, METH_VARARGS|METH_KEYWORDS, "void NSRectFill(NSRect aRect);" }, \
	{ "NSRectFillUsingOperation", (PyCFunction)objc_NSRectFillUsingOperation, METH_VARARGS|METH_KEYWORDS, "void NSRectFillUsingOperation(NSRect aRect, NSCompositingOperation op);" }, \
	{ "NSFrameRect", (PyCFunction)objc_NSFrameRect, METH_VARARGS|METH_KEYWORDS, "void NSFrameRect(NSRect aRect);" }, \
	{ "NSFrameRectWithWidth", (PyCFunction)objc_NSFrameRectWithWidth, METH_VARARGS|METH_KEYWORDS, "void NSFrameRectWithWidth(NSRect aRect, float frameWidth);" }, \
	{ "NSFrameRectWithWidthUsingOperation", (PyCFunction)objc_NSFrameRectWithWidthUsingOperation, METH_VARARGS|METH_KEYWORDS, "void NSFrameRectWithWidthUsingOperation(NSRect aRect, float frameWidth, NSCompositingOperation op);" }, \
	{ "NSRectClip", (PyCFunction)objc_NSRectClip, METH_VARARGS|METH_KEYWORDS, "void NSRectClip(NSRect aRect);" }, \
	{ "NSDrawGrayBezel", (PyCFunction)objc_NSDrawGrayBezel, METH_VARARGS|METH_KEYWORDS, "void NSDrawGrayBezel(NSRect aRect, NSRect clipRect);" }, \
	{ "NSDrawGroove", (PyCFunction)objc_NSDrawGroove, METH_VARARGS|METH_KEYWORDS, "void NSDrawGroove(NSRect aRect, NSRect clipRect);" }, \
	{ "NSDrawWhiteBezel", (PyCFunction)objc_NSDrawWhiteBezel, METH_VARARGS|METH_KEYWORDS, "void NSDrawWhiteBezel(NSRect aRect, NSRect clipRect);" }, \
	{ "NSDrawButton", (PyCFunction)objc_NSDrawButton, METH_VARARGS|METH_KEYWORDS, "void NSDrawButton(NSRect aRect, NSRect clipRect);" }, \
	{ "NSEraseRect", (PyCFunction)objc_NSEraseRect, METH_VARARGS|METH_KEYWORDS, "void NSEraseRect(NSRect aRect);" }, \
	{ "NSCopyBits", (PyCFunction)objc_NSCopyBits, METH_VARARGS|METH_KEYWORDS, "void NSCopyBits(int srcGState, NSRect srcRect, NSPoint destPoint);" }, \
	{ "NSHighlightRect", (PyCFunction)objc_NSHighlightRect, METH_VARARGS|METH_KEYWORDS, "void NSHighlightRect(NSRect aRect);" }, \
	{ "NSBeep", (PyCFunction)objc_NSBeep, METH_VARARGS|METH_KEYWORDS, "void NSBeep(void);" }, \
	{ "NSDrawDarkBezel", (PyCFunction)objc_NSDrawDarkBezel, METH_VARARGS|METH_KEYWORDS, "void NSDrawDarkBezel(NSRect aRect, NSRect clipRect);" }, \
	{ "NSDrawLightBezel", (PyCFunction)objc_NSDrawLightBezel, METH_VARARGS|METH_KEYWORDS, "void NSDrawLightBezel(NSRect aRect, NSRect clipRect);" }, \
	{ "NSDottedFrameRect", (PyCFunction)objc_NSDottedFrameRect, METH_VARARGS|METH_KEYWORDS, "void NSDottedFrameRect(NSRect aRect);" }, \
	{ "NSDrawWindowBackground", (PyCFunction)objc_NSDrawWindowBackground, METH_VARARGS|METH_KEYWORDS, "void NSDrawWindowBackground(NSRect aRect);" }, \
	{ "NSSetFocusRingStyle", (PyCFunction)objc_NSSetFocusRingStyle, METH_VARARGS|METH_KEYWORDS, "void NSSetFocusRingStyle(NSFocusRingPlacement placement);" }, \
	{ "NSReleaseAlertPanel", (PyCFunction)objc_NSReleaseAlertPanel, METH_VARARGS|METH_KEYWORDS, "void NSReleaseAlertPanel(id panel);" }, \
	/* END */
