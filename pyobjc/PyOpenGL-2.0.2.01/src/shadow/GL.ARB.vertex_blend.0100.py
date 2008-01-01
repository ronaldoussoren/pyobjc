# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _vertex_blend

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


__version__ = _vertex_blend.__version__
__date__ = _vertex_blend.__date__
__api_version__ = _vertex_blend.__api_version__
__author__ = _vertex_blend.__author__
__doc__ = _vertex_blend.__doc__

glInitVertexBlendARB = _vertex_blend.glInitVertexBlendARB

glWeightbvARB = _vertex_blend.glWeightbvARB

glWeightubvARB = _vertex_blend.glWeightubvARB

glWeightsvARB = _vertex_blend.glWeightsvARB

glWeightusvARB = _vertex_blend.glWeightusvARB

glWeightivARB = _vertex_blend.glWeightivARB

glWeightuivARB = _vertex_blend.glWeightuivARB

glWeightfvARB = _vertex_blend.glWeightfvARB

glWeightdvARB = _vertex_blend.glWeightdvARB

glWeightPointerARB = _vertex_blend.glWeightPointerARB

glWeightPointerubARB = _vertex_blend.glWeightPointerubARB

glWeightPointerbARB = _vertex_blend.glWeightPointerbARB

glWeightPointerusARB = _vertex_blend.glWeightPointerusARB

glWeightPointersARB = _vertex_blend.glWeightPointersARB

glWeightPointeruiARB = _vertex_blend.glWeightPointeruiARB

glWeightPointeriARB = _vertex_blend.glWeightPointeriARB

glWeightPointerfARB = _vertex_blend.glWeightPointerfARB

glWeightPointerdARB = _vertex_blend.glWeightPointerdARB

glWeightBlendARB = _vertex_blend.glWeightBlendARB

__info = _vertex_blend.__info
GL_MAX_VERTEX_UNITS_ARB = _vertex_blend.GL_MAX_VERTEX_UNITS_ARB
GL_ACTIVE_VERTEX_UNITS_ARB = _vertex_blend.GL_ACTIVE_VERTEX_UNITS_ARB
GL_WEIGHT_SUM_UNITY_ARB = _vertex_blend.GL_WEIGHT_SUM_UNITY_ARB
GL_VERTEX_BLEND_ARB = _vertex_blend.GL_VERTEX_BLEND_ARB
GL_MODELVIEW0_ARB = _vertex_blend.GL_MODELVIEW0_ARB
GL_MODELVIEW1_ARB = _vertex_blend.GL_MODELVIEW1_ARB
GL_MODELVIEW2_ARB = _vertex_blend.GL_MODELVIEW2_ARB
GL_MODELVIEW3_ARB = _vertex_blend.GL_MODELVIEW3_ARB
GL_MODELVIEW4_ARB = _vertex_blend.GL_MODELVIEW4_ARB
GL_MODELVIEW5_ARB = _vertex_blend.GL_MODELVIEW5_ARB
GL_MODELVIEW6_ARB = _vertex_blend.GL_MODELVIEW6_ARB
GL_MODELVIEW7_ARB = _vertex_blend.GL_MODELVIEW7_ARB
GL_MODELVIEW8_ARB = _vertex_blend.GL_MODELVIEW8_ARB
GL_MODELVIEW9_ARB = _vertex_blend.GL_MODELVIEW9_ARB
GL_MODELVIEW10_ARB = _vertex_blend.GL_MODELVIEW10_ARB
GL_MODELVIEW11_ARB = _vertex_blend.GL_MODELVIEW11_ARB
GL_MODELVIEW12_ARB = _vertex_blend.GL_MODELVIEW12_ARB
GL_MODELVIEW13_ARB = _vertex_blend.GL_MODELVIEW13_ARB
GL_MODELVIEW14_ARB = _vertex_blend.GL_MODELVIEW14_ARB
GL_MODELVIEW15_ARB = _vertex_blend.GL_MODELVIEW15_ARB
GL_MODELVIEW16_ARB = _vertex_blend.GL_MODELVIEW16_ARB
GL_MODELVIEW17_ARB = _vertex_blend.GL_MODELVIEW17_ARB
GL_MODELVIEW18_ARB = _vertex_blend.GL_MODELVIEW18_ARB
GL_MODELVIEW19_ARB = _vertex_blend.GL_MODELVIEW19_ARB
GL_MODELVIEW20_ARB = _vertex_blend.GL_MODELVIEW20_ARB
GL_MODELVIEW21_ARB = _vertex_blend.GL_MODELVIEW21_ARB
GL_MODELVIEW22_ARB = _vertex_blend.GL_MODELVIEW22_ARB
GL_MODELVIEW23_ARB = _vertex_blend.GL_MODELVIEW23_ARB
GL_MODELVIEW24_ARB = _vertex_blend.GL_MODELVIEW24_ARB
GL_MODELVIEW25_ARB = _vertex_blend.GL_MODELVIEW25_ARB
GL_MODELVIEW26_ARB = _vertex_blend.GL_MODELVIEW26_ARB
GL_MODELVIEW27_ARB = _vertex_blend.GL_MODELVIEW27_ARB
GL_MODELVIEW28_ARB = _vertex_blend.GL_MODELVIEW28_ARB
GL_MODELVIEW29_ARB = _vertex_blend.GL_MODELVIEW29_ARB
GL_MODELVIEW30_ARB = _vertex_blend.GL_MODELVIEW30_ARB
GL_MODELVIEW31_ARB = _vertex_blend.GL_MODELVIEW31_ARB
GL_CURRENT_WEIGHT_ARB = _vertex_blend.GL_CURRENT_WEIGHT_ARB
GL_WEIGHT_ARRAY_TYPE_ARB = _vertex_blend.GL_WEIGHT_ARRAY_TYPE_ARB
GL_WEIGHT_ARRAY_STRIDE_ARB = _vertex_blend.GL_WEIGHT_ARRAY_STRIDE_ARB
GL_WEIGHT_ARRAY_SIZE_ARB = _vertex_blend.GL_WEIGHT_ARRAY_SIZE_ARB
GL_WEIGHT_ARRAY_POINTER_ARB = _vertex_blend.GL_WEIGHT_ARRAY_POINTER_ARB
GL_WEIGHT_ARRAY_ARB = _vertex_blend.GL_WEIGHT_ARRAY_ARB

