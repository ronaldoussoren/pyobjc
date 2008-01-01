# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _clipmap

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


__version__ = _clipmap.__version__
__date__ = _clipmap.__date__
__api_version__ = _clipmap.__api_version__
__author__ = _clipmap.__author__
__doc__ = _clipmap.__doc__
GL_LINEAR_CLIPMAP_LINEAR_SGIX = _clipmap.GL_LINEAR_CLIPMAP_LINEAR_SGIX
GL_TEXTURE_CLIPMAP_CENTER_SGIX = _clipmap.GL_TEXTURE_CLIPMAP_CENTER_SGIX
GL_TEXTURE_CLIPMAP_FRAME_SGIX = _clipmap.GL_TEXTURE_CLIPMAP_FRAME_SGIX
GL_TEXTURE_CLIPMAP_OFFSET_SGIX = _clipmap.GL_TEXTURE_CLIPMAP_OFFSET_SGIX
GL_TEXTURE_CLIPMAP_VIRTUAL_DEPTH_SGIX = _clipmap.GL_TEXTURE_CLIPMAP_VIRTUAL_DEPTH_SGIX
GL_TEXTURE_CLIPMAP_LOD_OFFSET_SGIX = _clipmap.GL_TEXTURE_CLIPMAP_LOD_OFFSET_SGIX
GL_TEXTURE_CLIPMAP_DEPTH_SGIX = _clipmap.GL_TEXTURE_CLIPMAP_DEPTH_SGIX
GL_MAX_CLIPMAP_DEPTH_SGIX = _clipmap.GL_MAX_CLIPMAP_DEPTH_SGIX
GL_MAX_CLIPMAP_VIRTUAL_DEPTH_SGIX = _clipmap.GL_MAX_CLIPMAP_VIRTUAL_DEPTH_SGIX
GL_NEAREST_CLIPMAP_NEAREST_SGIX = _clipmap.GL_NEAREST_CLIPMAP_NEAREST_SGIX
GL_NEAREST_CLIPMAP_LINEAR_SGIX = _clipmap.GL_NEAREST_CLIPMAP_LINEAR_SGIX
GL_LINEAR_CLIPMAP_NEAREST_SGIX = _clipmap.GL_LINEAR_CLIPMAP_NEAREST_SGIX

glInitClipmapSGIX = _clipmap.glInitClipmapSGIX

__info = _clipmap.__info

