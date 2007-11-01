# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _texture_select

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


__version__ = _texture_select.__version__
__date__ = _texture_select.__date__
__api_version__ = _texture_select.__api_version__
__author__ = _texture_select.__author__
__doc__ = _texture_select.__doc__
GL_DUAL_ALPHA4_SGIS = _texture_select.GL_DUAL_ALPHA4_SGIS
GL_DUAL_ALPHA8_SGIS = _texture_select.GL_DUAL_ALPHA8_SGIS
GL_DUAL_ALPHA12_SGIS = _texture_select.GL_DUAL_ALPHA12_SGIS
GL_DUAL_ALPHA16_SGIS = _texture_select.GL_DUAL_ALPHA16_SGIS
GL_DUAL_LUMINANCE4_SGIS = _texture_select.GL_DUAL_LUMINANCE4_SGIS
GL_DUAL_LUMINANCE8_SGIS = _texture_select.GL_DUAL_LUMINANCE8_SGIS
GL_DUAL_LUMINANCE12_SGIS = _texture_select.GL_DUAL_LUMINANCE12_SGIS
GL_DUAL_LUMINANCE16_SGIS = _texture_select.GL_DUAL_LUMINANCE16_SGIS
GL_DUAL_INTENSITY4_SGIS = _texture_select.GL_DUAL_INTENSITY4_SGIS
GL_DUAL_INTENSITY8_SGIS = _texture_select.GL_DUAL_INTENSITY8_SGIS
GL_DUAL_INTENSITY12_SGIS = _texture_select.GL_DUAL_INTENSITY12_SGIS
GL_DUAL_INTENSITY16_SGIS = _texture_select.GL_DUAL_INTENSITY16_SGIS
GL_DUAL_LUMINANCE_ALPHA4_SGIS = _texture_select.GL_DUAL_LUMINANCE_ALPHA4_SGIS
GL_DUAL_LUMINANCE_ALPHA8_SGIS = _texture_select.GL_DUAL_LUMINANCE_ALPHA8_SGIS
GL_QUAD_ALPHA4_SGIS = _texture_select.GL_QUAD_ALPHA4_SGIS
GL_QUAD_ALPHA8_SGIS = _texture_select.GL_QUAD_ALPHA8_SGIS
GL_QUAD_LUMINANCE4_SGIS = _texture_select.GL_QUAD_LUMINANCE4_SGIS
GL_QUAD_LUMINANCE8_SGIS = _texture_select.GL_QUAD_LUMINANCE8_SGIS
GL_QUAD_INTENSITY4_SGIS = _texture_select.GL_QUAD_INTENSITY4_SGIS
GL_QUAD_INTENSITY8_SGIS = _texture_select.GL_QUAD_INTENSITY8_SGIS
GL_DUAL_TEXTURE_SELECT_SGIS = _texture_select.GL_DUAL_TEXTURE_SELECT_SGIS
GL_QUAD_TEXTURE_SELECT_SGIS = _texture_select.GL_QUAD_TEXTURE_SELECT_SGIS

glInitTextureSelectSGIS = _texture_select.glInitTextureSelectSGIS

__info = _texture_select.__info

