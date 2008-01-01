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

glInitWindowPosARB = _window_pos.glInitWindowPosARB

glWindowPos2dARB = _window_pos.glWindowPos2dARB

glWindowPos2fARB = _window_pos.glWindowPos2fARB

glWindowPos2iARB = _window_pos.glWindowPos2iARB

glWindowPos2sARB = _window_pos.glWindowPos2sARB

glWindowPos2dvARB = _window_pos.glWindowPos2dvARB

glWindowPos2fvARB = _window_pos.glWindowPos2fvARB

glWindowPos2ivARB = _window_pos.glWindowPos2ivARB

glWindowPos2svARB = _window_pos.glWindowPos2svARB

glWindowPos3dARB = _window_pos.glWindowPos3dARB

glWindowPos3fARB = _window_pos.glWindowPos3fARB

glWindowPos3iARB = _window_pos.glWindowPos3iARB

glWindowPos3sARB = _window_pos.glWindowPos3sARB

glWindowPos3dvARB = _window_pos.glWindowPos3dvARB

glWindowPos3fvARB = _window_pos.glWindowPos3fvARB

glWindowPos3ivARB = _window_pos.glWindowPos3ivARB

glWindowPos3svARB = _window_pos.glWindowPos3svARB

__info = _window_pos.__info

