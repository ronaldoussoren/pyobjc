static inline int convert_NSPoint(PyObject* object, void* pvar)
{
	int err;

	err = ObjC_PythonToObjC(@encode(NSPoint), object, pvar);
	if (err == -1) {
		return 0;
	}
	return 1;
}
static inline int convert_NSSize(PyObject* object, void* pvar)
{
	int err;

	err = ObjC_PythonToObjC(@encode(NSSize), object, pvar);
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
static inline int convert_NSRange(PyObject* object, void* pvar)
{
	int err;

	err = ObjC_PythonToObjC(@encode(NSRange), object, pvar);
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

/* BOOL NSIsFreedObject(id anObject); */
PyObject* objc_NSIsFreedObject(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "anObject", NULL };
	PyObject* result;
	BOOL objc_result;
	id objc_anObject;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSIsFreedObject", keywords, convert_id, &objc_anObject) < 0) return NULL;
	NS_DURING
		objc_result = NSIsFreedObject(
objc_anObject);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* unsigned NSCountFrames(void); */
PyObject* objc_NSCountFrames(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	unsigned objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSCountFrames", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSCountFrames(
);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSEqualPoints(NSPoint aPoint, NSPoint bPoint); */
PyObject* objc_NSEqualPoints(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aPoint", "bPoint", NULL };
	PyObject* result;
	BOOL objc_result;
	NSPoint objc_aPoint;
	NSPoint objc_bPoint;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSEqualPoints", keywords, convert_NSPoint, &objc_aPoint, convert_NSPoint, &objc_bPoint) < 0) return NULL;
	NS_DURING
		objc_result = NSEqualPoints(
objc_aPoint, objc_bPoint);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSEqualSizes(NSSize aSize, NSSize bSize); */
PyObject* objc_NSEqualSizes(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aSize", "bSize", NULL };
	PyObject* result;
	BOOL objc_result;
	NSSize objc_aSize;
	NSSize objc_bSize;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSEqualSizes", keywords, convert_NSSize, &objc_aSize, convert_NSSize, &objc_bSize) < 0) return NULL;
	NS_DURING
		objc_result = NSEqualSizes(
objc_aSize, objc_bSize);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSEqualRects(NSRect aRect, NSRect bRect); */
PyObject* objc_NSEqualRects(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "bRect", NULL };
	PyObject* result;
	BOOL objc_result;
	NSRect objc_aRect;
	NSRect objc_bRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSEqualRects", keywords, convert_NSRect, &objc_aRect, convert_NSRect, &objc_bRect) < 0) return NULL;
	NS_DURING
		objc_result = NSEqualRects(
objc_aRect, objc_bRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSIsEmptyRect(NSRect aRect); */
PyObject* objc_NSIsEmptyRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", NULL };
	PyObject* result;
	BOOL objc_result;
	NSRect objc_aRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSIsEmptyRect", keywords, convert_NSRect, &objc_aRect) < 0) return NULL;
	NS_DURING
		objc_result = NSIsEmptyRect(
objc_aRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* NSRect NSInsetRect(NSRect aRect, float dX, float dY); */
PyObject* objc_NSInsetRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "dX", "dY", NULL };
	PyObject* result;
	NSRect objc_result;
	NSRect objc_aRect;
	float objc_dX;
	float objc_dY;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&ff:NSInsetRect", keywords, convert_NSRect, &objc_aRect, &objc_dX, &objc_dY) < 0) return NULL;
	NS_DURING
		objc_result = NSInsetRect(
objc_aRect, objc_dX, objc_dY);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_ObjCToPython(@encode(NSRect), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* NSRect NSIntegralRect(NSRect aRect); */
PyObject* objc_NSIntegralRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", NULL };
	PyObject* result;
	NSRect objc_result;
	NSRect objc_aRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSIntegralRect", keywords, convert_NSRect, &objc_aRect) < 0) return NULL;
	NS_DURING
		objc_result = NSIntegralRect(
objc_aRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_ObjCToPython(@encode(NSRect), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* NSRect NSUnionRect(NSRect aRect, NSRect bRect); */
PyObject* objc_NSUnionRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "bRect", NULL };
	PyObject* result;
	NSRect objc_result;
	NSRect objc_aRect;
	NSRect objc_bRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSUnionRect", keywords, convert_NSRect, &objc_aRect, convert_NSRect, &objc_bRect) < 0) return NULL;
	NS_DURING
		objc_result = NSUnionRect(
objc_aRect, objc_bRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_ObjCToPython(@encode(NSRect), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* NSRect NSIntersectionRect(NSRect aRect, NSRect bRect); */
PyObject* objc_NSIntersectionRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "bRect", NULL };
	PyObject* result;
	NSRect objc_result;
	NSRect objc_aRect;
	NSRect objc_bRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSIntersectionRect", keywords, convert_NSRect, &objc_aRect, convert_NSRect, &objc_bRect) < 0) return NULL;
	NS_DURING
		objc_result = NSIntersectionRect(
objc_aRect, objc_bRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_ObjCToPython(@encode(NSRect), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* NSRect NSOffsetRect(NSRect aRect, float dX, float dY); */
PyObject* objc_NSOffsetRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "dX", "dY", NULL };
	PyObject* result;
	NSRect objc_result;
	NSRect objc_aRect;
	float objc_dX;
	float objc_dY;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&ff:NSOffsetRect", keywords, convert_NSRect, &objc_aRect, &objc_dX, &objc_dY) < 0) return NULL;
	NS_DURING
		objc_result = NSOffsetRect(
objc_aRect, objc_dX, objc_dY);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_ObjCToPython(@encode(NSRect), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSPointInRect(NSPoint aPoint, NSRect aRect); */
PyObject* objc_NSPointInRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aPoint", "aRect", NULL };
	PyObject* result;
	BOOL objc_result;
	NSPoint objc_aPoint;
	NSRect objc_aRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSPointInRect", keywords, convert_NSPoint, &objc_aPoint, convert_NSRect, &objc_aRect) < 0) return NULL;
	NS_DURING
		objc_result = NSPointInRect(
objc_aPoint, objc_aRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSMouseInRect(NSPoint aPoint, NSRect aRect, BOOL flipped); */
PyObject* objc_NSMouseInRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aPoint", "aRect", "flipped", NULL };
	PyObject* result;
	BOOL objc_result;
	NSPoint objc_aPoint;
	NSRect objc_aRect;
	BOOL objc_flipped;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&O&:NSMouseInRect", keywords, convert_NSPoint, &objc_aPoint, convert_NSRect, &objc_aRect, convert_BOOL, &objc_flipped) < 0) return NULL;
	NS_DURING
		objc_result = NSMouseInRect(
objc_aPoint, objc_aRect, objc_flipped);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSContainsRect(NSRect aRect, NSRect bRect); */
PyObject* objc_NSContainsRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "bRect", NULL };
	PyObject* result;
	BOOL objc_result;
	NSRect objc_aRect;
	NSRect objc_bRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSContainsRect", keywords, convert_NSRect, &objc_aRect, convert_NSRect, &objc_bRect) < 0) return NULL;
	NS_DURING
		objc_result = NSContainsRect(
objc_aRect, objc_bRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSIntersectsRect(NSRect aRect, NSRect bRect); */
PyObject* objc_NSIntersectsRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", "bRect", NULL };
	PyObject* result;
	BOOL objc_result;
	NSRect objc_aRect;
	NSRect objc_bRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSIntersectsRect", keywords, convert_NSRect, &objc_aRect, convert_NSRect, &objc_bRect) < 0) return NULL;
	NS_DURING
		objc_result = NSIntersectsRect(
objc_aRect, objc_bRect);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* id NSJavaSetupVirtualMachine(void); */
PyObject* objc_NSJavaSetupVirtualMachine(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	id objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSJavaSetupVirtualMachine", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSJavaSetupVirtualMachine(
);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* void NSDeallocateObject(id <NSObject>object); */
PyObject* objc_NSDeallocateObject(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "object", NULL };
	PyObject* result;
	id objc_object;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSDeallocateObject", keywords, convert_id, &objc_object) < 0) return NULL;
	NS_DURING
		NSDeallocateObject(
objc_object);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSIncrementExtraRefCount(id object); */
PyObject* objc_NSIncrementExtraRefCount(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "object", NULL };
	PyObject* result;
	id objc_object;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSIncrementExtraRefCount", keywords, convert_id, &objc_object) < 0) return NULL;
	NS_DURING
		NSIncrementExtraRefCount(
objc_object);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* BOOL NSDecrementExtraRefCountWasZero(id object); */
PyObject* objc_NSDecrementExtraRefCountWasZero(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "object", NULL };
	PyObject* result;
	BOOL objc_result;
	id objc_object;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSDecrementExtraRefCountWasZero", keywords, convert_id, &objc_object) < 0) return NULL;
	NS_DURING
		objc_result = NSDecrementExtraRefCountWasZero(
objc_object);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* unsigned NSExtraRefCount(id object); */
PyObject* objc_NSExtraRefCount(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "object", NULL };
	PyObject* result;
	unsigned objc_result;
	id objc_object;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSExtraRefCount", keywords, convert_id, &objc_object) < 0) return NULL;
	NS_DURING
		objc_result = NSExtraRefCount(
objc_object);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* NSRange NSUnionRange(NSRange range1, NSRange range2); */
PyObject* objc_NSUnionRange(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "range1", "range2", NULL };
	PyObject* result;
	NSRange objc_result;
	NSRange objc_range1;
	NSRange objc_range2;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSUnionRange", keywords, convert_NSRange, &objc_range1, convert_NSRange, &objc_range2) < 0) return NULL;
	NS_DURING
		objc_result = NSUnionRange(
objc_range1, objc_range2);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_ObjCToPython(@encode(NSRange), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* NSRange NSIntersectionRange(NSRange range1, NSRange range2); */
PyObject* objc_NSIntersectionRange(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "range1", "range2", NULL };
	PyObject* result;
	NSRange objc_result;
	NSRange objc_range1;
	NSRange objc_range2;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSIntersectionRange", keywords, convert_NSRange, &objc_range1, convert_NSRange, &objc_range2) < 0) return NULL;
	NS_DURING
		objc_result = NSIntersectionRange(
objc_range1, objc_range2);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = ObjC_ObjCToPython(@encode(NSRange), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* unsigned NSPageSize(void); */
PyObject* objc_NSPageSize(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	unsigned objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSPageSize", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSPageSize(
);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* unsigned NSLogPageSize(void); */
PyObject* objc_NSLogPageSize(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	unsigned objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSLogPageSize", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSLogPageSize(
);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* unsigned NSRoundUpToMultipleOfPageSize(unsigned bytes); */
PyObject* objc_NSRoundUpToMultipleOfPageSize(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "bytes", NULL };
	PyObject* result;
	unsigned objc_result;
	unsigned objc_bytes;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "i:NSRoundUpToMultipleOfPageSize", keywords, &objc_bytes) < 0) return NULL;
	NS_DURING
		objc_result = NSRoundUpToMultipleOfPageSize(
objc_bytes);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* unsigned NSRoundDownToMultipleOfPageSize(unsigned bytes); */
PyObject* objc_NSRoundDownToMultipleOfPageSize(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "bytes", NULL };
	PyObject* result;
	unsigned objc_result;
	unsigned objc_bytes;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "i:NSRoundDownToMultipleOfPageSize", keywords, &objc_bytes) < 0) return NULL;
	NS_DURING
		objc_result = NSRoundDownToMultipleOfPageSize(
objc_bytes);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* unsigned NSRealMemoryAvailable(void); */
PyObject* objc_NSRealMemoryAvailable(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	unsigned objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSRealMemoryAvailable", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSRealMemoryAvailable(
);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}

#define METHOD_TABLE_ENTRIES \
	{ "NSIsFreedObject", (PyCFunction)objc_NSIsFreedObject, METH_VARARGS|METH_KEYWORDS, "BOOL NSIsFreedObject(id anObject);" }, \
	{ "NSCountFrames", (PyCFunction)objc_NSCountFrames, METH_VARARGS|METH_KEYWORDS, "unsigned NSCountFrames(void);" }, \
	{ "NSEqualPoints", (PyCFunction)objc_NSEqualPoints, METH_VARARGS|METH_KEYWORDS, "BOOL NSEqualPoints(NSPoint aPoint, NSPoint bPoint);" }, \
	{ "NSEqualSizes", (PyCFunction)objc_NSEqualSizes, METH_VARARGS|METH_KEYWORDS, "BOOL NSEqualSizes(NSSize aSize, NSSize bSize);" }, \
	{ "NSEqualRects", (PyCFunction)objc_NSEqualRects, METH_VARARGS|METH_KEYWORDS, "BOOL NSEqualRects(NSRect aRect, NSRect bRect);" }, \
	{ "NSIsEmptyRect", (PyCFunction)objc_NSIsEmptyRect, METH_VARARGS|METH_KEYWORDS, "BOOL NSIsEmptyRect(NSRect aRect);" }, \
	{ "NSInsetRect", (PyCFunction)objc_NSInsetRect, METH_VARARGS|METH_KEYWORDS, "NSRect NSInsetRect(NSRect aRect, float dX, float dY);" }, \
	{ "NSIntegralRect", (PyCFunction)objc_NSIntegralRect, METH_VARARGS|METH_KEYWORDS, "NSRect NSIntegralRect(NSRect aRect);" }, \
	{ "NSUnionRect", (PyCFunction)objc_NSUnionRect, METH_VARARGS|METH_KEYWORDS, "NSRect NSUnionRect(NSRect aRect, NSRect bRect);" }, \
	{ "NSIntersectionRect", (PyCFunction)objc_NSIntersectionRect, METH_VARARGS|METH_KEYWORDS, "NSRect NSIntersectionRect(NSRect aRect, NSRect bRect);" }, \
	{ "NSOffsetRect", (PyCFunction)objc_NSOffsetRect, METH_VARARGS|METH_KEYWORDS, "NSRect NSOffsetRect(NSRect aRect, float dX, float dY);" }, \
	{ "NSPointInRect", (PyCFunction)objc_NSPointInRect, METH_VARARGS|METH_KEYWORDS, "BOOL NSPointInRect(NSPoint aPoint, NSRect aRect);" }, \
	{ "NSMouseInRect", (PyCFunction)objc_NSMouseInRect, METH_VARARGS|METH_KEYWORDS, "BOOL NSMouseInRect(NSPoint aPoint, NSRect aRect, BOOL flipped);" }, \
	{ "NSContainsRect", (PyCFunction)objc_NSContainsRect, METH_VARARGS|METH_KEYWORDS, "BOOL NSContainsRect(NSRect aRect, NSRect bRect);" }, \
	{ "NSIntersectsRect", (PyCFunction)objc_NSIntersectsRect, METH_VARARGS|METH_KEYWORDS, "BOOL NSIntersectsRect(NSRect aRect, NSRect bRect);" }, \
	{ "NSJavaSetupVirtualMachine", (PyCFunction)objc_NSJavaSetupVirtualMachine, METH_VARARGS|METH_KEYWORDS, "id NSJavaSetupVirtualMachine(void);" }, \
	{ "NSDeallocateObject", (PyCFunction)objc_NSDeallocateObject, METH_VARARGS|METH_KEYWORDS, "void NSDeallocateObject(id <NSObject>object);" }, \
	{ "NSIncrementExtraRefCount", (PyCFunction)objc_NSIncrementExtraRefCount, METH_VARARGS|METH_KEYWORDS, "void NSIncrementExtraRefCount(id object);" }, \
	{ "NSDecrementExtraRefCountWasZero", (PyCFunction)objc_NSDecrementExtraRefCountWasZero, METH_VARARGS|METH_KEYWORDS, "BOOL NSDecrementExtraRefCountWasZero(id object);" }, \
	{ "NSExtraRefCount", (PyCFunction)objc_NSExtraRefCount, METH_VARARGS|METH_KEYWORDS, "unsigned NSExtraRefCount(id object);" }, \
	{ "NSUnionRange", (PyCFunction)objc_NSUnionRange, METH_VARARGS|METH_KEYWORDS, "NSRange NSUnionRange(NSRange range1, NSRange range2);" }, \
	{ "NSIntersectionRange", (PyCFunction)objc_NSIntersectionRange, METH_VARARGS|METH_KEYWORDS, "NSRange NSIntersectionRange(NSRange range1, NSRange range2);" }, \
	{ "NSPageSize", (PyCFunction)objc_NSPageSize, METH_VARARGS|METH_KEYWORDS, "unsigned NSPageSize(void);" }, \
	{ "NSLogPageSize", (PyCFunction)objc_NSLogPageSize, METH_VARARGS|METH_KEYWORDS, "unsigned NSLogPageSize(void);" }, \
	{ "NSRoundUpToMultipleOfPageSize", (PyCFunction)objc_NSRoundUpToMultipleOfPageSize, METH_VARARGS|METH_KEYWORDS, "unsigned NSRoundUpToMultipleOfPageSize(unsigned bytes);" }, \
	{ "NSRoundDownToMultipleOfPageSize", (PyCFunction)objc_NSRoundDownToMultipleOfPageSize, METH_VARARGS|METH_KEYWORDS, "unsigned NSRoundDownToMultipleOfPageSize(unsigned bytes);" }, \
	{ "NSRealMemoryAvailable", (PyCFunction)objc_NSRealMemoryAvailable, METH_VARARGS|METH_KEYWORDS, "unsigned NSRealMemoryAvailable(void);" }, \
	/* END */
