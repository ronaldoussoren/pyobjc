# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _texture_object

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


__version__ = _texture_object.__version__
__date__ = _texture_object.__date__
__api_version__ = _texture_object.__api_version__
__author__ = _texture_object.__author__
__doc__ = _texture_object.__doc__

glAreTexturesResidentEXT = _texture_object.glAreTexturesResidentEXT

glBindTextureEXT = _texture_object.glBindTextureEXT

glDeleteTexturesEXT = _texture_object.glDeleteTexturesEXT

glGenTexturesEXT = _texture_object.glGenTexturesEXT

glIsTextureEXT = _texture_object.glIsTextureEXT

glPrioritizeTexturesEXT = _texture_object.glPrioritizeTexturesEXT

glInitTextureObjectEXT = _texture_object.glInitTextureObjectEXT

glInitTexObjectEXT = _texture_object.glInitTexObjectEXT

__info = _texture_object.__info
GL_TEXTURE_PRIORITY_EXT = _texture_object.GL_TEXTURE_PRIORITY_EXT
GL_TEXTURE_RESIDENT_EXT = _texture_object.GL_TEXTURE_RESIDENT_EXT
GL_TEXTURE_1D_BINDING_EXT = _texture_object.GL_TEXTURE_1D_BINDING_EXT
GL_TEXTURE_2D_BINDING_EXT = _texture_object.GL_TEXTURE_2D_BINDING_EXT
GL_TEXTURE_3D_BINDING_EXT = _texture_object.GL_TEXTURE_3D_BINDING_EXT

