# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _texture_shader3

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


__version__ = _texture_shader3.__version__
__date__ = _texture_shader3.__date__
__api_version__ = _texture_shader3.__api_version__
__author__ = _texture_shader3.__author__
__doc__ = _texture_shader3.__doc__
GL_OFFSET_PROJECTIVE_TEXTURE_2D_NV = _texture_shader3.GL_OFFSET_PROJECTIVE_TEXTURE_2D_NV
GL_OFFSET_PROJECTIVE_TEXTURE_2D_SCALE_NV = _texture_shader3.GL_OFFSET_PROJECTIVE_TEXTURE_2D_SCALE_NV
GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_NV = _texture_shader3.GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_NV
GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_SCALE_NV = _texture_shader3.GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_SCALE_NV
GL_OFFSET_HILO_TEXTURE_2D_NV = _texture_shader3.GL_OFFSET_HILO_TEXTURE_2D_NV
GL_OFFSET_HILO_TEXTURE_RECTANGLE_NV = _texture_shader3.GL_OFFSET_HILO_TEXTURE_RECTANGLE_NV
GL_OFFSET_HILO_PROJECTIVE_TEXTURE_2D_NV = _texture_shader3.GL_OFFSET_HILO_PROJECTIVE_TEXTURE_2D_NV
GL_OFFSET_HILO_PROJECTIVE_TEXTURE_RECTANGLE_NV = _texture_shader3.GL_OFFSET_HILO_PROJECTIVE_TEXTURE_RECTANGLE_NV
GL_DEPENDENT_HILO_TEXTURE_2D_NV = _texture_shader3.GL_DEPENDENT_HILO_TEXTURE_2D_NV
GL_DEPENDENT_RGB_TEXTURE_3D_NV = _texture_shader3.GL_DEPENDENT_RGB_TEXTURE_3D_NV
GL_DEPENDENT_RGB_TEXTURE_CUBE_MAP_NV = _texture_shader3.GL_DEPENDENT_RGB_TEXTURE_CUBE_MAP_NV
GL_DOT_PRODUCT_PASS_THROUGH_NV = _texture_shader3.GL_DOT_PRODUCT_PASS_THROUGH_NV
GL_DOT_PRODUCT_TEXTURE_1D_NV = _texture_shader3.GL_DOT_PRODUCT_TEXTURE_1D_NV
GL_DOT_PRODUCT_AFFINE_DEPTH_REPLACE_NV = _texture_shader3.GL_DOT_PRODUCT_AFFINE_DEPTH_REPLACE_NV
GL_HILO8_NV = _texture_shader3.GL_HILO8_NV
GL_SIGNED_HILO8_NV = _texture_shader3.GL_SIGNED_HILO8_NV
GL_FORCE_BLUE_TO_ONE_NV = _texture_shader3.GL_FORCE_BLUE_TO_ONE_NV

glInitTextureShader3NV = _texture_shader3.glInitTextureShader3NV

__info = _texture_shader3.__info

