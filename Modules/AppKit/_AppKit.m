/*
 * Mapping of static items in the AppKit kit:
 * 
 * - constants  (mostly done)
 * - data types (TODO)
 * - enumerations
 * - exceptions 
 * - global functions (TODO)
 */
#include <Python.h>

#import <AppKit/AppKit.h>
#import <AppKit/NSGraphics.h>
#ifndef GNUSTEP
#import <AppKit/NSAccessibility.h>
#import <AppKit/NSTypesetter.h>
#endif

#include "pyobjc-api.h"
#include "objc_support.h"
#include "OC_PythonObject.h"
#include "wrapper-const-table.h"
#ifndef GNU_RUNTIME
#include <objc/objc-runtime.h>
#endif

/** Functions */

/* The headings below refer to the reference pages on developer.apple.com */

/* 'Applications' */

static PyObject* 
objc_NSApplicationMain(PyObject* self, PyObject* args, PyObject* kwds)
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

	{
	  typedef struct {
	    @defs(NSProcessInfo)
	  } NSProcessInfoStruct;
	  
	  // everything in this scope is evil and wrong.  It leaks, too.
	  NSMutableArray *args = [[NSMutableArray alloc] init];
	  NSProcessInfo *processInfo = [NSProcessInfo processInfo];
	  char **anArg = argv;
	  while(*anArg) {
	    [args addObject: [NSString stringWithUTF8String: *anArg]];
	    anArg++;
	  }
	  ((NSProcessInfoStruct *)processInfo)->arguments = args;
	}

	NS_DURING
		res = NSApplicationMain(argc, (const char**)argv);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
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
objc_NSApp(PyObject* self, PyObject* args, PyObject* kwds)
{
static  char* keywords[] = { NULL };
        PyObject* result;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, ":NSApp", keywords)) {
		return NULL;
	}

	result = ObjC_IdToPython(NSApp);

	return result;                               
}

static PyObject*
objc_NSCountWindows(PyObject* self, PyObject* args, PyObject* kwds)
{
static  char* keywords[] = { NULL };
	int       count;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, ":NSCountWindows", keywords)) {
		return NULL;
	}

	NS_DURING
		NSCountWindows(&count);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
	NS_ENDHANDLER
	if (PyErr_Occurred()) return NULL;

	return PyInt_FromLong(count);
}

static PyObject*
objc_NSCountWindowsForContext(PyObject* self, PyObject* args, PyObject* kwds)
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
		ObjCErr_FromObjC(localException);
	NS_ENDHANDLER
	if (PyErr_Occurred()) return NULL;

	return PyInt_FromLong(count);
}

static PyObject*
objc_NSAvailableWindowDepths(PyObject* self, PyObject* args, PyObject* kwds)
{
static  char* keywords[] = { NULL };
	int       count;
	const NSWindowDepth*	  depths;
	PyObject *result, *tmp;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, ":NSAvailableWindowDepts", keywords)) {
		return NULL;
	}

	NS_DURING
		depths = NSAvailableWindowDepths();
	NS_HANDLER
		ObjCErr_FromObjC(localException);
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
objc_NSRectFillList(PyObject* self, PyObject* args, PyObject* kwds)
{
  unsigned char *rectBytes;
  int rectByteLength;
  int rectCount = -1;
  if  (PyArg_ParseTuple(args, "s#|i", &rectBytes, &rectByteLength, &rectCount) < 0) {
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
    if (rectCount > (rectByteLength / sizeof(NSRect))) {
      PyErr_SetString(PyExc_ValueError, "Rect count specified, but was longer than supplied array of rectangles.");
      return NULL;
    }
  } else
    rectCount = rectByteLength / sizeof(NSRect);

  NSRectFillList((NSRect *) rectBytes, rectCount);

  Py_INCREF(Py_None);
  return Py_None; 
}

static PyObject*
objc_NSGetWindowServerMemory(PyObject* self, PyObject* args, PyObject* kwds)
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
		ObjCErr_FromObjC(localException);
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

	v = ObjC_IdToPython(windowDumpStream);
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

#if MAC_OS_X_VERSION_10_2 <= MAC_OS_X_VERSION_MAX_ALLOWED
#include "_App_Functions.inc"
#endif

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

#if MAC_OS_X_VERSION_10_2 <= MAC_OS_X_VERSION_MAX_ALLOWED
#include "_App_Enum.inc"
#include "_App_Str.inc"
#endif

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



void init_AppKit(void)
{
	PyObject *m, *d;

	m = Py_InitModule4("_AppKit", appkit_methods, appkit_doc, 
		NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (ObjC_ImportModule(m) < 0) {
		return;
	}

	if (register_ints(d, enum_table) < 0) return;
	if (register_strings(d, string_table) < 0) return;

#ifdef GNUSTEP

#	include "_App_Var.GNUstep.inc"

#else /* !GNUSTEP */

#if MAC_OS_X_VERSION_10_2 <= MAC_OS_X_VERSION_MAX_ALLOWED
#	include "_App_Var.inc"
#endif

#endif /* !GNUSTEP */

	/* And some troublesome definitions 
	 * All of these found by 'grep #define *.h' in the AppKit header 
	 * directory
	 */

#ifndef GNUSTEP
	/* NSOpenGL.h */
	INT_VAR(NSOPENGL_CURRENT_VERSION);

	/* NSStatusBar.h */
	INT_VAR(NSVariableStatusItemLength);
	INT_VAR(NSSquareStatusItemLength);

	/* NSTypesetter.h */
	INT_VAR(NSBaselineNotSet);
	INT_VAR(NumGlyphsToGetEachTime);
#endif

	/* NSWindow.h */
	INT_VAR(NSNormalWindowLevel);
	INT_VAR(NSFloatingWindowLevel);
	INT_VAR(NSSubmenuWindowLevel);
	INT_VAR(NSTornOffMenuWindowLevel);
	INT_VAR(NSMainMenuWindowLevel);
	INT_VAR(NSStatusWindowLevel);
	INT_VAR(NSModalPanelWindowLevel);
	INT_VAR(NSPopUpMenuWindowLevel);
	INT_VAR(NSScreenSaverWindowLevel);


	INT_VAR(NSNoCellMask);
	INT_VAR(NSContentsCellMask);
	INT_VAR(NSPushInCellMask);
	INT_VAR(NSChangeGrayCellMask);
	INT_VAR(NSChangeBackgroundCellMask);
	INT_VAR(NSColorPanelGrayModeMask);
	INT_VAR(NSColorPanelRGBModeMask);
	INT_VAR(NSColorPanelCMYKModeMask);
	INT_VAR(NSColorPanelHSBModeMask);
	INT_VAR(NSColorPanelCustomPaletteModeMask);
	INT_VAR(NSColorPanelColorListModeMask);
	INT_VAR(NSColorPanelWheelModeMask);
#ifndef GNUSTEP
	INT_VAR(NSColorPanelCrayonModeMask);
#endif
	INT_VAR(NSColorPanelAllModesMask);
	INT_VAR(NSLeftMouseDownMask);
	INT_VAR(NSLeftMouseUpMask);
	INT_VAR(NSRightMouseDownMask);
	INT_VAR(NSRightMouseUpMask);
	INT_VAR(NSMouseMovedMask);
	INT_VAR(NSLeftMouseDraggedMask);
	INT_VAR(NSRightMouseDraggedMask);
	INT_VAR(NSMouseEnteredMask);
	INT_VAR(NSMouseExitedMask);
	INT_VAR(NSKeyDownMask);
	INT_VAR(NSKeyUpMask);
	INT_VAR(NSFlagsChangedMask);
	INT_VAR(NSAppKitDefinedMask);
	INT_VAR(NSSystemDefinedMask);
	INT_VAR(NSApplicationDefinedMask);
	INT_VAR(NSPeriodicMask);
	INT_VAR(NSCursorUpdateMask);
	INT_VAR(NSScrollWheelMask);
	INT_VAR(NSOtherMouseDownMask);
	INT_VAR(NSOtherMouseUpMask);
	INT_VAR(NSOtherMouseDraggedMask);
	INT_VAR(NSAnyEventMask);
	INT_VAR(NSAlphaShiftKeyMask);
	INT_VAR(NSShiftKeyMask);
	INT_VAR(NSControlKeyMask);
	INT_VAR(NSAlternateKeyMask);
	INT_VAR(NSCommandKeyMask);
	INT_VAR(NSNumericPadKeyMask);
	INT_VAR(NSHelpKeyMask);
	INT_VAR(NSFunctionKeyMask);
	INT_VAR(NSItalicFontMask);
	INT_VAR(NSBoldFontMask);
	INT_VAR(NSUnboldFontMask);
	INT_VAR(NSNonStandardCharacterSetFontMask);
	INT_VAR(NSNarrowFontMask);
	INT_VAR(NSExpandedFontMask);
	INT_VAR(NSCondensedFontMask);
	INT_VAR(NSSmallCapsFontMask);
	INT_VAR(NSPosterFontMask);
	INT_VAR(NSCompressedFontMask);
	INT_VAR(NSFixedPitchFontMask);
	INT_VAR(NSUnitalicFontMask);
	INT_VAR(NSUtilityWindowMask);
	INT_VAR(NSDocModalWindowMask);
#ifndef GNUSTEP
	INT_VAR(NSNonactivatingPanelMask);
#endif
	INT_VAR(NSBorderlessWindowMask);
	INT_VAR(NSTitledWindowMask);
	INT_VAR(NSClosableWindowMask);
	INT_VAR(NSMiniaturizableWindowMask);
	INT_VAR(NSResizableWindowMask);
#ifndef GNUSTEP
	INT_VAR(NSTexturedBackgroundWindowMask);
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
}
