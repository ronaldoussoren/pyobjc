# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _list_priority

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


__version__ = _list_priority.__version__
__date__ = _list_priority.__date__
__api_version__ = _list_priority.__api_version__
__author__ = _list_priority.__author__
__doc__ = _list_priority.__doc__

glInitListPrioritySGIX = _list_priority.glInitListPrioritySGIX

glListParameterfSGIX = _list_priority.glListParameterfSGIX

glListParameterfvSGIX = _list_priority.glListParameterfvSGIX

glListParameteriSGIX = _list_priority.glListParameteriSGIX

glListParameterivSGIX = _list_priority.glListParameterivSGIX

glGetListParameterfvSGIX = _list_priority.glGetListParameterfvSGIX

glGetListParameterivSGIX = _list_priority.glGetListParameterivSGIX

__info = _list_priority.__info

