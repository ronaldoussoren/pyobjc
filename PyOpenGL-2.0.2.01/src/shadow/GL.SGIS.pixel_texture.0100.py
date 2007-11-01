# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _pixel_texture

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


__version__ = _pixel_texture.__version__
__date__ = _pixel_texture.__date__
__api_version__ = _pixel_texture.__api_version__
__author__ = _pixel_texture.__author__
__doc__ = _pixel_texture.__doc__

glInitPixelTextureSGIS = _pixel_texture.glInitPixelTextureSGIS

glInitPixelTexSGIS = _pixel_texture.glInitPixelTexSGIS

glPixelTexGenParameteriSGIS = _pixel_texture.glPixelTexGenParameteriSGIS

glPixelTexGenParameterfSGIS = _pixel_texture.glPixelTexGenParameterfSGIS

glGetPixelTexGenParameterfvSGIS = _pixel_texture.glGetPixelTexGenParameterfvSGIS

glGetPixelTexGenParameterivSGIS = _pixel_texture.glGetPixelTexGenParameterivSGIS

__info = _pixel_texture.__info
GL_PIXEL_TEXTURE_SGIS = _pixel_texture.GL_PIXEL_TEXTURE_SGIS
GL_PIXEL_FRAGMENT_RGB_SOURCE_SGIS = _pixel_texture.GL_PIXEL_FRAGMENT_RGB_SOURCE_SGIS
GL_PIXEL_FRAGMENT_ALPHA_SOURCE_SGIS = _pixel_texture.GL_PIXEL_FRAGMENT_ALPHA_SOURCE_SGIS
GL_PIXEL_GROUP_COLOR_SGIS = _pixel_texture.GL_PIXEL_GROUP_COLOR_SGIS

