static inline int convert_NSPoint(PyObject* object, void* pvar)
{
	const char* errstr;

	errstr = PyObjC_PythonToObjC(@encode(NSPoint), object, pvar);
	if (errstr) {
		PyErr_SetString(PyExc_TypeError, errstr);
		return 0;
	}
	return 1;
}
static inline int convert_NSSize(PyObject* object, void* pvar)
{
	const char* errstr;

	errstr = PyObjC_PythonToObjC(@encode(NSSize), object, pvar);
	if (errstr) {
		PyErr_SetString(PyExc_TypeError, errstr);
		return 0;
	}
	return 1;
}
static inline int convert_NSRect(PyObject* object, void* pvar)
{
	const char* errstr;

	errstr = PyObjC_PythonToObjC(@encode(NSRect), object, pvar);
	if (errstr) {
		PyErr_SetString(PyExc_TypeError, errstr);
		return 0;
	}
	return 1;
}
static inline int convert_NSRange(PyObject* object, void* pvar)
{
	const char* errstr;

	errstr = PyObjC_PythonToObjC(@encode(NSRange), object, pvar);
	if (errstr) {
		PyErr_SetString(PyExc_TypeError, errstr);
		return 0;
	}
	return 1;
}
/*
 * This is a generated file.
 */

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

	*pid = PyObjC_PythonToId(object);

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
	if (!PyObjCClass_Check(object)) {
		PyErr_SetString(PyExc_TypeError, "Excpected objective-C class");
		return 0;
	}

	*(Class*)pvar = PyObjCClass_GetClass(object);
	if (*(Class*)pvar == NULL) return 0;
	return 1;
}

#ifndef GNUSTEP
/* NSObject *NXReadNSObjectFromCoder(NSCoder *decoder); */
static PyObject* objc_NXReadNSObjectFromCoder(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "decoder", NULL };
	PyObject* result;
	NSObject* objc_result;
	id objc_decoder;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NXReadNSObjectFromCoder", keywords, convert_id, &objc_decoder) < 0) return NULL;
	NS_DURING
		objc_result = NXReadNSObjectFromCoder(
objc_decoder);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
#endif

#ifndef GNUSTEP
/* BOOL NSIsFreedObject(id anObject); */
static PyObject* objc_NSIsFreedObject(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
#endif
/* unsigned NSCountFrames(void); */
static PyObject* objc_NSCountFrames(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	unsigned objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSCountFrames", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSCountFrames(
);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSEqualPoints(NSPoint aPoint, NSPoint bPoint); */
static PyObject* objc_NSEqualPoints(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSEqualSizes(NSSize aSize, NSSize bSize); */
static PyObject* objc_NSEqualSizes(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSEqualRects(NSRect aRect, NSRect bRect); */
static PyObject* objc_NSEqualRects(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSIsEmptyRect(NSRect aRect); */
static PyObject* objc_NSIsEmptyRect(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* NSRect NSInsetRect(NSRect aRect, float dX, float dY); */
static PyObject* objc_NSInsetRect(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_ObjCToPython(@encode(NSRect), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* NSRect NSIntegralRect(NSRect aRect); */
static PyObject* objc_NSIntegralRect(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_ObjCToPython(@encode(NSRect), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* NSRect NSUnionRect(NSRect aRect, NSRect bRect); */
static PyObject* objc_NSUnionRect(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_ObjCToPython(@encode(NSRect), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* NSRect NSIntersectionRect(NSRect aRect, NSRect bRect); */
static PyObject* objc_NSIntersectionRect(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_ObjCToPython(@encode(NSRect), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* NSRect NSOffsetRect(NSRect aRect, float dX, float dY); */
static PyObject* objc_NSOffsetRect(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_ObjCToPython(@encode(NSRect), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSPointInRect(NSPoint aPoint, NSRect aRect); */
static PyObject* objc_NSPointInRect(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSMouseInRect(NSPoint aPoint, NSRect aRect, BOOL flipped); */
static PyObject* objc_NSMouseInRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aPoint", "aRect", "flipped", NULL };
	PyObject* result;
	BOOL objc_result;
	NSPoint objc_aPoint;
	NSRect objc_aRect;
	BOOL objc_flipped;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&i:NSMouseInRect", keywords, convert_NSPoint, &objc_aPoint, convert_NSRect, &objc_aRect, &objc_flipped) < 0) return NULL;
	NS_DURING
		objc_result = NSMouseInRect(
objc_aPoint, objc_aRect, objc_flipped);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSContainsRect(NSRect aRect, NSRect bRect); */
static PyObject* objc_NSContainsRect(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSIntersectsRect(NSRect aRect, NSRect bRect); */
static PyObject* objc_NSIntersectsRect(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* NSString *NSStringFromPoint(NSPoint aPoint); */
static PyObject* objc_NSStringFromPoint(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aPoint", NULL };
	PyObject* result;
	NSString* objc_result;
	NSPoint objc_aPoint;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSStringFromPoint", keywords, convert_NSPoint, &objc_aPoint) < 0) return NULL;
	NS_DURING
		objc_result = NSStringFromPoint(
objc_aPoint);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSString *NSStringFromSize(NSSize aSize); */
static PyObject* objc_NSStringFromSize(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aSize", NULL };
	PyObject* result;
	NSString* objc_result;
	NSSize objc_aSize;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSStringFromSize", keywords, convert_NSSize, &objc_aSize) < 0) return NULL;
	NS_DURING
		objc_result = NSStringFromSize(
objc_aSize);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSString *NSStringFromRect(NSRect aRect); */
static PyObject* objc_NSStringFromRect(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aRect", NULL };
	PyObject* result;
	NSString* objc_result;
	NSRect objc_aRect;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSStringFromRect", keywords, convert_NSRect, &objc_aRect) < 0) return NULL;
	NS_DURING
		objc_result = NSStringFromRect(
objc_aRect);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSPoint NSPointFromString(NSString *aString); */
static PyObject* objc_NSPointFromString(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aString", NULL };
	PyObject* result;
	NSPoint objc_result;
	id objc_aString;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSPointFromString", keywords, convert_id, &objc_aString) < 0) return NULL;
	NS_DURING
		objc_result = NSPointFromString(
objc_aString);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_ObjCToPython(@encode(NSPoint), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* NSSize NSSizeFromString(NSString *aString); */
static PyObject* objc_NSSizeFromString(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aString", NULL };
	PyObject* result;
	NSSize objc_result;
	id objc_aString;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSSizeFromString", keywords, convert_id, &objc_aString) < 0) return NULL;
	NS_DURING
		objc_result = NSSizeFromString(
objc_aString);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_ObjCToPython(@encode(NSSize), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* NSRect NSRectFromString(NSString *aString); */
static PyObject* objc_NSRectFromString(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aString", NULL };
	PyObject* result;
	NSRect objc_result;
	id objc_aString;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSRectFromString", keywords, convert_id, &objc_aString) < 0) return NULL;
	NS_DURING
		objc_result = NSRectFromString(
objc_aString);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_ObjCToPython(@encode(NSRect), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
#ifndef GNUSTEP
/* NSString *NSHFSTypeOfFile(NSString *fullFilePath); */
static PyObject* objc_NSHFSTypeOfFile(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "fullFilePath", NULL };
	PyObject* result;
	NSString* objc_result;
	id objc_fullFilePath;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSHFSTypeOfFile", keywords, convert_id, &objc_fullFilePath) < 0) return NULL;
	NS_DURING
		objc_result = NSHFSTypeOfFile(
objc_fullFilePath);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* BOOL NSJavaNeedsVirtualMachine(NSDictionary *plist); */
static PyObject* objc_NSJavaNeedsVirtualMachine(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "plist", NULL };
	PyObject* result;
	BOOL objc_result;
	id objc_plist;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSJavaNeedsVirtualMachine", keywords, convert_id, &objc_plist) < 0) return NULL;
	NS_DURING
		objc_result = NSJavaNeedsVirtualMachine(
objc_plist);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}

/* BOOL NSJavaProvidesClasses(NSDictionary *plist); */
static PyObject* objc_NSJavaProvidesClasses(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "plist", NULL };
	PyObject* result;
	BOOL objc_result;
	id objc_plist;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSJavaProvidesClasses", keywords, convert_id, &objc_plist) < 0) return NULL;
	NS_DURING
		objc_result = NSJavaProvidesClasses(
objc_plist);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* BOOL NSJavaNeedsToLoadClasses(NSDictionary *plist); */
static PyObject* objc_NSJavaNeedsToLoadClasses(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "plist", NULL };
	PyObject* result;
	BOOL objc_result;
	id objc_plist;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSJavaNeedsToLoadClasses", keywords, convert_id, &objc_plist) < 0) return NULL;
	NS_DURING
		objc_result = NSJavaNeedsToLoadClasses(
objc_plist);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* id NSJavaSetup(NSDictionary *plist); */
static PyObject* objc_NSJavaSetup(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "plist", NULL };
	PyObject* result;
	id objc_result;
	id objc_plist;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSJavaSetup", keywords, convert_id, &objc_plist) < 0) return NULL;
	NS_DURING
		objc_result = NSJavaSetup(
objc_plist);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* id NSJavaSetupVirtualMachine(void); */
static PyObject* objc_NSJavaSetupVirtualMachine(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	id objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSJavaSetupVirtualMachine", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSJavaSetupVirtualMachine(
);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* id NSJavaObjectNamedInPath(NSString *name, NSArray *path); */
static PyObject* objc_NSJavaObjectNamedInPath(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "name", "path", NULL };
	PyObject* result;
	id objc_result;
	id objc_name;
	id objc_path;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSJavaObjectNamedInPath", keywords, convert_id, &objc_name, convert_id, &objc_path) < 0) return NULL;
	NS_DURING
		objc_result = NSJavaObjectNamedInPath(
objc_name, objc_path);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* id NSJavaBundleSetup(NSBundle *bundle, NSDictionary *plist); */
static PyObject* objc_NSJavaBundleSetup(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "bundle", "plist", NULL };
	PyObject* result;
	id objc_result;
	id objc_bundle;
	id objc_plist;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSJavaBundleSetup", keywords, convert_id, &objc_bundle, convert_id, &objc_plist) < 0) return NULL;
	NS_DURING
		objc_result = NSJavaBundleSetup(
objc_bundle, objc_plist);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* void NSJavaBundleCleanup(NSBundle *bundle, NSDictionary *plist); */
static PyObject* objc_NSJavaBundleCleanup(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "bundle", "plist", NULL };
	PyObject* result;
	id objc_bundle;
	id objc_plist;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSJavaBundleCleanup", keywords, convert_id, &objc_bundle, convert_id, &objc_plist) < 0) return NULL;
	NS_DURING
		NSJavaBundleCleanup(
objc_bundle, objc_plist);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
#endif

/* NSString *NSStringFromSelector(SEL aSelector); */
static PyObject* objc_NSStringFromSelector(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aSelector", NULL };
	PyObject* result;
	NSString* objc_result;
	SEL objc_aSelector;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSStringFromSelector", keywords, convert_SEL, &objc_aSelector) < 0) return NULL;
	NS_DURING
		objc_result = NSStringFromSelector(
objc_aSelector);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* SEL NSSelectorFromString(NSString *aSelectorName); */
static PyObject* objc_NSSelectorFromString(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aSelectorName", NULL };
	PyObject* result;
	SEL objc_result;
	id objc_aSelectorName;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSSelectorFromString", keywords, convert_id, &objc_aSelectorName) < 0) return NULL;
	NS_DURING
		objc_result = NSSelectorFromString(
objc_aSelectorName);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyString_FromString(SELNAME(objc_result));
	if (result == NULL) return NULL;
	return result;
}
/* Class NSClassFromString(NSString *aClassName); */
static PyObject* objc_NSClassFromString(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aClassName", NULL };
	PyObject* result;
	Class objc_result;
	id objc_aClassName;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSClassFromString", keywords, convert_id, &objc_aClassName) < 0) return NULL;
	NS_DURING
		objc_result = NSClassFromString(
objc_aClassName);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCClass_New(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* NSString *NSStringFromClass(Class aClass); */
static PyObject* objc_NSStringFromClass(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aClass", NULL };
	PyObject* result;
	NSString* objc_result;
	Class objc_aClass;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSStringFromClass", keywords, convert_Class, &objc_aClass) < 0) return NULL;
	NS_DURING
		objc_result = NSStringFromClass(
objc_aClass);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* void NSDeallocateObject(id <NSObject>object); */
static PyObject* objc_NSDeallocateObject(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "object", NULL };
	PyObject* result;
	id objc_object;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSDeallocateObject", keywords, convert_id, &objc_object) < 0) return NULL;
	NS_DURING
		NSDeallocateObject(
objc_object);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* void NSIncrementExtraRefCount(id object); */
static PyObject* objc_NSIncrementExtraRefCount(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "object", NULL };
	PyObject* result;
	id objc_object;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSIncrementExtraRefCount", keywords, convert_id, &objc_object) < 0) return NULL;
	NS_DURING
		NSIncrementExtraRefCount(
objc_object);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}
/* BOOL NSDecrementExtraRefCountWasZero(id object); */
static PyObject* objc_NSDecrementExtraRefCountWasZero(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjCBool_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* unsigned NSExtraRefCount(id object); */
static PyObject* objc_NSExtraRefCount(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* NSString *NSUserName(void); */
static PyObject* objc_NSUserName(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	NSString* objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSUserName", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSUserName(
);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSString *NSFullUserName(void); */
static PyObject* objc_NSFullUserName(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	NSString* objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSFullUserName", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSFullUserName(
);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSString *NSHomeDirectory(void); */
static PyObject* objc_NSHomeDirectory(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	NSString* objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSHomeDirectory", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSHomeDirectory(
);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSString *NSHomeDirectoryForUser(NSString *userName); */
static PyObject* objc_NSHomeDirectoryForUser(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "userName", NULL };
	PyObject* result;
	NSString* objc_result;
	id objc_userName;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSHomeDirectoryForUser", keywords, convert_id, &objc_userName) < 0) return NULL;
	NS_DURING
		objc_result = NSHomeDirectoryForUser(
objc_userName);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSString *NSTemporaryDirectory(void); */
static PyObject* objc_NSTemporaryDirectory(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	NSString* objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSTemporaryDirectory", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSTemporaryDirectory(
);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSString *NSOpenStepRootDirectory(void); */
static PyObject* objc_NSOpenStepRootDirectory(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	NSString* objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSOpenStepRootDirectory", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSOpenStepRootDirectory(
);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSArray *NSSearchPathForDirectoriesInDomains(NSSearchPathDirectory directory, NSSearchPathDomainMask domainMask, BOOL expandTilde); */
static PyObject* objc_NSSearchPathForDirectoriesInDomains(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "directory", "domainMask", "expandTilde", NULL };
	PyObject* result;
	NSArray* objc_result;
	NSSearchPathDirectory objc_directory;
	NSSearchPathDomainMask objc_domainMask;
	BOOL objc_expandTilde;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "iii:NSSearchPathForDirectoriesInDomains", keywords, &objc_directory, &objc_domainMask, &objc_expandTilde) < 0) return NULL;
	NS_DURING
		objc_result = NSSearchPathForDirectoriesInDomains(
objc_directory, objc_domainMask, objc_expandTilde);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSRange NSUnionRange(NSRange range1, NSRange range2); */
static PyObject* objc_NSUnionRange(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_ObjCToPython(@encode(NSRange), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* NSRange NSIntersectionRange(NSRange range1, NSRange range2); */
static PyObject* objc_NSIntersectionRange(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_ObjCToPython(@encode(NSRange), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* NSString *NSStringFromRange(NSRange range); */
static PyObject* objc_NSStringFromRange(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "range", NULL };
	PyObject* result;
	NSString* objc_result;
	NSRange objc_range;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSStringFromRange", keywords, convert_NSRange, &objc_range) < 0) return NULL;
	NS_DURING
		objc_result = NSStringFromRange(
objc_range);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_IdToPython(objc_result); if (result == NULL) return NULL;
	return result;
}
/* NSRange NSRangeFromString(NSString *aString); */
static PyObject* objc_NSRangeFromString(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "aString", NULL };
	PyObject* result;
	NSRange objc_result;
	id objc_aString;

	if (PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSRangeFromString", keywords, convert_id, &objc_aString) < 0) return NULL;
	NS_DURING
		objc_result = NSRangeFromString(
objc_aString);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyObjC_ObjCToPython(@encode(NSRange), (void*)&objc_result); 
	if (result == NULL) return NULL;
	return result;
}
/* unsigned NSPageSize(void); */
static PyObject* objc_NSPageSize(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	unsigned objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSPageSize", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSPageSize(
);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* unsigned NSLogPageSize(void); */
static PyObject* objc_NSLogPageSize(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	unsigned objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSLogPageSize", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSLogPageSize(
);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* unsigned NSRoundUpToMultipleOfPageSize(unsigned bytes); */
static PyObject* objc_NSRoundUpToMultipleOfPageSize(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* unsigned NSRoundDownToMultipleOfPageSize(unsigned bytes); */
static PyObject* objc_NSRoundDownToMultipleOfPageSize(PyObject* self, PyObject* args, PyObject* kwds)
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
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}
/* unsigned NSRealMemoryAvailable(void); */
static PyObject* objc_NSRealMemoryAvailable(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { NULL };
	PyObject* result;
	unsigned objc_result;

	if (PyArg_ParseTupleAndKeywords(args, kwds, ":NSRealMemoryAvailable", keywords) < 0) return NULL;
	NS_DURING
		objc_result = NSRealMemoryAvailable(
);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		return NULL;
	NS_ENDHANDLER
		result = PyInt_FromLong(objc_result);
	if (result == NULL) return NULL;
	return result;
}

#ifndef GNUSTEP
#define METHOD_TABLE_ENTRIES \
	{ "NXReadNSObjectFromCoder", (PyCFunction)objc_NXReadNSObjectFromCoder, METH_VARARGS|METH_KEYWORDS, "NSObject *NXReadNSObjectFromCoder(NSCoder *decoder);" }, \
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
	{ "NSStringFromPoint", (PyCFunction)objc_NSStringFromPoint, METH_VARARGS|METH_KEYWORDS, "NSString *NSStringFromPoint(NSPoint aPoint);" }, \
	{ "NSStringFromSize", (PyCFunction)objc_NSStringFromSize, METH_VARARGS|METH_KEYWORDS, "NSString *NSStringFromSize(NSSize aSize);" }, \
	{ "NSStringFromRect", (PyCFunction)objc_NSStringFromRect, METH_VARARGS|METH_KEYWORDS, "NSString *NSStringFromRect(NSRect aRect);" }, \
	{ "NSPointFromString", (PyCFunction)objc_NSPointFromString, METH_VARARGS|METH_KEYWORDS, "NSPoint NSPointFromString(NSString *aString);" }, \
	{ "NSSizeFromString", (PyCFunction)objc_NSSizeFromString, METH_VARARGS|METH_KEYWORDS, "NSSize NSSizeFromString(NSString *aString);" }, \
	{ "NSRectFromString", (PyCFunction)objc_NSRectFromString, METH_VARARGS|METH_KEYWORDS, "NSRect NSRectFromString(NSString *aString);" }, \
	{ "NSHFSTypeOfFile", (PyCFunction)objc_NSHFSTypeOfFile, METH_VARARGS|METH_KEYWORDS, "NSString *NSHFSTypeOfFile(NSString *fullFilePath);" }, \
	{ "NSJavaNeedsVirtualMachine", (PyCFunction)objc_NSJavaNeedsVirtualMachine, METH_VARARGS|METH_KEYWORDS, "BOOL NSJavaNeedsVirtualMachine(NSDictionary *plist);" }, \
	{ "NSJavaProvidesClasses", (PyCFunction)objc_NSJavaProvidesClasses, METH_VARARGS|METH_KEYWORDS, "BOOL NSJavaProvidesClasses(NSDictionary *plist);" }, \
	{ "NSJavaNeedsToLoadClasses", (PyCFunction)objc_NSJavaNeedsToLoadClasses, METH_VARARGS|METH_KEYWORDS, "BOOL NSJavaNeedsToLoadClasses(NSDictionary *plist);" }, \
	{ "NSJavaSetup", (PyCFunction)objc_NSJavaSetup, METH_VARARGS|METH_KEYWORDS, "id NSJavaSetup(NSDictionary *plist);" }, \
	{ "NSJavaSetupVirtualMachine", (PyCFunction)objc_NSJavaSetupVirtualMachine, METH_VARARGS|METH_KEYWORDS, "id NSJavaSetupVirtualMachine(void);" }, \
	{ "NSJavaObjectNamedInPath", (PyCFunction)objc_NSJavaObjectNamedInPath, METH_VARARGS|METH_KEYWORDS, "id NSJavaObjectNamedInPath(NSString *name, NSArray *path);" }, \
	{ "NSJavaBundleSetup", (PyCFunction)objc_NSJavaBundleSetup, METH_VARARGS|METH_KEYWORDS, "id NSJavaBundleSetup(NSBundle *bundle, NSDictionary *plist);" }, \
	{ "NSJavaBundleCleanup", (PyCFunction)objc_NSJavaBundleCleanup, METH_VARARGS|METH_KEYWORDS, "void NSJavaBundleCleanup(NSBundle *bundle, NSDictionary *plist);" }, \
	{ "NSStringFromSelector", (PyCFunction)objc_NSStringFromSelector, METH_VARARGS|METH_KEYWORDS, "NSString *NSStringFromSelector(SEL aSelector);" }, \
	{ "NSSelectorFromString", (PyCFunction)objc_NSSelectorFromString, METH_VARARGS|METH_KEYWORDS, "SEL NSSelectorFromString(NSString *aSelectorName);" }, \
	{ "NSClassFromString", (PyCFunction)objc_NSClassFromString, METH_VARARGS|METH_KEYWORDS, "Class NSClassFromString(NSString *aClassName);" }, \
	{ "NSStringFromClass", (PyCFunction)objc_NSStringFromClass, METH_VARARGS|METH_KEYWORDS, "NSString *NSStringFromClass(Class aClass);" }, \
	{ "NSDeallocateObject", (PyCFunction)objc_NSDeallocateObject, METH_VARARGS|METH_KEYWORDS, "void NSDeallocateObject(id <NSObject>object);" }, \
	{ "NSIncrementExtraRefCount", (PyCFunction)objc_NSIncrementExtraRefCount, METH_VARARGS|METH_KEYWORDS, "void NSIncrementExtraRefCount(id object);" }, \
	{ "NSDecrementExtraRefCountWasZero", (PyCFunction)objc_NSDecrementExtraRefCountWasZero, METH_VARARGS|METH_KEYWORDS, "BOOL NSDecrementExtraRefCountWasZero(id object);" }, \
	{ "NSExtraRefCount", (PyCFunction)objc_NSExtraRefCount, METH_VARARGS|METH_KEYWORDS, "unsigned NSExtraRefCount(id object);" }, \
	{ "NSUserName", (PyCFunction)objc_NSUserName, METH_VARARGS|METH_KEYWORDS, "NSString *NSUserName(void);" }, \
	{ "NSFullUserName", (PyCFunction)objc_NSFullUserName, METH_VARARGS|METH_KEYWORDS, "NSString *NSFullUserName(void);" }, \
	{ "NSHomeDirectory", (PyCFunction)objc_NSHomeDirectory, METH_VARARGS|METH_KEYWORDS, "NSString *NSHomeDirectory(void);" }, \
	{ "NSHomeDirectoryForUser", (PyCFunction)objc_NSHomeDirectoryForUser, METH_VARARGS|METH_KEYWORDS, "NSString *NSHomeDirectoryForUser(NSString *userName);" }, \
	{ "NSTemporaryDirectory", (PyCFunction)objc_NSTemporaryDirectory, METH_VARARGS|METH_KEYWORDS, "NSString *NSTemporaryDirectory(void);" }, \
	{ "NSOpenStepRootDirectory", (PyCFunction)objc_NSOpenStepRootDirectory, METH_VARARGS|METH_KEYWORDS, "NSString *NSOpenStepRootDirectory(void);" }, \
	{ "NSSearchPathForDirectoriesInDomains", (PyCFunction)objc_NSSearchPathForDirectoriesInDomains, METH_VARARGS|METH_KEYWORDS, "NSArray *NSSearchPathForDirectoriesInDomains(NSSearchPathDirectory directory, NSSearchPathDomainMask domainMask, BOOL expandTilde);" }, \
	{ "NSUnionRange", (PyCFunction)objc_NSUnionRange, METH_VARARGS|METH_KEYWORDS, "NSRange NSUnionRange(NSRange range1, NSRange range2);" }, \
	{ "NSIntersectionRange", (PyCFunction)objc_NSIntersectionRange, METH_VARARGS|METH_KEYWORDS, "NSRange NSIntersectionRange(NSRange range1, NSRange range2);" }, \
	{ "NSStringFromRange", (PyCFunction)objc_NSStringFromRange, METH_VARARGS|METH_KEYWORDS, "NSString *NSStringFromRange(NSRange range);" }, \
	{ "NSRangeFromString", (PyCFunction)objc_NSRangeFromString, METH_VARARGS|METH_KEYWORDS, "NSRange NSRangeFromString(NSString *aString);" }, \
	{ "NSPageSize", (PyCFunction)objc_NSPageSize, METH_VARARGS|METH_KEYWORDS, "unsigned NSPageSize(void);" }, \
	{ "NSLogPageSize", (PyCFunction)objc_NSLogPageSize, METH_VARARGS|METH_KEYWORDS, "unsigned NSLogPageSize(void);" }, \
	{ "NSRoundUpToMultipleOfPageSize", (PyCFunction)objc_NSRoundUpToMultipleOfPageSize, METH_VARARGS|METH_KEYWORDS, "unsigned NSRoundUpToMultipleOfPageSize(unsigned bytes);" }, \
	{ "NSRoundDownToMultipleOfPageSize", (PyCFunction)objc_NSRoundDownToMultipleOfPageSize, METH_VARARGS|METH_KEYWORDS, "unsigned NSRoundDownToMultipleOfPageSize(unsigned bytes);" }, \
	{ "NSRealMemoryAvailable", (PyCFunction)objc_NSRealMemoryAvailable, METH_VARARGS|METH_KEYWORDS, "unsigned NSRealMemoryAvailable(void);" }, \
	/* END */

#else /* GNUSTEP */

#define METHOD_TABLE_ENTRIES \
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
	{ "NSStringFromPoint", (PyCFunction)objc_NSStringFromPoint, METH_VARARGS|METH_KEYWORDS, "NSString *NSStringFromPoint(NSPoint aPoint);" }, \
	{ "NSStringFromSize", (PyCFunction)objc_NSStringFromSize, METH_VARARGS|METH_KEYWORDS, "NSString *NSStringFromSize(NSSize aSize);" }, \
	{ "NSStringFromRect", (PyCFunction)objc_NSStringFromRect, METH_VARARGS|METH_KEYWORDS, "NSString *NSStringFromRect(NSRect aRect);" }, \
	{ "NSPointFromString", (PyCFunction)objc_NSPointFromString, METH_VARARGS|METH_KEYWORDS, "NSPoint NSPointFromString(NSString *aString);" }, \
	{ "NSSizeFromString", (PyCFunction)objc_NSSizeFromString, METH_VARARGS|METH_KEYWORDS, "NSSize NSSizeFromString(NSString *aString);" }, \
	{ "NSRectFromString", (PyCFunction)objc_NSRectFromString, METH_VARARGS|METH_KEYWORDS, "NSRect NSRectFromString(NSString *aString);" }, \
	{ "NSStringFromSelector", (PyCFunction)objc_NSStringFromSelector, METH_VARARGS|METH_KEYWORDS, "NSString *NSStringFromSelector(SEL aSelector);" }, \
	{ "NSSelectorFromString", (PyCFunction)objc_NSSelectorFromString, METH_VARARGS|METH_KEYWORDS, "SEL NSSelectorFromString(NSString *aSelectorName);" }, \
	{ "NSClassFromString", (PyCFunction)objc_NSClassFromString, METH_VARARGS|METH_KEYWORDS, "Class NSClassFromString(NSString *aClassName);" }, \
	{ "NSStringFromClass", (PyCFunction)objc_NSStringFromClass, METH_VARARGS|METH_KEYWORDS, "NSString *NSStringFromClass(Class aClass);" }, \
	{ "NSDeallocateObject", (PyCFunction)objc_NSDeallocateObject, METH_VARARGS|METH_KEYWORDS, "void NSDeallocateObject(id <NSObject>object);" }, \
	{ "NSIncrementExtraRefCount", (PyCFunction)objc_NSIncrementExtraRefCount, METH_VARARGS|METH_KEYWORDS, "void NSIncrementExtraRefCount(id object);" }, \
	{ "NSDecrementExtraRefCountWasZero", (PyCFunction)objc_NSDecrementExtraRefCountWasZero, METH_VARARGS|METH_KEYWORDS, "BOOL NSDecrementExtraRefCountWasZero(id object);" }, \
	{ "NSExtraRefCount", (PyCFunction)objc_NSExtraRefCount, METH_VARARGS|METH_KEYWORDS, "unsigned NSExtraRefCount(id object);" }, \
	{ "NSUserName", (PyCFunction)objc_NSUserName, METH_VARARGS|METH_KEYWORDS, "NSString *NSUserName(void);" }, \
	{ "NSFullUserName", (PyCFunction)objc_NSFullUserName, METH_VARARGS|METH_KEYWORDS, "NSString *NSFullUserName(void);" }, \
	{ "NSHomeDirectory", (PyCFunction)objc_NSHomeDirectory, METH_VARARGS|METH_KEYWORDS, "NSString *NSHomeDirectory(void);" }, \
	{ "NSHomeDirectoryForUser", (PyCFunction)objc_NSHomeDirectoryForUser, METH_VARARGS|METH_KEYWORDS, "NSString *NSHomeDirectoryForUser(NSString *userName);" }, \
	{ "NSTemporaryDirectory", (PyCFunction)objc_NSTemporaryDirectory, METH_VARARGS|METH_KEYWORDS, "NSString *NSTemporaryDirectory(void);" }, \
	{ "NSOpenStepRootDirectory", (PyCFunction)objc_NSOpenStepRootDirectory, METH_VARARGS|METH_KEYWORDS, "NSString *NSOpenStepRootDirectory(void);" }, \
	{ "NSSearchPathForDirectoriesInDomains", (PyCFunction)objc_NSSearchPathForDirectoriesInDomains, METH_VARARGS|METH_KEYWORDS, "NSArray *NSSearchPathForDirectoriesInDomains(NSSearchPathDirectory directory, NSSearchPathDomainMask domainMask, BOOL expandTilde);" }, \
	{ "NSUnionRange", (PyCFunction)objc_NSUnionRange, METH_VARARGS|METH_KEYWORDS, "NSRange NSUnionRange(NSRange range1, NSRange range2);" }, \
	{ "NSIntersectionRange", (PyCFunction)objc_NSIntersectionRange, METH_VARARGS|METH_KEYWORDS, "NSRange NSIntersectionRange(NSRange range1, NSRange range2);" }, \
	{ "NSStringFromRange", (PyCFunction)objc_NSStringFromRange, METH_VARARGS|METH_KEYWORDS, "NSString *NSStringFromRange(NSRange range);" }, \
	{ "NSRangeFromString", (PyCFunction)objc_NSRangeFromString, METH_VARARGS|METH_KEYWORDS, "NSRange NSRangeFromString(NSString *aString);" }, \
	{ "NSPageSize", (PyCFunction)objc_NSPageSize, METH_VARARGS|METH_KEYWORDS, "unsigned NSPageSize(void);" }, \
	{ "NSLogPageSize", (PyCFunction)objc_NSLogPageSize, METH_VARARGS|METH_KEYWORDS, "unsigned NSLogPageSize(void);" }, \
	{ "NSRoundUpToMultipleOfPageSize", (PyCFunction)objc_NSRoundUpToMultipleOfPageSize, METH_VARARGS|METH_KEYWORDS, "unsigned NSRoundUpToMultipleOfPageSize(unsigned bytes);" }, \
	{ "NSRoundDownToMultipleOfPageSize", (PyCFunction)objc_NSRoundDownToMultipleOfPageSize, METH_VARARGS|METH_KEYWORDS, "unsigned NSRoundDownToMultipleOfPageSize(unsigned bytes);" }, \
	{ "NSRealMemoryAvailable", (PyCFunction)objc_NSRealMemoryAvailable, METH_VARARGS|METH_KEYWORDS, "unsigned NSRealMemoryAvailable(void);" }, \
	/* END */

#endif
