# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _pn_triangles

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


__version__ = _pn_triangles.__version__
__date__ = _pn_triangles.__date__
__api_version__ = _pn_triangles.__api_version__
__author__ = _pn_triangles.__author__
__doc__ = _pn_triangles.__doc__

glPNTrianglesiATI = _pn_triangles.glPNTrianglesiATI

glPNTrianglesfATI = _pn_triangles.glPNTrianglesfATI

glInitPNTrianglesATI = _pn_triangles.glInitPNTrianglesATI

__info = _pn_triangles.__info
GL_MAX_PN_TRIANGLES_TESSELATION_LEVEL_ATI = _pn_triangles.GL_MAX_PN_TRIANGLES_TESSELATION_LEVEL_ATI
GL_PN_TRIANGLES_POINT_MODE_ATI = _pn_triangles.GL_PN_TRIANGLES_POINT_MODE_ATI
GL_PN_TRIANGLES_NORMAL_MODE_ATI = _pn_triangles.GL_PN_TRIANGLES_NORMAL_MODE_ATI
GL_PN_TRIANGLES_TESSELATION_LEVEL_ATI = _pn_triangles.GL_PN_TRIANGLES_TESSELATION_LEVEL_ATI
GL_PN_TRIANGLES_POINT_MODE_LINEAR_ATI = _pn_triangles.GL_PN_TRIANGLES_POINT_MODE_LINEAR_ATI
GL_PN_TRIANGLES_POINT_MODE_CUBIC_ATI = _pn_triangles.GL_PN_TRIANGLES_POINT_MODE_CUBIC_ATI
GL_PN_TRIANGLES_NORMAL_MODE_LINEAR_ATI = _pn_triangles.GL_PN_TRIANGLES_NORMAL_MODE_LINEAR_ATI
GL_PN_TRIANGLES_NORMAL_MODE_QUADRATIC_ATI = _pn_triangles.GL_PN_TRIANGLES_NORMAL_MODE_QUADRATIC_ATI

