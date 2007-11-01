# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _convolution

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


__version__ = _convolution.__version__
__date__ = _convolution.__date__
__api_version__ = _convolution.__api_version__
__author__ = _convolution.__author__
__doc__ = _convolution.__doc__

glConvolutionParameteriEXT = _convolution.glConvolutionParameteriEXT

glConvolutionParameterivEXT = _convolution.glConvolutionParameterivEXT

glConvolutionParameterfEXT = _convolution.glConvolutionParameterfEXT

glConvolutionParameterfvEXT = _convolution.glConvolutionParameterfvEXT

glGetConvolutionParameterivEXT = _convolution.glGetConvolutionParameterivEXT

glGetConvolutionParameterfvEXT = _convolution.glGetConvolutionParameterfvEXT

glConvolutionFilter1DEXT = _convolution.glConvolutionFilter1DEXT

glConvolutionFilter2DEXT = _convolution.glConvolutionFilter2DEXT

glCopyConvolutionFilter1DEXT = _convolution.glCopyConvolutionFilter1DEXT

glCopyConvolutionFilter2DEXT = _convolution.glCopyConvolutionFilter2DEXT

glGetConvolutionFilterEXT = _convolution.glGetConvolutionFilterEXT

glSeparableFilter2DEXT = _convolution.glSeparableFilter2DEXT

glInitConvolutionEXT = _convolution.glInitConvolutionEXT

__info = _convolution.__info
GL_CONVOLUTION_1D_EXT = _convolution.GL_CONVOLUTION_1D_EXT
GL_CONVOLUTION_2D_EXT = _convolution.GL_CONVOLUTION_2D_EXT
GL_SEPARABLE_2D_EXT = _convolution.GL_SEPARABLE_2D_EXT
GL_CONVOLUTION_BORDER_MODE_EXT = _convolution.GL_CONVOLUTION_BORDER_MODE_EXT
GL_CONVOLUTION_FILTER_SCALE_EXT = _convolution.GL_CONVOLUTION_FILTER_SCALE_EXT
GL_CONVOLUTION_FILTER_BIAS_EXT = _convolution.GL_CONVOLUTION_FILTER_BIAS_EXT
GL_REDUCE_EXT = _convolution.GL_REDUCE_EXT
GL_CONVOLUTION_FORMAT_EXT = _convolution.GL_CONVOLUTION_FORMAT_EXT
GL_CONVOLUTION_WIDTH_EXT = _convolution.GL_CONVOLUTION_WIDTH_EXT
GL_CONVOLUTION_HEIGHT_EXT = _convolution.GL_CONVOLUTION_HEIGHT_EXT
GL_MAX_CONVOLUTION_WIDTH_EXT = _convolution.GL_MAX_CONVOLUTION_WIDTH_EXT
GL_MAX_CONVOLUTION_HEIGHT_EXT = _convolution.GL_MAX_CONVOLUTION_HEIGHT_EXT
GL_POST_CONVOLUTION_RED_SCALE_EXT = _convolution.GL_POST_CONVOLUTION_RED_SCALE_EXT
GL_POST_CONVOLUTION_GREEN_SCALE_EXT = _convolution.GL_POST_CONVOLUTION_GREEN_SCALE_EXT
GL_POST_CONVOLUTION_BLUE_SCALE_EXT = _convolution.GL_POST_CONVOLUTION_BLUE_SCALE_EXT
GL_POST_CONVOLUTION_ALPHA_SCALE_EXT = _convolution.GL_POST_CONVOLUTION_ALPHA_SCALE_EXT
GL_POST_CONVOLUTION_RED_BIAS_EXT = _convolution.GL_POST_CONVOLUTION_RED_BIAS_EXT
GL_POST_CONVOLUTION_GREEN_BIAS_EXT = _convolution.GL_POST_CONVOLUTION_GREEN_BIAS_EXT
GL_POST_CONVOLUTION_BLUE_BIAS_EXT = _convolution.GL_POST_CONVOLUTION_BLUE_BIAS_EXT
GL_POST_CONVOLUTION_ALPHA_BIAS_EXT = _convolution.GL_POST_CONVOLUTION_ALPHA_BIAS_EXT

