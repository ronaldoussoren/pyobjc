# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _float_buffer

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


__version__ = _float_buffer.__version__
__date__ = _float_buffer.__date__
__api_version__ = _float_buffer.__api_version__
__author__ = _float_buffer.__author__
__doc__ = _float_buffer.__doc__
GL_FLOAT_R_NV = _float_buffer.GL_FLOAT_R_NV
GL_FLOAT_RG_NV = _float_buffer.GL_FLOAT_RG_NV
GL_FLOAT_RGB_NV = _float_buffer.GL_FLOAT_RGB_NV
GL_FLOAT_RGBA_NV = _float_buffer.GL_FLOAT_RGBA_NV
GL_FLOAT_R16_NV = _float_buffer.GL_FLOAT_R16_NV
GL_FLOAT_R32_NV = _float_buffer.GL_FLOAT_R32_NV
GL_FLOAT_RG16_NV = _float_buffer.GL_FLOAT_RG16_NV
GL_FLOAT_RG32_NV = _float_buffer.GL_FLOAT_RG32_NV
GL_FLOAT_RGB16_NV = _float_buffer.GL_FLOAT_RGB16_NV
GL_FLOAT_RGB32_NV = _float_buffer.GL_FLOAT_RGB32_NV
GL_FLOAT_RGBA16_NV = _float_buffer.GL_FLOAT_RGBA16_NV
GL_FLOAT_RGBA32_NV = _float_buffer.GL_FLOAT_RGBA32_NV
GL_TEXTURE_FLOAT_COMPONENTS_NV = _float_buffer.GL_TEXTURE_FLOAT_COMPONENTS_NV
GL_FLOAT_CLEAR_COLOR_VALUE_NV = _float_buffer.GL_FLOAT_CLEAR_COLOR_VALUE_NV
GL_FLOAT_RGBA_MODE_NV = _float_buffer.GL_FLOAT_RGBA_MODE_NV

glInitFloatBufferNV = _float_buffer.glInitFloatBufferNV

__info = _float_buffer.__info

