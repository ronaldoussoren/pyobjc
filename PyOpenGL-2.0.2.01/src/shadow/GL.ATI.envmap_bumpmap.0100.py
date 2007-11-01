# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _envmap_bumpmap

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


__version__ = _envmap_bumpmap.__version__
__date__ = _envmap_bumpmap.__date__
__api_version__ = _envmap_bumpmap.__api_version__
__author__ = _envmap_bumpmap.__author__
__doc__ = _envmap_bumpmap.__doc__

glTexBumpParameterivEXT = _envmap_bumpmap.glTexBumpParameterivEXT

glTexBumpParameterfvEXT = _envmap_bumpmap.glTexBumpParameterfvEXT

glGetTexBumpParameterivEXT = _envmap_bumpmap.glGetTexBumpParameterivEXT

glGetTexBumpParameterfvEXT = _envmap_bumpmap.glGetTexBumpParameterfvEXT

glInitTexBumpmapATI = _envmap_bumpmap.glInitTexBumpmapATI

__info = _envmap_bumpmap.__info
GL_BUMP_ROT_MATRIX_ATI = _envmap_bumpmap.GL_BUMP_ROT_MATRIX_ATI
GL_BUMP_ROT_MATRIX_SIZE_ATI = _envmap_bumpmap.GL_BUMP_ROT_MATRIX_SIZE_ATI
GL_BUMP_NUM_TEX_UNITS_ATI = _envmap_bumpmap.GL_BUMP_NUM_TEX_UNITS_ATI
GL_BUMP_TEX_UNITS_ATI = _envmap_bumpmap.GL_BUMP_TEX_UNITS_ATI
GL_DUDV_ATI = _envmap_bumpmap.GL_DUDV_ATI
GL_DU8DV8_ATI = _envmap_bumpmap.GL_DU8DV8_ATI
GL_BUMP_ENVMAP_ATI = _envmap_bumpmap.GL_BUMP_ENVMAP_ATI
GL_BUMP_TARGET_ATI = _envmap_bumpmap.GL_BUMP_TARGET_ATI

