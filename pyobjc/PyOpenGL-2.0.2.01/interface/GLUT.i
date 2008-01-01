/*
# API versions are set to GLUT_XLIB_IMPLEMENTATION instead of GLUT_API_VERSION since 
# GLUT_API_VERSION doesn't carry the minor version number (needed to support provisional 
# GLUT 4 routines)
#
#
# BUILD api_versions [1, 2, 5, 7, 9, 11, 13, 20]
# BUILD macro_template 'GLUT_XLIB_IMPLEMENTATION >= %(api_version)d || FREEGLUT_VERSION_2_0'
# BUILD libs ['GLUT']
*/

%module GLUT

#define __version__ "$Revision: 1.49.4.2 $"
#define __date__ "$Date: 2004/11/14 23:27:25 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>\nMike C. Fletcher <mcfletch@users.sourceforge.net>"
#define __credits__ "The GLUT module of PyOpenGL is based on PyGLUT by Andrew Cox."
#define __doc__ "The module provides an interface to the GLUT library.\n\
\n\
Documentation:\n\
    Man Pages:  http:\057\057pyopengl.sourceforge.net/documentation/ref/glut.html\n\
    GLUT Homepage:  http:\057\057reality.sgi.com/mjk/glut3/glut3.html\n\
    OpenGL.org:  http:\057\057www.opengl.org\057developers\057documentation\057glut.html"

%include util.inc

%{
/*
#
# GLUT Module for PyOpenGL
#  
# Date: May 2001
# 
# This module is derived from PyGLUT, by Andrew Cox
# 
# Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
#          Mike C. Fletcher
# 
#
#
# This file is derived from the glut.h distributed with GLUT 3.7. 
# It is a complete wrapper for GLUT API version 4 (provisional) including the 
# game functionality. 
# 
# The conversion to a SWIG interface file was done by me: 
# Andrew Cox (acox@globalnet.co.uk). 
# Any correspondence about PyGlut should be directed to me. 
# 
# Any updates will be made available at my homepage: 
# http://www.users.globalnet.co.uk/~acox/ 
# 
# I place no additional limitations on what can be done with the contents of 
# this file beyond those it inherits from GLUT. 
# 
# DISCLAIMER: 
# PyGlut is provided AS IS without warranty of any kind, either express or 
# implied, including but not limited to the implied warranties of 
# merchantability and fitness for a particular purpose. In no event shall 
# Andrew Cox be liable for any damages whatsoever including direct, indirect, 
# incidental, consequential, loss of business profits or special damages, 
# even if Andrew Cox has been advised of the possibility of such damages.
#
# Copyright (c) Mark J. Kilgard, 1994, 1995, 1996, 1998.
#
# This program is freely distributable without licensing fees  and is
#  provided without guarantee or warrantee expressed or  implied. This
#  program is -not- in the public domain. 
# 
# ToDo:  
# > Rather than refcounting menu callbacks passed in, do something less fragile 
#   in the face of misuse of Glut's Create/Destroy interface. 
# */
%}

%include py_exception_handler.inc

/* GLUT initialization sub-API. */

%{
#if defined(__APPLE__) || defined(MACOSX)
/* Apple's GLUT changes directory after glutInit, you probably don't want that to happen, so we undo it :) */
#include <unistd.h>
#include <sys/param.h>
#endif

PyObject *_glutInit(PyObject* args)
{
	int argc, i;
	char **argv;
	PyObject *o, *s;
	
#if defined(__APPLE__) || defined(MACOSX)
	/* store path before glut messes it up on osx */
	char apple_preserve_path[MAXPATHLEN];
	getcwd(apple_preserve_path, MAXPATHLEN);
#endif
	if (!PyString_Check(args) && PySequence_Check(args))
	{
		argc = PySequence_Size(args);

		if (argc == 0)
		{
			argv = PyMem_New(char*, argc = 1);
			argv[0] = "foo";
		}
		else
		{
			argv = PyMem_New(char*, argc);
			for (i = 0; i < argc; i++)
			{
				o = PySequence_GetItem(args, i);
				s = PyObject_Str(o);
				
				if (s)
				{
					argv[i] = PyString_AsString(s);
					Py_DECREF(o);
					Py_DECREF(s);
				}
				else
				{
					PyMem_Del(argv);
					Py_DECREF(o);
					PyErr_SetString(PyExc_TypeError, "list must contain strings");
					return NULL;
				}
			}
		}
	}
	else
	{
		PyErr_SetString(PyExc_TypeError, "not a list");
		return NULL;
	}
	
	glutInit(&argc, argv);

#if defined(__APPLE__) || defined(MACOSX)
	/* switch back to original path on OSX */
	chdir(apple_preserve_path);
#endif
	
	o = PyList_New(argc);
	for (i = 0; i < argc; i++) PyList_SetItem(o, i, PyString_FromString(argv[i]));
	PyMem_Del(argv);

	return o;
}
%}

%name(glutInit) PyObject *_glutInit(PyObject* args);
DOC(glutInit, "glutInit(argv) -> argv")

void glutInitDisplayMode(unsigned int mode);
DOC(glutInitDisplayMode, "glutInitDisplayMode(mode) -> None")

void glutInitWindowPosition(int x, int y);
DOC(glutInitWindowPosition, "glutInitWindowPosition(x, y) -> None")

void glutInitWindowSize(int width, int height);
DOC(glutInitWindowSize, "glutInitWindowSize(width, height) -> None")

void glutMainLoop(void);
DOC(glutMainLoop, "glutMainLoop() -> None")

/* **************************************************************************** 
# 
# The Callback enabling functionality: 
# From Python, callable PyObjects are registered with functions that are named 
# the same as their C equivalents in Glut but which are not simple wrappers. 
# What they do is store a global pointer to the callable object and register 
# a C callback with Glut which knows about the global pointer. 
# When Glut calls the callback, it converts it's arguments to Python types and 
# evaluates the callable Python object referenced by the global pointer, 
# passing it the converted arguments. */

%{
PyObject *windows, *menus;

/* glutXXXFunc implementation, e.g. glutDisplayFunc */
int setCallback(const char* name, PyObject* func)
{
	PyObject *window_id = NULL;
	PyObject *window = NULL;
	int iwindow_id = glutGetWindow();
	if (iwindow_id) {
		/* there is a currently-defined window */
		window_id = PyInt_FromLong(iwindow_id);
		window = PyDict_GetItem(windows, window_id);

		if (!window)
		{
			window = PyDict_New();
			PyDict_SetItem(windows, window_id, window);
		}
		Py_DECREF(window_id);
		PyDict_SetItemString(window, (char*)name, func);
		return 1;
	} else {
		/* no currently defined window */
		PyErr_SetString(PyExc_RuntimeError, "Attempted to set callback with no active window");
		return 0;
	}
}

PyObject *getCallback(const char* name)
{
	PyObject *window_id = PyInt_FromLong(glutGetWindow());
	PyObject *window = PyDict_GetItem(windows, window_id);

	Py_DECREF(window_id);
	if (!window) return NULL;
	return PyDict_GetItemString(window, (char*)name);
}

/*
 * Utilities that build argument lists for Python callbacks and then eval them.
 */

void eval_no_args(PyObject *func)
{
	if (func && func != Py_None)
	{
		PyObject *result = PyObject_CallFunction(func, NULL);
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}

void eval_1int_arg(PyObject *func, int arg1)
{
	if (func && func != Py_None)
	{
		PyObject *result = PyObject_CallFunction(func, "(i)", arg1);
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}

/* Call a PyObject that takes two int arguments.*/
void eval_2int_args(PyObject *func, int arg1, int arg2)
{
	if (func && func != Py_None)
	{
		PyObject *result = PyObject_CallFunction(func, "ii", arg1, arg2);
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}

void eval_3int_args(PyObject *func, int arg1, int arg2, int arg3)
{
	if (func && func != Py_None)
	{
		PyObject *result = PyObject_CallFunction(func, "iii", arg1, arg2, arg3);
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}

void eval_4int_args(PyObject *func, int arg1, int arg2, int arg3, int arg4)
{
	if (func && func != Py_None)
	{
		PyObject *result = PyObject_CallFunction(func, "iiii", arg1, arg2, arg3, arg4);
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}

void eval_1uchar_2int_args(PyObject *func, unsigned char arg1, int arg2, int arg3)
{
	if (func && func != Py_None)
	{
		PyObject *result = PyObject_CallFunction(func, "cii", arg1, arg2, arg3);
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}


#define GLOBAL_CALLBACK(NAME)\
void _glut##NAME##Func(PyObject *pyfunc)\
{\
    PyObject *old = NAME##Func;\
    NAME##Func = pyfunc;\
    Py_XINCREF(pyfunc);\
    glut##NAME##Func((pyfunc == Py_None) ? NULL : NAME##Callback);\
    Py_XDECREF(old);\
}


#define WIN_CALLBACK(NAME)\
void _glut##NAME##Func(PyObject *pyfunc)\
{\
	if (setCallback(#NAME, pyfunc)) {\
		glut##NAME##Func((pyfunc == Py_None) ? NULL : NAME##Callback);\
	}\
}
%}

%init
%{
windows = PyDict_New();
menus = PyDict_New();
%}

/*
# Wrapped Functions
*/

/* Callback registration: */

/* GLUT window callback sub-API. */
%{
void DisplayCallback(void)
{
	eval_no_args(getCallback("Display"));
}

WIN_CALLBACK(Display)
%}

%name(glutDisplayFunc) void _glutDisplayFunc(PyObject * pyfunc);
DOC(glutDisplayFunc, "glutDisplayFunc(func) -> None")

%{
void ReshapeCallback(int x, int y)
{
	eval_2int_args(getCallback("Reshape"), x, y);
}

WIN_CALLBACK(Reshape)
%}

%name(glutReshapeFunc) void _glutReshapeFunc(PyObject * pyfunc);
DOC(glutReshapeFunc, "glutReshapeFunc(func) -> None")

%{
void KeyboardCallback(unsigned char key, int x, int y)
{
    eval_1uchar_2int_args(getCallback("Keyboard"), key, x, y);
}

WIN_CALLBACK(Keyboard)
%}

%name(glutKeyboardFunc) void _glutKeyboardFunc(PyObject * pyfunc);
DOC(glutKeyboardFunc, "glutKeyboardFunc(func) -> None")

%{
void MouseCallback(int button, int state, int x, int y)
{
    eval_4int_args(getCallback("Mouse"), button, state, x, y);
}

WIN_CALLBACK(Mouse)
%}

%name(glutMouseFunc) void _glutMouseFunc(PyObject * pyfunc);
DOC(glutMouseFunc, "glutMouseFunc(func) -> None")

%{
void MotionCallback(int x, int y)
{
    eval_2int_args(getCallback("Motion"), x, y);
}

WIN_CALLBACK(Motion)
%}

%name(glutMotionFunc) void _glutMotionFunc(PyObject * pyfunc);
DOC(glutMotionFunc, "glutMotionFunc(func) -> None")

%{
void PassiveMotionCallback(int x, int y)
{
    eval_2int_args(getCallback("PassiveMotion"), x, y);
}

WIN_CALLBACK(PassiveMotion)
%}

%name(glutPassiveMotionFunc) void _glutPassiveMotionFunc(PyObject * pyfunc);
DOC(glutPassiveMotionFunc, "glutPassiveMotionFunc(func) -> None")

%{
void EntryCallback(int state)
{
    eval_1int_arg(getCallback("Entry"), state);
}

WIN_CALLBACK(Entry)
%}

%name(glutEntryFunc) void _glutEntryFunc(PyObject * pyfunc);
DOC(glutEntryFunc, "glutEntryFunc(func) -> None")

%{
void VisibilityCallback(int state)
{
    eval_1int_arg(getCallback("Visibility"), state);
}

WIN_CALLBACK(Visibility)
%}

%name(glutVisibilityFunc) void _glutVisibilityFunc(PyObject * pyfunc);
DOC(glutVisibilityFunc, "glutVisibilityFunc(func) -> None")

#if API_VERSION >= 2
%{
void SpecialCallback(int key, int x, int y)
{
    eval_3int_args(getCallback("Special"), key, x, y);
}

WIN_CALLBACK(Special)
%}

%name(glutSpecialFunc) void _glutSpecialFunc(PyObject *pyfunc);
DOC(glutSpecialFunc, "glutSpecialFunc(func) -> None")

%{
void SpaceballMotionCallback(int x, int y, int z)
{
    eval_3int_args(getCallback("SpaceballMotion"), x, y, z);
}

WIN_CALLBACK(SpaceballMotion)
%}

%name(glutSpaceballMotionFunc) void _glutSpaceballMotionFunc(PyObject *pyfunc);
DOC(glutSpaceballMotionFunc, "glutSpaceballMotionFunc(func) -> None")

%{
void SpaceballRotateCallback(int x, int y, int z)
{
    eval_3int_args(getCallback("SpaceballRotate"), x, y, z);
}

WIN_CALLBACK(SpaceballRotate)
%}

%name(glutSpaceballRotateFunc) void _glutSpaceballRotateFunc(PyObject *pyfunc);
DOC(glutSpaceballRotateFunc, "glutSpaceballRotateFunc(func) -> None")

%{
void SpaceballButtonCallback(int button, int state)
{
    eval_2int_args(getCallback("SpaceballButton"), button, state);
}

WIN_CALLBACK(SpaceballButton)
%}

%name(glutSpaceballButtonFunc) void _glutSpaceballButtonFunc(PyObject *pyfunc);
DOC(glutSpaceballButtonFunc, "glutSpaceballButtonFunc(func) -> None")

%{
void ButtonBoxCallback(int button, int state)
{
    eval_2int_args(getCallback("ButtonBox"), button, state);
}

WIN_CALLBACK(ButtonBox)
%}

%name(glutButtonBoxFunc) void _glutButtonBoxFunc(PyObject *pyfunc);
DOC(glutButtonBoxFunc, "glutButtonBoxFunc(func) -> None")

%{
void DialsCallback(int dial, int value)
{
    eval_2int_args(getCallback("Dials"), dial, value);
}

WIN_CALLBACK(Dials)
%}

%name(glutDialsFunc) void _glutDialsFunc(PyObject *pyfunc);
DOC(glutDialsFunc, "glutDialsFunc(func) -> None")

%{
void TabletMotionCallback(int x, int y)
{
    eval_2int_args(getCallback("TabletMotion"), x, y);
}

WIN_CALLBACK(TabletMotion)
%}

%name(glutTabletMotionFunc) void _glutTabletMotionFunc(PyObject *pyfunc);
DOC(glutTabletMotionFunc, "glutTabletMotionFunc(func) -> None")

%{
void TabletButtonCallback(int button, int state, int x, int y)
{
    eval_4int_args(getCallback("TabletButton"), button, state, x, y);
}

WIN_CALLBACK(TabletButton)
%}

%name(glutTabletButtonFunc) void _glutTabletButtonFunc(PyObject *pyfunc);
DOC(glutTabletButtonFunc, "glutTabletButtonFunc(func) -> None")
#endif

#if API_VERSION >= 13
%{
void SpecialUpCallback(int key, int x, int y)
{
    eval_3int_args(getCallback("SpecialUp"), key, x, y);
}

WIN_CALLBACK(SpecialUp)
%}

%name(glutSpecialUpFunc)  void _glutSpecialUpFunc(PyObject * pyfunc);
DOC(glutSpecialUpFunc, "glutSpecialUpFunc(func) -> None")

%{
void KeyboardUpCallback(unsigned char key, int x, int y)
{
	eval_1uchar_2int_args(getCallback("KeyboardUp"), key, x, y);
}

WIN_CALLBACK(KeyboardUp)
%}

%name(glutKeyboardUpFunc) void _glutKeyboardUpFunc(PyObject * pyfunc);
DOC(glutKeyboardUpFunc, "glutKeyboardUpFunc(func) -> None")

%{
void JoystickCallback(unsigned int button_mask, int x, int y, int z)
{
    eval_4int_args(getCallback("Joystick"), button_mask, x, y, z);
}

void _glutJoystickFunc(PyObject * pyfunc, int poll_interval)
{
	setCallback("Joystick", pyfunc);
	glutJoystickFunc((pyfunc == Py_None) ? NULL : JoystickCallback, poll_interval);
}
%}

%name(glutJoystickFunc) void _glutJoystickFunc(PyObject * pyfunc, int poll_interval);
DOC(glutJoystickFunc, "glutJoystickFunc(func, poll_interval) -> None")
#endif

#if API_VERSION >= 5
%{
void OverlayDisplayCallback(void)
{
    eval_no_args(getCallback("OverlayDisplay"));
}

WIN_CALLBACK(OverlayDisplay)
%}

%name(glutOverlayDisplayFunc) void _glutOverlayDisplayFunc(PyObject * pyfunc);
DOC(glutOverlayDisplayFunc, "glutOverlayDisplayFunc(func) -> None")
#endif

/* Global Callbacks */
%{
static PyObject *IdleFunc = NULL;

void IdleCallback(void)
{
    eval_no_args(IdleFunc);
}

GLOBAL_CALLBACK(Idle)
%}

%name(glutIdleFunc) void _glutIdleFunc(PyObject * pyfunc);
DOC(glutIdleFunc, "glutIdleFunc(func) -> None")

%{
static PyObject *TimerFunc = NULL;

void TimerCallback(int state)
{
    eval_1int_arg(TimerFunc, state);
}

void _glutTimerFunc(unsigned int millis, PyObject *pyfunc, int value)
{
    PyObject *old = TimerFunc;
    TimerFunc = pyfunc;
    Py_XINCREF(pyfunc);
    glutTimerFunc(millis, (pyfunc == Py_None) ? NULL : TimerCallback, value);
    Py_XDECREF(old);
}
%}

%name(glutTimerFunc) void _glutTimerFunc(unsigned int millis, PyObject * pyfunc, int state);
DOC(glutTimerFunc, "glutTimerFunc(millis, func, state) -> None")

%{
static PyObject *MenuStateFunc = NULL;

void MenuStateCallback(int state)
{
	eval_1int_arg(MenuStateFunc, state);
}

GLOBAL_CALLBACK(MenuState)
%}

%name(glutMenuStateFunc) void _glutMenuStateFunc(PyObject * pyfunc);
DOC(glutMenuStateFunc, "glutMenuStateFunc(func) -> None")


#if API_VERSION >= 5
%{
static PyObject *MenuStatusFunc = NULL;

void MenuStatusCallback(int status, int x, int y)
{
    eval_3int_args(MenuStatusFunc, status, x, y);
}

GLOBAL_CALLBACK(MenuStatus)
%}

%name(glutMenuStatusFunc) void _glutMenuStatusFunc(PyObject * pyfunc);
DOC(glutMenuStatusFunc, "glutMenuStatusFunc(func) -> None")
#endif

#if API_VERSION >= 7
%{
static PyObject *WindowStatusFunc = NULL;

void WindowStatusCallback(int state)
{
    eval_1int_arg(WindowStatusFunc, state);
}

GLOBAL_CALLBACK(WindowStatus)
%}

%name(glutWindowStatusFunc) void _glutWindowStatusFunc(PyObject *pyfunc);
DOC(glutWindowStatusFunc, "glutWindowStatusFunc(func) -> None")
#endif


%include gl_exception_handler.inc

/* GLUT window sub-API. */
int glutCreateWindow(const char *title);
DOC(glutCreateWindow, "glutCreateWindow(title) -> win")

int glutCreateSubWindow(int win, int x, int y, int width, int height);
DOC(glutCreateSubWindow, "glutCreateSubWindow(win, x, y, width, height) -> win")

%{
void _glutDestroyWindow(int win)
{
	PyObject *window_id = PyInt_FromLong(win);

	PyDict_DelItem(windows, window_id);
	PyErr_Clear();
	Py_DECREF(window_id);
	
	glutDestroyWindow(win);
}
%}

%name(glutDestroyWindow) void _glutDestroyWindow(int win);
DOC(glutDestroyWindow, "glutDestroyWindow(win) -> None")

void glutPostRedisplay(void);
DOC(glutPostRedisplay, "glutPostRedisplay() -> None")

void glutSwapBuffers(void);
DOC(glutSwapBuffers, "glutSwapBuffers() -> None")

int glutGetWindow(void);
DOC(glutGetWindow, "glutGetWindow() -> None")

void glutSetWindow(int win);
DOC(glutSetWindow, "glutSetWindow() -> None")

void glutSetWindowTitle(const char *title);
DOC(glutSetWindowTitle, "glutSetWindowTitle(title) -> None")

void glutSetIconTitle(const char *title);
DOC(glutSetIconTitle, "glutSetIconTitle(title) -> None")

void glutPositionWindow(int x, int y);
DOC(glutPositionWindow, "glutPositionWindow(x, y) -> None")

void glutReshapeWindow(int width, int height);
DOC(glutReshapeWindow, "glutReshapeWindow(width, height) -> None")

void glutPopWindow(void);
DOC(glutPopWindow, "glutPopWindow() -> None")

void glutPushWindow(void);
DOC(glutPushWindow, "glutPushWindow() -> None")

void glutIconifyWindow(void);
DOC(glutIconifyWindow, "glutIconifyWindow() -> None")

void glutShowWindow(void);
DOC(glutShowWindow, "glutShowWindow() -> None")

void glutHideWindow(void);
DOC(glutHideWindow, "glutHideWindow() -> None")

/* GLUT menu sub-API. */
%{
void MenuCallback(int event)
{
	PyObject *menu_id = PyInt_FromLong(glutGetMenu());
	PyObject *func = PyDict_GetItem(menus, menu_id);

	Py_DECREF(menu_id);
	eval_1int_arg(func, event);
}

int _glutCreateMenu(PyObject *pyfunc)
{
	int menu = glutCreateMenu(MenuCallback);
	PyObject *menu_id = PyInt_FromLong(menu);

	PyDict_SetItem(menus, menu_id, pyfunc);
	Py_DECREF(menu_id);

	return menu;
}

void _glutDestroyMenu(int menu)
{
	PyObject *menu_id = PyInt_FromLong(glutGetMenu());

	PyDict_DelItem(menus, menu_id);
	Py_DECREF(menu_id);
	glutDestroyMenu(menu);
}
%}

%name(glutCreateMenu) int _glutCreateMenu(PyObject * pyfunc);
DOC(glutCreateMenu, "glutCreateMenu(func) -> menu")

%name(glutDestroyMenu) void _glutDestroyMenu(int menu);
DOC(glutDestroyMenu, "glutDestroyMenu(menu) -> None")

int glutGetMenu(void);
DOC(glutGetMenu, "glutGetMenu() -> mene")

void glutSetMenu(int menu);
DOC(glutSetMenu, "glutSetMenu(menu) -> None")

void glutAddMenuEntry(const char *label, int value);
DOC(glutAddMenuEntry, "glutAddMenuEntry(label, value) -> None")

void glutAddSubMenu(const char *label, int submenu);
DOC(glutAddSubMenu, "glutAddSubMenu(label, submenu) -> None")

void glutChangeToMenuEntry(int item, const char *label, int value);
DOC(glutChangeToMenuEntry, "glutChangeToMenuEntry(item, label, value) -> None")

void glutChangeToSubMenu(int item, const char *label, int submenu);
DOC(glutChangeToSubMenu, "glutChangeToSubMenu(item, label, submenu) -> None")

void glutRemoveMenuItem(int item);
DOC(glutRemoveMenuItem, "glutRemoveMenuItem(item) -> None")

void glutAttachMenu(int button);
DOC(glutAttachMenu, "glutAttachMenu(button) -> None")

void glutDetachMenu(int button);
DOC(glutDetachMenu, "glutDetachMenu(button) -> None")

/* GLUT color index sub-API. */
void glutSetColor(int cell, GLfloat red, GLfloat green, GLfloat blue);
DOC(glutSetColor, "glutSetColor(cell, red, green, blue) -> None")

GLfloat glutGetColor(int ndx, int component);
DOC(glutGetColor, "glutGetColor(ndx, component) -> None")

void glutCopyColormap(int win);
DOC(glutCopyColormap, "glutCopyColormap(win) -> None")

/* GLUT state retrieval sub-API. */
int glutGet(GLenum type);
DOC(glutGet, "glutGet(type) -> None")

int glutDeviceGet(GLenum type);
DOC(glutDeviceGet, "glutDeviceGet() -> None")


/* GLUT font sub-API */
%{
/* On MS Windows fonts are ints disguised as void*s. On Unix they realy are 
# void*s. 
# On the Python side fonts are known by int values. */

void* _PyInt_AsFont(PyObject *x)
{
	if (PyInt_Check(x))
	{
		switch (PyInt_AsLong(x))
		{
		case 0:
			return GLUT_STROKE_ROMAN;
		case 1:
			return GLUT_STROKE_MONO_ROMAN;
		case 2:
			return GLUT_BITMAP_9_BY_15;
		case 3:
			return GLUT_BITMAP_8_BY_13;
		case 4:
			return GLUT_BITMAP_TIMES_ROMAN_10;
		case 5:
			return GLUT_BITMAP_TIMES_ROMAN_24;
#if (GLUT_API_VERSION >= 3)
		case 6:
			return GLUT_BITMAP_HELVETICA_10;
		case 7:
			return GLUT_BITMAP_HELVETICA_12;
		case 8:
			return GLUT_BITMAP_HELVETICA_18;
#endif
		}
		
		PyErr_SetString(PyExc_ValueError, "Unknown font.");
	}
	else PyErr_SetString(PyExc_ValueError, "Invalid font identifier.");
	
	return 0;
}
%}

/* Convert int to font */
%typemap(python, in) void *font
{
	$1 = _PyInt_AsFont($input);
	if (PyErr_Occurred()) return NULL;
}

void glutBitmapCharacter(void *font, int character);
DOC(glutBitmapCharacter, "glutBitmapCharacter(font, character) -> None")

int glutBitmapWidth(void *font, int character);
DOC(glutBitmapWidth, "glutBitmapWidth(font, character) -> None")

void glutStrokeCharacter(void *font, int character);
DOC(glutStrokeCharacter, "glutStrokeCharacter(font, character) -> None")

int glutStrokeWidth(void *font, int character);
DOC(glutStrokeWidth, "glutStrokeWidth(font, character) -> None")

/* GLUT pre-built models sub-API */

void glutWireSphere(GLdouble radius, GLint slices, GLint stacks);
DOC(glutWireSphere, "glutWireSphere(radius, slices, stacks) -> None")

void glutSolidSphere(GLdouble radius, GLint slices, GLint stacks);
DOC(glutSolidSphere, "glutSolidSphere(radius, slices, stacks) -> None")

void glutWireCone(GLdouble base, GLdouble height, GLint slices, GLint stacks);
DOC(glutWireCone, "glutWireCone(base, height, slices, stacks) -> None")

void glutSolidCone(GLdouble base, GLdouble height, GLint slices, GLint stacks);
DOC(glutSolidCone, "glutSolidCone(base, height, slices, stacks) -> None")

void glutWireCube(GLdouble size);
DOC(glutWireCube, "glutWireCube(size) -> None")

void glutSolidCube(GLdouble size);
DOC(glutSolidCube, "glutSolidCube(size) -> None")

void glutWireTorus(GLdouble innerRadius, GLdouble outerRadius, GLint sides, GLint rings);
DOC(glutWireTorus, "glutWireTorus(innerRadius, outerRadius, size, rings) -> None")

void glutSolidTorus(GLdouble innerRadius, GLdouble outerRadius, GLint sides, GLint rings);
DOC(glutSolidTorus, "glutSolidTorus(innerRadius, outerRadius, size, rings) -> None")

void glutWireDodecahedron(void);
DOC(glutWireDodecahedron, "glutWireDodecahedron() -> None")

void glutSolidDodecahedron(void);
DOC(glutSolidDodecahedron, "glutSolidDodecahedron() -> None")

void glutWireTeapot(GLdouble size);
DOC(glutWireTeapot, "glutWireTeapot(size) -> None")

void glutSolidTeapot(GLdouble size);
DOC(glutSolidTeapot, "glutSolidTeapot(size) -> None")

void glutWireOctahedron(void);
DOC(glutWireOctahedron, "glutWireOctahedron() -> None")

void glutSolidOctahedron(void);
DOC(glutSolidOctahedron, "glutSolidOctahedron() -> None")

void glutWireTetrahedron(void);
DOC(glutWireTetrahedron, "glutWireTetrahedron() -> None")

void glutSolidTetrahedron(void);
DOC(glutSolidTetrahedron, "glutSolidTetrahedron() -> None")

void glutWireIcosahedron(void);
DOC(glutWireIcosahedron, "glutWireIcosahedron() -> None")

void glutSolidIcosahedron(void);
DOC(glutSolidIcosahedron, "glutSolidIcosahedron() -> None")

#if API_VERSION >= 2
/* GLUT extension support sub-API */
int glutExtensionSupported(const char *name);
DOC(glutExtensionSupported, "glutExtensionSupported(name) -> int")
#endif

#if API_VERSION >= 5
void glutFullScreen(void);
DOC(glutFullScreen, "glutFullScreen() -> None")

void glutSetCursor(int cursor);
DOC(glutSetCursor, "glutSetCursor(cursor) -> None")

/* GLUT overlay sub-API. */
void glutEstablishOverlay(void);
DOC(glutEstablishOverlay, "glutEstablishOverlay() -> None")

void glutRemoveOverlay(void);
DOC(glutRemoveOverlay, "glutRemoveOverlay(func) -> None")

void glutUseLayer(GLenum layer);
DOC(glutUseLayer, "glutUseLayer(layer) -> None")

void glutPostOverlayRedisplay(void);
DOC(glutPostOverlayRedisplay, "glutPostOverlayRedisplay() -> None")

void glutShowOverlay(void);
DOC(glutShowOverlay, "glutShowOverlay() -> None")

void glutHideOverlay(void);
DOC(glutHideOverlay, "glutHideOverlay() -> None")

int glutGetModifiers(void);
DOC(glutGetModifiers, "glutGetModifiers() -> None")

int glutLayerGet(GLenum type);
DOC(glutLayerGet, "glutLayerGet(type) -> None")
#endif

#if API_VERSION >= 7

void glutWarpPointer(int x, int y);
DOC(glutWarpPointer, "glutWarpPointer(x, y) -> None")

/* GLUT video resize sub-API. */
int glutVideoResizeGet(GLenum param);
DOC(glutVideoResizeGet, "glutVideoResizeGet(param) -> None")

void glutSetupVideoResizing(void);
DOC(glutSetupVideoResizing, "glutSetupVideoResizing() -> None")

void glutStopVideoResizing(void);
DOC(glutStopVideoResizing, "glutStopVideoResizing() -> None")

void glutVideoResize(int x, int y, int width, int height);
DOC(glutVideoResize, "glutVideoResize(x, y, width, height) -> None")

void glutVideoPan(int x, int y, int width, int height);
DOC(glutVideoPan, "glutVideoPan(x, y, width, height) -> None")

#endif

#if API_VERSION >= 9

void glutInitDisplayString(const char *string);
DOC(glutInitDisplayString, "glutInitDisplayString(string) -> None")

int glutBitmapLength(void *font, const unsigned char *string);
DOC(glutBitmapLength, "glutBitmapLength(font, string) -> None")

int glutStrokeLength(void *font, const unsigned char *string);
DOC(glutStrokeLength, "glutStrokeLength(font, string) -> None")

/* GLUT debugging sub-API. */
void glutReportErrors(void);
DOC(glutReportErrors, "glutReportErrors() -> None")

#endif

#if API_VERSION >= 11

void glutPostWindowRedisplay(int win);
DOC(glutPostWindowRedisplay, "glutPostWindowRedisplay(win) -> None")

void glutPostWindowOverlayRedisplay(int win);
DOC(glutPostWindowOverlayRedisplay, "glutPostWindowOverlayRedisplay(win) -> None")

#endif

#if API_VERSION >= 13

void glutIgnoreKeyRepeat(int ignore);
DOC(glutIgnoreKeyRepeat, "glutIgnoreKeyRepeat() -> None")

void glutSetKeyRepeat(int repeatMode);
DOC(glutSetKeyRepeat, "glutSetKeyRepeat(repeatMode) -> None")

void glutForceJoystickFunc(void);
DOC(glutForceJoystickFunc, "glutForceJoystickFunc() -> None")

void glutGameModeString(const char *string);
DOC(glutGameModeString, "glutGameModeString(string) -> None")

int glutEnterGameMode(void);
DOC(glutEnterGameMode, "glutEnterGameMode() -> None")

void glutLeaveGameMode(void);
DOC(glutLeaveGameMode, "glutLeaveGameMode() -> None")

int glutGameModeGet(GLenum mode);
DOC(glutGameModeGet, "glutGameModeGet(mode) -> None")

#endif

#if API_VERSION >= 20 /* freeglut/openglut */
/*
 * Process loop function, see freeglut_main.c
 */
void     glutMainLoopEvent( void );
DOC(glutMainLoopEvent, "glutMainLoopEvent() Run one iteration of GLUT mainloop (FreeGLUT extension)" )
void     glutLeaveMainLoop( void );
DOC(glutLeaveMainLoop, "glutLeaveMainLoop() Terminate the GLUT mainloop without terminating application (FreeGLUT extension)" )

/*
 * Window-specific callback functions, see freeglut_callbacks.c
 */

%{
void MouseWheelCallback(int button, int state, int x, int y)
{
    eval_4int_args(getCallback("MouseWheel"), button, state, x, y);
}

WIN_CALLBACK(MouseWheel)
%}

%name(glutMouseWheelFunc) void _glutMouseWheelFunc(PyObject * pyfunc);
DOC(glutMouseWheelFunc, "glutMouseWheelFunc(func) -> Register handler for mouse-wheel event taking (button,state,x,y) (FreeGLUT extension)")


%{
void CloseCallback(void)
{
    eval_no_args(getCallback("Close"));
}

WIN_CALLBACK(Close)
%}

%name(glutCloseFunc) void _glutCloseFunc(PyObject * pyfunc);
DOC(glutCloseFunc, "glutCloseFunc(func) -> Register handler for close-of-window event taking no arguments (FreeGLUT extension)")
/* glutWMCloseFunc is deprecated, so not wrapped */


/* MenuDestroy wrapper has not been tested yet (2004-10-05) */
%{
void MenuDestroyCallback(void)
{
    eval_no_args(getCallback("MenuDestroy"));
}

WIN_CALLBACK(MenuDestroy)
%}

%name(glutMenuDestroyFunc) void _glutMenuDestroyFunc(PyObject * pyfunc);
DOC(glutMenuDestroyFunc, "glutMenuDestroyFunc(func) -> Register handler for destruction-of-menu event taking no arguments (FreeGLUT extension)")

/*
 * State setting and retrieval functions, see freeglut_state.c
 */
 /* glutSetOption doesn't seem to do anything on my Gentoo box :( */
void     glutSetOption ( GLenum option_flag, int value ) ;

/* These are wrapped, but don't expect them to work... */
void*    glutGetWindowData( void );
void     glutSetWindowData(void* data);
void*    glutGetMenuData( void );
void     glutSetMenuData(void* data);

/*
 * Font stuff, see freeglut_font.c
 */
 /* these seem to work, but produce weird arrangements with embedded newlines in the strings */
int      glutBitmapHeight( void* font );
GLfloat  glutStrokeHeight( void* font );
void     glutBitmapString( void* font, const unsigned char *string );
void     glutStrokeString( void* font, const unsigned char *string );

/*
 * Geometry functions, see freeglut_geometry.c
 */

void     glutWireRhombicDodecahedron( void );
void     glutSolidRhombicDodecahedron( void );
void     glutWireSierpinskiSponge ( int num_levels, GLdouble offset[3], GLdouble scale ) ;
void     glutSolidSierpinskiSponge ( int num_levels, GLdouble offset[3], GLdouble scale ) ;
void     glutWireCylinder( GLdouble radius, GLdouble height, GLint slices, GLint stacks);
void     glutSolidCylinder( GLdouble radius, GLdouble height, GLint slices, GLint stacks);

/*
 * Extension functions, see freeglut_ext.c
 */
/* this almost certainly will return useless values for Python */
void *  glutGetProcAddress( const char *procName );

#endif /* freeglut */


%{
PyObject *__info()
{
	return PyList_New(0);
}
%}

PyObject *__info();



/* Glut Defines */

#define GLUT_XLIB_IMPLEMENTATION API_VERSION

#if API_VERSION >= 5
#define GLUT_API_VERSION 3
#endif

#if API_VERSION >= 2 && API_VERSION < 5
#define GLUT_API_VERSION 2
#endif

#if API_VERSION == 1
#define GLUT_API_VERSION 1
#endif

/* Display mode bit masks. */
#define GLUT_RGB			0
#define GLUT_RGBA			GLUT_RGB
#define GLUT_INDEX			1
#define GLUT_SINGLE			0
#define GLUT_DOUBLE			2
#define GLUT_ACCUM			4
#define GLUT_ALPHA			8
#define GLUT_DEPTH			16
#define GLUT_STENCIL			32

/* Mouse buttons. */
#define GLUT_LEFT_BUTTON		0
#define GLUT_MIDDLE_BUTTON		1
#define GLUT_RIGHT_BUTTON		2

/* Mouse button  state. */
#define GLUT_DOWN			0
#define GLUT_UP				1


/* Entry/exit  state. */
#define GLUT_LEFT			0
#define GLUT_ENTERED			1

/* Menu usage  state. */
#define GLUT_MENU_NOT_IN_USE		0
#define GLUT_MENU_IN_USE		1

/* Visibility  state. */
#define GLUT_NOT_VISIBLE		0
#define GLUT_VISIBLE			1

/* Window status  state. */
#define GLUT_HIDDEN			0
#define GLUT_FULLY_RETAINED		1
#define GLUT_PARTIALLY_RETAINED		2
#define GLUT_FULLY_COVERED		3

/* Color index component selection values. */
#define GLUT_RED			0
#define GLUT_GREEN			1
#define GLUT_BLUE			2

/* Stroke font constants (use these in GLUT program). */
#define GLUT_STROKE_ROMAN		0
#define GLUT_STROKE_MONO_ROMAN	1

/* Bitmap font constants (use these in GLUT program). */
#define GLUT_BITMAP_9_BY_15		2
#define GLUT_BITMAP_8_BY_13		3
#define GLUT_BITMAP_TIMES_ROMAN_10	4
#define GLUT_BITMAP_TIMES_ROMAN_24	5

/* glutGet parameters. */
#define GLUT_WINDOW_X			100
#define GLUT_WINDOW_Y			101
#define GLUT_WINDOW_WIDTH		102
#define GLUT_WINDOW_HEIGHT		103
#define GLUT_WINDOW_BUFFER_SIZE		104
#define GLUT_WINDOW_STENCIL_SIZE	105
#define GLUT_WINDOW_DEPTH_SIZE		106
#define GLUT_WINDOW_RED_SIZE		107
#define GLUT_WINDOW_GREEN_SIZE		108
#define GLUT_WINDOW_BLUE_SIZE		109
#define GLUT_WINDOW_ALPHA_SIZE		110
#define GLUT_WINDOW_ACCUM_RED_SIZE	111
#define GLUT_WINDOW_ACCUM_GREEN_SIZE	112
#define GLUT_WINDOW_ACCUM_BLUE_SIZE	113
#define GLUT_WINDOW_ACCUM_ALPHA_SIZE	114
#define GLUT_WINDOW_DOUBLEBUFFER	115
#define GLUT_WINDOW_RGBA		116
#define GLUT_WINDOW_PARENT		117
#define GLUT_WINDOW_NUM_CHILDREN	118
#define GLUT_WINDOW_COLORMAP_SIZE	119

#define GLUT_SCREEN_WIDTH		200
#define GLUT_SCREEN_HEIGHT		201
#define GLUT_SCREEN_WIDTH_MM		202
#define GLUT_SCREEN_HEIGHT_MM		203
#define GLUT_MENU_NUM_ITEMS		300
#define GLUT_DISPLAY_MODE_POSSIBLE	400
#define GLUT_INIT_WINDOW_X		500
#define GLUT_INIT_WINDOW_Y		501
#define GLUT_INIT_WINDOW_WIDTH		502
#define GLUT_INIT_WINDOW_HEIGHT		503
#define GLUT_INIT_DISPLAY_MODE		504


#if API_VERSION >= 2

#define GLUT_MULTISAMPLE		128
#define GLUT_STEREO			256

/* function keys */
#define GLUT_KEY_F1			1
#define GLUT_KEY_F2			2
#define GLUT_KEY_F3			3
#define GLUT_KEY_F4			4
#define GLUT_KEY_F5			5
#define GLUT_KEY_F6			6
#define GLUT_KEY_F7			7
#define GLUT_KEY_F8			8
#define GLUT_KEY_F9			9
#define GLUT_KEY_F10			10
#define GLUT_KEY_F11			11
#define GLUT_KEY_F12			12
/* directional keys */
#define GLUT_KEY_LEFT			100
#define GLUT_KEY_UP			101
#define GLUT_KEY_RIGHT			102
#define GLUT_KEY_DOWN			103
#define GLUT_KEY_PAGE_UP		104
#define GLUT_KEY_PAGE_DOWN		105
#define GLUT_KEY_HOME			106
#define GLUT_KEY_END			107
#define GLUT_KEY_INSERT			108


#define GLUT_WINDOW_NUM_SAMPLES		120
#define GLUT_WINDOW_STEREO		121
#define GLUT_ELAPSED_TIME		700

/* glutDeviceGet parameters. */
#define GLUT_HAS_KEYBOARD		600
#define GLUT_HAS_MOUSE			601
#define GLUT_HAS_SPACEBALL		602
#define GLUT_HAS_DIAL_AND_BUTTON_BOX	603
#define GLUT_HAS_TABLET			604
#define GLUT_NUM_MOUSE_BUTTONS		605
#define GLUT_NUM_SPACEBALL_BUTTONS	606
#define GLUT_NUM_BUTTON_BOX_BUTTONS	607
#define GLUT_NUM_DIALS			608
#define GLUT_NUM_TABLET_BUTTONS		609

#endif

#if API_VERSION >= 5
/* This interface represents the features
	which should only be included if GLUT_API_VERSION
	is 3 or above.  Based on PyGLUT
*/
#define GLUT_LUMINANCE			512

#define GLUT_BITMAP_HELVETICA_10	6
#define GLUT_BITMAP_HELVETICA_12	7
#define GLUT_BITMAP_HELVETICA_18	8
#define GLUT_WINDOW_CURSOR		122

/* glutLayerGet parameters. */
#define GLUT_OVERLAY_POSSIBLE           800
#define GLUT_LAYER_IN_USE		801
#define GLUT_HAS_OVERLAY		802
#define GLUT_TRANSPARENT_INDEX		803
#define GLUT_NORMAL_DAMAGED		804
#define GLUT_OVERLAY_DAMAGED		805
/* glutUseLayer parameters. */
#define GLUT_NORMAL			0 /* These two are #defined earlier in the file(???). */
#define GLUT_OVERLAY			1

/* glutGetModifiers return mask. */
#define GLUT_ACTIVE_SHIFT               1
#define GLUT_ACTIVE_CTRL                2
#define GLUT_ACTIVE_ALT                 4

/* glutSetCursor parameters. 
# Basic arrows. */
#define GLUT_CURSOR_RIGHT_ARROW		0
#define GLUT_CURSOR_LEFT_ARROW		1
/* Symbolic cursor shapes. */
#define GLUT_CURSOR_INFO		2
#define GLUT_CURSOR_DESTROY		3
#define GLUT_CURSOR_HELP		4
#define GLUT_CURSOR_CYCLE		5
#define GLUT_CURSOR_SPRAY		6
#define GLUT_CURSOR_WAIT		7
#define GLUT_CURSOR_TEXT		8
#define GLUT_CURSOR_CROSSHAIR		9
/* Directional cursors. */
#define GLUT_CURSOR_UP_DOWN		10
#define GLUT_CURSOR_LEFT_RIGHT		11
/* Sizing cursors. */
#define GLUT_CURSOR_TOP_SIDE		12
#define GLUT_CURSOR_BOTTOM_SIDE		13
#define GLUT_CURSOR_LEFT_SIDE		14
#define GLUT_CURSOR_RIGHT_SIDE		15
#define GLUT_CURSOR_TOP_LEFT_CORNER	16
#define GLUT_CURSOR_TOP_RIGHT_CORNER	17
#define GLUT_CURSOR_BOTTOM_RIGHT_CORNER	18
#define GLUT_CURSOR_BOTTOM_LEFT_CORNER	19
/* Inherit from parent window. */
#define GLUT_CURSOR_INHERIT		100
/* Blank cursor. */
#define GLUT_CURSOR_NONE		101
/* Fullscreen crosshair (if available). */
#define GLUT_CURSOR_FULL_CROSSHAIR	102

#endif


#if API_VERSION >= 7

/* glutVideoResizeGet parameters. */
#define GLUT_VIDEO_RESIZE_POSSIBLE	900
#define GLUT_VIDEO_RESIZE_IN_USE	901
#define GLUT_VIDEO_RESIZE_X_DELTA	902
#define GLUT_VIDEO_RESIZE_Y_DELTA	903
#define GLUT_VIDEO_RESIZE_WIDTH_DELTA	904
#define GLUT_VIDEO_RESIZE_HEIGHT_DELTA	905
#define GLUT_VIDEO_RESIZE_X		906
#define GLUT_VIDEO_RESIZE_Y		907
#define GLUT_VIDEO_RESIZE_WIDTH		908
#define GLUT_VIDEO_RESIZE_HEIGHT	909

#endif


#if API_VERSION >= 13

#define GLUT_WINDOW_FORMAT_ID		123

#define GLUT_DEVICE_IGNORE_KEY_REPEAT   610
#define GLUT_DEVICE_KEY_REPEAT          611
#define GLUT_HAS_JOYSTICK		612
#define GLUT_OWNS_JOYSTICK		613
#define GLUT_JOYSTICK_BUTTONS		614
#define GLUT_JOYSTICK_AXES		615
#define GLUT_JOYSTICK_POLL_RATE		616

/* glutSetKeyRepeat modes. */
#define GLUT_KEY_REPEAT_OFF		0
#define GLUT_KEY_REPEAT_ON		1
#define GLUT_KEY_REPEAT_DEFAULT		2

/* Joystick button masks. */
#define GLUT_JOYSTICK_BUTTON_A		1
#define GLUT_JOYSTICK_BUTTON_B		2
#define GLUT_JOYSTICK_BUTTON_C		4
#define GLUT_JOYSTICK_BUTTON_D		8

/* GLUT game mode sub-API. 
# glutGameModeGet. */
#define GLUT_GAME_MODE_ACTIVE           0
#define GLUT_GAME_MODE_POSSIBLE         1
#define GLUT_GAME_MODE_WIDTH            2
#define GLUT_GAME_MODE_HEIGHT           3
#define GLUT_GAME_MODE_PIXEL_DEPTH      4
#define GLUT_GAME_MODE_REFRESH_RATE     5
#define GLUT_GAME_MODE_DISPLAY_CHANGED  6

#endif



/* Rest of the file is nonstandard extensions by FreeGLUT/OpenGLUT */
#if API_VERSION >= 20
%{
#include <GL/freeglut_ext.h>
%}
/*
 * GLUT API Extension macro definitions -- behaviour when the user clicks on an "x" to close a window
 */
#define GLUT_ACTION_EXIT                         0
#define GLUT_ACTION_GLUTMAINLOOP_RETURNS         1
#define GLUT_ACTION_CONTINUE_EXECUTION           2

/*
 * Create a new rendering context when the user opens a new window?
 */
#define GLUT_CREATE_NEW_CONTEXT                  0
#define GLUT_USE_CURRENT_CONTEXT                 1

/*
 * GLUT API Extension macro definitions -- the glutGet parameters
 */
#define  GLUT_ACTION_ON_WINDOW_CLOSE        0x01F9

#define  GLUT_WINDOW_BORDER_WIDTH           0x01FA
#define  GLUT_WINDOW_HEADER_HEIGHT          0x01FB

#define  GLUT_VERSION                       0x01FC

#define  GLUT_RENDERING_CONTEXT             0x01FD



#endif

