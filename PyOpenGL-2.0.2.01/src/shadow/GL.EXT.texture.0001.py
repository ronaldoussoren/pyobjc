# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _texture

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


__version__ = _texture.__version__
__date__ = _texture.__date__
__api_version__ = _texture.__api_version__
__author__ = _texture.__author__
__doc__ = _texture.__doc__
GL_ALPHA4_EXT = _texture.GL_ALPHA4_EXT
GL_ALPHA8_EXT = _texture.GL_ALPHA8_EXT
GL_ALPHA12_EXT = _texture.GL_ALPHA12_EXT
GL_ALPHA16_EXT = _texture.GL_ALPHA16_EXT
GL_LUMINANCE4_EXT = _texture.GL_LUMINANCE4_EXT
GL_LUMINANCE8_EXT = _texture.GL_LUMINANCE8_EXT
GL_LUMINANCE12_EXT = _texture.GL_LUMINANCE12_EXT
GL_LUMINANCE16_EXT = _texture.GL_LUMINANCE16_EXT
GL_LUMINANCE4_ALPHA4_EXT = _texture.GL_LUMINANCE4_ALPHA4_EXT
GL_LUMINANCE6_ALPHA2_EXT = _texture.GL_LUMINANCE6_ALPHA2_EXT
GL_LUMINANCE8_ALPHA8_EXT = _texture.GL_LUMINANCE8_ALPHA8_EXT
GL_LUMINANCE12_ALPHA4_EXT = _texture.GL_LUMINANCE12_ALPHA4_EXT
GL_LUMINANCE12_ALPHA12_EXT = _texture.GL_LUMINANCE12_ALPHA12_EXT
GL_LUMINANCE16_ALPHA16_EXT = _texture.GL_LUMINANCE16_ALPHA16_EXT
GL_INTENSITY_EXT = _texture.GL_INTENSITY_EXT
GL_INTENSITY4_EXT = _texture.GL_INTENSITY4_EXT
GL_INTENSITY8_EXT = _texture.GL_INTENSITY8_EXT
GL_INTENSITY12_EXT = _texture.GL_INTENSITY12_EXT
GL_INTENSITY16_EXT = _texture.GL_INTENSITY16_EXT
GL_RGB2_EXT = _texture.GL_RGB2_EXT
GL_RGB4_EXT = _texture.GL_RGB4_EXT
GL_RGB5_EXT = _texture.GL_RGB5_EXT
GL_RGB8_EXT = _texture.GL_RGB8_EXT
GL_RGB10_EXT = _texture.GL_RGB10_EXT
GL_RGB12_EXT = _texture.GL_RGB12_EXT
GL_RGB16_EXT = _texture.GL_RGB16_EXT
GL_RGBA2_EXT = _texture.GL_RGBA2_EXT
GL_RGBA4_EXT = _texture.GL_RGBA4_EXT
GL_RGB5_A1_EXT = _texture.GL_RGB5_A1_EXT
GL_RGBA8_EXT = _texture.GL_RGBA8_EXT
GL_RGB10_A2_EXT = _texture.GL_RGB10_A2_EXT
GL_RGBA12_EXT = _texture.GL_RGBA12_EXT
GL_RGBA16_EXT = _texture.GL_RGBA16_EXT
GL_TEXTURE_RED_SIZE_EXT = _texture.GL_TEXTURE_RED_SIZE_EXT
GL_TEXTURE_GREEN_SIZE_EXT = _texture.GL_TEXTURE_GREEN_SIZE_EXT
GL_TEXTURE_BLUE_SIZE_EXT = _texture.GL_TEXTURE_BLUE_SIZE_EXT
GL_TEXTURE_ALPHA_SIZE_EXT = _texture.GL_TEXTURE_ALPHA_SIZE_EXT
GL_TEXTURE_LUMINANCE_SIZE_EXT = _texture.GL_TEXTURE_LUMINANCE_SIZE_EXT
GL_TEXTURE_INTENSITY_SIZE_EXT = _texture.GL_TEXTURE_INTENSITY_SIZE_EXT
GL_REPLACE_EXT = _texture.GL_REPLACE_EXT
GL_PROXY_TEXTURE_1D_EXT = _texture.GL_PROXY_TEXTURE_1D_EXT
GL_PROXY_TEXTURE_2D_EXT = _texture.GL_PROXY_TEXTURE_2D_EXT
GL_TEXTURE_TOO_LARGE_EXT = _texture.GL_TEXTURE_TOO_LARGE_EXT

glInitTextureEXT = _texture.glInitTextureEXT

__info = _texture.__info

