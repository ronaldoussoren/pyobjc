# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _element_array

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


__version__ = _element_array.__version__
__date__ = _element_array.__date__
__api_version__ = _element_array.__api_version__
__author__ = _element_array.__author__
__doc__ = _element_array.__doc__

glElementPointerATI = _element_array.glElementPointerATI

glDrawElementArrayATI = _element_array.glDrawElementArrayATI

glDrawRangeElementArrayATI = _element_array.glDrawRangeElementArrayATI
GL_ELEMENT_ARRAY_ATI = _element_array.GL_ELEMENT_ARRAY_ATI
GL_ELEMENT_ARRAY_TYPE_ATI = _element_array.GL_ELEMENT_ARRAY_TYPE_ATI
GL_ELEMENT_ARRAY_POINTER_ATI = _element_array.GL_ELEMENT_ARRAY_POINTER_ATI

glInitElementArrayATI = _element_array.glInitElementArrayATI

__info = _element_array.__info

