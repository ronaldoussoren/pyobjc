/*
 * Mapping of static items in the AppKit kit:
 * 
 * - constants  (mostly done)
 * - data types (TODO)
 * - enumerations
 * - exceptions 
 * - global functions (TODO)
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
objc_NSApplicationMain(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
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
objc_NSApp(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
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
objc_NSCountWindows(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
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
objc_NSCountWindowsForContext(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
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
objc_NSAvailableWindowDepths(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static  char* keywords[] = { NULL };
	const NSWindowDepth*	  depths;
	PyObject *result, *tmp;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, ":NSAvailableWindowDepts", keywords)) {
		return NULL;
	}

	NS_DURING
		depths = NSAvailableWindowDepths();
	NS_HANDLER
		depths = NULL;
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER
	if (PyErr_Occurred()) return NULL;

	result = PyList_New(0);
	if (result == NULL) return NULL;

	while (*depths != 0) {
		PyObject* v = PyInt_FromLong(*depths);
		if (v == NULL) {
			Py_DECREF(result);
			return NULL;
		}

		if (PyList_Append(result, v) == -1) {
			Py_DECREF(result);
			return NULL;
		}

		depths++;
	}

	tmp = PyList_AsTuple(result);
	Py_XDECREF(result);
	return tmp;
}


static PyObject*
compat_NSRectFillList(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "bytes", "count", 0 };
	unsigned char *rectBytes;
	int rectByteLength;
	int rectCount = -1;
	if  (!PyArg_ParseTupleAndKeywords(args, kwds, "s#i", keywords, &rectBytes, &rectByteLength, &rectCount)) {
		return NULL;
	}

	if ( (rectByteLength == 0) || (rectCount == 0) ) {
		Py_INCREF(Py_None);
		return Py_None; 
	}

	if ( rectByteLength % sizeof(NSRect) ) {
		PyErr_SetString(PyExc_ValueError, "length of array of packed floats is not a multiple of a length of array of NSRect (float * 4).");
		return NULL;
	}

	if (rectCount < -1 ) {
		PyErr_SetString(PyExc_ValueError, "RectCount was less than zero.");
		return NULL;
	}
        

	if (rectCount >= 0 ) {
		if ((size_t)rectCount > (rectByteLength / sizeof(NSRect))) {
                    PyErr_SetString(PyExc_ValueError, 
				"Rect count specified, but was longer than supplied array of rectangles.");
			return NULL;
		}
	} else {
		rectCount = rectByteLength / sizeof(NSRect);
	}

	NSRectFillList((NSRect *) rectBytes, rectCount);

	Py_INCREF(Py_None);
	return Py_None; 
}

static PyObject*
objc_NSRectFillList(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "rects", "count", 0 };
	NSRect* rects;
	PyObject* rectList;
	PyObject* seq;
	int i, len;
	int rectCount;

	{
		/* Upto PyObjC 1.0b2 compat_NSRectFillList was the wrapper for NSRectFillList
		 * this implementation is not consistant w.r.t. the rest of the bridge and
		 * therefore depricated.
		 */
		char* s1; 
		int i1, i2;
                static char* klist[] = { "bytes", "count", 0 };

		if  (PyArg_ParseTupleAndKeywords(args, kwds, "s#i", klist, &s1, &i1, &i2)) {
			return compat_NSRectFillList(self, args, kwds);
		}
		PyErr_Clear();
	}

	if  (!PyArg_ParseTupleAndKeywords(args, kwds, "Oi", keywords, &rectList, &rectCount)) {
		return NULL;
	}

	seq = PySequence_Fast(rectList, "expecting a list of NSRect objects");
	if (seq == NULL) {
		return NULL;
	}
	Py_DECREF(rectList);

	if (PySequence_Fast_GET_SIZE(seq) < rectCount) {
		Py_DECREF(seq);
		PyErr_SetString(PyExc_ValueError, "too few rects");
		return NULL;
	}


	if (rectCount < -1 ) {
		Py_DECREF(seq);
		PyErr_SetString(PyExc_ValueError, "RectCount was less than zero.");
		return NULL;
	}

#warning The (*4) in the following is bogus.   Without it, we crash with what appears to be corrupted memory.  I don't know why but figure that not crashing is preferable to crashing until one of us has time to figure this out.  Really,  I suspect Ronald will take one look at this and, being about 10x brighter than me at this sort of thing, will know exactly what is wrong...  :-)
	rects = malloc((rectCount * sizeof(NSRect)) * 4);
	if (rects == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	len = PySequence_Fast_GET_SIZE(seq);
	for (i = 0; i < len; i++) {
		PyObject* v = PySequence_Fast_GET_ITEM(seq, i);
		int r  = PyObjC_PythonToObjC(@encode(NSRect), v, rects + i);
		if (r == -1) {
			Py_DECREF(seq);
			return NULL;
		}
	}

	NSRectFillList(rects, rectCount);

	free(rects);

	Py_INCREF(Py_None);
	return Py_None; 
}

static PyObject*
objc_NSGetWindowServerMemory(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
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
		NULL
	},
	{ 
		"NSApp", 
		(PyCFunction)objc_NSApp, 
		METH_VARARGS|METH_KEYWORDS, 
		NULL
	},
	{ 
		"NSCountWindows", 
		(PyCFunction)objc_NSCountWindows, 
		METH_VARARGS|METH_KEYWORDS, 
		NULL
	},
	{ 
		"NSCountWindowsForContext", 
		(PyCFunction)objc_NSCountWindowsForContext, 
		METH_VARARGS|METH_KEYWORDS, 
		NULL
	},
	{
	        "NSRectFillList",
		(PyCFunction)objc_NSRectFillList,
		METH_VARARGS,
		NULL
	},
	{
	        "NSAvailableWindowDepths",
		(PyCFunction)objc_NSAvailableWindowDepths,
		METH_VARARGS,
		NULL
	},
	{
		"NSGetWindowServerMemory",
		(PyCFunction)objc_NSGetWindowServerMemory,
		METH_VARARGS,
		NULL
	},

	METHOD_TABLE_ENTRIES

	{ 0, 0, 0, 0 } /* sentinel */
};

PyDoc_STRVAR(appkit_doc,
"Cocoa._Foundation defines constants, types and global functions used by "
"Cocoa.Foundation."
);


/* TODO:
 * actual variables: 
 * - NSApp
 *
 * floats:
 NSColor-Grayscale Values

 const float NSWhite;
 const float NSLightGray;
 const float NSDarkGray;
 const float NSBlack;

 NSFont-PostScript Transformation Matrix

 const float *NSFontIdentityMatrix;

 Discussion

 NSFontIdentityMatrix is a transformation matrix useful as a parameter to the NSFont method fontWithName:matrix: .

 NSWindow-Sizes

 NSSize NSIconSize;
 NSSize NSTokenSize;


 */


#ifdef GNUSTEP

#include "_App_Enum.GNUstep.inc"
#include "_App_Str.GNUstep.inc"

#else /* !GNUSTEP */

#include "_App_Enum.inc"
#include "_App_Str.inc"

#endif /* !GNUSTEP */

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
		return PyDict_SetItemString(d, name, Py_None);
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
	
	if (PyDict_SetItemString(d, name, v) == -1) {
		Py_DECREF(v);
		return -1;
	}
	Py_DECREF(v);
	return 0;
}


void init_AppKit(void);

void init_AppKit(void)
{
	PyObject *m, *d;
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


	add_int(d, "NSNoCellMask", NSNoCellMask);
	add_int(d, "NSContentsCellMask", NSContentsCellMask);
	add_int(d, "NSPushInCellMask", NSPushInCellMask);
	add_int(d, "NSChangeGrayCellMask", NSChangeGrayCellMask);
	add_int(d, "NSChangeBackgroundCellMask", NSChangeBackgroundCellMask);
	add_int(d, "NSColorPanelGrayModeMask", NSColorPanelGrayModeMask);
	add_int(d, "NSColorPanelRGBModeMask", NSColorPanelRGBModeMask);
	add_int(d, "NSColorPanelCMYKModeMask", NSColorPanelCMYKModeMask);
	add_int(d, "NSColorPanelHSBModeMask", NSColorPanelHSBModeMask);
	add_int(d, "NSColorPanelCustomPaletteModeMask", NSColorPanelCustomPaletteModeMask);
	add_int(d, "NSColorPanelColorListModeMask", NSColorPanelColorListModeMask);
	add_int(d, "NSColorPanelWheelModeMask", NSColorPanelWheelModeMask);
#ifndef GNUSTEP
#if MAC_OS_X_VERSION_10_2 <= MAC_OS_X_VERSION_MAX_ALLOWED
	add_int(d, "NSColorPanelCrayonModeMask", NSColorPanelCrayonModeMask);
#endif
#endif
	add_int(d, "NSColorPanelAllModesMask", NSColorPanelAllModesMask);
	add_int(d, "NSLeftMouseDownMask", NSLeftMouseDownMask);
	add_int(d, "NSLeftMouseUpMask", NSLeftMouseUpMask);
	add_int(d, "NSRightMouseDownMask", NSRightMouseDownMask);
	add_int(d, "NSRightMouseUpMask", NSRightMouseUpMask);
	add_int(d, "NSMouseMovedMask", NSMouseMovedMask);
	add_int(d, "NSLeftMouseDraggedMask", NSLeftMouseDraggedMask);
	add_int(d, "NSRightMouseDraggedMask", NSRightMouseDraggedMask);
	add_int(d, "NSMouseEnteredMask", NSMouseEnteredMask);
	add_int(d, "NSMouseExitedMask", NSMouseExitedMask);
	add_int(d, "NSKeyDownMask", NSKeyDownMask);
	add_int(d, "NSKeyUpMask", NSKeyUpMask);
	add_int(d, "NSFlagsChangedMask", NSFlagsChangedMask);
	add_int(d, "NSAppKitDefinedMask", NSAppKitDefinedMask);
	add_int(d, "NSSystemDefinedMask", NSSystemDefinedMask);
	add_int(d, "NSApplicationDefinedMask", NSApplicationDefinedMask);
	add_int(d, "NSPeriodicMask", NSPeriodicMask);
	add_int(d, "NSCursorUpdateMask", NSCursorUpdateMask);
	add_int(d, "NSScrollWheelMask", NSScrollWheelMask);
	add_int(d, "NSOtherMouseDownMask", NSOtherMouseDownMask);
	add_int(d, "NSOtherMouseUpMask", NSOtherMouseUpMask);
	add_int(d, "NSOtherMouseDraggedMask", NSOtherMouseDraggedMask);
	add_int(d, "NSAnyEventMask", NSAnyEventMask);
	add_int(d, "NSAlphaShiftKeyMask", NSAlphaShiftKeyMask);
	add_int(d, "NSShiftKeyMask", NSShiftKeyMask);
	add_int(d, "NSControlKeyMask", NSControlKeyMask);
	add_int(d, "NSAlternateKeyMask", NSAlternateKeyMask);
	add_int(d, "NSCommandKeyMask", NSCommandKeyMask);
	add_int(d, "NSNumericPadKeyMask", NSNumericPadKeyMask);
	add_int(d, "NSHelpKeyMask", NSHelpKeyMask);
	add_int(d, "NSFunctionKeyMask", NSFunctionKeyMask);
	add_int(d, "NSItalicFontMask", NSItalicFontMask);
	add_int(d, "NSBoldFontMask", NSBoldFontMask);
	add_int(d, "NSUnboldFontMask", NSUnboldFontMask);
	add_int(d, "NSNonStandardCharacterSetFontMask", NSNonStandardCharacterSetFontMask);
	add_int(d, "NSNarrowFontMask", NSNarrowFontMask);
	add_int(d, "NSExpandedFontMask", NSExpandedFontMask);
	add_int(d, "NSCondensedFontMask", NSCondensedFontMask);
	add_int(d, "NSSmallCapsFontMask", NSSmallCapsFontMask);
	add_int(d, "NSPosterFontMask", NSPosterFontMask);
	add_int(d, "NSCompressedFontMask", NSCompressedFontMask);
	add_int(d, "NSFixedPitchFontMask", NSFixedPitchFontMask);
	add_int(d, "NSUnitalicFontMask", NSUnitalicFontMask);
	add_int(d, "NSUtilityWindowMask", NSUtilityWindowMask);
	add_int(d, "NSDocModalWindowMask", NSDocModalWindowMask);
#ifndef GNUSTEP
#if MAC_OS_X_VERSION_10_2 <= MAC_OS_X_VERSION_MAX_ALLOWED
	add_int(d, "NSNonactivatingPanelMask", NSNonactivatingPanelMask);
#endif
#endif
	add_int(d, "NSBorderlessWindowMask", NSBorderlessWindowMask);
	add_int(d, "NSTitledWindowMask", NSTitledWindowMask);
	add_int(d, "NSClosableWindowMask", NSClosableWindowMask);
	add_int(d, "NSMiniaturizableWindowMask", NSMiniaturizableWindowMask);
	add_int(d, "NSResizableWindowMask", NSResizableWindowMask);
#ifndef GNUSTEP
#if MAC_OS_X_VERSION_10_2 <= MAC_OS_X_VERSION_MAX_ALLOWED
	add_int(d, "NSTexturedBackgroundWindowMask", NSTexturedBackgroundWindowMask);
#endif
#endif

	{
	  struct uchar_table*  cur = g_unicode_characters;
	  PyObject* v;
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
}
