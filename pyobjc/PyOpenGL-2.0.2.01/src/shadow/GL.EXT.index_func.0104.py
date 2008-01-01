# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _index_func

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


__version__ = _index_func.__version__
__date__ = _index_func.__date__
__api_version__ = _index_func.__api_version__
__author__ = _index_func.__author__
__doc__ = _index_func.__doc__

glIndexFuncEXT = _index_func.glIndexFuncEXT

glInitIndexFuncEXT = _index_func.glInitIndexFuncEXT

__info = _index_func.__info
GL_INDEX_TEST_EXT = _index_func.GL_INDEX_TEST_EXT
GL_INDEX_TEST_FUNC_EXT = _index_func.GL_INDEX_TEST_FUNC_EXT
GL_INDEX_TEST_REF_EXT = _index_func.GL_INDEX_TEST_REF_EXT

