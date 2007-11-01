# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _pixel_transform

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


__version__ = _pixel_transform.__version__
__date__ = _pixel_transform.__date__
__api_version__ = _pixel_transform.__api_version__
__author__ = _pixel_transform.__author__
__doc__ = _pixel_transform.__doc__

glPixelTransformParameteriEXT = _pixel_transform.glPixelTransformParameteriEXT

glPixelTransformParameterfEXT = _pixel_transform.glPixelTransformParameterfEXT

glPixelTransformParameterivEXT = _pixel_transform.glPixelTransformParameterivEXT

glPixelTransformParameterfvEXT = _pixel_transform.glPixelTransformParameterfvEXT

glGetPixelTransformParameterfvEXT = _pixel_transform.glGetPixelTransformParameterfvEXT

glGetPixelTransformParameterivEXT = _pixel_transform.glGetPixelTransformParameterivEXT

glInitPixelTransformEXT = _pixel_transform.glInitPixelTransformEXT

__info = _pixel_transform.__info
GL_PIXEL_MAG_FILTER_EXT = _pixel_transform.GL_PIXEL_MAG_FILTER_EXT
GL_PIXEL_MIN_FILTER_EXT = _pixel_transform.GL_PIXEL_MIN_FILTER_EXT
GL_PIXEL_CUBIC_WEIGHT_EXT = _pixel_transform.GL_PIXEL_CUBIC_WEIGHT_EXT
GL_CUBIC_EXT = _pixel_transform.GL_CUBIC_EXT
GL_AVERAGE_EXT = _pixel_transform.GL_AVERAGE_EXT
GL_PIXEL_TRANSFORM_2D_EXT = _pixel_transform.GL_PIXEL_TRANSFORM_2D_EXT
GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT = _pixel_transform.GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT
GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT = _pixel_transform.GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT
GL_PIXEL_TRANSFORM_2D_MATRIX_EXT = _pixel_transform.GL_PIXEL_TRANSFORM_2D_MATRIX_EXT

