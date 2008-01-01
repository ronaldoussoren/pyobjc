# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _convolution_border_modes

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


__version__ = _convolution_border_modes.__version__
__date__ = _convolution_border_modes.__date__
__api_version__ = _convolution_border_modes.__api_version__
__author__ = _convolution_border_modes.__author__
__doc__ = _convolution_border_modes.__doc__
GL_IGNORE_BORDER_HP = _convolution_border_modes.GL_IGNORE_BORDER_HP
GL_CONSTANT_BORDER_HP = _convolution_border_modes.GL_CONSTANT_BORDER_HP
GL_REPLICATE_BORDER_HP = _convolution_border_modes.GL_REPLICATE_BORDER_HP
GL_CONVOLUTION_BORDER_COLOR_HP = _convolution_border_modes.GL_CONVOLUTION_BORDER_COLOR_HP

glInitConvolutionBorderModesHP = _convolution_border_modes.glInitConvolutionBorderModesHP

__info = _convolution_border_modes.__info

