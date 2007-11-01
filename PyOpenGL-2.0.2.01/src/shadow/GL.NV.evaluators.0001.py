# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _evaluators

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


__version__ = _evaluators.__version__
__date__ = _evaluators.__date__
__api_version__ = _evaluators.__api_version__
__author__ = _evaluators.__author__
__doc__ = _evaluators.__doc__

glMapControlPointsNV = _evaluators.glMapControlPointsNV

glMapParameterivNV = _evaluators.glMapParameterivNV

glMapParameterfvNV = _evaluators.glMapParameterfvNV

glGetMapControlPointsNV = _evaluators.glGetMapControlPointsNV

glGetMapParameterivNV = _evaluators.glGetMapParameterivNV

glGetMapParameterfvNV = _evaluators.glGetMapParameterfvNV

glGetMapAttribParameterivNV = _evaluators.glGetMapAttribParameterivNV

glGetMapAttribParameterfvNV = _evaluators.glGetMapAttribParameterfvNV

glEvalMapsNV = _evaluators.glEvalMapsNV
GL_EVAL_2D_NV = _evaluators.GL_EVAL_2D_NV
GL_EVAL_TRIANGULAR_2D_NV = _evaluators.GL_EVAL_TRIANGULAR_2D_NV
GL_MAP_TESSELLATION_NV = _evaluators.GL_MAP_TESSELLATION_NV
GL_MAP_ATTRIB_U_ORDER_NV = _evaluators.GL_MAP_ATTRIB_U_ORDER_NV
GL_MAP_ATTRIB_V_ORDER_NV = _evaluators.GL_MAP_ATTRIB_V_ORDER_NV
GL_EVAL_FRACTIONAL_TESSELLATION_NV = _evaluators.GL_EVAL_FRACTIONAL_TESSELLATION_NV
GL_EVAL_VERTEX_ATTRIB0_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB0_NV
GL_EVAL_VERTEX_ATTRIB1_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB1_NV
GL_EVAL_VERTEX_ATTRIB2_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB2_NV
GL_EVAL_VERTEX_ATTRIB3_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB3_NV
GL_EVAL_VERTEX_ATTRIB4_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB4_NV
GL_EVAL_VERTEX_ATTRIB5_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB5_NV
GL_EVAL_VERTEX_ATTRIB6_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB6_NV
GL_EVAL_VERTEX_ATTRIB7_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB7_NV
GL_EVAL_VERTEX_ATTRIB8_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB8_NV
GL_EVAL_VERTEX_ATTRIB9_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB9_NV
GL_EVAL_VERTEX_ATTRIB10_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB10_NV
GL_EVAL_VERTEX_ATTRIB11_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB11_NV
GL_EVAL_VERTEX_ATTRIB12_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB12_NV
GL_EVAL_VERTEX_ATTRIB13_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB13_NV
GL_EVAL_VERTEX_ATTRIB14_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB14_NV
GL_EVAL_VERTEX_ATTRIB15_NV = _evaluators.GL_EVAL_VERTEX_ATTRIB15_NV
GL_MAX_MAP_TESSELLATION_NV = _evaluators.GL_MAX_MAP_TESSELLATION_NV
GL_MAX_RATIONAL_EVAL_ORDER_NV = _evaluators.GL_MAX_RATIONAL_EVAL_ORDER_NV

glInitEvaluatorsNV = _evaluators.glInitEvaluatorsNV

__info = _evaluators.__info

