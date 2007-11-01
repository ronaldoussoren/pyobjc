# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _misc_hints

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


__version__ = _misc_hints.__version__
__date__ = _misc_hints.__date__
__api_version__ = _misc_hints.__api_version__
__author__ = _misc_hints.__author__
__doc__ = _misc_hints.__doc__

glHintPGI = _misc_hints.glHintPGI

glInitMiscHintsPGI = _misc_hints.glInitMiscHintsPGI

__info = _misc_hints.__info
GL_PREFER_DOUBLEBUFFER_HINT_PGI = _misc_hints.GL_PREFER_DOUBLEBUFFER_HINT_PGI
GL_STRICT_DEPTHFUNC_HINT_PGI = _misc_hints.GL_STRICT_DEPTHFUNC_HINT_PGI
GL_STRICT_LIGHTING_HINT_PGI = _misc_hints.GL_STRICT_LIGHTING_HINT_PGI
GL_STRICT_SCISSOR_HINT_PGI = _misc_hints.GL_STRICT_SCISSOR_HINT_PGI
GL_FULL_STIPPLE_HINT_PGI = _misc_hints.GL_FULL_STIPPLE_HINT_PGI
GL_NATIVE_GRAPHICS_BEGIN_HINT_PGI = _misc_hints.GL_NATIVE_GRAPHICS_BEGIN_HINT_PGI
GL_NATIVE_GRAPHICS_END_HINT_PGI = _misc_hints.GL_NATIVE_GRAPHICS_END_HINT_PGI
GL_CONSERVE_MEMORY_HINT_PGI = _misc_hints.GL_CONSERVE_MEMORY_HINT_PGI
GL_RECLAIM_MEMORY_HINT_PGI = _misc_hints.GL_RECLAIM_MEMORY_HINT_PGI
GL_ALWAYS_FAST_HINT_PGI = _misc_hints.GL_ALWAYS_FAST_HINT_PGI
GL_ALWAYS_SOFT_HINT_PGI = _misc_hints.GL_ALWAYS_SOFT_HINT_PGI
GL_ALLOW_DRAW_OBJ_HINT_PGI = _misc_hints.GL_ALLOW_DRAW_OBJ_HINT_PGI
GL_ALLOW_DRAW_WIN_HINT_PGI = _misc_hints.GL_ALLOW_DRAW_WIN_HINT_PGI
GL_ALLOW_DRAW_FRG_HINT_PGI = _misc_hints.GL_ALLOW_DRAW_FRG_HINT_PGI
GL_ALLOW_DRAW_MEM_HINT_PGI = _misc_hints.GL_ALLOW_DRAW_MEM_HINT_PGI
GL_CLIP_NEAR_HINT_PGI = _misc_hints.GL_CLIP_NEAR_HINT_PGI
GL_CLIP_FAR_HINT_PGI = _misc_hints.GL_CLIP_FAR_HINT_PGI
GL_WIDE_LINE_HINT_PGI = _misc_hints.GL_WIDE_LINE_HINT_PGI
GL_BACK_NORMALS_HINT_PGI = _misc_hints.GL_BACK_NORMALS_HINT_PGI
GL_NATIVE_GRAPHICS_HANDLE_PGI = _misc_hints.GL_NATIVE_GRAPHICS_HANDLE_PGI

