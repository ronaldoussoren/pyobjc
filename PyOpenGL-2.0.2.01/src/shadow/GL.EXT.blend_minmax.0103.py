# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _blend_minmax

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


__version__ = _blend_minmax.__version__
__date__ = _blend_minmax.__date__
__api_version__ = _blend_minmax.__api_version__
__author__ = _blend_minmax.__author__
__doc__ = _blend_minmax.__doc__

glBlendEquationEXT = _blend_minmax.glBlendEquationEXT

glInitBlendMinmaxEXT = _blend_minmax.glInitBlendMinmaxEXT

__info = _blend_minmax.__info
GL_FUNC_ADD_EXT = _blend_minmax.GL_FUNC_ADD_EXT
GL_MIN_EXT = _blend_minmax.GL_MIN_EXT
GL_MAX_EXT = _blend_minmax.GL_MAX_EXT
GL_BLEND_EQUATION_EXT = _blend_minmax.GL_BLEND_EQUATION_EXT

