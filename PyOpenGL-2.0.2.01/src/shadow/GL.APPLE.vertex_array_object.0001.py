# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _vertex_array_object

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


__version__ = _vertex_array_object.__version__
__date__ = _vertex_array_object.__date__
__api_version__ = _vertex_array_object.__api_version__
__author__ = _vertex_array_object.__author__
__doc__ = _vertex_array_object.__doc__

glBindVertexArrayAPPLE = _vertex_array_object.glBindVertexArrayAPPLE

glDeleteVertexArraysAPPLE = _vertex_array_object.glDeleteVertexArraysAPPLE

glGenVertexArraysAPPLE = _vertex_array_object.glGenVertexArraysAPPLE

glIsVertexArrayAPPLE = _vertex_array_object.glIsVertexArrayAPPLE
GL_VERTEX_ARRAY_BINDING_APPLE = _vertex_array_object.GL_VERTEX_ARRAY_BINDING_APPLE

glInitVertexArrayObjectAPPLE = _vertex_array_object.glInitVertexArrayObjectAPPLE

__info = _vertex_array_object.__info

