# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _texture_shader

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


__version__ = _texture_shader.__version__
__date__ = _texture_shader.__date__
__api_version__ = _texture_shader.__api_version__
__author__ = _texture_shader.__author__
__doc__ = _texture_shader.__doc__
GL_OFFSET_TEXTURE_RECTANGLE_NV = _texture_shader.GL_OFFSET_TEXTURE_RECTANGLE_NV
GL_OFFSET_TEXTURE_RECTANGLE_SCALE_NV = _texture_shader.GL_OFFSET_TEXTURE_RECTANGLE_SCALE_NV
GL_DOT_PRODUCT_TEXTURE_RECTANGLE_NV = _texture_shader.GL_DOT_PRODUCT_TEXTURE_RECTANGLE_NV
GL_RGBA_UNSIGNED_DOT_PRODUCT_MAPPING_NV = _texture_shader.GL_RGBA_UNSIGNED_DOT_PRODUCT_MAPPING_NV
GL_UNSIGNED_INT_S8_S8_8_8_NV = _texture_shader.GL_UNSIGNED_INT_S8_S8_8_8_NV
GL_UNSIGNED_INT_8_8_S8_S8_REV_NV = _texture_shader.GL_UNSIGNED_INT_8_8_S8_S8_REV_NV
GL_DSDT_MAG_INTENSITY_NV = _texture_shader.GL_DSDT_MAG_INTENSITY_NV
GL_SHADER_CONSISTENT_NV = _texture_shader.GL_SHADER_CONSISTENT_NV
GL_TEXTURE_SHADER_NV = _texture_shader.GL_TEXTURE_SHADER_NV
GL_SHADER_OPERATION_NV = _texture_shader.GL_SHADER_OPERATION_NV
GL_CULL_MODES_NV = _texture_shader.GL_CULL_MODES_NV
GL_OFFSET_TEXTURE_MATRIX_NV = _texture_shader.GL_OFFSET_TEXTURE_MATRIX_NV
GL_OFFSET_TEXTURE_SCALE_NV = _texture_shader.GL_OFFSET_TEXTURE_SCALE_NV
GL_OFFSET_TEXTURE_BIAS_NV = _texture_shader.GL_OFFSET_TEXTURE_BIAS_NV
GL_PREVIOUS_TEXTURE_INPUT_NV = _texture_shader.GL_PREVIOUS_TEXTURE_INPUT_NV
GL_CONST_EYE_NV = _texture_shader.GL_CONST_EYE_NV
GL_PASS_THROUGH_NV = _texture_shader.GL_PASS_THROUGH_NV
GL_CULL_FRAGMENT_NV = _texture_shader.GL_CULL_FRAGMENT_NV
GL_OFFSET_TEXTURE_2D_NV = _texture_shader.GL_OFFSET_TEXTURE_2D_NV
GL_DEPENDENT_AR_TEXTURE_2D_NV = _texture_shader.GL_DEPENDENT_AR_TEXTURE_2D_NV
GL_DEPENDENT_GB_TEXTURE_2D_NV = _texture_shader.GL_DEPENDENT_GB_TEXTURE_2D_NV
GL_DOT_PRODUCT_NV = _texture_shader.GL_DOT_PRODUCT_NV
GL_DOT_PRODUCT_DEPTH_REPLACE_NV = _texture_shader.GL_DOT_PRODUCT_DEPTH_REPLACE_NV
GL_DOT_PRODUCT_TEXTURE_2D_NV = _texture_shader.GL_DOT_PRODUCT_TEXTURE_2D_NV
GL_DOT_PRODUCT_TEXTURE_CUBE_MAP_NV = _texture_shader.GL_DOT_PRODUCT_TEXTURE_CUBE_MAP_NV
GL_DOT_PRODUCT_DIFFUSE_CUBE_MAP_NV = _texture_shader.GL_DOT_PRODUCT_DIFFUSE_CUBE_MAP_NV
GL_DOT_PRODUCT_REFLECT_CUBE_MAP_NV = _texture_shader.GL_DOT_PRODUCT_REFLECT_CUBE_MAP_NV
GL_DOT_PRODUCT_CONST_EYE_REFLECT_CUBE_MAP_NV = _texture_shader.GL_DOT_PRODUCT_CONST_EYE_REFLECT_CUBE_MAP_NV
GL_HILO_NV = _texture_shader.GL_HILO_NV
GL_DSDT_NV = _texture_shader.GL_DSDT_NV
GL_DSDT_MAG_NV = _texture_shader.GL_DSDT_MAG_NV
GL_DSDT_MAG_VIB_NV = _texture_shader.GL_DSDT_MAG_VIB_NV
GL_HILO16_NV = _texture_shader.GL_HILO16_NV
GL_SIGNED_HILO_NV = _texture_shader.GL_SIGNED_HILO_NV
GL_SIGNED_HILO16_NV = _texture_shader.GL_SIGNED_HILO16_NV
GL_SIGNED_RGBA_NV = _texture_shader.GL_SIGNED_RGBA_NV
GL_SIGNED_RGBA8_NV = _texture_shader.GL_SIGNED_RGBA8_NV
GL_SIGNED_RGB_NV = _texture_shader.GL_SIGNED_RGB_NV
GL_SIGNED_RGB8_NV = _texture_shader.GL_SIGNED_RGB8_NV
GL_SIGNED_LUMINANCE_NV = _texture_shader.GL_SIGNED_LUMINANCE_NV
GL_SIGNED_LUMINANCE8_NV = _texture_shader.GL_SIGNED_LUMINANCE8_NV
GL_SIGNED_LUMINANCE_ALPHA_NV = _texture_shader.GL_SIGNED_LUMINANCE_ALPHA_NV
GL_SIGNED_LUMINANCE8_ALPHA8_NV = _texture_shader.GL_SIGNED_LUMINANCE8_ALPHA8_NV
GL_SIGNED_ALPHA_NV = _texture_shader.GL_SIGNED_ALPHA_NV
GL_SIGNED_ALPHA8_NV = _texture_shader.GL_SIGNED_ALPHA8_NV
GL_SIGNED_INTENSITY_NV = _texture_shader.GL_SIGNED_INTENSITY_NV
GL_SIGNED_INTENSITY8_NV = _texture_shader.GL_SIGNED_INTENSITY8_NV
GL_DSDT8_NV = _texture_shader.GL_DSDT8_NV
GL_DSDT8_MAG8_NV = _texture_shader.GL_DSDT8_MAG8_NV
GL_DSDT8_MAG8_INTENSITY8_NV = _texture_shader.GL_DSDT8_MAG8_INTENSITY8_NV
GL_SIGNED_RGB_UNSIGNED_ALPHA_NV = _texture_shader.GL_SIGNED_RGB_UNSIGNED_ALPHA_NV
GL_SIGNED_RGB8_UNSIGNED_ALPHA8_NV = _texture_shader.GL_SIGNED_RGB8_UNSIGNED_ALPHA8_NV
GL_HI_SCALE_NV = _texture_shader.GL_HI_SCALE_NV
GL_LO_SCALE_NV = _texture_shader.GL_LO_SCALE_NV
GL_DS_SCALE_NV = _texture_shader.GL_DS_SCALE_NV
GL_DT_SCALE_NV = _texture_shader.GL_DT_SCALE_NV
GL_MAGNITUDE_SCALE_NV = _texture_shader.GL_MAGNITUDE_SCALE_NV
GL_VIBRANCE_SCALE_NV = _texture_shader.GL_VIBRANCE_SCALE_NV
GL_HI_BIAS_NV = _texture_shader.GL_HI_BIAS_NV
GL_LO_BIAS_NV = _texture_shader.GL_LO_BIAS_NV
GL_DS_BIAS_NV = _texture_shader.GL_DS_BIAS_NV
GL_DT_BIAS_NV = _texture_shader.GL_DT_BIAS_NV
GL_MAGNITUDE_BIAS_NV = _texture_shader.GL_MAGNITUDE_BIAS_NV
GL_VIBRANCE_BIAS_NV = _texture_shader.GL_VIBRANCE_BIAS_NV
GL_TEXTURE_BORDER_VALUES_NV = _texture_shader.GL_TEXTURE_BORDER_VALUES_NV
GL_TEXTURE_HI_SIZE_NV = _texture_shader.GL_TEXTURE_HI_SIZE_NV
GL_TEXTURE_LO_SIZE_NV = _texture_shader.GL_TEXTURE_LO_SIZE_NV
GL_TEXTURE_DS_SIZE_NV = _texture_shader.GL_TEXTURE_DS_SIZE_NV
GL_TEXTURE_DT_SIZE_NV = _texture_shader.GL_TEXTURE_DT_SIZE_NV
GL_TEXTURE_MAG_SIZE_NV = _texture_shader.GL_TEXTURE_MAG_SIZE_NV

glInitTextureShaderNV = _texture_shader.glInitTextureShaderNV

__info = _texture_shader.__info

