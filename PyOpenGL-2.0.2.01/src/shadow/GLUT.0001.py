# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _GLUT

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name) or (name == "thisown"):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


__version__ = _GLUT.__version__
__date__ = _GLUT.__date__
__api_version__ = _GLUT.__api_version__
__author__ = _GLUT.__author__
__credits__ = _GLUT.__credits__
__doc__ = _GLUT.__doc__

glutInit = _GLUT.glutInit

glutInitDisplayMode = _GLUT.glutInitDisplayMode

glutInitWindowPosition = _GLUT.glutInitWindowPosition

glutInitWindowSize = _GLUT.glutInitWindowSize

glutMainLoop = _GLUT.glutMainLoop

glutDisplayFunc = _GLUT.glutDisplayFunc

glutReshapeFunc = _GLUT.glutReshapeFunc

glutKeyboardFunc = _GLUT.glutKeyboardFunc

glutMouseFunc = _GLUT.glutMouseFunc

glutMotionFunc = _GLUT.glutMotionFunc

glutPassiveMotionFunc = _GLUT.glutPassiveMotionFunc

glutEntryFunc = _GLUT.glutEntryFunc

glutVisibilityFunc = _GLUT.glutVisibilityFunc

glutIdleFunc = _GLUT.glutIdleFunc

glutTimerFunc = _GLUT.glutTimerFunc

glutMenuStateFunc = _GLUT.glutMenuStateFunc

glutCreateWindow = _GLUT.glutCreateWindow

glutCreateSubWindow = _GLUT.glutCreateSubWindow

glutDestroyWindow = _GLUT.glutDestroyWindow

glutPostRedisplay = _GLUT.glutPostRedisplay

glutSwapBuffers = _GLUT.glutSwapBuffers

glutGetWindow = _GLUT.glutGetWindow

glutSetWindow = _GLUT.glutSetWindow

glutSetWindowTitle = _GLUT.glutSetWindowTitle

glutSetIconTitle = _GLUT.glutSetIconTitle

glutPositionWindow = _GLUT.glutPositionWindow

glutReshapeWindow = _GLUT.glutReshapeWindow

glutPopWindow = _GLUT.glutPopWindow

glutPushWindow = _GLUT.glutPushWindow

glutIconifyWindow = _GLUT.glutIconifyWindow

glutShowWindow = _GLUT.glutShowWindow

glutHideWindow = _GLUT.glutHideWindow

glutCreateMenu = _GLUT.glutCreateMenu

glutDestroyMenu = _GLUT.glutDestroyMenu

glutGetMenu = _GLUT.glutGetMenu

glutSetMenu = _GLUT.glutSetMenu

glutAddMenuEntry = _GLUT.glutAddMenuEntry

glutAddSubMenu = _GLUT.glutAddSubMenu

glutChangeToMenuEntry = _GLUT.glutChangeToMenuEntry

glutChangeToSubMenu = _GLUT.glutChangeToSubMenu

glutRemoveMenuItem = _GLUT.glutRemoveMenuItem

glutAttachMenu = _GLUT.glutAttachMenu

glutDetachMenu = _GLUT.glutDetachMenu

glutSetColor = _GLUT.glutSetColor

glutGetColor = _GLUT.glutGetColor

glutCopyColormap = _GLUT.glutCopyColormap

glutGet = _GLUT.glutGet

glutDeviceGet = _GLUT.glutDeviceGet

glutBitmapCharacter = _GLUT.glutBitmapCharacter

glutBitmapWidth = _GLUT.glutBitmapWidth

glutStrokeCharacter = _GLUT.glutStrokeCharacter

glutStrokeWidth = _GLUT.glutStrokeWidth

glutWireSphere = _GLUT.glutWireSphere

glutSolidSphere = _GLUT.glutSolidSphere

glutWireCone = _GLUT.glutWireCone

glutSolidCone = _GLUT.glutSolidCone

glutWireCube = _GLUT.glutWireCube

glutSolidCube = _GLUT.glutSolidCube

glutWireTorus = _GLUT.glutWireTorus

glutSolidTorus = _GLUT.glutSolidTorus

glutWireDodecahedron = _GLUT.glutWireDodecahedron

glutSolidDodecahedron = _GLUT.glutSolidDodecahedron

glutWireTeapot = _GLUT.glutWireTeapot

glutSolidTeapot = _GLUT.glutSolidTeapot

glutWireOctahedron = _GLUT.glutWireOctahedron

glutSolidOctahedron = _GLUT.glutSolidOctahedron

glutWireTetrahedron = _GLUT.glutWireTetrahedron

glutSolidTetrahedron = _GLUT.glutSolidTetrahedron

glutWireIcosahedron = _GLUT.glutWireIcosahedron

glutSolidIcosahedron = _GLUT.glutSolidIcosahedron

__info = _GLUT.__info
GLUT_XLIB_IMPLEMENTATION = _GLUT.GLUT_XLIB_IMPLEMENTATION
GLUT_API_VERSION = _GLUT.GLUT_API_VERSION
GLUT_RGB = _GLUT.GLUT_RGB
GLUT_RGBA = _GLUT.GLUT_RGBA
GLUT_INDEX = _GLUT.GLUT_INDEX
GLUT_SINGLE = _GLUT.GLUT_SINGLE
GLUT_DOUBLE = _GLUT.GLUT_DOUBLE
GLUT_ACCUM = _GLUT.GLUT_ACCUM
GLUT_ALPHA = _GLUT.GLUT_ALPHA
GLUT_DEPTH = _GLUT.GLUT_DEPTH
GLUT_STENCIL = _GLUT.GLUT_STENCIL
GLUT_LEFT_BUTTON = _GLUT.GLUT_LEFT_BUTTON
GLUT_MIDDLE_BUTTON = _GLUT.GLUT_MIDDLE_BUTTON
GLUT_RIGHT_BUTTON = _GLUT.GLUT_RIGHT_BUTTON
GLUT_DOWN = _GLUT.GLUT_DOWN
GLUT_UP = _GLUT.GLUT_UP
GLUT_LEFT = _GLUT.GLUT_LEFT
GLUT_ENTERED = _GLUT.GLUT_ENTERED
GLUT_MENU_NOT_IN_USE = _GLUT.GLUT_MENU_NOT_IN_USE
GLUT_MENU_IN_USE = _GLUT.GLUT_MENU_IN_USE
GLUT_NOT_VISIBLE = _GLUT.GLUT_NOT_VISIBLE
GLUT_VISIBLE = _GLUT.GLUT_VISIBLE
GLUT_HIDDEN = _GLUT.GLUT_HIDDEN
GLUT_FULLY_RETAINED = _GLUT.GLUT_FULLY_RETAINED
GLUT_PARTIALLY_RETAINED = _GLUT.GLUT_PARTIALLY_RETAINED
GLUT_FULLY_COVERED = _GLUT.GLUT_FULLY_COVERED
GLUT_RED = _GLUT.GLUT_RED
GLUT_GREEN = _GLUT.GLUT_GREEN
GLUT_BLUE = _GLUT.GLUT_BLUE
GLUT_STROKE_ROMAN = _GLUT.GLUT_STROKE_ROMAN
GLUT_STROKE_MONO_ROMAN = _GLUT.GLUT_STROKE_MONO_ROMAN
GLUT_BITMAP_9_BY_15 = _GLUT.GLUT_BITMAP_9_BY_15
GLUT_BITMAP_8_BY_13 = _GLUT.GLUT_BITMAP_8_BY_13
GLUT_BITMAP_TIMES_ROMAN_10 = _GLUT.GLUT_BITMAP_TIMES_ROMAN_10
GLUT_BITMAP_TIMES_ROMAN_24 = _GLUT.GLUT_BITMAP_TIMES_ROMAN_24
GLUT_WINDOW_X = _GLUT.GLUT_WINDOW_X
GLUT_WINDOW_Y = _GLUT.GLUT_WINDOW_Y
GLUT_WINDOW_WIDTH = _GLUT.GLUT_WINDOW_WIDTH
GLUT_WINDOW_HEIGHT = _GLUT.GLUT_WINDOW_HEIGHT
GLUT_WINDOW_BUFFER_SIZE = _GLUT.GLUT_WINDOW_BUFFER_SIZE
GLUT_WINDOW_STENCIL_SIZE = _GLUT.GLUT_WINDOW_STENCIL_SIZE
GLUT_WINDOW_DEPTH_SIZE = _GLUT.GLUT_WINDOW_DEPTH_SIZE
GLUT_WINDOW_RED_SIZE = _GLUT.GLUT_WINDOW_RED_SIZE
GLUT_WINDOW_GREEN_SIZE = _GLUT.GLUT_WINDOW_GREEN_SIZE
GLUT_WINDOW_BLUE_SIZE = _GLUT.GLUT_WINDOW_BLUE_SIZE
GLUT_WINDOW_ALPHA_SIZE = _GLUT.GLUT_WINDOW_ALPHA_SIZE
GLUT_WINDOW_ACCUM_RED_SIZE = _GLUT.GLUT_WINDOW_ACCUM_RED_SIZE
GLUT_WINDOW_ACCUM_GREEN_SIZE = _GLUT.GLUT_WINDOW_ACCUM_GREEN_SIZE
GLUT_WINDOW_ACCUM_BLUE_SIZE = _GLUT.GLUT_WINDOW_ACCUM_BLUE_SIZE
GLUT_WINDOW_ACCUM_ALPHA_SIZE = _GLUT.GLUT_WINDOW_ACCUM_ALPHA_SIZE
GLUT_WINDOW_DOUBLEBUFFER = _GLUT.GLUT_WINDOW_DOUBLEBUFFER
GLUT_WINDOW_RGBA = _GLUT.GLUT_WINDOW_RGBA
GLUT_WINDOW_PARENT = _GLUT.GLUT_WINDOW_PARENT
GLUT_WINDOW_NUM_CHILDREN = _GLUT.GLUT_WINDOW_NUM_CHILDREN
GLUT_WINDOW_COLORMAP_SIZE = _GLUT.GLUT_WINDOW_COLORMAP_SIZE
GLUT_SCREEN_WIDTH = _GLUT.GLUT_SCREEN_WIDTH
GLUT_SCREEN_HEIGHT = _GLUT.GLUT_SCREEN_HEIGHT
GLUT_SCREEN_WIDTH_MM = _GLUT.GLUT_SCREEN_WIDTH_MM
GLUT_SCREEN_HEIGHT_MM = _GLUT.GLUT_SCREEN_HEIGHT_MM
GLUT_MENU_NUM_ITEMS = _GLUT.GLUT_MENU_NUM_ITEMS
GLUT_DISPLAY_MODE_POSSIBLE = _GLUT.GLUT_DISPLAY_MODE_POSSIBLE
GLUT_INIT_WINDOW_X = _GLUT.GLUT_INIT_WINDOW_X
GLUT_INIT_WINDOW_Y = _GLUT.GLUT_INIT_WINDOW_Y
GLUT_INIT_WINDOW_WIDTH = _GLUT.GLUT_INIT_WINDOW_WIDTH
GLUT_INIT_WINDOW_HEIGHT = _GLUT.GLUT_INIT_WINDOW_HEIGHT
GLUT_INIT_DISPLAY_MODE = _GLUT.GLUT_INIT_DISPLAY_MODE

