# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _coordinate_frame

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


__version__ = _coordinate_frame.__version__
__date__ = _coordinate_frame.__date__
__api_version__ = _coordinate_frame.__api_version__
__author__ = _coordinate_frame.__author__
__doc__ = _coordinate_frame.__doc__

glTangent3bEXT = _coordinate_frame.glTangent3bEXT

glTangent3sEXT = _coordinate_frame.glTangent3sEXT

glTangent3iEXT = _coordinate_frame.glTangent3iEXT

glTangent3fEXT = _coordinate_frame.glTangent3fEXT

glTangent3dEXT = _coordinate_frame.glTangent3dEXT

glTangent3bvEXT = _coordinate_frame.glTangent3bvEXT

glTangent3svEXT = _coordinate_frame.glTangent3svEXT

glTangent3ivEXT = _coordinate_frame.glTangent3ivEXT

glTangent3fvEXT = _coordinate_frame.glTangent3fvEXT

glTangent3dvEXT = _coordinate_frame.glTangent3dvEXT

glBinomial3bEXT = _coordinate_frame.glBinomial3bEXT

glBinomial3sEXT = _coordinate_frame.glBinomial3sEXT

glBinomial3iEXT = _coordinate_frame.glBinomial3iEXT

glBinomial3fEXT = _coordinate_frame.glBinomial3fEXT

glBinomial3dEXT = _coordinate_frame.glBinomial3dEXT

glBinomial3bvEXT = _coordinate_frame.glBinomial3bvEXT

glBinomial3svEXT = _coordinate_frame.glBinomial3svEXT

glBinomial3ivEXT = _coordinate_frame.glBinomial3ivEXT

glBinomial3fvEXT = _coordinate_frame.glBinomial3fvEXT

glBinomial3dvEXT = _coordinate_frame.glBinomial3dvEXT

glTangentPointerEXT = _coordinate_frame.glTangentPointerEXT

glTangentPointerbEXT = _coordinate_frame.glTangentPointerbEXT

glTangentPointersEXT = _coordinate_frame.glTangentPointersEXT

glTangentPointeriEXT = _coordinate_frame.glTangentPointeriEXT

glTangentPointerfEXT = _coordinate_frame.glTangentPointerfEXT

glTangentPointerdEXT = _coordinate_frame.glTangentPointerdEXT

glBinomialPointerEXT = _coordinate_frame.glBinomialPointerEXT

glBinomialPointerbEXT = _coordinate_frame.glBinomialPointerbEXT

glBinomialPointersEXT = _coordinate_frame.glBinomialPointersEXT

glBinomialPointeriEXT = _coordinate_frame.glBinomialPointeriEXT

glBinomialPointerfEXT = _coordinate_frame.glBinomialPointerfEXT

glBinomialPointerdEXT = _coordinate_frame.glBinomialPointerdEXT

glInitCoordinateFrameEXT = _coordinate_frame.glInitCoordinateFrameEXT

glInitCoordFrameEXT = _coordinate_frame.glInitCoordFrameEXT

__info = _coordinate_frame.__info
GL_TANGENT_ARRAY_EXT = _coordinate_frame.GL_TANGENT_ARRAY_EXT
GL_BINORMAL_ARRAY_EXT = _coordinate_frame.GL_BINORMAL_ARRAY_EXT
GL_CURRENT_TANGENT_EXT = _coordinate_frame.GL_CURRENT_TANGENT_EXT
GL_CURRENT_BINORMAL_EXT = _coordinate_frame.GL_CURRENT_BINORMAL_EXT
GL_TANGENT_ARRAY_TYPE_EXT = _coordinate_frame.GL_TANGENT_ARRAY_TYPE_EXT
GL_TANGENT_ARRAY_STRIDE_EXT = _coordinate_frame.GL_TANGENT_ARRAY_STRIDE_EXT
GL_BINORMAL_ARRAY_TYPE_EXT = _coordinate_frame.GL_BINORMAL_ARRAY_TYPE_EXT
GL_BINORMAL_ARRAY_STRIDE_EXT = _coordinate_frame.GL_BINORMAL_ARRAY_STRIDE_EXT
GL_MAP1_TANGENT_EXT = _coordinate_frame.GL_MAP1_TANGENT_EXT
GL_MAP2_TANGENT_EXT = _coordinate_frame.GL_MAP2_TANGENT_EXT
GL_MAP1_BINORMAL_EXT = _coordinate_frame.GL_MAP1_BINORMAL_EXT
GL_MAP2_BINORMAL_EXT = _coordinate_frame.GL_MAP2_BINORMAL_EXT

