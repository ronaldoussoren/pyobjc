# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _window_pos

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


__version__ = _window_pos.__version__
__date__ = _window_pos.__date__
__api_version__ = _window_pos.__api_version__
__author__ = _window_pos.__author__
__doc__ = _window_pos.__doc__

glWindowPos2dMESA = _window_pos.glWindowPos2dMESA

glWindowPos2fMESA = _window_pos.glWindowPos2fMESA

glWindowPos2iMESA = _window_pos.glWindowPos2iMESA

glWindowPos2sMESA = _window_pos.glWindowPos2sMESA

glWindowPos3dMESA = _window_pos.glWindowPos3dMESA

glWindowPos3fMESA = _window_pos.glWindowPos3fMESA

glWindowPos3iMESA = _window_pos.glWindowPos3iMESA

glWindowPos3sMESA = _window_pos.glWindowPos3sMESA

glWindowPos4dMESA = _window_pos.glWindowPos4dMESA

glWindowPos4fMESA = _window_pos.glWindowPos4fMESA

glWindowPos4iMESA = _window_pos.glWindowPos4iMESA

glWindowPos4sMESA = _window_pos.glWindowPos4sMESA

glWindowPos2dvMESA = _window_pos.glWindowPos2dvMESA

glWindowPos2fvMESA = _window_pos.glWindowPos2fvMESA

glWindowPos2ivMESA = _window_pos.glWindowPos2ivMESA

glWindowPos2svMESA = _window_pos.glWindowPos2svMESA

glWindowPos3dvMESA = _window_pos.glWindowPos3dvMESA

glWindowPos3fvMESA = _window_pos.glWindowPos3fvMESA

glWindowPos3ivMESA = _window_pos.glWindowPos3ivMESA

glWindowPos3svMESA = _window_pos.glWindowPos3svMESA

glWindowPos4dvMESA = _window_pos.glWindowPos4dvMESA

glWindowPos4fvMESA = _window_pos.glWindowPos4fvMESA

glWindowPos4ivMESA = _window_pos.glWindowPos4ivMESA

glWindowPos4svMESA = _window_pos.glWindowPos4svMESA

glInitWindowPosMESA = _window_pos.glInitWindowPosMESA

__info = _window_pos.__info

