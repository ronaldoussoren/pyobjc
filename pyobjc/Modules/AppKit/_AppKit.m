/*
 * Mapping of static items in the AppKit kit and helper functions for mapping
 * "difficult" methods.
 */
#import <AppKit/AppKit.h>
#import <AppKit/NSGraphics.h>
#import <CoreFoundation/CoreFoundation.h>

#include <Python.h>
#include "pyobjc-api.h"
#include "wrapper-const-table.h"

#ifndef GNUSTEP

#if MAC_OS_X_VERSION_MAX_ALLOWED > MAC_OS_X_VERSION_10_2
#import <AppKit/NSNib.h>
#endif

#if MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_2
#import <AppKit/NSAccessibility.h>
#endif

#import <AppKit/NSTypesetter.h>
#endif


/** Functions */

/* The headings below refer to the reference pages on developer.apple.com */

/* 'Applications' */

static PyObject* 
objc_NSApplicationMain(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static	char* keywords[] = { "argv", NULL };
	char** argv = NULL;
	int    argc;
	PyObject* arglist;
	int       i;
	PyObject* v;
	int       res;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O:NSApplicationMain",
			keywords, &arglist)) {
		return NULL;
	}

	if (!PySequence_Check(arglist)) {
		PyErr_SetString(PyExc_TypeError, 
			"NSApplicationMain: need list of strings as argument");
		return NULL;
	}

	argc = PySequence_Size(arglist);
	argv = calloc((argc + 1), sizeof(char**));
	if (argv == NULL) {
		PyErr_SetString(PyExc_MemoryError,
			"Out of memory");
		return NULL;
	}

	for  (i = 0; i < argc; i++) {
		v = PySequence_GetItem(arglist, i);
		if (v == NULL) {
			goto error_cleanup;
		}
		if (!PyString_Check(v)) {
			PyErr_SetString(PyExc_TypeError, 
				"NSApplicationMain: need list of strings "
				"as argument");
			goto error_cleanup;
		}

		argv[i] = strdup(PyString_AsString(v));
		if (argv[i] == NULL) {
			PyErr_SetString(PyExc_MemoryError,
				"Out of memory");
			goto error_cleanup;
		}
	}

	argv[argc] = NULL;

#ifdef MACOSX
	/*
	 * NSApplicationMain on MacOS X completely ignores its arguments and 
	 * reads the argv from the shared NSProcessInfo. We *HACK* around this 
	 * by setting a (private) instance variable of the object.
	 *
	 * This code is evil. Look away if you're easily scared.
	 */
	{
		typedef struct {
			@defs(NSProcessInfo)
		} NSProcessInfoStruct;
	  
		NSMutableArray *newarglist = [[NSMutableArray alloc] init];
		NSProcessInfo *processInfo = [NSProcessInfo processInfo];
		char **anArg = argv;

		while(*anArg) {
			[newarglist addObject: 
				[NSString stringWithUTF8String: *anArg]];
			anArg++;
		}

		// Don't release the orignal arguments, unknown whether this 
		// list is owned by the object.
		//[((NSProcessInfoStruct *)processInfo)->arguments release]; 
		((NSProcessInfoStruct *)processInfo)->arguments = newarglist;
	}
#endif /* MACOSX */

	NS_DURING
		res = NSApplicationMain(argc, (const char**)argv);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		res = -1;
	NS_ENDHANDLER

	for (i = 0; i < argc; i++) {
		free(argv[i]);
	}
	free(argv);

	if (res == -1 && PyErr_Occurred())
		return NULL;
	return PyInt_FromLong(res);

error_cleanup:
	if (argv != NULL) {
		for (i = 0; i < argc; i++) {\
			if (argv[i] != NULL) {
				free(argv[i]);
				argv[i] = NULL;
			}
		}
		free(argv);
		argv = NULL;
	}

	return NULL;
}


static PyObject*
objc_NSApp(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static  char* keywords[] = { NULL };
        PyObject* result;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, ":NSApp", keywords)) {
		return NULL;
	}

	result = PyObjC_IdToPython(NSApp);

	return result;                               
}

static PyObject*
objc_NSCountWindows(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static  char* keywords[] = { NULL };
	int       count;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, ":NSCountWindows", keywords)) {
		return NULL;
	}

	NS_DURING
		NSCountWindows(&count);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER
	if (PyErr_Occurred()) return NULL;

	return PyInt_FromLong(count);
}

static PyObject*
objc_NSCountWindowsForContext(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static  char* keywords[] = { "context", NULL };
	int       count;
	int	  context;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, ":NSCountWindows", keywords, &context)) {
		return NULL;
	}

	NS_DURING
		NSCountWindowsForContext(context, &count);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER
	if (PyErr_Occurred()) return NULL;

	return PyInt_FromLong(count);
}

static PyObject*
objc_NSRectFillList(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static char* keywords[] = { "rects", "count", 0 };
	PyObject* pyList;
	PyObject* pyCount = NULL;
	NSRect* rects;
	int rectCount;
	int arrayToken;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O|O", keywords, &pyList, &pyCount)) {
		return NULL;
	}

	arrayToken = PyObjC_PythonToCArray(
		@encode(NSRect), pyList, pyCount, (void**)&rects, &rectCount);

	if (arrayToken == -1) return NULL;

	NS_DURING
		NSRectFillList(rects, rectCount);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	PyObjC_FreeCArray(arrayToken, rects);

	if (PyErr_Occurred()) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None; 
}

static int
Convert_NSCompositingOperation(PyObject* arg, void* out)
{
	int r;

	r = PyObjC_PythonToObjC(@encode(NSCompositingOperation), arg, out);
	if (r == -1) {
		return 0;
	}
	return 1;
}

static PyObject*
objc_NSRectFillListUsingOperation(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static char* keywords[] = { "rects", "count", "operation", 0 };
	PyObject* pyList;
	PyObject* pyCount = NULL;
	NSRect* rects;
	int rectCount;
	int arrayToken;
	NSCompositingOperation operation;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "OOO&", keywords, &pyList, &pyCount, Convert_NSCompositingOperation, &operation)) {
		return NULL;
	}

	arrayToken = PyObjC_PythonToCArray(
		@encode(NSRect), pyList, pyCount, (void**)&rects, &rectCount);

	if (arrayToken == -1) return NULL;

	NS_DURING
		NSRectFillListUsingOperation(rects, rectCount, operation);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	PyObjC_FreeCArray(arrayToken, rects);

	if (PyErr_Occurred()) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None; 
}

static PyObject*
objc_NSRectFillListWithColors(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static char* keywords[] = { "rects", "colors", "count", 0 };
	PyObject* pyList;
	PyObject* pyColors;
	PyObject* pyCount = NULL;
	NSRect* rects;
	id* colors;
	int rectCount;
	int colorCount;
	int rectToken;
	int colorToken;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "OO|O", keywords, &pyList, &pyColors, &pyCount)) {
		return NULL;
	}

	rectToken = PyObjC_PythonToCArray(
		@encode(NSRect), pyList, pyCount, (void**)&rects, &rectCount);

	if (rectToken == -1) return NULL;

	colorToken = PyObjC_PythonToCArray(
		@encode(id), pyColors, pyCount, (void**)&colors, &colorCount);

	if (colorToken == -1)  {
		PyObjC_FreeCArray(rectToken, rects);
		return NULL;
	}

	if (colorCount != rectCount) {
		PyErr_Format(PyExc_ValueError,
				"Passing %d rects and %d colors",
				rectCount, colorCount);
		PyObjC_FreeCArray(rectToken, rects);
		PyObjC_FreeCArray(colorToken, colors);
		return NULL;
	}
		

	NS_DURING
		NSRectFillListWithColors(rects, colors, rectCount);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	PyObjC_FreeCArray(rectToken, rects);
	PyObjC_FreeCArray(colorToken, colors);

	if (PyErr_Occurred()) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None; 
}

static PyObject*
objc_NSRectFillListWithColorsUsingOperation(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static char* keywords[] = { "rects", "colors", "count", "operation", 0 };
	PyObject* pyList;
	PyObject* pyColors;
	PyObject* pyCount = NULL;
	NSRect* rects;
	id* colors;
	int rectCount;
	int colorCount;
	int rectToken;
	int colorToken;
	NSCompositingOperation operation;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "OOOO&", keywords, &pyList, &pyColors, &pyCount, Convert_NSCompositingOperation, &operation)) {
		return NULL;
	}

	rectToken = PyObjC_PythonToCArray(
		@encode(NSRect), pyList, pyCount, (void**)&rects, &rectCount);

	if (rectToken == -1) return NULL;

	colorToken = PyObjC_PythonToCArray(
		@encode(id), pyColors, pyCount, (void**)&colors, &colorCount);

	if (colorToken == -1)  {
		PyObjC_FreeCArray(rectToken, rects);
		return NULL;
	}

	if (colorCount != rectCount) {
		PyErr_Format(PyExc_ValueError,
				"Passing %d rects and %d colors",
				rectCount, colorCount);
		PyObjC_FreeCArray(rectToken, rects);
		PyObjC_FreeCArray(colorToken, colors);
		return NULL;
	}
		

	NS_DURING
		NSRectFillListWithColorsUsingOperation(rects, colors, rectCount, operation);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	PyObjC_FreeCArray(rectToken, rects);
	PyObjC_FreeCArray(colorToken, colors);

	if (PyErr_Occurred()) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None; 
}

static PyObject*
objc_NSRectFillListWithGrays(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static char* keywords[] = { "rects", "grays", "count", 0 };
	PyObject* pyList;
	PyObject* pyGrays;
	PyObject* pyCount = NULL;
	NSRect* rects;
	float* grays;
	int rectCount;
	int grayCount;
	int rectToken;
	int grayToken;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "OO|O", keywords, &pyList, &pyGrays, &pyCount)) {
		return NULL;
	}

	rectToken = PyObjC_PythonToCArray(
		@encode(NSRect), pyList, pyCount, (void**)&rects, &rectCount);

	if (rectToken == -1) return NULL;

	grayToken = PyObjC_PythonToCArray(
		@encode(float), pyGrays, pyCount, (void**)&grays, &grayCount);

	if (grayToken == -1)  {
		PyObjC_FreeCArray(rectToken, rects);
		return NULL;
	}

	if (grayCount != rectCount) {
		PyErr_Format(PyExc_ValueError,
				"Passing %d rects and %d colors",
				rectCount, grayCount);
		PyObjC_FreeCArray(rectToken, rects);
		PyObjC_FreeCArray(grayToken, grays);
		return NULL;
	}
		

	NS_DURING
		NSRectFillListWithGrays(rects, grays, rectCount);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	PyObjC_FreeCArray(rectToken, rects);
	PyObjC_FreeCArray(grayToken, grays);

	if (PyErr_Occurred()) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None; 
}

static PyObject*
objc_NSDrawTiledRects(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static char* keywords[] = { "boundsRect", "clipRect", "sides", "grays", "count", 0 };
	PyObject* pyBounds;
	PyObject* pyClip;
	PyObject* pySides;
	PyObject* pyGrays;
	PyObject* pyCount = NULL;
	NSRect boundsRect;
	NSRect clipRect;
	NSRectEdge* sides;
	float* grays;
	int sidesCount;
	int graysCount;
	int sidesToken;
	int graysToken;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "OOOO|O", keywords, &pyBounds, &pyClip, &pySides, &pyGrays, &pyCount)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(NSRect), pyBounds, &boundsRect) == -1) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(NSRect), pyClip, &clipRect) == -1) {
		return NULL;
	}

	sidesToken = PyObjC_PythonToCArray(
		@encode(NSRectEdge), pySides, pyCount, (void**)&sides, &sidesCount);

	if (sidesToken == -1) return NULL;

	graysToken = PyObjC_PythonToCArray(
		@encode(id), pyGrays, pyCount, (void**)&grays, &graysCount);

	if (graysToken == -1)  {
		PyObjC_FreeCArray(sidesToken, sides);
		return NULL;
	}

	if (graysCount != sidesCount) {
		PyErr_Format(PyExc_ValueError,
				"Passing %d sides and %d grays",
				sidesCount, graysCount);
		PyObjC_FreeCArray(sidesToken, sides);
		PyObjC_FreeCArray(graysToken, grays);
		return NULL;
	}
		

	NS_DURING
		NSDrawTiledRects(boundsRect, clipRect, sides, grays, sidesCount);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	PyObjC_FreeCArray(sidesToken, sides);
	PyObjC_FreeCArray(graysToken, grays);

	if (PyErr_Occurred()) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None; 
}

static PyObject*
objc_NSDrawColorTiledRects(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static char* keywords[] = { "boundsRect", "clipRect", "sides", "grays", "count", 0 };
	PyObject* pyBounds;
	PyObject* pyClip;
	PyObject* pySides;
	PyObject* pyColors;
	PyObject* pyCount = NULL;
	NSRect boundsRect;
	NSRect clipRect;
	NSRectEdge* sides;
	id* colors;
	int sidesCount;
	int colorsCount;
	int sidesToken;
	int colorsToken;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "OOOO|O", keywords, &pyBounds, &pyClip, &pySides, &pyColors, &pyCount)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(NSRect), pyBounds, &boundsRect) == -1) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(NSRect), pyClip, &clipRect) == -1) {
		return NULL;
	}

	sidesToken = PyObjC_PythonToCArray(
		@encode(NSRectEdge), pySides, pyCount, (void**)&sides, &sidesCount);

	if (sidesToken == -1) return NULL;

	colorsToken = PyObjC_PythonToCArray(
		@encode(id), pyColors, pyCount, (void**)&colors, &colorsCount);

	if (colorsToken == -1)  {
		PyObjC_FreeCArray(sidesToken, sides);
		return NULL;
	}

	if (colorsCount != sidesCount) {
		PyErr_Format(PyExc_ValueError,
				"Passing %d sides and %d colors",
				sidesCount, colorsCount);
		PyObjC_FreeCArray(sidesToken, sides);
		PyObjC_FreeCArray(colorsToken, colors);
		return NULL;
	}
		

	NS_DURING
		NSDrawColorTiledRects(boundsRect, clipRect, sides, colors, sidesCount);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	PyObjC_FreeCArray(sidesToken, sides);
	PyObjC_FreeCArray(colorsToken, colors);

	if (PyErr_Occurred()) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None; 
}

static PyObject* 
objc_NSWindowListForContext(
	PyObject* self __attribute__((__unused__)),
	PyObject* args,
	PyObject* kwds)
{
	static char* keywords[] = { "context", "count", NULL };
	int context;
	int size;
	int* list;
	PyObject* result;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "ii", keywords, &context, &size)) {
		return NULL;
	}

	list = malloc(sizeof(int)*size);
	if (list == NULL) {
		PyErr_NoMemory();
		return 0;
	}
	memset(list, 0, sizeof(int)*size);

	NS_DURING
		NSWindowListForContext(context, size, list);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	if (PyErr_Occurred()) {
		free(list);
		return NULL;
	}

	result = PyObjC_CArrayToPython(@encode(int), list, size);
	free(list);
	return result;
}

static PyObject* 
objc_NSWindowList(
	PyObject* self __attribute__((__unused__)),
	PyObject* args,
	PyObject* kwds)
{
	static char* keywords[] = { "count", NULL };
	int size;
	int* list;
	PyObject* result;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "i", keywords, &size)) {
		return NULL;
	}

	list = malloc(sizeof(int)*size);
	if (list == NULL) {
		PyErr_NoMemory();
		return 0;
	}
	memset(list, 0, sizeof(int)*size);

	NS_DURING
		NSWindowList(size, list);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	if (PyErr_Occurred()) {
		free(list);
		return NULL;
	}

	result = PyObjC_CArrayToPython(@encode(int), list, size);
	free(list);
	return result;
}

static PyObject* 
objc_NSAvailableWindowDepths(
	PyObject* self __attribute__((__unused__)),
	PyObject* args,
	PyObject* kwds)
{
	static char* keywords[] = { NULL };
	int size;
	const int* list;
	PyObject* result;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "", keywords)) {
		return NULL;
	}

	NS_DURING
		list = NSAvailableWindowDepths();
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		list = NULL;
	NS_ENDHANDLER

	if (list == NULL && PyErr_Occurred()) {
		return NULL;
	}
	size = 0;
	if (list != NULL) {
		for (size=0; list[size] != 0; size++) ;
		size ++;
	}

	result = PyObjC_CArrayToPython(@encode(int), (int*)list, size);
	return result;
}

static PyObject* 
objc_NSBestDepth(
	PyObject* self __attribute__((__unused__)),
	PyObject* args,
	PyObject* kwds)
{
	static char* keywords[] = { "colorSpace", "bps", "bpp", "planar" };
	PyObject* pyColorSpace;
	id colorSpace;
	int bps;
	int bpp;
	PyObject* pyPlanar;
	BOOL planarVal; // planar is a global symbol??
	BOOL exactMatch;
	NSWindowDepth bestDepth;
	PyObject* result;
	PyObject* v;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "OiiO", keywords, &pyColorSpace, &bps, &bpp, &pyPlanar)) {
		return NULL;
	}
	
	colorSpace = PyObjC_PythonToId(pyColorSpace);
	planarVal = PyObject_IsTrue(pyPlanar);

	NS_DURING
		bestDepth = NSBestDepth(colorSpace, bps, bpp, planarVal, &exactMatch);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	result = PyTuple_New(2);
	if (result == NULL) return NULL;

	v = PyObjC_ObjCToPython(@encode(NSWindowDepth), &bestDepth);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	PyTuple_SET_ITEM(result, 0, v);

	v = PyObjCBool_FromLong(exactMatch);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	PyTuple_SET_ITEM(result, 1, v);

	return result;
}

static PyObject* 
objc_NSRectClipList(
	PyObject* self __attribute__((__unused__)),
	PyObject* args,
	PyObject* kwds)
{
	static char* keywords[] = { "rects", "count", NULL };
	PyObject* pyList;
	PyObject* pyCount = NULL;
	NSRect* rects;
	int count;
	int arrayToken;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O|O", keywords, &pyList, &pyCount)) {
		return NULL;
	}

	arrayToken = PyObjC_PythonToCArray(
		@encode(NSRect), pyList, pyCount, (void**)&rects, &count);
	if (arrayToken == -1) return NULL;

	NS_DURING
		NSRectClipList(rects, count);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	PyObjC_FreeCArray(arrayToken, rects);

	if (PyErr_Occurred()) return NULL;

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject*
objc_NSGetWindowServerMemory(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static char* keywords[] = { "context", "windowDumpStream", NULL };
	int context;
	int virtualMemory = 0;
	int doDumpStream;
	int res;
	int windowBackingMemory = 0;
	NSString* windowDumpStream = NULL;
	PyObject* result;
	PyObject* v;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "ii:NSGetWindowServerMemory", keywords, &context, &doDumpStream)) {
		return NULL;
	}

	NS_DURING
		if (doDumpStream) {
			res = NSGetWindowServerMemory(
				context, &virtualMemory, &windowBackingMemory,
				&windowDumpStream);
		} else {
			res = NSGetWindowServerMemory(
				context, &virtualMemory, &windowBackingMemory,
				NULL);
		}

	NS_HANDLER
		res = 0;
		PyObjCErr_FromObjC(localException);

	NS_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	result = PyTuple_New(4);
	if (result == NULL) return NULL;

	v = PyInt_FromLong(res);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	PyTuple_SET_ITEM(result, 0, v);

	v = PyInt_FromLong(virtualMemory);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	PyTuple_SET_ITEM(result, 1, v);

	v = PyInt_FromLong(windowBackingMemory);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	PyTuple_SET_ITEM(result, 2, v);

	v = PyObjC_IdToPython(windowDumpStream);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	PyTuple_SET_ITEM(result, 3, v);

	return result;
}

#ifdef GNUSTEP
#include "_App_Functions.GNUstep.inc"

#else /* !GNUSTEP */

#include "_App_Functions.inc"

#endif /* !GNUSTEP */

static PyMethodDef appkit_methods[] = {
	{ 
		"NSApplicationMain", 
		(PyCFunction)objc_NSApplicationMain, 
		METH_VARARGS|METH_KEYWORDS, 
		"int NSApplicationMain(int argc, const char *argv[]);"
	},
	{ 
		"NSApp", 
		(PyCFunction)objc_NSApp, 
		METH_VARARGS|METH_KEYWORDS, 
		"NSApplication* NSApp(void);"
	},
	{ 
		"NSCountWindows", 
		(PyCFunction)objc_NSCountWindows, 
		METH_VARARGS|METH_KEYWORDS, 
		"void NSCountWindows(int *count);"
	},
	{ 
		"NSWindowList", 
		(PyCFunction)objc_NSWindowList, 
		METH_VARARGS|METH_KEYWORDS, 
		"void NSWindowList(int size, int list[]);"
	},
	{ 
		"NSWindowListForContext", 
		(PyCFunction)objc_NSWindowListForContext, 
		METH_VARARGS|METH_KEYWORDS, 
		"void NSWindowListForContext(int context, int size, int list[]);"
	},
	{ 
		"NSCountWindowsForContext", 
		(PyCFunction)objc_NSCountWindowsForContext, 
		METH_VARARGS|METH_KEYWORDS, 
		"void NSCountWindowsForContext(int context, int *count);"
	},
	{
	        "NSRectFillList",
		(PyCFunction)objc_NSRectFillList,
		METH_VARARGS,
		"void NSRectFillList(const NSRect *rects, int count);"
	},
	{
	        "NSBestDepth",
		(PyCFunction)objc_NSBestDepth,
		METH_VARARGS,
		"NSWindowDepth NSBestDepth(NSString *colorSpace, int bps, int bpp, BOOL planar, BOOL *exactMatch);"
	},
	{
	        "NSAvailableWindowDepths",
		(PyCFunction)objc_NSAvailableWindowDepths,
		METH_VARARGS,
		"int* NSAvailableWindowDepths(void);"
	},
	{
	        "NSRectClipList",
		(PyCFunction)objc_NSRectClipList,
		METH_VARARGS,
		"void NSRectClipList(const NSRect *rects, int count);"
	},
	{
	        "NSDrawTiledRects",
		(PyCFunction)objc_NSDrawTiledRects,
		METH_VARARGS,
		"void NSDrawTiledRects(NSRect boundsRect, NSRect clipRect, const NSRectEdge* sides, const float* grays, int count);"
	},
	{
	        "NSDrawColorTiledRects",
		(PyCFunction)objc_NSDrawColorTiledRects,
		METH_VARARGS,
		"void NSDrawColorTiledRects(NSRect boundsRect, NSRect clipRect, const NSRectEdge* sides, const NSColor** colors, int count);"
	},
	{
	        "NSRectFillListWithColors",
		(PyCFunction)objc_NSRectFillListWithColors,
		METH_VARARGS,
		"void NSRectFillListWithColors(const NSRect *rects, NSColor **colors, int count);"
	},
	{
	        "NSRectFillListWithColorsUsingOperation",
		(PyCFunction)objc_NSRectFillListWithColorsUsingOperation,
		METH_VARARGS,
		"void NSRectFillListWithColorsUsingOperation(const NSRect *rects, NSColor **colors, int count, NSCompositingOperation op)"
	},
	{
	        "NSRectFillListWithGrays",
		(PyCFunction)objc_NSRectFillListWithGrays,
		METH_VARARGS,
		"void NSRectFillListWithGrays(const NSRect *rects, const float *grays, int count);"
	},
	{
	        "NSRectFillListUsingOperation",
		(PyCFunction)objc_NSRectFillListUsingOperation,
		METH_VARARGS,
		"void NSRectFillListUsingOperation(const NSRect *rects, int count, NSCompositingOperation op);"
	},
	{
		"NSGetWindowServerMemory",
		(PyCFunction)objc_NSGetWindowServerMemory,
		METH_VARARGS,
		"int NSGetWindowServerMemory(int context, int *virtualMemory, int *windowBackingMemory, NSString **windowDumpString);"
	},

	METHOD_TABLE_ENTRIES

	{ 0, 0, 0, 0 } /* sentinel */
};

PyDoc_STRVAR(appkit_doc,
"AppKit._AppKit defines constants, types and global functions used by "
"AppKit"
);

#include "_App_Enum.inc"
#include "_App_Str.inc"

/*
 * Manually added, will be automatic in next version of generator script
 */
struct uchar_table {
	char*       name;
	Py_UNICODE  value;
} g_unicode_characters[] = {
    { "NSUpArrowFunctionKey", NSUpArrowFunctionKey },
    { "NSDownArrowFunctionKey", NSDownArrowFunctionKey },
    { "NSLeftArrowFunctionKey", NSLeftArrowFunctionKey },
    { "NSRightArrowFunctionKey", NSRightArrowFunctionKey },
    { "NSF1FunctionKey", NSF1FunctionKey },
    { "NSF2FunctionKey", NSF2FunctionKey },
    { "NSF3FunctionKey", NSF3FunctionKey },
    { "NSF4FunctionKey", NSF4FunctionKey },
    { "NSF5FunctionKey", NSF5FunctionKey },
    { "NSF6FunctionKey", NSF6FunctionKey },
    { "NSF7FunctionKey", NSF7FunctionKey },
    { "NSF8FunctionKey", NSF8FunctionKey },
    { "NSF9FunctionKey", NSF9FunctionKey },
    { "NSF10FunctionKey", NSF10FunctionKey },
    { "NSF11FunctionKey", NSF11FunctionKey },
    { "NSF12FunctionKey", NSF12FunctionKey },
    { "NSF13FunctionKey", NSF13FunctionKey },
    { "NSF14FunctionKey", NSF14FunctionKey },
    { "NSF15FunctionKey", NSF15FunctionKey },
    { "NSF16FunctionKey", NSF16FunctionKey },
    { "NSF17FunctionKey", NSF17FunctionKey },
    { "NSF18FunctionKey", NSF18FunctionKey },
    { "NSF19FunctionKey", NSF19FunctionKey },
    { "NSF20FunctionKey", NSF20FunctionKey },
    { "NSF21FunctionKey", NSF21FunctionKey },
    { "NSF22FunctionKey", NSF22FunctionKey },
    { "NSF23FunctionKey", NSF23FunctionKey },
    { "NSF24FunctionKey", NSF24FunctionKey },
    { "NSF25FunctionKey", NSF25FunctionKey },
    { "NSF26FunctionKey", NSF26FunctionKey },
    { "NSF27FunctionKey", NSF27FunctionKey },
    { "NSF28FunctionKey", NSF28FunctionKey },
    { "NSF29FunctionKey", NSF29FunctionKey },
    { "NSF30FunctionKey", NSF30FunctionKey },
    { "NSF31FunctionKey", NSF31FunctionKey },
    { "NSF32FunctionKey", NSF32FunctionKey },
    { "NSF33FunctionKey", NSF33FunctionKey },
    { "NSF34FunctionKey", NSF34FunctionKey },
    { "NSF35FunctionKey", NSF35FunctionKey },
    { "NSInsertFunctionKey", NSInsertFunctionKey },
    { "NSDeleteFunctionKey", NSDeleteFunctionKey },
    { "NSHomeFunctionKey", NSHomeFunctionKey },
    { "NSBeginFunctionKey", NSBeginFunctionKey },
    { "NSEndFunctionKey", NSEndFunctionKey },
    { "NSPageUpFunctionKey", NSPageUpFunctionKey },
    { "NSPageDownFunctionKey", NSPageDownFunctionKey },
    { "NSPrintScreenFunctionKey", NSPrintScreenFunctionKey },
    { "NSScrollLockFunctionKey", NSScrollLockFunctionKey },
    { "NSPauseFunctionKey", NSPauseFunctionKey },
    { "NSSysReqFunctionKey", NSSysReqFunctionKey },
    { "NSBreakFunctionKey", NSBreakFunctionKey },
    { "NSResetFunctionKey", NSResetFunctionKey },
    { "NSStopFunctionKey", NSStopFunctionKey },
    { "NSMenuFunctionKey", NSMenuFunctionKey },
    { "NSUserFunctionKey", NSUserFunctionKey },
    { "NSSystemFunctionKey", NSSystemFunctionKey },
    { "NSPrintFunctionKey", NSPrintFunctionKey },
    { "NSClearLineFunctionKey", NSClearLineFunctionKey },
    { "NSClearDisplayFunctionKey", NSClearDisplayFunctionKey },
    { "NSInsertLineFunctionKey", NSInsertLineFunctionKey },
    { "NSDeleteLineFunctionKey", NSDeleteLineFunctionKey },
    { "NSInsertCharFunctionKey", NSInsertCharFunctionKey },
    { "NSDeleteCharFunctionKey", NSDeleteCharFunctionKey },
    { "NSPrevFunctionKey", NSPrevFunctionKey },
    { "NSNextFunctionKey", NSNextFunctionKey },
    { "NSSelectFunctionKey", NSSelectFunctionKey },
    { "NSExecuteFunctionKey", NSExecuteFunctionKey },
    { "NSUndoFunctionKey", NSUndoFunctionKey },
    { "NSRedoFunctionKey", NSRedoFunctionKey },
    { "NSFindFunctionKey", NSFindFunctionKey },
    { "NSHelpFunctionKey", NSHelpFunctionKey },
    { "NSModeSwitchFunctionKey", NSModeSwitchFunctionKey },
    { NULL, 0 }
};


static int 
fontMatrix(PyObject* d, const char* name, const float* value)
{
	int i;

	if (value == NULL) {
		return PyDict_SetItemString(d, (char*)name, Py_None);
	}
	PyObject* v = PyTuple_New(6);
	if (v == NULL) {
		return -1;
	}

	for (i = 0; i < 6; i++) {
		PyObject* t;

		t = PyFloat_FromDouble(value[i]);
		if (t == NULL) {
			Py_DECREF(v);
			return -1;
		}
	}
	
	if (PyDict_SetItemString(d, (char*)name, v) == -1) {
		Py_DECREF(v);
		return -1;
	}
	Py_DECREF(v);
	return 0;
}

#include "_AppKitMapping_NSApplication.m"
#include "_AppKitMapping_NSATSTypeSetter.m"
#include "_AppKitMapping_NSBezierPath.m"
#include "_AppKitMapping_NSBitmap.m"
#include "_AppKitMapping_NSBitmapImageRep.m"
#include "_AppKitMapping_NSFont.m"
#include "_AppKitMapping_NSGraphicsContext.m"
#include "_AppKitMapping_NSLayoutManager.m"
#include "_AppKitMapping_NSMatrix.m"
#include "_AppKitMapping_NSMovie.m"
#include "_AppKitMapping_NSOpenGLContext.m"
#include "_AppKitMapping_NSOpenGLPixelFormat.m"
#include "_AppKitMapping_NSQuickDrawView.m"
#include "_AppKitMapping_NSSimpleHorizontalTypesetter.m"
#include "_AppKitMapping_NSView.m"
#include "_AppKitMapping_NSWindow.m"

static const char* NSAffineTransformStruct_name = "AppKit.NSAffineTransformStruct";
static const char* NSAffineTransformStruct_doc = "struct NSAffineTransformStruct (m11, m12, m21, m22, tX, tY)";
static const char* NSAffineTransformStruct_fields[] = {
	"m11",
	"m12",
	"m21",
	"m22",
	"tX",
	"tY"
};

void init_AppKit(void);

void init_AppKit(void)
{
	PyObject *m, *d, *v;
	CFBundleRef bundle;

	m = Py_InitModule4("_AppKit", appkit_methods, appkit_doc, 
		NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

	bundle = CFBundleCreate(NULL,
		(CFURLRef)[NSURL fileURLWithPath:@"/System/Library/Frameworks/AppKit.framework"]);

	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, (sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;

	//CFRelease(bundle);

#ifdef GNUSTEP

#	include "_App_Var.GNUstep.inc"

#else /* !GNUSTEP */

#	include "_App_Var.inc"

#endif /* !GNUSTEP */

	/* And some troublesome definitions 
	 * All of these found by 'grep #define *.h' in the AppKit header 
	 * directory
	 */

#ifndef GNUSTEP
	/* NSOpenGL.h */
	add_int(d, "NSOPENGL_CURRENT_VERSION", NSOPENGL_CURRENT_VERSION);

	/* NSStatusBar.h */
	add_int(d, "NSVariableStatusItemLength", NSVariableStatusItemLength);
	add_int(d, "NSSquareStatusItemLength", NSSquareStatusItemLength);

	/* NSTypesetter.h */
	add_int(d, "NSBaselineNotSet", NSBaselineNotSet);
	add_int(d, "NumGlyphsToGetEachTime", NumGlyphsToGetEachTime);
#endif

	/* NSWindow.h */
	add_int(d, "NSNormalWindowLevel", NSNormalWindowLevel);
	add_int(d, "NSFloatingWindowLevel", NSFloatingWindowLevel);
	add_int(d, "NSSubmenuWindowLevel", NSSubmenuWindowLevel);
	add_int(d, "NSTornOffMenuWindowLevel", NSTornOffMenuWindowLevel);
	add_int(d, "NSMainMenuWindowLevel", NSMainMenuWindowLevel);
	add_int(d, "NSStatusWindowLevel", NSStatusWindowLevel);
	add_int(d, "NSModalPanelWindowLevel", NSModalPanelWindowLevel);
	add_int(d, "NSPopUpMenuWindowLevel", NSPopUpMenuWindowLevel);
	add_int(d, "NSScreenSaverWindowLevel", NSScreenSaverWindowLevel);

	{
	  struct uchar_table*  cur = g_unicode_characters;
	  int       res;

	  for (; cur->name != NULL; cur++) {
		  v = PyUnicode_FromUnicode(&cur->value, 1);
		  if (v == NULL) return;

	          res = PyDict_SetItemString(d, cur->name, v);
	          if (res < 0) return;
	  }
	}

	/* Some special constants */
	fontMatrix(d, "NSFontIdentityMatrix", NSFontIdentityMatrix);

	/* Struct definitions */
	v = PyObjC_RegisterStructType(@encode(NSAffineTransformStruct),
			NSAffineTransformStruct_name, 
			NSAffineTransformStruct_doc, 
			NULL,
			6, NSAffineTransformStruct_fields);
	if (v == NULL) return;
	PyDict_SetItemString(d, "NSAffineTransformStruct", v);
	Py_DECREF(v);

	/* TODO: NSTypesetterGlyphInfo */

	/* register other method mappings */
	if (_pyobjc_install_NSApplication() < 0) return;
	if (_pyobjc_install_NSATSTypesetter() < 0) return;
	if (_pyobjc_install_NSBezierPath() < 0) return;
	if (_pyobjc_install_NSBitmap() < 0) return;
	if (_pyobjc_install_NSBitmapImageRep() < 0) return;
	if (_pyobjc_install_NSFont() < 0) return;
	if (_pyobjc_install_NSGraphicsContext() < 0) return;
	if (_pyobjc_install_NSLayoutManager() < 0) return;
	if (_pyobjc_install_NSMatrix() < 0) return;
	if (_pyobjc_install_NSMovie() < 0) return;
	if (_pyobjc_install_NSOpenGLContext() < 0) return;
	if (_pyobjc_install_NSOpenGLPixelFormat() < 0) return;
	if (_pyobjc_install_NSQuickDrawView() < 0) return;
	if (_pyobjc_install_NSSimpleHorizontalTypesetter() < 0) return;
	if (_pyobjc_install_NSView() < 0) return;
	if (_pyobjc_install_NSWindow() < 0) return;
}
