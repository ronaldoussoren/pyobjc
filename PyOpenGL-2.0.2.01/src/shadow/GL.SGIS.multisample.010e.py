# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _multisample

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


__version__ = _multisample.__version__
__date__ = _multisample.__date__
__api_version__ = _multisample.__api_version__
__author__ = _multisample.__author__
__doc__ = _multisample.__doc__

glInitMultisampleSGIS = _multisample.glInitMultisampleSGIS

glSampleMaskSGIS = _multisample.glSampleMaskSGIS

glSamplePatternSGIS = _multisample.glSamplePatternSGIS

__info = _multisample.__info
GL_MULTISAMPLE_SGIS = _multisample.GL_MULTISAMPLE_SGIS
GL_SAMPLE_ALPHA_TO_MASK_SGIS = _multisample.GL_SAMPLE_ALPHA_TO_MASK_SGIS
GL_SAMPLE_ALPHA_TO_ONE_SGIS = _multisample.GL_SAMPLE_ALPHA_TO_ONE_SGIS
GL_SAMPLE_MASK_SGIS = _multisample.GL_SAMPLE_MASK_SGIS
GL_MULTISAMPLE_BIT_EXT = _multisample.GL_MULTISAMPLE_BIT_EXT
GL_1PASS_SGIS = _multisample.GL_1PASS_SGIS
GL_2PASS_0_SGIS = _multisample.GL_2PASS_0_SGIS
GL_2PASS_1_SGIS = _multisample.GL_2PASS_1_SGIS
GL_4PASS_0_SGIS = _multisample.GL_4PASS_0_SGIS
GL_4PASS_1_SGIS = _multisample.GL_4PASS_1_SGIS
GL_4PASS_2_SGIS = _multisample.GL_4PASS_2_SGIS
GL_4PASS_3_SGIS = _multisample.GL_4PASS_3_SGIS
GL_SAMPLE_BUFFERS_SGIS = _multisample.GL_SAMPLE_BUFFERS_SGIS
GL_SAMPLES_SGIS = _multisample.GL_SAMPLES_SGIS
GL_SAMPLE_MASK_VALUE_SGIS = _multisample.GL_SAMPLE_MASK_VALUE_SGIS
GL_SAMPLE_MASK_INVERT_SGIS = _multisample.GL_SAMPLE_MASK_INVERT_SGIS
GL_SAMPLE_PATTERN_SGIS = _multisample.GL_SAMPLE_PATTERN_SGIS

