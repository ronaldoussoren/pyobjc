# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _draw_buffers

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


__version__ = _draw_buffers.__version__
__date__ = _draw_buffers.__date__
__api_version__ = _draw_buffers.__api_version__
__author__ = _draw_buffers.__author__
__doc__ = _draw_buffers.__doc__

glDrawBuffersARB = _draw_buffers.glDrawBuffersARB
GL_MAX_DRAW_BUFFERS_ARB = _draw_buffers.GL_MAX_DRAW_BUFFERS_ARB
GL_DRAW_BUFFER0_ARB = _draw_buffers.GL_DRAW_BUFFER0_ARB
GL_DRAW_BUFFER1_ARB = _draw_buffers.GL_DRAW_BUFFER1_ARB
GL_DRAW_BUFFER2_ARB = _draw_buffers.GL_DRAW_BUFFER2_ARB
GL_DRAW_BUFFER3_ARB = _draw_buffers.GL_DRAW_BUFFER3_ARB
GL_DRAW_BUFFER4_ARB = _draw_buffers.GL_DRAW_BUFFER4_ARB
GL_DRAW_BUFFER5_ARB = _draw_buffers.GL_DRAW_BUFFER5_ARB
GL_DRAW_BUFFER6_ARB = _draw_buffers.GL_DRAW_BUFFER6_ARB
GL_DRAW_BUFFER7_ARB = _draw_buffers.GL_DRAW_BUFFER7_ARB
GL_DRAW_BUFFER8_ARB = _draw_buffers.GL_DRAW_BUFFER8_ARB
GL_DRAW_BUFFER9_ARB = _draw_buffers.GL_DRAW_BUFFER9_ARB
GL_DRAW_BUFFER10_ARB = _draw_buffers.GL_DRAW_BUFFER10_ARB
GL_DRAW_BUFFER11_ARB = _draw_buffers.GL_DRAW_BUFFER11_ARB
GL_DRAW_BUFFER12_ARB = _draw_buffers.GL_DRAW_BUFFER12_ARB
GL_DRAW_BUFFER13_ARB = _draw_buffers.GL_DRAW_BUFFER13_ARB
GL_DRAW_BUFFER14_ARB = _draw_buffers.GL_DRAW_BUFFER14_ARB
GL_DRAW_BUFFER15_ARB = _draw_buffers.GL_DRAW_BUFFER15_ARB

glInitDrawBuffersARB = _draw_buffers.glInitDrawBuffersARB

__info = _draw_buffers.__info

