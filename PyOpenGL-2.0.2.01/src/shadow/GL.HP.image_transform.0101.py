# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _image_transform

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


__version__ = _image_transform.__version__
__date__ = _image_transform.__date__
__api_version__ = _image_transform.__api_version__
__author__ = _image_transform.__author__
__doc__ = _image_transform.__doc__

glImageTransformParameteriHP = _image_transform.glImageTransformParameteriHP

glImageTransformParameterfHP = _image_transform.glImageTransformParameterfHP

glImageTransformParameterivHP = _image_transform.glImageTransformParameterivHP

glImageTransformParameterfvHP = _image_transform.glImageTransformParameterfvHP

glGetImageTransformParameterfvHP = _image_transform.glGetImageTransformParameterfvHP

glGetImageTransformParameterivHP = _image_transform.glGetImageTransformParameterivHP

glInitImageTransformHP = _image_transform.glInitImageTransformHP

__info = _image_transform.__info
GL_IMAGE_SCALE_X_HP = _image_transform.GL_IMAGE_SCALE_X_HP
GL_IMAGE_SCALE_Y_HP = _image_transform.GL_IMAGE_SCALE_Y_HP
GL_IMAGE_TRANSLATE_X_HP = _image_transform.GL_IMAGE_TRANSLATE_X_HP
GL_IMAGE_TRANSLATE_Y_HP = _image_transform.GL_IMAGE_TRANSLATE_Y_HP
GL_IMAGE_ROTATE_ANGLE_HP = _image_transform.GL_IMAGE_ROTATE_ANGLE_HP
GL_IMAGE_ROTATE_ORIGIN_X_HP = _image_transform.GL_IMAGE_ROTATE_ORIGIN_X_HP
GL_IMAGE_ROTATE_ORIGIN_Y_HP = _image_transform.GL_IMAGE_ROTATE_ORIGIN_Y_HP
GL_IMAGE_MAG_FILTER_HP = _image_transform.GL_IMAGE_MAG_FILTER_HP
GL_IMAGE_MIN_FILTER_HP = _image_transform.GL_IMAGE_MIN_FILTER_HP
GL_IMAGE_CUBIC_WEIGHT_HP = _image_transform.GL_IMAGE_CUBIC_WEIGHT_HP
GL_CUBIC_HP = _image_transform.GL_CUBIC_HP
GL_AVERAGE_HP = _image_transform.GL_AVERAGE_HP
GL_IMAGE_TRANSFORM_2D_HP = _image_transform.GL_IMAGE_TRANSFORM_2D_HP
GL_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP = _image_transform.GL_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP
GL_PROXY_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP = _image_transform.GL_PROXY_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP

