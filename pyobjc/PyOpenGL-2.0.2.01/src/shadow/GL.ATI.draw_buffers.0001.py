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

glDrawBuffersATI = _draw_buffers.glDrawBuffersATI
GL_MAX_DRAW_BUFFERS_ATI = _draw_buffers.GL_MAX_DRAW_BUFFERS_ATI
GL_DRAW_BUFFER0_ATI = _draw_buffers.GL_DRAW_BUFFER0_ATI
GL_DRAW_BUFFER1_ATI = _draw_buffers.GL_DRAW_BUFFER1_ATI
GL_DRAW_BUFFER2_ATI = _draw_buffers.GL_DRAW_BUFFER2_ATI
GL_DRAW_BUFFER3_ATI = _draw_buffers.GL_DRAW_BUFFER3_ATI
GL_DRAW_BUFFER4_ATI = _draw_buffers.GL_DRAW_BUFFER4_ATI
GL_DRAW_BUFFER5_ATI = _draw_buffers.GL_DRAW_BUFFER5_ATI
GL_DRAW_BUFFER6_ATI = _draw_buffers.GL_DRAW_BUFFER6_ATI
GL_DRAW_BUFFER7_ATI = _draw_buffers.GL_DRAW_BUFFER7_ATI
GL_DRAW_BUFFER8_ATI = _draw_buffers.GL_DRAW_BUFFER8_ATI
GL_DRAW_BUFFER9_ATI = _draw_buffers.GL_DRAW_BUFFER9_ATI
GL_DRAW_BUFFER10_ATI = _draw_buffers.GL_DRAW_BUFFER10_ATI
GL_DRAW_BUFFER11_ATI = _draw_buffers.GL_DRAW_BUFFER11_ATI
GL_DRAW_BUFFER12_ATI = _draw_buffers.GL_DRAW_BUFFER12_ATI
GL_DRAW_BUFFER13_ATI = _draw_buffers.GL_DRAW_BUFFER13_ATI
GL_DRAW_BUFFER14_ATI = _draw_buffers.GL_DRAW_BUFFER14_ATI
GL_DRAW_BUFFER15_ATI = _draw_buffers.GL_DRAW_BUFFER15_ATI

glInitDrawBuffersATI = _draw_buffers.glInitDrawBuffersATI

__info = _draw_buffers.__info

