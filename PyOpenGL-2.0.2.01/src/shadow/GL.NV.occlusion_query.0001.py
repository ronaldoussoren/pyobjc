# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _occlusion_query

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


__version__ = _occlusion_query.__version__
__date__ = _occlusion_query.__date__
__api_version__ = _occlusion_query.__api_version__
__author__ = _occlusion_query.__author__
__doc__ = _occlusion_query.__doc__

glGenOcclusionQueriesNV = _occlusion_query.glGenOcclusionQueriesNV

glDeleteOcclusionQueriesNV = _occlusion_query.glDeleteOcclusionQueriesNV

glIsOcclusionQueryNV = _occlusion_query.glIsOcclusionQueryNV

glBeginOcclusionQueryNV = _occlusion_query.glBeginOcclusionQueryNV

glEndOcclusionQueryNV = _occlusion_query.glEndOcclusionQueryNV

glGetOcclusionQueryivNV = _occlusion_query.glGetOcclusionQueryivNV

glGetOcclusionQueryuivNV = _occlusion_query.glGetOcclusionQueryuivNV
GL_PIXEL_COUNTER_BITS_NV = _occlusion_query.GL_PIXEL_COUNTER_BITS_NV
GL_CURRENT_OCCLUSION_QUERY_ID_NV = _occlusion_query.GL_CURRENT_OCCLUSION_QUERY_ID_NV
GL_PIXEL_COUNT_NV = _occlusion_query.GL_PIXEL_COUNT_NV
GL_PIXEL_COUNT_AVAILABLE_NV = _occlusion_query.GL_PIXEL_COUNT_AVAILABLE_NV

glInitOcclusionQueryNV = _occlusion_query.glInitOcclusionQueryNV

__info = _occlusion_query.__info

