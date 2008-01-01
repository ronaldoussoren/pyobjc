# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _texture_env_combine

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


__version__ = _texture_env_combine.__version__
__date__ = _texture_env_combine.__date__
__api_version__ = _texture_env_combine.__api_version__
__author__ = _texture_env_combine.__author__
__doc__ = _texture_env_combine.__doc__
GL_COMBINE_EXT = _texture_env_combine.GL_COMBINE_EXT
GL_COMBINE_RGB_EXT = _texture_env_combine.GL_COMBINE_RGB_EXT
GL_COMBINE_ALPHA_EXT = _texture_env_combine.GL_COMBINE_ALPHA_EXT
GL_RGB_SCALE_EXT = _texture_env_combine.GL_RGB_SCALE_EXT
GL_ADD_SIGNED_EXT = _texture_env_combine.GL_ADD_SIGNED_EXT
GL_INTERPOLATE_EXT = _texture_env_combine.GL_INTERPOLATE_EXT
GL_CONSTANT_EXT = _texture_env_combine.GL_CONSTANT_EXT
GL_PRIMARY_COLOR_EXT = _texture_env_combine.GL_PRIMARY_COLOR_EXT
GL_PREVIOUS_EXT = _texture_env_combine.GL_PREVIOUS_EXT
GL_SOURCE0_RGB_EXT = _texture_env_combine.GL_SOURCE0_RGB_EXT
GL_SOURCE1_RGB_EXT = _texture_env_combine.GL_SOURCE1_RGB_EXT
GL_SOURCE2_RGB_EXT = _texture_env_combine.GL_SOURCE2_RGB_EXT
GL_SOURCE0_ALPHA_EXT = _texture_env_combine.GL_SOURCE0_ALPHA_EXT
GL_SOURCE1_ALPHA_EXT = _texture_env_combine.GL_SOURCE1_ALPHA_EXT
GL_SOURCE2_ALPHA_EXT = _texture_env_combine.GL_SOURCE2_ALPHA_EXT
GL_OPERAND0_RGB_EXT = _texture_env_combine.GL_OPERAND0_RGB_EXT
GL_OPERAND1_RGB_EXT = _texture_env_combine.GL_OPERAND1_RGB_EXT
GL_OPERAND2_RGB_EXT = _texture_env_combine.GL_OPERAND2_RGB_EXT
GL_OPERAND0_ALPHA_EXT = _texture_env_combine.GL_OPERAND0_ALPHA_EXT
GL_OPERAND1_ALPHA_EXT = _texture_env_combine.GL_OPERAND1_ALPHA_EXT
GL_OPERAND2_ALPHA_EXT = _texture_env_combine.GL_OPERAND2_ALPHA_EXT

glInitTextureEnvCombineEXT = _texture_env_combine.glInitTextureEnvCombineEXT

__info = _texture_env_combine.__info

