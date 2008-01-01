# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _vertex_array

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


__version__ = _vertex_array.__version__
__date__ = _vertex_array.__date__
__api_version__ = _vertex_array.__api_version__
__author__ = _vertex_array.__author__
__doc__ = _vertex_array.__doc__

glArrayElementEXT = _vertex_array.glArrayElementEXT

glColorPointerEXT = _vertex_array.glColorPointerEXT

glColorPointerubEXT = _vertex_array.glColorPointerubEXT

glColorPointerbEXT = _vertex_array.glColorPointerbEXT

glColorPointerusEXT = _vertex_array.glColorPointerusEXT

glColorPointersEXT = _vertex_array.glColorPointersEXT

glColorPointeruiEXT = _vertex_array.glColorPointeruiEXT

glColorPointeriEXT = _vertex_array.glColorPointeriEXT

glColorPointerfEXT = _vertex_array.glColorPointerfEXT

glColorPointerdEXT = _vertex_array.glColorPointerdEXT

glDrawArraysEXT = _vertex_array.glDrawArraysEXT

glEdgeFlagPointerEXT = _vertex_array.glEdgeFlagPointerEXT

glEdgeFlagPointerbEXT = _vertex_array.glEdgeFlagPointerbEXT

glIndexPointerEXT = _vertex_array.glIndexPointerEXT

glIndexPointerubEXT = _vertex_array.glIndexPointerubEXT

glIndexPointerbEXT = _vertex_array.glIndexPointerbEXT

glIndexPointersEXT = _vertex_array.glIndexPointersEXT

glIndexPointeriEXT = _vertex_array.glIndexPointeriEXT

glIndexPointerfEXT = _vertex_array.glIndexPointerfEXT

glIndexPointerdEXT = _vertex_array.glIndexPointerdEXT

glNormalPointerEXT = _vertex_array.glNormalPointerEXT

glNormalPointerbEXT = _vertex_array.glNormalPointerbEXT

glNormalPointersEXT = _vertex_array.glNormalPointersEXT

glNormalPointeriEXT = _vertex_array.glNormalPointeriEXT

glNormalPointerfEXT = _vertex_array.glNormalPointerfEXT

glNormalPointerdEXT = _vertex_array.glNormalPointerdEXT

glTexCoordPointerEXT = _vertex_array.glTexCoordPointerEXT

glTexCoordPointerbEXT = _vertex_array.glTexCoordPointerbEXT

glTexCoordPointersEXT = _vertex_array.glTexCoordPointersEXT

glTexCoordPointeriEXT = _vertex_array.glTexCoordPointeriEXT

glTexCoordPointerfEXT = _vertex_array.glTexCoordPointerfEXT

glTexCoordPointerdEXT = _vertex_array.glTexCoordPointerdEXT

glVertexPointerEXT = _vertex_array.glVertexPointerEXT

glVertexPointerbEXT = _vertex_array.glVertexPointerbEXT

glVertexPointersEXT = _vertex_array.glVertexPointersEXT

glVertexPointeriEXT = _vertex_array.glVertexPointeriEXT

glVertexPointerfEXT = _vertex_array.glVertexPointerfEXT

glVertexPointerdEXT = _vertex_array.glVertexPointerdEXT

glInitVertexArrayEXT = _vertex_array.glInitVertexArrayEXT

__info = _vertex_array.__info
GL_VERTEX_ARRAY_EXT = _vertex_array.GL_VERTEX_ARRAY_EXT
GL_NORMAL_ARRAY_EXT = _vertex_array.GL_NORMAL_ARRAY_EXT
GL_COLOR_ARRAY_EXT = _vertex_array.GL_COLOR_ARRAY_EXT
GL_INDEX_ARRAY_EXT = _vertex_array.GL_INDEX_ARRAY_EXT
GL_TEXTURE_COORD_ARRAY_EXT = _vertex_array.GL_TEXTURE_COORD_ARRAY_EXT
GL_EDGE_FLAG_ARRAY_EXT = _vertex_array.GL_EDGE_FLAG_ARRAY_EXT
GL_DOUBLE_EXT = _vertex_array.GL_DOUBLE_EXT
GL_VERTEX_ARRAY_SIZE_EXT = _vertex_array.GL_VERTEX_ARRAY_SIZE_EXT
GL_VERTEX_ARRAY_TYPE_EXT = _vertex_array.GL_VERTEX_ARRAY_TYPE_EXT
GL_VERTEX_ARRAY_STRIDE_EXT = _vertex_array.GL_VERTEX_ARRAY_STRIDE_EXT
GL_VERTEX_ARRAY_COUNT_EXT = _vertex_array.GL_VERTEX_ARRAY_COUNT_EXT
GL_NORMAL_ARRAY_TYPE_EXT = _vertex_array.GL_NORMAL_ARRAY_TYPE_EXT
GL_NORMAL_ARRAY_STRIDE_EXT = _vertex_array.GL_NORMAL_ARRAY_STRIDE_EXT
GL_NORMAL_ARRAY_COUNT_EXT = _vertex_array.GL_NORMAL_ARRAY_COUNT_EXT
GL_COLOR_ARRAY_SIZE_EXT = _vertex_array.GL_COLOR_ARRAY_SIZE_EXT
GL_COLOR_ARRAY_TYPE_EXT = _vertex_array.GL_COLOR_ARRAY_TYPE_EXT
GL_COLOR_ARRAY_STRIDE_EXT = _vertex_array.GL_COLOR_ARRAY_STRIDE_EXT
GL_COLOR_ARRAY_COUNT_EXT = _vertex_array.GL_COLOR_ARRAY_COUNT_EXT
GL_INDEX_ARRAY_TYPE_EXT = _vertex_array.GL_INDEX_ARRAY_TYPE_EXT
GL_INDEX_ARRAY_STRIDE_EXT = _vertex_array.GL_INDEX_ARRAY_STRIDE_EXT
GL_INDEX_ARRAY_COUNT_EXT = _vertex_array.GL_INDEX_ARRAY_COUNT_EXT
GL_TEXTURE_COORD_ARRAY_SIZE_EXT = _vertex_array.GL_TEXTURE_COORD_ARRAY_SIZE_EXT
GL_TEXTURE_COORD_ARRAY_TYPE_EXT = _vertex_array.GL_TEXTURE_COORD_ARRAY_TYPE_EXT
GL_TEXTURE_COORD_ARRAY_STRIDE_EXT = _vertex_array.GL_TEXTURE_COORD_ARRAY_STRIDE_EXT
GL_TEXTURE_COORD_ARRAY_COUNT_EXT = _vertex_array.GL_TEXTURE_COORD_ARRAY_COUNT_EXT
GL_EDGE_FLAG_ARRAY_STRIDE_EXT = _vertex_array.GL_EDGE_FLAG_ARRAY_STRIDE_EXT
GL_EDGE_FLAG_ARRAY_COUNT_EXT = _vertex_array.GL_EDGE_FLAG_ARRAY_COUNT_EXT
GL_VERTEX_ARRAY_POINTER_EXT = _vertex_array.GL_VERTEX_ARRAY_POINTER_EXT
GL_NORMAL_ARRAY_POINTER_EXT = _vertex_array.GL_NORMAL_ARRAY_POINTER_EXT
GL_COLOR_ARRAY_POINTER_EXT = _vertex_array.GL_COLOR_ARRAY_POINTER_EXT
GL_INDEX_ARRAY_POINTER_EXT = _vertex_array.GL_INDEX_ARRAY_POINTER_EXT
GL_TEXTURE_COORD_ARRAY_POINTER_EXT = _vertex_array.GL_TEXTURE_COORD_ARRAY_POINTER_EXT
GL_EDGE_FLAG_ARRAY_POINTER_EXT = _vertex_array.GL_EDGE_FLAG_ARRAY_POINTER_EXT

