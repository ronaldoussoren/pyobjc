# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _fog_coord

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


__version__ = _fog_coord.__version__
__date__ = _fog_coord.__date__
__api_version__ = _fog_coord.__api_version__
__author__ = _fog_coord.__author__
__doc__ = _fog_coord.__doc__

glFogCoordPointerEXT = _fog_coord.glFogCoordPointerEXT

glFogCoordPointerubEXT = _fog_coord.glFogCoordPointerubEXT

glFogCoordPointerbEXT = _fog_coord.glFogCoordPointerbEXT

glFogCoordPointerusEXT = _fog_coord.glFogCoordPointerusEXT

glFogCoordPointersEXT = _fog_coord.glFogCoordPointersEXT

glFogCoordPointeruiEXT = _fog_coord.glFogCoordPointeruiEXT

glFogCoordPointeriEXT = _fog_coord.glFogCoordPointeriEXT

glFogCoordPointerfEXT = _fog_coord.glFogCoordPointerfEXT

glFogCoordPointerdEXT = _fog_coord.glFogCoordPointerdEXT

glFogCoordfEXT = _fog_coord.glFogCoordfEXT

glFogCoorddEXT = _fog_coord.glFogCoorddEXT

glFogCoordfvEXT = _fog_coord.glFogCoordfvEXT

glFogCoorddvEXT = _fog_coord.glFogCoorddvEXT

glInitFogCoordEXT = _fog_coord.glInitFogCoordEXT

__info = _fog_coord.__info
GL_FOG_COORDINATE_SOURCE_EXT = _fog_coord.GL_FOG_COORDINATE_SOURCE_EXT
GL_FOG_COORDINATE_EXT = _fog_coord.GL_FOG_COORDINATE_EXT
GL_FRAGMENT_DEPTH_EXT = _fog_coord.GL_FRAGMENT_DEPTH_EXT
GL_CURRENT_FOG_COORDINATE_EXT = _fog_coord.GL_CURRENT_FOG_COORDINATE_EXT
GL_FOG_COORDINATE_ARRAY_TYPE_EXT = _fog_coord.GL_FOG_COORDINATE_ARRAY_TYPE_EXT
GL_FOG_COORDINATE_ARRAY_STRIDE_EXT = _fog_coord.GL_FOG_COORDINATE_ARRAY_STRIDE_EXT
GL_FOG_COORDINATE_ARRAY_POINTER_EXT = _fog_coord.GL_FOG_COORDINATE_ARRAY_POINTER_EXT
GL_FOG_COORDINATE_ARRAY_EXT = _fog_coord.GL_FOG_COORDINATE_ARRAY_EXT

