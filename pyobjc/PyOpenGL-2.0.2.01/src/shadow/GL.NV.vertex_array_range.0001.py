# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _vertex_array_range

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


__version__ = _vertex_array_range.__version__
__date__ = _vertex_array_range.__date__
__api_version__ = _vertex_array_range.__api_version__
__author__ = _vertex_array_range.__author__
__doc__ = _vertex_array_range.__doc__

glFlushVertexArrayRangeNV = _vertex_array_range.glFlushVertexArrayRangeNV

glVertexArrayRangeNV = _vertex_array_range.glVertexArrayRangeNV
GL_VERTEX_ARRAY_RANGE_NV = _vertex_array_range.GL_VERTEX_ARRAY_RANGE_NV
GL_VERTEX_ARRAY_RANGE_LENGTH_NV = _vertex_array_range.GL_VERTEX_ARRAY_RANGE_LENGTH_NV
GL_VERTEX_ARRAY_RANGE_VALID_NV = _vertex_array_range.GL_VERTEX_ARRAY_RANGE_VALID_NV
GL_MAX_VERTEX_ARRAY_RANGE_ELEMENT_NV = _vertex_array_range.GL_MAX_VERTEX_ARRAY_RANGE_ELEMENT_NV
GL_VERTEX_ARRAY_RANGE_POINTER_NV = _vertex_array_range.GL_VERTEX_ARRAY_RANGE_POINTER_NV

glInitVertexArrayRangeNV = _vertex_array_range.glInitVertexArrayRangeNV

__info = _vertex_array_range.__info

