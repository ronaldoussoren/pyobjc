# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _global_alpha

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


__version__ = _global_alpha.__version__
__date__ = _global_alpha.__date__
__api_version__ = _global_alpha.__api_version__
__author__ = _global_alpha.__author__
__doc__ = _global_alpha.__doc__

__info = _global_alpha.__info

glInitGlobalAlphaSUN = _global_alpha.glInitGlobalAlphaSUN

glGlobalAlphaFactorbSUN = _global_alpha.glGlobalAlphaFactorbSUN

glGlobalAlphaFactorsSUN = _global_alpha.glGlobalAlphaFactorsSUN

glGlobalAlphaFactoriSUN = _global_alpha.glGlobalAlphaFactoriSUN

glGlobalAlphaFactorfSUN = _global_alpha.glGlobalAlphaFactorfSUN

glGlobalAlphaFactordSUN = _global_alpha.glGlobalAlphaFactordSUN

glGlobalAlphaFactorubSUN = _global_alpha.glGlobalAlphaFactorubSUN

glGlobalAlphaFactorusSUN = _global_alpha.glGlobalAlphaFactorusSUN

glGlobalAlphaFactoruiSUN = _global_alpha.glGlobalAlphaFactoruiSUN
GL_GLOBAL_ALPHA_SUN = _global_alpha.GL_GLOBAL_ALPHA_SUN
GL_GLOBAL_ALPHA_FACTOR_SUN = _global_alpha.GL_GLOBAL_ALPHA_FACTOR_SUN

