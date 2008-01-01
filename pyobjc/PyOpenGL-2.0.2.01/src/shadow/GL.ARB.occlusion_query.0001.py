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

glGenQueriesARB = _occlusion_query.glGenQueriesARB

glDeleteQueriesARB = _occlusion_query.glDeleteQueriesARB

glIsQueryARB = _occlusion_query.glIsQueryARB

glBeginQueryARB = _occlusion_query.glBeginQueryARB

glEndQueryARB = _occlusion_query.glEndQueryARB

glGetQueryivARB = _occlusion_query.glGetQueryivARB

glGetQueryObjectivARB = _occlusion_query.glGetQueryObjectivARB

glGetQueryObjectuivARB = _occlusion_query.glGetQueryObjectuivARB
GL_QUERY_COUNTER_BITS_ARB = _occlusion_query.GL_QUERY_COUNTER_BITS_ARB
GL_CURRENT_QUERY_ARB = _occlusion_query.GL_CURRENT_QUERY_ARB
GL_QUERY_RESULT_ARB = _occlusion_query.GL_QUERY_RESULT_ARB
GL_QUERY_RESULT_AVAILABLE_ARB = _occlusion_query.GL_QUERY_RESULT_AVAILABLE_ARB
GL_SAMPLES_PASSED_ARB = _occlusion_query.GL_SAMPLES_PASSED_ARB

glInitOcclusionQueryARB = _occlusion_query.glInitOcclusionQueryARB

__info = _occlusion_query.__info

