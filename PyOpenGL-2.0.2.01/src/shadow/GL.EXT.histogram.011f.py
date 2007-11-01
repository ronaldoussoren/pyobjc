# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _histogram

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


__version__ = _histogram.__version__
__date__ = _histogram.__date__
__api_version__ = _histogram.__api_version__
__author__ = _histogram.__author__
__doc__ = _histogram.__doc__

glResetHistogramEXT = _histogram.glResetHistogramEXT

glInitHistogramEXT = _histogram.glInitHistogramEXT

__info = _histogram.__info
GL_HISTOGRAM_EXT = _histogram.GL_HISTOGRAM_EXT
GL_PROXY_HISTOGRAM_EXT = _histogram.GL_PROXY_HISTOGRAM_EXT
GL_HISTOGRAM_WIDTH_EXT = _histogram.GL_HISTOGRAM_WIDTH_EXT
GL_HISTOGRAM_FORMAT_EXT = _histogram.GL_HISTOGRAM_FORMAT_EXT
GL_HISTOGRAM_RED_SIZE_EXT = _histogram.GL_HISTOGRAM_RED_SIZE_EXT
GL_HISTOGRAM_GREEN_SIZE_EXT = _histogram.GL_HISTOGRAM_GREEN_SIZE_EXT
GL_HISTOGRAM_BLUE_SIZE_EXT = _histogram.GL_HISTOGRAM_BLUE_SIZE_EXT
GL_HISTOGRAM_ALPHA_SIZE_EXT = _histogram.GL_HISTOGRAM_ALPHA_SIZE_EXT
GL_HISTOGRAM_LUMINANCE_SIZE_EXT = _histogram.GL_HISTOGRAM_LUMINANCE_SIZE_EXT
GL_HISTOGRAM_SINK_EXT = _histogram.GL_HISTOGRAM_SINK_EXT
GL_MINMAX_EXT = _histogram.GL_MINMAX_EXT
GL_MINMAX_FORMAT_EXT = _histogram.GL_MINMAX_FORMAT_EXT
GL_MINMAX_SINK_EXT = _histogram.GL_MINMAX_SINK_EXT

