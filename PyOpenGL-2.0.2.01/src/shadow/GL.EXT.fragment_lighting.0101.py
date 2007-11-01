# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _fragment_lighting

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


__version__ = _fragment_lighting.__version__
__date__ = _fragment_lighting.__date__
__api_version__ = _fragment_lighting.__api_version__
__author__ = _fragment_lighting.__author__
__doc__ = _fragment_lighting.__doc__

glFragmentMaterialfEXT = _fragment_lighting.glFragmentMaterialfEXT

glFragmentMaterialfvEXT = _fragment_lighting.glFragmentMaterialfvEXT

glFragmentMaterialiEXT = _fragment_lighting.glFragmentMaterialiEXT

glFragmentMaterialivEXT = _fragment_lighting.glFragmentMaterialivEXT

glFragmentLightModelfEXT = _fragment_lighting.glFragmentLightModelfEXT

glFragmentLightModelfvEXT = _fragment_lighting.glFragmentLightModelfvEXT

glFragmentLightModeliEXT = _fragment_lighting.glFragmentLightModeliEXT

glFragmentLightModelivEXT = _fragment_lighting.glFragmentLightModelivEXT

glFragmentLightfEXT = _fragment_lighting.glFragmentLightfEXT

glFragmentLightfvEXT = _fragment_lighting.glFragmentLightfvEXT

glFragmentLightiEXT = _fragment_lighting.glFragmentLightiEXT

glFragmentLightivEXT = _fragment_lighting.glFragmentLightivEXT

glGetFragmentLightfvEXT = _fragment_lighting.glGetFragmentLightfvEXT

glGetFragmentLightivEXT = _fragment_lighting.glGetFragmentLightivEXT

glFragmentColorMaterialEXT = _fragment_lighting.glFragmentColorMaterialEXT

glGetFragmentMaterialfvEXT = _fragment_lighting.glGetFragmentMaterialfvEXT

glGetFragmentMaterialivEXT = _fragment_lighting.glGetFragmentMaterialivEXT

glLightEnviEXT = _fragment_lighting.glLightEnviEXT

glInitFragmentLightingEXT = _fragment_lighting.glInitFragmentLightingEXT

__info = _fragment_lighting.__info
GL_FRAGMENT_LIGHTING_EXT = _fragment_lighting.GL_FRAGMENT_LIGHTING_EXT
GL_FRAGMENT_COLOR_MATERIAL_EXT = _fragment_lighting.GL_FRAGMENT_COLOR_MATERIAL_EXT
GL_FRAGMENT_COLOR_MATERIAL_FACE_EXT = _fragment_lighting.GL_FRAGMENT_COLOR_MATERIAL_FACE_EXT
GL_FRAGMENT_COLOR_MATERIAL_PARAMETER_EXT = _fragment_lighting.GL_FRAGMENT_COLOR_MATERIAL_PARAMETER_EXT
GL_MAX_FRAGMENT_LIGHTS_EXT = _fragment_lighting.GL_MAX_FRAGMENT_LIGHTS_EXT
GL_MAX_ACTIVE_LIGHTS_EXT = _fragment_lighting.GL_MAX_ACTIVE_LIGHTS_EXT
GL_CURRENT_RASTER_NORMAL_EXT = _fragment_lighting.GL_CURRENT_RASTER_NORMAL_EXT
GL_LIGHT_ENV_MODE_EXT = _fragment_lighting.GL_LIGHT_ENV_MODE_EXT
GL_FRAGMENT_LIGHT_MODEL_LOCAL_VIEWER_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT_MODEL_LOCAL_VIEWER_EXT
GL_FRAGMENT_LIGHT_MODEL_TWO_SIDE_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT_MODEL_TWO_SIDE_EXT
GL_FRAGMENT_LIGHT_MODEL_AMBIENT_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT_MODEL_AMBIENT_EXT
GL_FRAGMENT_LIGHT_MODEL_NORMAL_INTERPOLATION_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT_MODEL_NORMAL_INTERPOLATION_EXT
GL_FRAGMENT_LIGHT0_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT0_EXT
GL_FRAGMENT_LIGHT1_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT1_EXT
GL_FRAGMENT_LIGHT2_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT2_EXT
GL_FRAGMENT_LIGHT3_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT3_EXT
GL_FRAGMENT_LIGHT4_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT4_EXT
GL_FRAGMENT_LIGHT5_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT5_EXT
GL_FRAGMENT_LIGHT6_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT6_EXT
GL_FRAGMENT_LIGHT7_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT7_EXT
GL_FRAGMENT_LIGHT8_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT8_EXT
GL_FRAGMENT_LIGHT9_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT9_EXT
GL_FRAGMENT_LIGHT10_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT10_EXT
GL_FRAGMENT_LIGHT11_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT11_EXT
GL_FRAGMENT_LIGHT12_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT12_EXT
GL_FRAGMENT_LIGHT13_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT13_EXT
GL_FRAGMENT_LIGHT14_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT14_EXT
GL_FRAGMENT_LIGHT15_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT15_EXT
GL_FRAGMENT_LIGHT16_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT16_EXT
GL_FRAGMENT_LIGHT17_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT17_EXT
GL_FRAGMENT_LIGHT18_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT18_EXT
GL_FRAGMENT_LIGHT19_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT19_EXT
GL_FRAGMENT_LIGHT20_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT20_EXT
GL_FRAGMENT_LIGHT21_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT21_EXT
GL_FRAGMENT_LIGHT22_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT22_EXT
GL_FRAGMENT_LIGHT23_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT23_EXT
GL_FRAGMENT_LIGHT24_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT24_EXT
GL_FRAGMENT_LIGHT25_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT25_EXT
GL_FRAGMENT_LIGHT26_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT26_EXT
GL_FRAGMENT_LIGHT27_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT27_EXT
GL_FRAGMENT_LIGHT28_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT28_EXT
GL_FRAGMENT_LIGHT29_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT29_EXT
GL_FRAGMENT_LIGHT30_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT30_EXT
GL_FRAGMENT_LIGHT31_EXT = _fragment_lighting.GL_FRAGMENT_LIGHT31_EXT

