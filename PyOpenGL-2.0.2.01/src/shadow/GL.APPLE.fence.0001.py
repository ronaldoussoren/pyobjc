# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _fence

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


__version__ = _fence.__version__
__date__ = _fence.__date__
__api_version__ = _fence.__api_version__
__author__ = _fence.__author__
__doc__ = _fence.__doc__

glGenFencesAPPLE = _fence.glGenFencesAPPLE

glDeleteFencesAPPLE = _fence.glDeleteFencesAPPLE

glSetFenceAPPLE = _fence.glSetFenceAPPLE

glIsFenceAPPLE = _fence.glIsFenceAPPLE

glTestFenceAPPLE = _fence.glTestFenceAPPLE

glFinishFenceAPPLE = _fence.glFinishFenceAPPLE

glTestObjectAPPLE = _fence.glTestObjectAPPLE

glFinishObjectAPPLE = _fence.glFinishObjectAPPLE
GL_DRAW_PIXELS_APPLE = _fence.GL_DRAW_PIXELS_APPLE
GL_FENCE_APPLE = _fence.GL_FENCE_APPLE

glInitFenceAPPLE = _fence.glInitFenceAPPLE

__info = _fence.__info

