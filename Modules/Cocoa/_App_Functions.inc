static inline int convert_NSAffineTransformStruct(PyObject* object, void* pvar)
{
	const char* errstr;

	errstr = ObjC_PythonToObjC(@encode(NSAffineTransformStruct), object, pvar);
	if (errstr) {
		PyErr_SetString(PyExc_TypeError, errstr);
		return 0;
	}
	return 1;
}
static inline int convert_NSRect(PyObject* object, void* pvar)
{
	const char* errstr;

	errstr = ObjC_PythonToObjC(@encode(NSRect), object, pvar);
	if (errstr) {
		PyErr_SetString(PyExc_TypeError, errstr);
		return 0;
	}
	return 1;
}
static inline int convert_NSPoint(PyObject* object, void* pvar)
{
	const char* errstr;

	errstr = ObjC_PythonToObjC(@encode(NSPoint), object, pvar);
	if (errstr) {
		PyErr_SetString(PyExc_TypeError, errstr);
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

	return (*pid != nil);
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
	if (!ObjCClass_Check(object)) {
		PyErr_SetString(PyExc_TypeError, "Excpected objective-C class");
		return 0;
	}

	*(Class*)pvar = ObjCClass_GetClass(object);
	if (*(Class*)pvar == NULL) return 0;
	return 1;
}

/* id NSAccessibilityUnignoredAncestor(id element); */
PyObject* objc_NSAccessibilityUnignoredAncestor(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "element", NULL };
	PyObject* result;
	id objc_result;
	id objc_element;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSAccessibilityUnignoredAncestor", keywords, convert_id, &objc_element) < 0) return NULL;
	NS_DURING
		objc_result = NSAccessibilityUnignoredAncestor(
objc_element);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* id NSAccessibilityUnignoredDescendant(id element); */
PyObject* objc_NSAccessibilityUnignoredDescendant(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "element", NULL };
	PyObject* result;
	id objc_result;
	id objc_element;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSAccessibilityUnignoredDescendant", keywords, convert_id, &objc_element) < 0) return NULL;
	NS_DURING
		objc_result = NSAccessibilityUnignoredDescendant(
objc_element);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSArray *NSAccessibilityUnignoredChildren(NSArray *originalChildren); */
PyObject* objc_NSAccessibilityUnignoredChildren(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "originalChildren", NULL };
	PyObject* result;
	NSArray* objc_result;
	id objc_originalChildren;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSAccessibilityUnignoredChildren", keywords, convert_id, &objc_originalChildren) < 0) return NULL;
	NS_DURING
		objc_result = NSAccessibilityUnignoredChildren(
objc_originalChildren);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSArray *NSAccessibilityUnignoredChildrenForOnlyChild(id originalChild); */
PyObject* objc_NSAccessibilityUnignoredChildrenForOnlyChild(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "originalChild", NULL };
	PyObject* result;
	NSArray* objc_result;
	id objc_originalChild;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSAccessibilityUnignoredChildrenForOnlyChild", keywords, convert_id, &objc_originalChild) < 0) return NULL;
	NS_DURING
		objc_result = NSAccessibilityUnignoredChildrenForOnlyChild(
objc_originalChild);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* void NSAccessibilityPostNotification(id element, NSString *notification); */
PyObject* objc_NSAccessibilityPostNotification(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "element", "notification", NULL };
	PyObject* result;
	id objc_element;
	id objc_notification;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSAccessibilityPostNotification", keywords, convert_id, &objc_element, convert_id, &objc_notification) < 0) return NULL;
	NS_DURING
		NSAccessibilityPostNotification(
objc_element, objc_notification);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* BOOL NSApplicationLoad(void); */
PyObject* objc_NSApplicationLoad(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	BOOL objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSApplicationLoad", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSApplicationLoad(
);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSShowsServicesMenuItem(NSString * itemName); */
PyObject* objc_NSShowsServicesMenuItem(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "itemName", NULL };
	PyObject* result;
	BOOL objc_result;
	id objc_itemName;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSShowsServicesMenuItem", keywords, convert_id, &objc_itemName) < 0) return NULL;
	NS_DURING
		objc_result = NSShowsServicesMenuItem(
objc_itemName);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* int NSSetShowsServicesMenuItem(NSString * itemName, BOOL enabled); */
PyObject* objc_NSSetShowsServicesMenuItem(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "itemName", "enabled", NULL };
	PyObject* result;
	int objc_result;
	id objc_itemName;
	BOOL objc_enabled;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSSetShowsServicesMenuItem", keywords, convert_id, &objc_itemName, convert_BOOL, &objc_enabled) < 0) return NULL;
	NS_DURING
		objc_result = NSSetShowsServicesMenuItem(
objc_itemName, objc_enabled);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
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
/* BOOL NSPerformService(NSString *itemName, NSPasteboard *pboard); */
PyObject* objc_NSPerformService(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "itemName", "pboard", NULL };
	PyObject* result;
	BOOL objc_result;
	id objc_itemName;
	id objc_pboard;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSPerformService", keywords, convert_id, &objc_itemName, convert_id, &objc_pboard) < 0) return NULL;
	NS_DURING
		objc_result = NSPerformService(
objc_itemName, objc_pboard);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* void NSRegisterServicesProvider(id provider, NSString *name); */
PyObject* objc_NSRegisterServicesProvider(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "provider", "name", NULL };
	PyObject* result;
	id objc_provider;
	id objc_name;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSRegisterServicesProvider", keywords, convert_id, &objc_provider, convert_id, &objc_name) < 0) return NULL;
	NS_DURING
		NSRegisterServicesProvider(
objc_provider, objc_name);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSUnregisterServicesProvider(NSString *name); */
PyObject* objc_NSUnregisterServicesProvider(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "name", NULL };
	PyObject* result;
	id objc_name;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSUnregisterServicesProvider", keywords, convert_id, &objc_name) < 0) return NULL;
	NS_DURING
		NSUnregisterServicesProvider(
objc_name);
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
		result = PyBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* NSString *NSColorSpaceFromDepth (NSWindowDepth depth); */
PyObject* objc_NSColorSpaceFromDepth(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "depth", NULL };
	PyObject* result;
	NSString* objc_result;
	NSWindowDepth objc_depth;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "i:NSColorSpaceFromDepth", keywords, &objc_depth) < 0) return NULL;
	NS_DURING
		objc_result = NSColorSpaceFromDepth(
objc_depth);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_IdToPython(objc_result); if (result == NULL) return NULL;
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
/* int NSNumberOfColorComponents (NSString *colorSpaceName); */
PyObject* objc_NSNumberOfColorComponents(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "colorSpaceName", NULL };
	PyObject* result;
	int objc_result;
	id objc_colorSpaceName;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSNumberOfColorComponents", keywords, convert_id, &objc_colorSpaceName) < 0) return NULL;
	NS_DURING
		objc_result = NSNumberOfColorComponents(
objc_colorSpaceName);
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
/* NSColor *NSReadPixel(NSPoint passedPoint); */
PyObject* objc_NSReadPixel(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "passedPoint", NULL };
	PyObject* result;
	NSColor* objc_result;
	NSPoint objc_passedPoint;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSReadPixel", keywords, convert_NSPoint, &objc_passedPoint) < 0) return NULL;
	NS_DURING
		objc_result = NSReadPixel(
objc_passedPoint);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
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
/* NSInterfaceStyle NSInterfaceStyleForKey(NSString *key, NSResponder *responder); */
PyObject* objc_NSInterfaceStyleForKey(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "key", "responder", NULL };
	PyObject* result;
	NSInterfaceStyle objc_result;
	id objc_key;
	id objc_responder;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSInterfaceStyleForKey", keywords, convert_id, &objc_key, convert_id, &objc_responder) < 0) return NULL;
	NS_DURING
		objc_result = NSInterfaceStyleForKey(
objc_key, objc_responder);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* int NSRunAlertPanel(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...); */
PyObject* objc_NSRunAlertPanel(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "title", "msg", "defaultButton", "alternateButton", "otherButton", NULL };
	PyObject* result;
	int objc_result;
	id objc_title;
	id objc_msg;
	id objc_defaultButton;
	id objc_alternateButton;
	id objc_otherButton;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&O&O&O&:NSRunAlertPanel", keywords, convert_id, &objc_title, convert_id, &objc_msg, convert_id, &objc_defaultButton, convert_id, &objc_alternateButton, convert_id, &objc_otherButton) < 0) return NULL;
	NS_DURING
		objc_result = NSRunAlertPanel(
objc_title, objc_msg, objc_defaultButton, objc_alternateButton, objc_otherButton);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* int NSRunInformationalAlertPanel(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...); */
PyObject* objc_NSRunInformationalAlertPanel(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "title", "msg", "defaultButton", "alternateButton", "otherButton", NULL };
	PyObject* result;
	int objc_result;
	id objc_title;
	id objc_msg;
	id objc_defaultButton;
	id objc_alternateButton;
	id objc_otherButton;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&O&O&O&:NSRunInformationalAlertPanel", keywords, convert_id, &objc_title, convert_id, &objc_msg, convert_id, &objc_defaultButton, convert_id, &objc_alternateButton, convert_id, &objc_otherButton) < 0) return NULL;
	NS_DURING
		objc_result = NSRunInformationalAlertPanel(
objc_title, objc_msg, objc_defaultButton, objc_alternateButton, objc_otherButton);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* int NSRunCriticalAlertPanel(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...); */
PyObject* objc_NSRunCriticalAlertPanel(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "title", "msg", "defaultButton", "alternateButton", "otherButton", NULL };
	PyObject* result;
	int objc_result;
	id objc_title;
	id objc_msg;
	id objc_defaultButton;
	id objc_alternateButton;
	id objc_otherButton;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&O&O&O&:NSRunCriticalAlertPanel", keywords, convert_id, &objc_title, convert_id, &objc_msg, convert_id, &objc_defaultButton, convert_id, &objc_alternateButton, convert_id, &objc_otherButton) < 0) return NULL;
	NS_DURING
		objc_result = NSRunCriticalAlertPanel(
objc_title, objc_msg, objc_defaultButton, objc_alternateButton, objc_otherButton);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* int NSRunAlertPanelRelativeToWindow(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, ...); */
PyObject* objc_NSRunAlertPanelRelativeToWindow(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "title", "msg", "defaultButton", "alternateButton", "otherButton", "docWindow", NULL };
	PyObject* result;
	int objc_result;
	id objc_title;
	id objc_msg;
	id objc_defaultButton;
	id objc_alternateButton;
	id objc_otherButton;
	id objc_docWindow;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&O&O&O&O&:NSRunAlertPanelRelativeToWindow", keywords, convert_id, &objc_title, convert_id, &objc_msg, convert_id, &objc_defaultButton, convert_id, &objc_alternateButton, convert_id, &objc_otherButton, convert_id, &objc_docWindow) < 0) return NULL;
	NS_DURING
		objc_result = NSRunAlertPanelRelativeToWindow(
objc_title, objc_msg, objc_defaultButton, objc_alternateButton, objc_otherButton, objc_docWindow);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* int NSRunInformationalAlertPanelRelativeToWindow(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, ...); */
PyObject* objc_NSRunInformationalAlertPanelRelativeToWindow(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "title", "msg", "defaultButton", "alternateButton", "otherButton", "docWindow", NULL };
	PyObject* result;
	int objc_result;
	id objc_title;
	id objc_msg;
	id objc_defaultButton;
	id objc_alternateButton;
	id objc_otherButton;
	id objc_docWindow;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&O&O&O&O&:NSRunInformationalAlertPanelRelativeToWindow", keywords, convert_id, &objc_title, convert_id, &objc_msg, convert_id, &objc_defaultButton, convert_id, &objc_alternateButton, convert_id, &objc_otherButton, convert_id, &objc_docWindow) < 0) return NULL;
	NS_DURING
		objc_result = NSRunInformationalAlertPanelRelativeToWindow(
objc_title, objc_msg, objc_defaultButton, objc_alternateButton, objc_otherButton, objc_docWindow);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* int NSRunCriticalAlertPanelRelativeToWindow(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, ...); */
PyObject* objc_NSRunCriticalAlertPanelRelativeToWindow(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "title", "msg", "defaultButton", "alternateButton", "otherButton", "docWindow", NULL };
	PyObject* result;
	int objc_result;
	id objc_title;
	id objc_msg;
	id objc_defaultButton;
	id objc_alternateButton;
	id objc_otherButton;
	id objc_docWindow;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&O&O&O&O&:NSRunCriticalAlertPanelRelativeToWindow", keywords, convert_id, &objc_title, convert_id, &objc_msg, convert_id, &objc_defaultButton, convert_id, &objc_alternateButton, convert_id, &objc_otherButton, convert_id, &objc_docWindow) < 0) return NULL;
	NS_DURING
		objc_result = NSRunCriticalAlertPanelRelativeToWindow(
objc_title, objc_msg, objc_defaultButton, objc_alternateButton, objc_otherButton, objc_docWindow);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* void NSBeginAlertSheet(NSString *title, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, id modalDelegate, SEL didEndSelector, SEL didDismissSelector, void *contextInfo, NSString *msg, ...); */
PyObject* objc_NSBeginAlertSheet(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "title", "defaultButton", "alternateButton", "otherButton", "docWindow", "modalDelegate", "didEndSelector", "didDismissSelector", "contextInfo", "msg", NULL };
	PyObject* result;
	id objc_title;
	id objc_defaultButton;
	id objc_alternateButton;
	id objc_otherButton;
	id objc_docWindow;
	id objc_modalDelegate;
	SEL objc_didEndSelector;
	SEL objc_didDismissSelector;
	PYOBJC_VOIDPTR objc_contextInfo;
	id objc_msg;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&O&O&O&O&O&O&iO&:NSBeginAlertSheet", keywords, convert_id, &objc_title, convert_id, &objc_defaultButton, convert_id, &objc_alternateButton, convert_id, &objc_otherButton, convert_id, &objc_docWindow, convert_id, &objc_modalDelegate, convert_SEL, &objc_didEndSelector, convert_SEL, &objc_didDismissSelector, &objc_contextInfo, convert_id, &objc_msg) < 0) return NULL;
	NS_DURING
		NSBeginAlertSheet(
objc_title, objc_defaultButton, objc_alternateButton, objc_otherButton, objc_docWindow, objc_modalDelegate, objc_didEndSelector, objc_didDismissSelector, objc_contextInfo, objc_msg);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSBeginInformationalAlertSheet(NSString *title, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, id modalDelegate, SEL didEndSelector, SEL didDismissSelector, void *contextInfo, NSString *msg, ...); */
PyObject* objc_NSBeginInformationalAlertSheet(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "title", "defaultButton", "alternateButton", "otherButton", "docWindow", "modalDelegate", "didEndSelector", "didDismissSelector", "contextInfo", "msg", NULL };
	PyObject* result;
	id objc_title;
	id objc_defaultButton;
	id objc_alternateButton;
	id objc_otherButton;
	id objc_docWindow;
	id objc_modalDelegate;
	SEL objc_didEndSelector;
	SEL objc_didDismissSelector;
	PYOBJC_VOIDPTR objc_contextInfo;
	id objc_msg;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&O&O&O&O&O&O&iO&:NSBeginInformationalAlertSheet", keywords, convert_id, &objc_title, convert_id, &objc_defaultButton, convert_id, &objc_alternateButton, convert_id, &objc_otherButton, convert_id, &objc_docWindow, convert_id, &objc_modalDelegate, convert_SEL, &objc_didEndSelector, convert_SEL, &objc_didDismissSelector, &objc_contextInfo, convert_id, &objc_msg) < 0) return NULL;
	NS_DURING
		NSBeginInformationalAlertSheet(
objc_title, objc_defaultButton, objc_alternateButton, objc_otherButton, objc_docWindow, objc_modalDelegate, objc_didEndSelector, objc_didDismissSelector, objc_contextInfo, objc_msg);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSBeginCriticalAlertSheet(NSString *title, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, id modalDelegate, SEL didEndSelector, SEL didDismissSelector, void *contextInfo, NSString *msg, ...); */
PyObject* objc_NSBeginCriticalAlertSheet(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "title", "defaultButton", "alternateButton", "otherButton", "docWindow", "modalDelegate", "didEndSelector", "didDismissSelector", "contextInfo", "msg", NULL };
	PyObject* result;
	id objc_title;
	id objc_defaultButton;
	id objc_alternateButton;
	id objc_otherButton;
	id objc_docWindow;
	id objc_modalDelegate;
	SEL objc_didEndSelector;
	SEL objc_didDismissSelector;
	PYOBJC_VOIDPTR objc_contextInfo;
	id objc_msg;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&O&O&O&O&O&O&iO&:NSBeginCriticalAlertSheet", keywords, convert_id, &objc_title, convert_id, &objc_defaultButton, convert_id, &objc_alternateButton, convert_id, &objc_otherButton, convert_id, &objc_docWindow, convert_id, &objc_modalDelegate, convert_SEL, &objc_didEndSelector, convert_SEL, &objc_didDismissSelector, &objc_contextInfo, convert_id, &objc_msg) < 0) return NULL;
	NS_DURING
		NSBeginCriticalAlertSheet(
objc_title, objc_defaultButton, objc_alternateButton, objc_otherButton, objc_docWindow, objc_modalDelegate, objc_didEndSelector, objc_didDismissSelector, objc_contextInfo, objc_msg);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* id NSGetAlertPanel(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...); */
PyObject* objc_NSGetAlertPanel(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "title", "msg", "defaultButton", "alternateButton", "otherButton", NULL };
	PyObject* result;
	id objc_result;
	id objc_title;
	id objc_msg;
	id objc_defaultButton;
	id objc_alternateButton;
	id objc_otherButton;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&O&O&O&:NSGetAlertPanel", keywords, convert_id, &objc_title, convert_id, &objc_msg, convert_id, &objc_defaultButton, convert_id, &objc_alternateButton, convert_id, &objc_otherButton) < 0) return NULL;
	NS_DURING
		objc_result = NSGetAlertPanel(
objc_title, objc_msg, objc_defaultButton, objc_alternateButton, objc_otherButton);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* id NSGetInformationalAlertPanel(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...); */
PyObject* objc_NSGetInformationalAlertPanel(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "title", "msg", "defaultButton", "alternateButton", "otherButton", NULL };
	PyObject* result;
	id objc_result;
	id objc_title;
	id objc_msg;
	id objc_defaultButton;
	id objc_alternateButton;
	id objc_otherButton;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&O&O&O&:NSGetInformationalAlertPanel", keywords, convert_id, &objc_title, convert_id, &objc_msg, convert_id, &objc_defaultButton, convert_id, &objc_alternateButton, convert_id, &objc_otherButton) < 0) return NULL;
	NS_DURING
		objc_result = NSGetInformationalAlertPanel(
objc_title, objc_msg, objc_defaultButton, objc_alternateButton, objc_otherButton);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* id NSGetCriticalAlertPanel(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...); */
PyObject* objc_NSGetCriticalAlertPanel(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "title", "msg", "defaultButton", "alternateButton", "otherButton", NULL };
	PyObject* result;
	id objc_result;
	id objc_title;
	id objc_msg;
	id objc_defaultButton;
	id objc_alternateButton;
	id objc_otherButton;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&O&O&O&:NSGetCriticalAlertPanel", keywords, convert_id, &objc_title, convert_id, &objc_msg, convert_id, &objc_defaultButton, convert_id, &objc_alternateButton, convert_id, &objc_otherButton) < 0) return NULL;
	NS_DURING
		objc_result = NSGetCriticalAlertPanel(
objc_title, objc_msg, objc_defaultButton, objc_alternateButton, objc_otherButton);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_IdToPython(objc_result); if (result == NULL) return NULL;
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
/* NSString *NSCreateFilenamePboardType(NSString *fileType); */
PyObject* objc_NSCreateFilenamePboardType(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "fileType", NULL };
	PyObject* result;
	NSString* objc_result;
	id objc_fileType;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSCreateFilenamePboardType", keywords, convert_id, &objc_fileType) < 0) return NULL;
	NS_DURING
		objc_result = NSCreateFilenamePboardType(
objc_fileType);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSString *NSCreateFileContentsPboardType(NSString *fileType); */
PyObject* objc_NSCreateFileContentsPboardType(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "fileType", NULL };
	PyObject* result;
	NSString* objc_result;
	id objc_fileType;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSCreateFileContentsPboardType", keywords, convert_id, &objc_fileType) < 0) return NULL;
	NS_DURING
		objc_result = NSCreateFileContentsPboardType(
objc_fileType);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSString *NSGetFileType(NSString *pboardType); */
PyObject* objc_NSGetFileType(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "pboardType", NULL };
	PyObject* result;
	NSString* objc_result;
	id objc_pboardType;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSGetFileType", keywords, convert_id, &objc_pboardType) < 0) return NULL;
	NS_DURING
		objc_result = NSGetFileType(
objc_pboardType);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSArray *NSGetFileTypes(NSArray *pboardTypes); */
PyObject* objc_NSGetFileTypes(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "pboardTypes", NULL };
	PyObject* result;
	NSArray* objc_result;
	id objc_pboardTypes;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSGetFileTypes", keywords, convert_id, &objc_pboardTypes) < 0) return NULL;
	NS_DURING
		objc_result = NSGetFileTypes(
objc_pboardTypes);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}

#define METHOD_TABLE_ENTRIES \
	{ "NSAccessibilityUnignoredAncestor", (PyCFunction)objc_NSAccessibilityUnignoredAncestor, METH_VARARGS|METH_KEYWORDS, "id NSAccessibilityUnignoredAncestor(id element);" }, \
	{ "NSAccessibilityUnignoredDescendant", (PyCFunction)objc_NSAccessibilityUnignoredDescendant, METH_VARARGS|METH_KEYWORDS, "id NSAccessibilityUnignoredDescendant(id element);" }, \
	{ "NSAccessibilityUnignoredChildren", (PyCFunction)objc_NSAccessibilityUnignoredChildren, METH_VARARGS|METH_KEYWORDS, "NSArray *NSAccessibilityUnignoredChildren(NSArray *originalChildren);" }, \
	{ "NSAccessibilityUnignoredChildrenForOnlyChild", (PyCFunction)objc_NSAccessibilityUnignoredChildrenForOnlyChild, METH_VARARGS|METH_KEYWORDS, "NSArray *NSAccessibilityUnignoredChildrenForOnlyChild(id originalChild);" }, \
	{ "NSAccessibilityPostNotification", (PyCFunction)objc_NSAccessibilityPostNotification, METH_VARARGS|METH_KEYWORDS, "void NSAccessibilityPostNotification(id element, NSString *notification);" }, \
	{ "NSApplicationLoad", (PyCFunction)objc_NSApplicationLoad, METH_VARARGS|METH_KEYWORDS, "BOOL NSApplicationLoad(void);" }, \
	{ "NSShowsServicesMenuItem", (PyCFunction)objc_NSShowsServicesMenuItem, METH_VARARGS|METH_KEYWORDS, "BOOL NSShowsServicesMenuItem(NSString * itemName);" }, \
	{ "NSSetShowsServicesMenuItem", (PyCFunction)objc_NSSetShowsServicesMenuItem, METH_VARARGS|METH_KEYWORDS, "int NSSetShowsServicesMenuItem(NSString * itemName, BOOL enabled);" }, \
	{ "NSUpdateDynamicServices", (PyCFunction)objc_NSUpdateDynamicServices, METH_VARARGS|METH_KEYWORDS, "void NSUpdateDynamicServices(void);" }, \
	{ "NSPerformService", (PyCFunction)objc_NSPerformService, METH_VARARGS|METH_KEYWORDS, "BOOL NSPerformService(NSString *itemName, NSPasteboard *pboard);" }, \
	{ "NSRegisterServicesProvider", (PyCFunction)objc_NSRegisterServicesProvider, METH_VARARGS|METH_KEYWORDS, "void NSRegisterServicesProvider(id provider, NSString *name);" }, \
	{ "NSUnregisterServicesProvider", (PyCFunction)objc_NSUnregisterServicesProvider, METH_VARARGS|METH_KEYWORDS, "void NSUnregisterServicesProvider(NSString *name);" }, \
	{ "NSPlanarFromDepth", (PyCFunction)objc_NSPlanarFromDepth, METH_VARARGS|METH_KEYWORDS, "BOOL NSPlanarFromDepth (NSWindowDepth depth);" }, \
	{ "NSColorSpaceFromDepth", (PyCFunction)objc_NSColorSpaceFromDepth, METH_VARARGS|METH_KEYWORDS, "NSString *NSColorSpaceFromDepth (NSWindowDepth depth);" }, \
	{ "NSBitsPerSampleFromDepth", (PyCFunction)objc_NSBitsPerSampleFromDepth, METH_VARARGS|METH_KEYWORDS, "int NSBitsPerSampleFromDepth (NSWindowDepth depth);" }, \
	{ "NSBitsPerPixelFromDepth", (PyCFunction)objc_NSBitsPerPixelFromDepth, METH_VARARGS|METH_KEYWORDS, "int NSBitsPerPixelFromDepth (NSWindowDepth depth);" }, \
	{ "NSNumberOfColorComponents", (PyCFunction)objc_NSNumberOfColorComponents, METH_VARARGS|METH_KEYWORDS, "int NSNumberOfColorComponents (NSString *colorSpaceName);" }, \
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
	{ "NSReadPixel", (PyCFunction)objc_NSReadPixel, METH_VARARGS|METH_KEYWORDS, "NSColor *NSReadPixel(NSPoint passedPoint);" }, \
	{ "NSCopyBits", (PyCFunction)objc_NSCopyBits, METH_VARARGS|METH_KEYWORDS, "void NSCopyBits(int srcGState, NSRect srcRect, NSPoint destPoint);" }, \
	{ "NSHighlightRect", (PyCFunction)objc_NSHighlightRect, METH_VARARGS|METH_KEYWORDS, "void NSHighlightRect(NSRect aRect);" }, \
	{ "NSBeep", (PyCFunction)objc_NSBeep, METH_VARARGS|METH_KEYWORDS, "void NSBeep(void);" }, \
	{ "NSDrawDarkBezel", (PyCFunction)objc_NSDrawDarkBezel, METH_VARARGS|METH_KEYWORDS, "void NSDrawDarkBezel(NSRect aRect, NSRect clipRect);" }, \
	{ "NSDrawLightBezel", (PyCFunction)objc_NSDrawLightBezel, METH_VARARGS|METH_KEYWORDS, "void NSDrawLightBezel(NSRect aRect, NSRect clipRect);" }, \
	{ "NSDottedFrameRect", (PyCFunction)objc_NSDottedFrameRect, METH_VARARGS|METH_KEYWORDS, "void NSDottedFrameRect(NSRect aRect);" }, \
	{ "NSDrawWindowBackground", (PyCFunction)objc_NSDrawWindowBackground, METH_VARARGS|METH_KEYWORDS, "void NSDrawWindowBackground(NSRect aRect);" }, \
	{ "NSSetFocusRingStyle", (PyCFunction)objc_NSSetFocusRingStyle, METH_VARARGS|METH_KEYWORDS, "void NSSetFocusRingStyle(NSFocusRingPlacement placement);" }, \
	{ "NSInterfaceStyleForKey", (PyCFunction)objc_NSInterfaceStyleForKey, METH_VARARGS|METH_KEYWORDS, "NSInterfaceStyle NSInterfaceStyleForKey(NSString *key, NSResponder *responder);" }, \
	{ "NSRunAlertPanel", (PyCFunction)objc_NSRunAlertPanel, METH_VARARGS|METH_KEYWORDS, "int NSRunAlertPanel(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...);" }, \
	{ "NSRunInformationalAlertPanel", (PyCFunction)objc_NSRunInformationalAlertPanel, METH_VARARGS|METH_KEYWORDS, "int NSRunInformationalAlertPanel(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...);" }, \
	{ "NSRunCriticalAlertPanel", (PyCFunction)objc_NSRunCriticalAlertPanel, METH_VARARGS|METH_KEYWORDS, "int NSRunCriticalAlertPanel(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...);" }, \
	{ "NSRunAlertPanelRelativeToWindow", (PyCFunction)objc_NSRunAlertPanelRelativeToWindow, METH_VARARGS|METH_KEYWORDS, "int NSRunAlertPanelRelativeToWindow(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, ...);" }, \
	{ "NSRunInformationalAlertPanelRelativeToWindow", (PyCFunction)objc_NSRunInformationalAlertPanelRelativeToWindow, METH_VARARGS|METH_KEYWORDS, "int NSRunInformationalAlertPanelRelativeToWindow(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, ...);" }, \
	{ "NSRunCriticalAlertPanelRelativeToWindow", (PyCFunction)objc_NSRunCriticalAlertPanelRelativeToWindow, METH_VARARGS|METH_KEYWORDS, "int NSRunCriticalAlertPanelRelativeToWindow(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, ...);" }, \
	{ "NSBeginAlertSheet", (PyCFunction)objc_NSBeginAlertSheet, METH_VARARGS|METH_KEYWORDS, "void NSBeginAlertSheet(NSString *title, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, id modalDelegate, SEL didEndSelector, SEL didDismissSelector, void *contextInfo, NSString *msg, ...);" }, \
	{ "NSBeginInformationalAlertSheet", (PyCFunction)objc_NSBeginInformationalAlertSheet, METH_VARARGS|METH_KEYWORDS, "void NSBeginInformationalAlertSheet(NSString *title, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, id modalDelegate, SEL didEndSelector, SEL didDismissSelector, void *contextInfo, NSString *msg, ...);" }, \
	{ "NSBeginCriticalAlertSheet", (PyCFunction)objc_NSBeginCriticalAlertSheet, METH_VARARGS|METH_KEYWORDS, "void NSBeginCriticalAlertSheet(NSString *title, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, id modalDelegate, SEL didEndSelector, SEL didDismissSelector, void *contextInfo, NSString *msg, ...);" }, \
	{ "NSGetAlertPanel", (PyCFunction)objc_NSGetAlertPanel, METH_VARARGS|METH_KEYWORDS, "id NSGetAlertPanel(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...);" }, \
	{ "NSGetInformationalAlertPanel", (PyCFunction)objc_NSGetInformationalAlertPanel, METH_VARARGS|METH_KEYWORDS, "id NSGetInformationalAlertPanel(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...);" }, \
	{ "NSGetCriticalAlertPanel", (PyCFunction)objc_NSGetCriticalAlertPanel, METH_VARARGS|METH_KEYWORDS, "id NSGetCriticalAlertPanel(NSString *title, NSString *msg, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...);" }, \
	{ "NSReleaseAlertPanel", (PyCFunction)objc_NSReleaseAlertPanel, METH_VARARGS|METH_KEYWORDS, "void NSReleaseAlertPanel(id panel);" }, \
	{ "NSCreateFilenamePboardType", (PyCFunction)objc_NSCreateFilenamePboardType, METH_VARARGS|METH_KEYWORDS, "NSString *NSCreateFilenamePboardType(NSString *fileType);" }, \
	{ "NSCreateFileContentsPboardType", (PyCFunction)objc_NSCreateFileContentsPboardType, METH_VARARGS|METH_KEYWORDS, "NSString *NSCreateFileContentsPboardType(NSString *fileType);" }, \
	{ "NSGetFileType", (PyCFunction)objc_NSGetFileType, METH_VARARGS|METH_KEYWORDS, "NSString *NSGetFileType(NSString *pboardType);" }, \
	{ "NSGetFileTypes", (PyCFunction)objc_NSGetFileTypes, METH_VARARGS|METH_KEYWORDS, "NSArray *NSGetFileTypes(NSArray *pboardTypes);" }, \
	/* END */
