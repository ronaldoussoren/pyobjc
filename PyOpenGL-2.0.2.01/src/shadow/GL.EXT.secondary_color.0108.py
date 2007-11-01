# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _secondary_color

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


__version__ = _secondary_color.__version__
__date__ = _secondary_color.__date__
__api_version__ = _secondary_color.__api_version__
__author__ = _secondary_color.__author__
__doc__ = _secondary_color.__doc__

glSecondaryColor3ubEXT = _secondary_color.glSecondaryColor3ubEXT

glSecondaryColor3bEXT = _secondary_color.glSecondaryColor3bEXT

glSecondaryColor3usEXT = _secondary_color.glSecondaryColor3usEXT

glSecondaryColor3sEXT = _secondary_color.glSecondaryColor3sEXT

glSecondaryColor3uiEXT = _secondary_color.glSecondaryColor3uiEXT

glSecondaryColor3iEXT = _secondary_color.glSecondaryColor3iEXT

glSecondaryColor3fEXT = _secondary_color.glSecondaryColor3fEXT

glSecondaryColor3dEXT = _secondary_color.glSecondaryColor3dEXT

glSecondaryColor3ubvEXT = _secondary_color.glSecondaryColor3ubvEXT

glSecondaryColor3bvEXT = _secondary_color.glSecondaryColor3bvEXT

glSecondaryColor3usvEXT = _secondary_color.glSecondaryColor3usvEXT

glSecondaryColor3svEXT = _secondary_color.glSecondaryColor3svEXT

glSecondaryColor3uivEXT = _secondary_color.glSecondaryColor3uivEXT

glSecondaryColor3ivEXT = _secondary_color.glSecondaryColor3ivEXT

glSecondaryColor3fvEXT = _secondary_color.glSecondaryColor3fvEXT

glSecondaryColor3dvEXT = _secondary_color.glSecondaryColor3dvEXT

glSecondaryColorPointerEXT = _secondary_color.glSecondaryColorPointerEXT

glSecondaryColorPointerubEXT = _secondary_color.glSecondaryColorPointerubEXT

glSecondaryColorPointerbEXT = _secondary_color.glSecondaryColorPointerbEXT

glSecondaryColorPointerusEXT = _secondary_color.glSecondaryColorPointerusEXT

glSecondaryColorPointersEXT = _secondary_color.glSecondaryColorPointersEXT

glSecondaryColorPointeruiEXT = _secondary_color.glSecondaryColorPointeruiEXT

glSecondaryColorPointeriEXT = _secondary_color.glSecondaryColorPointeriEXT

glSecondaryColorPointerfEXT = _secondary_color.glSecondaryColorPointerfEXT

glSecondaryColorPointerdEXT = _secondary_color.glSecondaryColorPointerdEXT

glInitSecondaryColorEXT = _secondary_color.glInitSecondaryColorEXT

__info = _secondary_color.__info
GL_COLOR_SUM_EXT = _secondary_color.GL_COLOR_SUM_EXT
GL_CURRENT_SECONDARY_COLOR_EXT = _secondary_color.GL_CURRENT_SECONDARY_COLOR_EXT
GL_SECONDARY_COLOR_ARRAY_SIZE_EXT = _secondary_color.GL_SECONDARY_COLOR_ARRAY_SIZE_EXT
GL_SECONDARY_COLOR_ARRAY_TYPE_EXT = _secondary_color.GL_SECONDARY_COLOR_ARRAY_TYPE_EXT
GL_SECONDARY_COLOR_ARRAY_STRIDE_EXT = _secondary_color.GL_SECONDARY_COLOR_ARRAY_STRIDE_EXT
GL_SECONDARY_COLOR_ARRAY_POINTER_EXT = _secondary_color.GL_SECONDARY_COLOR_ARRAY_POINTER_EXT
GL_SECONDARY_COLOR_ARRAY_EXT = _secondary_color.GL_SECONDARY_COLOR_ARRAY_EXT

