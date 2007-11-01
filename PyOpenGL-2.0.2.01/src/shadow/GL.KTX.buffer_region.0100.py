# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _buffer_region

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


__version__ = _buffer_region.__version__
__date__ = _buffer_region.__date__
__api_version__ = _buffer_region.__api_version__
__author__ = _buffer_region.__author__
__doc__ = _buffer_region.__doc__

glBufferRegionEnabled = _buffer_region.glBufferRegionEnabled

glNewBufferRegion = _buffer_region.glNewBufferRegion

glDeleteBufferRegion = _buffer_region.glDeleteBufferRegion

glReadBufferRegion = _buffer_region.glReadBufferRegion

glDrawBufferRegion = _buffer_region.glDrawBufferRegion

glInitBufferRegionKTX = _buffer_region.glInitBufferRegionKTX

__info = _buffer_region.__info
GL_KTX_FRONT_REGION = _buffer_region.GL_KTX_FRONT_REGION
GL_KTX_BACK_REGION = _buffer_region.GL_KTX_BACK_REGION
GL_KTX_Z_REGION = _buffer_region.GL_KTX_Z_REGION
GL_KTX_STENCIL_REGION = _buffer_region.GL_KTX_STENCIL_REGION

