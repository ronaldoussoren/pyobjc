# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _GLU__init__

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


__version__ = _GLU__init__.__version__
__date__ = _GLU__init__.__date__
__api_version__ = _GLU__init__.__api_version__
__author__ = _GLU__init__.__author__
__doc__ = _GLU__init__.__doc__
#-------------- SHADOW WRAPPERS ------------------


gluErrorString = _GLU__init__.gluErrorString

gluOrtho2D = _GLU__init__.gluOrtho2D

gluPerspective = _GLU__init__.gluPerspective

__gluPickMatrix = _GLU__init__.__gluPickMatrix
def gluPickMatrix(x, y, width, height, viewport = None):
    'gluPickMatrix(x, y, width, height, viewport = None) -> None'
    return __gluPickMatrix(x, y, width, height, viewport)


gluLookAt = _GLU__init__.gluLookAt

__gluProject = _GLU__init__.__gluProject
def gluProject(objx, objy, objz, modelMatrix = None, projMatrix = None, viewport = None):
    'gluProject(objx, objy, objz, modelMatrix = None, projMatrix = None, viewport = None) -> (winx, winy, winz)'
    return __gluProject(objx, objy, objz, modelMatrix, projMatrix, viewport)


__gluUnProject = _GLU__init__.__gluUnProject
def gluUnProject(winx, winy, winz, modelMatrix = None, projMatrix = None, viewport = None):
    'gluUnProject(winx, winy, winz, modelMatrix = None, projMatrix = None, viewport = None) -> (objx, objy, objz)'
    return __gluUnProject(winx, winy, winz, modelMatrix, projMatrix, viewport)


gluScaleImage = _GLU__init__.gluScaleImage

gluScaleImageb = _GLU__init__.gluScaleImageb

gluScaleImageub = _GLU__init__.gluScaleImageub

gluScaleImages = _GLU__init__.gluScaleImages

gluScaleImageus = _GLU__init__.gluScaleImageus

gluScaleImagei = _GLU__init__.gluScaleImagei

gluScaleImageui = _GLU__init__.gluScaleImageui

gluScaleImagef = _GLU__init__.gluScaleImagef

gluBuild1DMipmaps = _GLU__init__.gluBuild1DMipmaps

gluBuild1DMipmapsb = _GLU__init__.gluBuild1DMipmapsb

gluBuild1DMipmapsub = _GLU__init__.gluBuild1DMipmapsub

gluBuild1DMipmapss = _GLU__init__.gluBuild1DMipmapss

gluBuild1DMipmapsus = _GLU__init__.gluBuild1DMipmapsus

gluBuild1DMipmapsi = _GLU__init__.gluBuild1DMipmapsi

gluBuild1DMipmapsui = _GLU__init__.gluBuild1DMipmapsui

gluBuild1DMipmapsf = _GLU__init__.gluBuild1DMipmapsf

gluBuild2DMipmaps = _GLU__init__.gluBuild2DMipmaps

gluBuild2DMipmapsb = _GLU__init__.gluBuild2DMipmapsb

gluBuild2DMipmapsub = _GLU__init__.gluBuild2DMipmapsub

gluBuild2DMipmapss = _GLU__init__.gluBuild2DMipmapss

gluBuild2DMipmapsus = _GLU__init__.gluBuild2DMipmapsus

gluBuild2DMipmapsi = _GLU__init__.gluBuild2DMipmapsi

gluBuild2DMipmapsui = _GLU__init__.gluBuild2DMipmapsui

gluBuild2DMipmapsf = _GLU__init__.gluBuild2DMipmapsf

gluNewQuadric = _GLU__init__.gluNewQuadric

gluDeleteQuadric = _GLU__init__.gluDeleteQuadric

gluQuadricNormals = _GLU__init__.gluQuadricNormals

gluQuadricTexture = _GLU__init__.gluQuadricTexture

gluQuadricOrientation = _GLU__init__.gluQuadricOrientation

gluQuadricDrawStyle = _GLU__init__.gluQuadricDrawStyle

gluCylinder = _GLU__init__.gluCylinder

gluDisk = _GLU__init__.gluDisk

gluPartialDisk = _GLU__init__.gluPartialDisk

gluSphere = _GLU__init__.gluSphere

gluQuadricCallback = _GLU__init__.gluQuadricCallback

gluNewTess = _GLU__init__.gluNewTess

gluDeleteTess = _GLU__init__.gluDeleteTess

gluBeginPolygon = _GLU__init__.gluBeginPolygon

gluTessVertex = _GLU__init__.gluTessVertex

gluNextContour = _GLU__init__.gluNextContour

gluEndPolygon = _GLU__init__.gluEndPolygon

gluTessCallback = _GLU__init__.gluTessCallback

gluNewNurbsRenderer = _GLU__init__.gluNewNurbsRenderer

gluDeleteNurbsRenderer = _GLU__init__.gluDeleteNurbsRenderer

gluBeginSurface = _GLU__init__.gluBeginSurface

gluBeginCurve = _GLU__init__.gluBeginCurve

gluEndCurve = _GLU__init__.gluEndCurve

gluEndSurface = _GLU__init__.gluEndSurface

gluBeginTrim = _GLU__init__.gluBeginTrim

gluEndTrim = _GLU__init__.gluEndTrim

gluPwlCurve = _GLU__init__.gluPwlCurve

gluNurbsCurve = _GLU__init__.gluNurbsCurve

gluNurbsSurface = _GLU__init__.gluNurbsSurface

gluLoadSamplingMatrices = _GLU__init__.gluLoadSamplingMatrices

gluNurbsProperty = _GLU__init__.gluNurbsProperty

gluGetNurbsProperty = _GLU__init__.gluGetNurbsProperty

gluNurbsCallback = _GLU__init__.gluNurbsCallback

__gluNurbsCallbackDataEXT = _GLU__init__.__gluNurbsCallbackDataEXT

__gluInitNurbsTessellatorEXT = _GLU__init__.__gluInitNurbsTessellatorEXT
GLU_INVALID_ENUM = _GLU__init__.GLU_INVALID_ENUM
GLU_INVALID_VALUE = _GLU__init__.GLU_INVALID_VALUE
GLU_OUT_OF_MEMORY = _GLU__init__.GLU_OUT_OF_MEMORY
GLU_INCOMPATIBLE_GL_VERSION = _GLU__init__.GLU_INCOMPATIBLE_GL_VERSION
GLU_SMOOTH = _GLU__init__.GLU_SMOOTH
GLU_FLAT = _GLU__init__.GLU_FLAT
GLU_NONE = _GLU__init__.GLU_NONE
GLU_POINT = _GLU__init__.GLU_POINT
GLU_LINE = _GLU__init__.GLU_LINE
GLU_FILL = _GLU__init__.GLU_FILL
GLU_SILHOUETTE = _GLU__init__.GLU_SILHOUETTE
GLU_OUTSIDE = _GLU__init__.GLU_OUTSIDE
GLU_INSIDE = _GLU__init__.GLU_INSIDE
GLU_TESS_MAX_COORD = _GLU__init__.GLU_TESS_MAX_COORD
GLU_TESS_WINDING_RULE = _GLU__init__.GLU_TESS_WINDING_RULE
GLU_TESS_BOUNDARY_ONLY = _GLU__init__.GLU_TESS_BOUNDARY_ONLY
GLU_TESS_TOLERANCE = _GLU__init__.GLU_TESS_TOLERANCE
GLU_TESS_WINDING_ODD = _GLU__init__.GLU_TESS_WINDING_ODD
GLU_TESS_WINDING_NONZERO = _GLU__init__.GLU_TESS_WINDING_NONZERO
GLU_TESS_WINDING_POSITIVE = _GLU__init__.GLU_TESS_WINDING_POSITIVE
GLU_TESS_WINDING_NEGATIVE = _GLU__init__.GLU_TESS_WINDING_NEGATIVE
GLU_TESS_WINDING_ABS_GEQ_TWO = _GLU__init__.GLU_TESS_WINDING_ABS_GEQ_TWO
GLU_TESS_BEGIN = _GLU__init__.GLU_TESS_BEGIN
GLU_TESS_VERTEX = _GLU__init__.GLU_TESS_VERTEX
GLU_TESS_END = _GLU__init__.GLU_TESS_END
GLU_TESS_ERROR = _GLU__init__.GLU_TESS_ERROR
GLU_TESS_EDGE_FLAG = _GLU__init__.GLU_TESS_EDGE_FLAG
GLU_TESS_COMBINE = _GLU__init__.GLU_TESS_COMBINE
GLU_TESS_BEGIN_DATA = _GLU__init__.GLU_TESS_BEGIN_DATA
GLU_TESS_VERTEX_DATA = _GLU__init__.GLU_TESS_VERTEX_DATA
GLU_TESS_END_DATA = _GLU__init__.GLU_TESS_END_DATA
GLU_TESS_ERROR_DATA = _GLU__init__.GLU_TESS_ERROR_DATA
GLU_TESS_EDGE_FLAG_DATA = _GLU__init__.GLU_TESS_EDGE_FLAG_DATA
GLU_TESS_COMBINE_DATA = _GLU__init__.GLU_TESS_COMBINE_DATA
GLU_TESS_ERROR1 = _GLU__init__.GLU_TESS_ERROR1
GLU_TESS_ERROR2 = _GLU__init__.GLU_TESS_ERROR2
GLU_TESS_ERROR3 = _GLU__init__.GLU_TESS_ERROR3
GLU_TESS_ERROR4 = _GLU__init__.GLU_TESS_ERROR4
GLU_TESS_ERROR5 = _GLU__init__.GLU_TESS_ERROR5
GLU_TESS_ERROR6 = _GLU__init__.GLU_TESS_ERROR6
GLU_TESS_ERROR7 = _GLU__init__.GLU_TESS_ERROR7
GLU_TESS_ERROR8 = _GLU__init__.GLU_TESS_ERROR8
GLU_TESS_MISSING_BEGIN_POLYGON = _GLU__init__.GLU_TESS_MISSING_BEGIN_POLYGON
GLU_TESS_MISSING_BEGIN_CONTOUR = _GLU__init__.GLU_TESS_MISSING_BEGIN_CONTOUR
GLU_TESS_MISSING_END_POLYGON = _GLU__init__.GLU_TESS_MISSING_END_POLYGON
GLU_TESS_MISSING_END_CONTOUR = _GLU__init__.GLU_TESS_MISSING_END_CONTOUR
GLU_TESS_COORD_TOO_LARGE = _GLU__init__.GLU_TESS_COORD_TOO_LARGE
GLU_TESS_NEED_COMBINE_CALLBACK = _GLU__init__.GLU_TESS_NEED_COMBINE_CALLBACK
GLU_AUTO_LOAD_MATRIX = _GLU__init__.GLU_AUTO_LOAD_MATRIX
GLU_CULLING = _GLU__init__.GLU_CULLING
GLU_SAMPLING_TOLERANCE = _GLU__init__.GLU_SAMPLING_TOLERANCE
GLU_DISPLAY_MODE = _GLU__init__.GLU_DISPLAY_MODE
GLU_PATH_LENGTH = _GLU__init__.GLU_PATH_LENGTH
GLU_PARAMETRIC_ERROR = _GLU__init__.GLU_PARAMETRIC_ERROR
GLU_DOMAIN_DISTANCE = _GLU__init__.GLU_DOMAIN_DISTANCE
GLU_MAP1_TRIM_2 = _GLU__init__.GLU_MAP1_TRIM_2
GLU_MAP1_TRIM_3 = _GLU__init__.GLU_MAP1_TRIM_3
GLU_OUTLINE_POLYGON = _GLU__init__.GLU_OUTLINE_POLYGON
GLU_OUTLINE_PATCH = _GLU__init__.GLU_OUTLINE_PATCH
GLU_NURBS_ERROR1 = _GLU__init__.GLU_NURBS_ERROR1
GLU_NURBS_ERROR2 = _GLU__init__.GLU_NURBS_ERROR2
GLU_NURBS_ERROR3 = _GLU__init__.GLU_NURBS_ERROR3
GLU_NURBS_ERROR4 = _GLU__init__.GLU_NURBS_ERROR4
GLU_NURBS_ERROR5 = _GLU__init__.GLU_NURBS_ERROR5
GLU_NURBS_ERROR6 = _GLU__init__.GLU_NURBS_ERROR6
GLU_NURBS_ERROR7 = _GLU__init__.GLU_NURBS_ERROR7
GLU_NURBS_ERROR8 = _GLU__init__.GLU_NURBS_ERROR8
GLU_NURBS_ERROR9 = _GLU__init__.GLU_NURBS_ERROR9
GLU_NURBS_ERROR10 = _GLU__init__.GLU_NURBS_ERROR10
GLU_NURBS_ERROR11 = _GLU__init__.GLU_NURBS_ERROR11
GLU_NURBS_ERROR12 = _GLU__init__.GLU_NURBS_ERROR12
GLU_NURBS_ERROR13 = _GLU__init__.GLU_NURBS_ERROR13
GLU_NURBS_ERROR14 = _GLU__init__.GLU_NURBS_ERROR14
GLU_NURBS_ERROR15 = _GLU__init__.GLU_NURBS_ERROR15
GLU_NURBS_ERROR16 = _GLU__init__.GLU_NURBS_ERROR16
GLU_NURBS_ERROR17 = _GLU__init__.GLU_NURBS_ERROR17
GLU_NURBS_ERROR18 = _GLU__init__.GLU_NURBS_ERROR18
GLU_NURBS_ERROR19 = _GLU__init__.GLU_NURBS_ERROR19
GLU_NURBS_ERROR20 = _GLU__init__.GLU_NURBS_ERROR20
GLU_NURBS_ERROR21 = _GLU__init__.GLU_NURBS_ERROR21
GLU_NURBS_ERROR22 = _GLU__init__.GLU_NURBS_ERROR22
GLU_NURBS_ERROR23 = _GLU__init__.GLU_NURBS_ERROR23
GLU_NURBS_ERROR24 = _GLU__init__.GLU_NURBS_ERROR24
GLU_NURBS_ERROR25 = _GLU__init__.GLU_NURBS_ERROR25
GLU_NURBS_ERROR26 = _GLU__init__.GLU_NURBS_ERROR26
GLU_NURBS_ERROR27 = _GLU__init__.GLU_NURBS_ERROR27
GLU_NURBS_ERROR28 = _GLU__init__.GLU_NURBS_ERROR28
GLU_NURBS_ERROR29 = _GLU__init__.GLU_NURBS_ERROR29
GLU_NURBS_ERROR30 = _GLU__init__.GLU_NURBS_ERROR30
GLU_NURBS_ERROR31 = _GLU__init__.GLU_NURBS_ERROR31
GLU_NURBS_ERROR32 = _GLU__init__.GLU_NURBS_ERROR32
GLU_NURBS_ERROR33 = _GLU__init__.GLU_NURBS_ERROR33
GLU_NURBS_ERROR34 = _GLU__init__.GLU_NURBS_ERROR34
GLU_NURBS_ERROR35 = _GLU__init__.GLU_NURBS_ERROR35
GLU_NURBS_ERROR36 = _GLU__init__.GLU_NURBS_ERROR36
GLU_NURBS_ERROR37 = _GLU__init__.GLU_NURBS_ERROR37
GLU_CW = _GLU__init__.GLU_CW
GLU_CCW = _GLU__init__.GLU_CCW
GLU_INTERIOR = _GLU__init__.GLU_INTERIOR
GLU_EXTERIOR = _GLU__init__.GLU_EXTERIOR
GLU_UNKNOWN = _GLU__init__.GLU_UNKNOWN
GLU_BEGIN = _GLU__init__.GLU_BEGIN
GLU_VERTEX = _GLU__init__.GLU_VERTEX
GLU_END = _GLU__init__.GLU_END
GLU_ERROR = _GLU__init__.GLU_ERROR
GLU_EDGE_FLAG = _GLU__init__.GLU_EDGE_FLAG
def __info():
    import string
    return [('GLU_VERSION', GLU_VERSION, 'su'),
    ('GLU_EXTENSIONS', GLU_EXTENSIONS, 'eu')]


GLUerror = _GLU__init__.GLUerror

__api_version__ = _GLU__init__.__api_version__
__author__ = _GLU__init__.__author__
__date__ = _GLU__init__.__date__
__doc__ = _GLU__init__.__doc__
__version__ = _GLU__init__.__version__



