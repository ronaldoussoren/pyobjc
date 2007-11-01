# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _triangle_list

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


__version__ = _triangle_list.__version__
__date__ = _triangle_list.__date__
__api_version__ = _triangle_list.__api_version__
__author__ = _triangle_list.__author__
__doc__ = _triangle_list.__doc__

glInitTriangleListSUN = _triangle_list.glInitTriangleListSUN

glReplacementCodeuiSUN = _triangle_list.glReplacementCodeuiSUN

glReplacementCodeusSUN = _triangle_list.glReplacementCodeusSUN

glReplacementCodeubSUN = _triangle_list.glReplacementCodeubSUN

glReplacementCodeuivSUN = _triangle_list.glReplacementCodeuivSUN

glReplacementCodeusvSUN = _triangle_list.glReplacementCodeusvSUN

glReplacementCodeubvSUN = _triangle_list.glReplacementCodeubvSUN

glReplacementCodePointerSUN = _triangle_list.glReplacementCodePointerSUN

glReplacementCodePointerubSUN = _triangle_list.glReplacementCodePointerubSUN

glReplacementCodePointerusSUN = _triangle_list.glReplacementCodePointerusSUN

glReplacementCodePointeruiSUN = _triangle_list.glReplacementCodePointeruiSUN

__info = _triangle_list.__info
GL_TRIANGLE_LIST_SUN = _triangle_list.GL_TRIANGLE_LIST_SUN
GL_REPLACEMENT_CODE_SUN = _triangle_list.GL_REPLACEMENT_CODE_SUN
GL_RESTART_SUN = _triangle_list.GL_RESTART_SUN
GL_REPLACE_MIDDLE_SUN = _triangle_list.GL_REPLACE_MIDDLE_SUN
GL_REPLACE_OLDEST_SUN = _triangle_list.GL_REPLACE_OLDEST_SUN
GL_REPLACEMENT_CODE_ARRAY_SUN = _triangle_list.GL_REPLACEMENT_CODE_ARRAY_SUN
GL_REPLACEMENT_CODE_ARRAY_TYPE_SUN = _triangle_list.GL_REPLACEMENT_CODE_ARRAY_TYPE_SUN
GL_REPLACEMENT_CODE_ARRAY_STRIDE_SUN = _triangle_list.GL_REPLACEMENT_CODE_ARRAY_STRIDE_SUN
GL_REPLACEMENT_CODE_ARRAY_POINTER_SUN = _triangle_list.GL_REPLACEMENT_CODE_ARRAY_POINTER_SUN
GL_R1UI_V3F_SUN = _triangle_list.GL_R1UI_V3F_SUN
GL_R1UI_C4UB_V3F_SUN = _triangle_list.GL_R1UI_C4UB_V3F_SUN
GL_R1UI_C3F_V3F_SUN = _triangle_list.GL_R1UI_C3F_V3F_SUN
GL_R1UI_N3F_V3F_SUN = _triangle_list.GL_R1UI_N3F_V3F_SUN
GL_R1UI_C4F_N3F_V3F_SUN = _triangle_list.GL_R1UI_C4F_N3F_V3F_SUN
GL_R1UI_T2F_V3F_SUN = _triangle_list.GL_R1UI_T2F_V3F_SUN
GL_R1UI_T2F_N3F_V3F_SUN = _triangle_list.GL_R1UI_T2F_N3F_V3F_SUN
GL_R1UI_T2F_C4F_N3F_V3F_SUN = _triangle_list.GL_R1UI_T2F_C4F_N3F_V3F_SUN

