# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _tag_sample_buffer

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


__version__ = _tag_sample_buffer.__version__
__date__ = _tag_sample_buffer.__date__
__api_version__ = _tag_sample_buffer.__api_version__
__author__ = _tag_sample_buffer.__author__
__doc__ = _tag_sample_buffer.__doc__

glInitTagSampleBufferSGIX = _tag_sample_buffer.glInitTagSampleBufferSGIX

glTagSampleBufferSGIX = _tag_sample_buffer.glTagSampleBufferSGIX

__info = _tag_sample_buffer.__info
GL_REFERENCE_PLANE_SGIX = _tag_sample_buffer.GL_REFERENCE_PLANE_SGIX
GL_REFERENCE_PLANE_EQUATION_SGIX = _tag_sample_buffer.GL_REFERENCE_PLANE_EQUATION_SGIX

