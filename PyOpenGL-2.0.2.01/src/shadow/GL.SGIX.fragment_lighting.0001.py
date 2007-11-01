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

glFragmentColorMaterialSGIX = _fragment_lighting.glFragmentColorMaterialSGIX

glFragmentLightfSGIX = _fragment_lighting.glFragmentLightfSGIX

glFragmentLightfvSGIX = _fragment_lighting.glFragmentLightfvSGIX

glFragmentLightiSGIX = _fragment_lighting.glFragmentLightiSGIX

glFragmentLightivSGIX = _fragment_lighting.glFragmentLightivSGIX

glFragmentLightModelfSGIX = _fragment_lighting.glFragmentLightModelfSGIX

glFragmentLightModelfvSGIX = _fragment_lighting.glFragmentLightModelfvSGIX

glFragmentLightModeliSGIX = _fragment_lighting.glFragmentLightModeliSGIX

glFragmentLightModelivSGIX = _fragment_lighting.glFragmentLightModelivSGIX

glFragmentMaterialfSGIX = _fragment_lighting.glFragmentMaterialfSGIX

glFragmentMaterialfvSGIX = _fragment_lighting.glFragmentMaterialfvSGIX

glFragmentMaterialiSGIX = _fragment_lighting.glFragmentMaterialiSGIX

glFragmentMaterialivSGIX = _fragment_lighting.glFragmentMaterialivSGIX

glGetFragmentLightfvSGIX = _fragment_lighting.glGetFragmentLightfvSGIX

glGetFragmentLightivSGIX = _fragment_lighting.glGetFragmentLightivSGIX

glGetFragmentMaterialfvSGIX = _fragment_lighting.glGetFragmentMaterialfvSGIX

glGetFragmentMaterialivSGIX = _fragment_lighting.glGetFragmentMaterialivSGIX

glLightEnviSGIX = _fragment_lighting.glLightEnviSGIX
GL_FRAGMENT_LIGHTING_SGIX = _fragment_lighting.GL_FRAGMENT_LIGHTING_SGIX
GL_FRAGMENT_COLOR_MATERIAL_SGIX = _fragment_lighting.GL_FRAGMENT_COLOR_MATERIAL_SGIX
GL_FRAGMENT_COLOR_MATERIAL_FACE_SGIX = _fragment_lighting.GL_FRAGMENT_COLOR_MATERIAL_FACE_SGIX
GL_FRAGMENT_COLOR_MATERIAL_PARAMETER_SGIX = _fragment_lighting.GL_FRAGMENT_COLOR_MATERIAL_PARAMETER_SGIX
GL_MAX_FRAGMENT_LIGHTS_SGIX = _fragment_lighting.GL_MAX_FRAGMENT_LIGHTS_SGIX
GL_MAX_ACTIVE_LIGHTS_SGIX = _fragment_lighting.GL_MAX_ACTIVE_LIGHTS_SGIX
GL_CURRENT_RASTER_NORMAL_SGIX = _fragment_lighting.GL_CURRENT_RASTER_NORMAL_SGIX
GL_LIGHT_ENV_MODE_SGIX = _fragment_lighting.GL_LIGHT_ENV_MODE_SGIX
GL_FRAGMENT_LIGHT_MODEL_LOCAL_VIEWER_SGIX = _fragment_lighting.GL_FRAGMENT_LIGHT_MODEL_LOCAL_VIEWER_SGIX
GL_FRAGMENT_LIGHT_MODEL_TWO_SIDE_SGIX = _fragment_lighting.GL_FRAGMENT_LIGHT_MODEL_TWO_SIDE_SGIX
GL_FRAGMENT_LIGHT_MODEL_AMBIENT_SGIX = _fragment_lighting.GL_FRAGMENT_LIGHT_MODEL_AMBIENT_SGIX
GL_FRAGMENT_LIGHT_MODEL_NORMAL_INTERPOLATION_SGIX = _fragment_lighting.GL_FRAGMENT_LIGHT_MODEL_NORMAL_INTERPOLATION_SGIX
GL_FRAGMENT_LIGHT0_SGIX = _fragment_lighting.GL_FRAGMENT_LIGHT0_SGIX
GL_FRAGMENT_LIGHT1_SGIX = _fragment_lighting.GL_FRAGMENT_LIGHT1_SGIX
GL_FRAGMENT_LIGHT2_SGIX = _fragment_lighting.GL_FRAGMENT_LIGHT2_SGIX
GL_FRAGMENT_LIGHT3_SGIX = _fragment_lighting.GL_FRAGMENT_LIGHT3_SGIX
GL_FRAGMENT_LIGHT4_SGIX = _fragment_lighting.GL_FRAGMENT_LIGHT4_SGIX
GL_FRAGMENT_LIGHT5_SGIX = _fragment_lighting.GL_FRAGMENT_LIGHT5_SGIX
GL_FRAGMENT_LIGHT6_SGIX = _fragment_lighting.GL_FRAGMENT_LIGHT6_SGIX
GL_FRAGMENT_LIGHT7_SGIX = _fragment_lighting.GL_FRAGMENT_LIGHT7_SGIX

glInitFragmentLightingSGIX = _fragment_lighting.glInitFragmentLightingSGIX

__info = _fragment_lighting.__info

