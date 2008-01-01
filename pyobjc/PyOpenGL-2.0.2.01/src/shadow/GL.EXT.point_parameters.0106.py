# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _point_parameters

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


__version__ = _point_parameters.__version__
__date__ = _point_parameters.__date__
__api_version__ = _point_parameters.__api_version__
__author__ = _point_parameters.__author__
__doc__ = _point_parameters.__doc__

glPointParameterfEXT = _point_parameters.glPointParameterfEXT

glPointParameterfvEXT = _point_parameters.glPointParameterfvEXT

glInitPointParametersEXT = _point_parameters.glInitPointParametersEXT

__info = _point_parameters.__info
GL_POINT_SIZE_MIN_EXT = _point_parameters.GL_POINT_SIZE_MIN_EXT
GL_POINT_SIZE_MAX_EXT = _point_parameters.GL_POINT_SIZE_MAX_EXT
GL_POINT_FADE_THRESHOLD_SIZE_EXT = _point_parameters.GL_POINT_FADE_THRESHOLD_SIZE_EXT
GL_POINT_DISTANCE_ATTENUATION_EXT = _point_parameters.GL_POINT_DISTANCE_ATTENUATION_EXT

