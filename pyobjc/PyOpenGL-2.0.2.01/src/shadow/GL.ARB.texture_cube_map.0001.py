# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _texture_cube_map

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


__version__ = _texture_cube_map.__version__
__date__ = _texture_cube_map.__date__
__api_version__ = _texture_cube_map.__api_version__
__author__ = _texture_cube_map.__author__
__doc__ = _texture_cube_map.__doc__
GL_NORMAL_MAP_ARB = _texture_cube_map.GL_NORMAL_MAP_ARB
GL_REFLECTION_MAP_ARB = _texture_cube_map.GL_REFLECTION_MAP_ARB
GL_TEXTURE_CUBE_MAP_ARB = _texture_cube_map.GL_TEXTURE_CUBE_MAP_ARB
GL_TEXTURE_BINDING_CUBE_MAP_ARB = _texture_cube_map.GL_TEXTURE_BINDING_CUBE_MAP_ARB
GL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB = _texture_cube_map.GL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB
GL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB = _texture_cube_map.GL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB
GL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB = _texture_cube_map.GL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB = _texture_cube_map.GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB
GL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB = _texture_cube_map.GL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB = _texture_cube_map.GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB
GL_PROXY_TEXTURE_CUBE_MAP_ARB = _texture_cube_map.GL_PROXY_TEXTURE_CUBE_MAP_ARB
GL_MAX_CUBE_MAP_TEXTURE_SIZE_ARB = _texture_cube_map.GL_MAX_CUBE_MAP_TEXTURE_SIZE_ARB

glInitTextureCubeMapARB = _texture_cube_map.glInitTextureCubeMapARB

__info = _texture_cube_map.__info

