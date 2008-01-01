# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _vertex_weighting

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


__version__ = _vertex_weighting.__version__
__date__ = _vertex_weighting.__date__
__api_version__ = _vertex_weighting.__api_version__
__author__ = _vertex_weighting.__author__
__doc__ = _vertex_weighting.__doc__

glVertexWeightfvEXT = _vertex_weighting.glVertexWeightfvEXT

glVertexWeightfEXT = _vertex_weighting.glVertexWeightfEXT

glVertexWeightPointerEXT = _vertex_weighting.glVertexWeightPointerEXT

glVertexWeightPointerfEXT = _vertex_weighting.glVertexWeightPointerfEXT

glInitVertexWeightingEXT = _vertex_weighting.glInitVertexWeightingEXT

__info = _vertex_weighting.__info
GL_VERTEX_WEIGHTING_EXT = _vertex_weighting.GL_VERTEX_WEIGHTING_EXT
GL_MODELVIEW0_EXT = _vertex_weighting.GL_MODELVIEW0_EXT
GL_MODELVIEW1_EXT = _vertex_weighting.GL_MODELVIEW1_EXT
GL_CURRENT_VERTEX_WEIGHT_EXT = _vertex_weighting.GL_CURRENT_VERTEX_WEIGHT_EXT
GL_VERTEX_WEIGHT_ARRAY_EXT = _vertex_weighting.GL_VERTEX_WEIGHT_ARRAY_EXT
GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT = _vertex_weighting.GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT
GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT = _vertex_weighting.GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT
GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT = _vertex_weighting.GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT
GL_MODELVIEW0_STACK_DEPTH_EXT = _vertex_weighting.GL_MODELVIEW0_STACK_DEPTH_EXT
GL_MODELVIEW1_STACK_DEPTH_EXT = _vertex_weighting.GL_MODELVIEW1_STACK_DEPTH_EXT
GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT = _vertex_weighting.GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT

