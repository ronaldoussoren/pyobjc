# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _color_matrix

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


__version__ = _color_matrix.__version__
__date__ = _color_matrix.__date__
__api_version__ = _color_matrix.__api_version__
__author__ = _color_matrix.__author__
__doc__ = _color_matrix.__doc__
GL_COLOR_MATRIX_SGI = _color_matrix.GL_COLOR_MATRIX_SGI
GL_COLOR_MATRIX_STACK_DEPTH_SGI = _color_matrix.GL_COLOR_MATRIX_STACK_DEPTH_SGI
GL_MAX_COLOR_MATRIX_STACK_DEPTH_SGI = _color_matrix.GL_MAX_COLOR_MATRIX_STACK_DEPTH_SGI
GL_POST_COLOR_MATRIX_RED_SCALE_SGI = _color_matrix.GL_POST_COLOR_MATRIX_RED_SCALE_SGI
GL_POST_COLOR_MATRIX_GREEN_SCALE_SGI = _color_matrix.GL_POST_COLOR_MATRIX_GREEN_SCALE_SGI
GL_POST_COLOR_MATRIX_BLUE_SCALE_SGI = _color_matrix.GL_POST_COLOR_MATRIX_BLUE_SCALE_SGI
GL_POST_COLOR_MATRIX_ALPHA_SCALE_SGI = _color_matrix.GL_POST_COLOR_MATRIX_ALPHA_SCALE_SGI
GL_POST_COLOR_MATRIX_RED_BIAS_SGI = _color_matrix.GL_POST_COLOR_MATRIX_RED_BIAS_SGI
GL_POST_COLOR_MATRIX_GREEN_BIAS_SGI = _color_matrix.GL_POST_COLOR_MATRIX_GREEN_BIAS_SGI
GL_POST_COLOR_MATRIX_BLUE_BIAS_SGI = _color_matrix.GL_POST_COLOR_MATRIX_BLUE_BIAS_SGI
GL_POST_COLOR_MATRIX_ALPHA_BIAS_SGI = _color_matrix.GL_POST_COLOR_MATRIX_ALPHA_BIAS_SGI

glInitColorMatrixSGI = _color_matrix.glInitColorMatrixSGI

__info = _color_matrix.__info

