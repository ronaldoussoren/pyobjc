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
GL_COMBINE_ARB = _texture_env_combine.GL_COMBINE_ARB
GL_COMBINE_RGB_ARB = _texture_env_combine.GL_COMBINE_RGB_ARB
GL_COMBINE_ALPHA_ARB = _texture_env_combine.GL_COMBINE_ALPHA_ARB
GL_SOURCE0_RGB_ARB = _texture_env_combine.GL_SOURCE0_RGB_ARB
GL_SOURCE1_RGB_ARB = _texture_env_combine.GL_SOURCE1_RGB_ARB
GL_SOURCE2_RGB_ARB = _texture_env_combine.GL_SOURCE2_RGB_ARB
GL_SOURCE0_ALPHA_ARB = _texture_env_combine.GL_SOURCE0_ALPHA_ARB
GL_SOURCE1_ALPHA_ARB = _texture_env_combine.GL_SOURCE1_ALPHA_ARB
GL_SOURCE2_ALPHA_ARB = _texture_env_combine.GL_SOURCE2_ALPHA_ARB
GL_OPERAND0_RGB_ARB = _texture_env_combine.GL_OPERAND0_RGB_ARB
GL_OPERAND1_RGB_ARB = _texture_env_combine.GL_OPERAND1_RGB_ARB
GL_OPERAND2_RGB_ARB = _texture_env_combine.GL_OPERAND2_RGB_ARB
GL_OPERAND0_ALPHA_ARB = _texture_env_combine.GL_OPERAND0_ALPHA_ARB
GL_OPERAND1_ALPHA_ARB = _texture_env_combine.GL_OPERAND1_ALPHA_ARB
GL_OPERAND2_ALPHA_ARB = _texture_env_combine.GL_OPERAND2_ALPHA_ARB
GL_RGB_SCALE_ARB = _texture_env_combine.GL_RGB_SCALE_ARB
GL_ADD_SIGNED_ARB = _texture_env_combine.GL_ADD_SIGNED_ARB
GL_INTERPOLATE_ARB = _texture_env_combine.GL_INTERPOLATE_ARB
GL_SUBTRACT_ARB = _texture_env_combine.GL_SUBTRACT_ARB
GL_CONSTANT_ARB = _texture_env_combine.GL_CONSTANT_ARB
GL_PRIMARY_COLOR_ARB = _texture_env_combine.GL_PRIMARY_COLOR_ARB
GL_PREVIOUS_ARB = _texture_env_combine.GL_PREVIOUS_ARB

glInitTextureEnvCombineARB = _texture_env_combine.glInitTextureEnvCombineARB

__info = _texture_env_combine.__info

