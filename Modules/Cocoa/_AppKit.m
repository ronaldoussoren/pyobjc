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
#import <AppKit/NSAccessibility.h>
#import <AppKit/NSTypesetter.h>

#include "pyobjc-api.h"
#include "OC_PythonObject.h"
#include "const-table.h"
#include <objc/objc-runtime.h>

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

	res = NSApplicationMain(argc, argv);

	for (i = 0; i < argc; i++) {
		free(argv[i]);
	}
	free(argv);

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

/* NSGet{Alert,Information,CriticalAlert}Panel */

#define GetXPanel(PANELTYPE) \
	static PyObject* \
	objc_##PANELTYPE(PyObject* self, PyObject* args, PyObject* kwds) \
	{ \
	static  char* keywords[] = { "title", "msg", "defaultButton", "alternateButton", "otherButton", NULL }; \
		char*     title = NULL; \
		char*     msg = NULL; \
		char*     defaultButton = NULL; \
		char*     alternateButton = NULL; \
		char*     otherButton = NULL; \
		id        objc_title = nil; \
		id        objc_msg = nil; \
		id        objc_defaultButton = nil; \
		id        objc_alternateButton = nil; \
		id        objc_otherButton = nil; \
		id	  objc_result = nil; \
 \
		if (!PyArg_ParseTupleAndKeywords(args, kwds, "sssss:" STR(PANELTYPE), keywords, \
				&title, &msg, &defaultButton, &alternateButton, &otherButton)) { \
			return NULL; \
		} \
 \
		objc_title = [NSString stringWithCString:title]; \
		if (objc_title == nil) goto error_handler; \
		objc_msg = [NSString stringWithCString:msg]; \
		if (objc_msg == nil) goto error_handler; \
		objc_defaultButton = [NSString stringWithCString:defaultButton]; \
		if (objc_defaultButton == nil) goto error_handler; \
		objc_alternateButton = [NSString stringWithCString:alternateButton]; \
		if (objc_alternateButton == nil) goto error_handler; \
		objc_otherButton = [NSString stringWithCString:otherButton]; \
		if (objc_otherButton == nil) goto error_handler; \
 \
		NS_DURING \
			objc_result = PANELTYPE(objc_title, @"%@", objc_defaultButton, \
				objc_alternateButton, objc_otherButton, objc_msg); \
		NS_HANDLER \
			ObjCErr_FromObjC(localException); \
			objc_result = nil; \
		NS_ENDHANDLER \
 \
		[objc_title release]; \
		objc_title = nil; \
		[objc_msg release]; \
		objc_msg = nil; \
		[objc_defaultButton release]; \
		objc_defaultButton = nil; \
		[objc_alternateButton release]; \
		objc_alternateButton = nil; \
		[objc_otherButton release]; \
		objc_otherButton = nil; \
 \
		if (PyErr_Occurred()) return NULL; \
 \
		return ObjC_IdToPython(objc_result);\
\
	error_handler:\
		if (objc_title) [objc_title release];\
		if (objc_msg) [objc_msg release];\
		if (objc_defaultButton) [objc_defaultButton release];\
		if (objc_alternateButton) [objc_alternateButton release];\
		if (objc_otherButton) [objc_otherButton release];\
		return NULL;\
	}\

GetXPanel(NSGetAlertPanel)
GetXPanel(NSGetInformationalAlertPanel)
GetXPanel(NSGetCriticalAlertPanel)


/* NSRun{Alert,Information,CriticalAlert}Panel */

#define RunXPanel(PANELTYPE) \
	static PyObject* \
	objc_##PANELTYPE(PyObject* self, PyObject* args, PyObject* kwds) \
	{ \
	static  char* keywords[] = { "title", "msg", "defaultButton", "alternateButton", "otherButton", NULL }; \
		char*     title = NULL; \
		char*     msg = NULL; \
		char*     defaultButton = NULL; \
		char*     alternateButton = NULL; \
		char*     otherButton = NULL; \
		id        objc_title = nil; \
		id        objc_msg = nil; \
		id        objc_defaultButton = nil; \
		id        objc_alternateButton = nil; \
		id        objc_otherButton = nil; \
		int	  objc_result; \
 \
		if (!PyArg_ParseTupleAndKeywords(args, kwds, "sszzz:" STR(PANELTYPE), keywords, \
				&title, &msg, &defaultButton, &alternateButton, &otherButton)) { \
			return NULL; \
		} \
		\
		if (title) {\
			objc_title = [NSString stringWithCString:title]; \
			if (objc_title == nil) goto error_handler; \
		}\
		\
		if (msg) {\
			objc_msg = [NSString stringWithCString:msg]; \
			if (objc_msg == nil) goto error_handler; \
		}\
		\
		if (defaultButton) {\
			objc_defaultButton = [NSString stringWithCString:defaultButton]; \
			if (objc_defaultButton == nil) goto error_handler; \
		}\
		if (alternateButton) {\
			objc_alternateButton = [NSString stringWithCString:alternateButton]; \
			if (objc_alternateButton == nil) goto error_handler; \
		}\
		if (otherButton) {\
			objc_otherButton = [NSString stringWithCString:otherButton]; \
			if (objc_otherButton == nil) goto error_handler; \
		}\
 \
		NS_DURING \
			objc_result = PANELTYPE(objc_title, @"%@", objc_defaultButton, \
				objc_alternateButton, objc_otherButton, objc_msg); \
		NS_HANDLER \
			ObjCErr_FromObjC(localException); \
			objc_result = nil; \
		NS_ENDHANDLER \
 \
	/*WHY ARE THESE ALREADY RELEASED?	[objc_title release]; \
		objc_title = nil; \
		[objc_msg release]; \
		objc_msg = nil; \
		[objc_defaultButton release]; \
		objc_defaultButton = nil; \
		[objc_alternateButton release]; \
		objc_alternateButton = nil; \
		[objc_otherButton release]; \
		objc_otherButton = nil; */\
 \
		if (PyErr_Occurred()) return NULL; \
 \
		return PyInt_FromLong(objc_result);\
\
	error_handler:\
		if (objc_title) [objc_title release];\
		if (objc_msg) [objc_msg release];\
		if (objc_defaultButton) [objc_defaultButton release];\
		if (objc_alternateButton) [objc_alternateButton release];\
		if (objc_otherButton) [objc_otherButton release];\
		return NULL;\
	}\

RunXPanel(NSRunAlertPanel)
RunXPanel(NSRunInformationalAlertPanel)
RunXPanel(NSRunCriticalAlertPanel)

#include "_App_Functions.inc"

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
		"NSRunAlertPanel", 
		(PyCFunction)objc_NSRunAlertPanel, 
		METH_VARARGS|METH_KEYWORDS, 
		NULL
	},
	{ 
		"NSRunInformationPanel", 
		(PyCFunction)objc_NSRunInformationalAlertPanel, 
		METH_VARARGS|METH_KEYWORDS, 
		NULL
	},
	{ 
		"NSRunCriticalAlertPanel", 
		(PyCFunction)objc_NSRunCriticalAlertPanel, 
		METH_VARARGS|METH_KEYWORDS, 
		NULL
	},
	{ 
		"NSGetAlertPanel", 
		(PyCFunction)objc_NSGetAlertPanel, 
		METH_VARARGS|METH_KEYWORDS, 
		NULL
	},
	{ 
		"NSGetInformationPanel", 
		(PyCFunction)objc_NSGetInformationalAlertPanel, 
		METH_VARARGS|METH_KEYWORDS, 
		NULL
	},
	{ 
		"NSGetCriticalAlertPanel", 
		(PyCFunction)objc_NSGetCriticalAlertPanel, 
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
#	include "_App_Var.inc"

	/* And some troublesome definitions 
	 * All of these found by 'grep #define *.h' in the AppKit header 
	 * directory
	 */

	/* NSOpenGL.h */
	INT_VAR(NSOPENGL_CURRENT_VERSION);

	/* NSStatusBar.h */
	INT_VAR(NSVariableStatusItemLength);
	INT_VAR(NSSquareStatusItemLength);

	/* NSTypesetter.h */
	INT_VAR(NSBaselineNotSet);
	INT_VAR(NumGlyphsToGetEachTime);

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
	INT_VAR(NSColorPanelCrayonModeMask);
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
	INT_VAR(NSNonactivatingPanelMask);
	INT_VAR(NSBorderlessWindowMask);
	INT_VAR(NSTitledWindowMask);
	INT_VAR(NSClosableWindowMask);
	INT_VAR(NSMiniaturizableWindowMask);
	INT_VAR(NSResizableWindowMask);
	INT_VAR(NSTexturedBackgroundWindowMask);

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
