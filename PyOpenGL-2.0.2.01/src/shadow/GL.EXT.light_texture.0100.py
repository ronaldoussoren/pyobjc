# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _light_texture

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


__version__ = _light_texture.__version__
__date__ = _light_texture.__date__
__api_version__ = _light_texture.__api_version__
__author__ = _light_texture.__author__
__doc__ = _light_texture.__doc__

glApplyTextureEXT = _light_texture.glApplyTextureEXT

glTextureLightEXT = _light_texture.glTextureLightEXT

glTextureMaterialEXT = _light_texture.glTextureMaterialEXT

glInitLightTextureEXT = _light_texture.glInitLightTextureEXT

glInitLightTexEXT = _light_texture.glInitLightTexEXT

__info = _light_texture.__info
GL_FRAGMENT_MATERIAL_EXT = _light_texture.GL_FRAGMENT_MATERIAL_EXT
GL_FRAGMENT_NORMAL_EXT = _light_texture.GL_FRAGMENT_NORMAL_EXT
GL_FRAGMENT_DEPTH_EXT = _light_texture.GL_FRAGMENT_DEPTH_EXT
GL_FRAGMENT_COLOR_EXT = _light_texture.GL_FRAGMENT_COLOR_EXT
GL_ATTENUATION_EXT = _light_texture.GL_ATTENUATION_EXT
GL_SHADOW_ATTENUATION_EXT = _light_texture.GL_SHADOW_ATTENUATION_EXT
GL_TEXTURE_APPLICATION_MODE_EXT = _light_texture.GL_TEXTURE_APPLICATION_MODE_EXT
GL_TEXTURE_LIGHT_EXT = _light_texture.GL_TEXTURE_LIGHT_EXT
GL_TEXTURE_MATERIAL_FACE_EXT = _light_texture.GL_TEXTURE_MATERIAL_FACE_EXT
GL_TEXTURE_MATERIAL_PARAMETER_EXT = _light_texture.GL_TEXTURE_MATERIAL_PARAMETER_EXT

