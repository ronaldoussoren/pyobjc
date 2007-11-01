# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _GLE

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


__version__ = _GLE.__version__
__date__ = _GLE.__date__
__api_version__ = _GLE.__api_version__
__author__ = _GLE.__author__
__doc__ = _GLE.__doc__

gleGetJoinStyle = _GLE.gleGetJoinStyle

gleSetJoinStyle = _GLE.gleSetJoinStyle

gleGetNumSides = _GLE.gleGetNumSides

gleSetNumSides = _GLE.gleSetNumSides

glePolyCylinder = _GLE.glePolyCylinder

glePolyCone = _GLE.glePolyCone

gleExtrusion = _GLE.gleExtrusion

gleTwistExtrusion = _GLE.gleTwistExtrusion

gleSuperExtrusion = _GLE.gleSuperExtrusion

gleSpiral = _GLE.gleSpiral

gleLathe = _GLE.gleLathe

gleHelicoid = _GLE.gleHelicoid

gleToroid = _GLE.gleToroid

gleScrew = _GLE.gleScrew

gleTextureMode = _GLE.gleTextureMode

__info = _GLE.__info
TUBE_JN_RAW = _GLE.TUBE_JN_RAW
TUBE_JN_ANGLE = _GLE.TUBE_JN_ANGLE
TUBE_JN_CUT = _GLE.TUBE_JN_CUT
TUBE_JN_ROUND = _GLE.TUBE_JN_ROUND
TUBE_JN_MASK = _GLE.TUBE_JN_MASK
TUBE_JN_CAP = _GLE.TUBE_JN_CAP
TUBE_NORM_FACET = _GLE.TUBE_NORM_FACET
TUBE_NORM_EDGE = _GLE.TUBE_NORM_EDGE
TUBE_NORM_PATH_EDGE = _GLE.TUBE_NORM_PATH_EDGE
TUBE_NORM_MASK = _GLE.TUBE_NORM_MASK
TUBE_CONTOUR_CLOSED = _GLE.TUBE_CONTOUR_CLOSED
GLE_TEXTURE_ENABLE = _GLE.GLE_TEXTURE_ENABLE
GLE_TEXTURE_STYLE_MASK = _GLE.GLE_TEXTURE_STYLE_MASK
GLE_TEXTURE_VERTEX_FLAT = _GLE.GLE_TEXTURE_VERTEX_FLAT
GLE_TEXTURE_NORMAL_FLAT = _GLE.GLE_TEXTURE_NORMAL_FLAT
GLE_TEXTURE_VERTEX_CYL = _GLE.GLE_TEXTURE_VERTEX_CYL
GLE_TEXTURE_NORMAL_CYL = _GLE.GLE_TEXTURE_NORMAL_CYL
GLE_TEXTURE_VERTEX_SPH = _GLE.GLE_TEXTURE_VERTEX_SPH
GLE_TEXTURE_NORMAL_SPH = _GLE.GLE_TEXTURE_NORMAL_SPH
GLE_TEXTURE_VERTEX_MODEL_FLAT = _GLE.GLE_TEXTURE_VERTEX_MODEL_FLAT
GLE_TEXTURE_NORMAL_MODEL_FLAT = _GLE.GLE_TEXTURE_NORMAL_MODEL_FLAT
GLE_TEXTURE_VERTEX_MODEL_CYL = _GLE.GLE_TEXTURE_VERTEX_MODEL_CYL
GLE_TEXTURE_NORMAL_MODEL_CYL = _GLE.GLE_TEXTURE_NORMAL_MODEL_CYL
GLE_TEXTURE_VERTEX_MODEL_SPH = _GLE.GLE_TEXTURE_VERTEX_MODEL_SPH
GLE_TEXTURE_NORMAL_MODEL_SPH = _GLE.GLE_TEXTURE_NORMAL_MODEL_SPH

