# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _nurbs_tessellator

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


__version__ = _nurbs_tessellator.__version__
__date__ = _nurbs_tessellator.__date__
__api_version__ = _nurbs_tessellator.__api_version__
__author__ = _nurbs_tessellator.__author__
__doc__ = _nurbs_tessellator.__doc__

__gluNurbsCallbackDataEXT = _nurbs_tessellator.__gluNurbsCallbackDataEXT

gluInitNurbsTessellatorEXT = _nurbs_tessellator.gluInitNurbsTessellatorEXT

__info = _nurbs_tessellator.__info
GLU_NURBS_MODE_EXT = _nurbs_tessellator.GLU_NURBS_MODE_EXT
GLU_NURBS_TESSELLATOR_EXT = _nurbs_tessellator.GLU_NURBS_TESSELLATOR_EXT
GLU_NURBS_RENDERER_EXT = _nurbs_tessellator.GLU_NURBS_RENDERER_EXT
GLU_NURBS_BEGIN_EXT = _nurbs_tessellator.GLU_NURBS_BEGIN_EXT
GLU_NURBS_VERTEX_EXT = _nurbs_tessellator.GLU_NURBS_VERTEX_EXT
GLU_NURBS_NORMAL_EXT = _nurbs_tessellator.GLU_NURBS_NORMAL_EXT
GLU_NURBS_COLOR_EXT = _nurbs_tessellator.GLU_NURBS_COLOR_EXT
GLU_NURBS_TEXTURE_COORD_EXT = _nurbs_tessellator.GLU_NURBS_TEXTURE_COORD_EXT
GLU_NURBS_END_EXT = _nurbs_tessellator.GLU_NURBS_END_EXT
GLU_NURBS_BEGIN_DATA_EXT = _nurbs_tessellator.GLU_NURBS_BEGIN_DATA_EXT
GLU_NURBS_VERTEX_DATA_EXT = _nurbs_tessellator.GLU_NURBS_VERTEX_DATA_EXT
GLU_NURBS_NORMAL_DATA_EXT = _nurbs_tessellator.GLU_NURBS_NORMAL_DATA_EXT
GLU_NURBS_COLOR_DATA_EXT = _nurbs_tessellator.GLU_NURBS_COLOR_DATA_EXT
GLU_NURBS_TEXTURE_COORD_DATA_EXT = _nurbs_tessellator.GLU_NURBS_TEXTURE_COORD_DATA_EXT
GLU_NURBS_END_DATA_EXT = _nurbs_tessellator.GLU_NURBS_END_DATA_EXT

