# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _pixel_tiles

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


__version__ = _pixel_tiles.__version__
__date__ = _pixel_tiles.__date__
__api_version__ = _pixel_tiles.__api_version__
__author__ = _pixel_tiles.__author__
__doc__ = _pixel_tiles.__doc__
GL_PIXEL_TILE_BEST_ALIGNMENT_SGIX = _pixel_tiles.GL_PIXEL_TILE_BEST_ALIGNMENT_SGIX
GL_PIXEL_TILE_CACHE_INCREMENT_SGIX = _pixel_tiles.GL_PIXEL_TILE_CACHE_INCREMENT_SGIX
GL_PIXEL_TILE_WIDTH_SGIX = _pixel_tiles.GL_PIXEL_TILE_WIDTH_SGIX
GL_PIXEL_TILE_HEIGHT_SGIX = _pixel_tiles.GL_PIXEL_TILE_HEIGHT_SGIX
GL_PIXEL_TILE_GRID_WIDTH_SGIX = _pixel_tiles.GL_PIXEL_TILE_GRID_WIDTH_SGIX
GL_PIXEL_TILE_GRID_HEIGHT_SGIX = _pixel_tiles.GL_PIXEL_TILE_GRID_HEIGHT_SGIX
GL_PIXEL_TILE_GRID_DEPTH_SGIX = _pixel_tiles.GL_PIXEL_TILE_GRID_DEPTH_SGIX
GL_PIXEL_TILE_CACHE_SIZE_SGIX = _pixel_tiles.GL_PIXEL_TILE_CACHE_SIZE_SGIX

glInitPixelTilesSGIX = _pixel_tiles.glInitPixelTilesSGIX

__info = _pixel_tiles.__info

