# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _register_combiners

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


__version__ = _register_combiners.__version__
__date__ = _register_combiners.__date__
__api_version__ = _register_combiners.__api_version__
__author__ = _register_combiners.__author__
__doc__ = _register_combiners.__doc__

glCombinerParameterfvNV = _register_combiners.glCombinerParameterfvNV

glCombinerParameterivNV = _register_combiners.glCombinerParameterivNV

glCombinerParameterfNV = _register_combiners.glCombinerParameterfNV

glCombinerParameteriNV = _register_combiners.glCombinerParameteriNV

glCombinerInputNV = _register_combiners.glCombinerInputNV

glCombinerOutputNV = _register_combiners.glCombinerOutputNV

glFinalCombinerInputNV = _register_combiners.glFinalCombinerInputNV

glGetCombinerInputParameterfvNV = _register_combiners.glGetCombinerInputParameterfvNV

glGetCombinerInputParameterivNV = _register_combiners.glGetCombinerInputParameterivNV

glGetCombinerOutputParameterfvNV = _register_combiners.glGetCombinerOutputParameterfvNV

glGetCombinerOutputParameterivNV = _register_combiners.glGetCombinerOutputParameterivNV

glGetFinalCombinerInputParameterfvNV = _register_combiners.glGetFinalCombinerInputParameterfvNV

glGetFinalCombinerInputParameterivNV = _register_combiners.glGetFinalCombinerInputParameterivNV

glInitRegisterCombinersNV = _register_combiners.glInitRegisterCombinersNV

__info = _register_combiners.__info
GL_ALL_COMPLETED_NV = _register_combiners.GL_ALL_COMPLETED_NV
GL_REGISTER_COMBINERS_NV = _register_combiners.GL_REGISTER_COMBINERS_NV
GL_COMBINER0_NV = _register_combiners.GL_COMBINER0_NV
GL_COMBINER1_NV = _register_combiners.GL_COMBINER1_NV
GL_COMBINER2_NV = _register_combiners.GL_COMBINER2_NV
GL_COMBINER3_NV = _register_combiners.GL_COMBINER3_NV
GL_COMBINER4_NV = _register_combiners.GL_COMBINER4_NV
GL_COMBINER5_NV = _register_combiners.GL_COMBINER5_NV
GL_COMBINER6_NV = _register_combiners.GL_COMBINER6_NV
GL_COMBINER7_NV = _register_combiners.GL_COMBINER7_NV
GL_VARIABLE_A_NV = _register_combiners.GL_VARIABLE_A_NV
GL_VARIABLE_B_NV = _register_combiners.GL_VARIABLE_B_NV
GL_VARIABLE_C_NV = _register_combiners.GL_VARIABLE_C_NV
GL_VARIABLE_D_NV = _register_combiners.GL_VARIABLE_D_NV
GL_VARIABLE_E_NV = _register_combiners.GL_VARIABLE_E_NV
GL_VARIABLE_F_NV = _register_combiners.GL_VARIABLE_F_NV
GL_VARIABLE_G_NV = _register_combiners.GL_VARIABLE_G_NV
GL_CONSTANT_COLOR0_NV = _register_combiners.GL_CONSTANT_COLOR0_NV
GL_CONSTANT_COLOR1_NV = _register_combiners.GL_CONSTANT_COLOR1_NV
GL_PRIMARY_COLOR_NV = _register_combiners.GL_PRIMARY_COLOR_NV
GL_SECONDARY_COLOR_NV = _register_combiners.GL_SECONDARY_COLOR_NV
GL_SPARE0_NV = _register_combiners.GL_SPARE0_NV
GL_SPARE1_NV = _register_combiners.GL_SPARE1_NV
GL_UNSIGNED_IDENTITY_NV = _register_combiners.GL_UNSIGNED_IDENTITY_NV
GL_UNSIGNED_INVERT_NV = _register_combiners.GL_UNSIGNED_INVERT_NV
GL_EXPAND_NORMAL_NV = _register_combiners.GL_EXPAND_NORMAL_NV
GL_EXPAND_NEGATE_NV = _register_combiners.GL_EXPAND_NEGATE_NV
GL_HALF_BIAS_NORMAL_NV = _register_combiners.GL_HALF_BIAS_NORMAL_NV
GL_HALF_BIAS_NEGATE_NV = _register_combiners.GL_HALF_BIAS_NEGATE_NV
GL_SIGNED_IDENTITY_NV = _register_combiners.GL_SIGNED_IDENTITY_NV
GL_SIGNED_NEGATE_NV = _register_combiners.GL_SIGNED_NEGATE_NV
GL_E_TIMES_F_NV = _register_combiners.GL_E_TIMES_F_NV
GL_SPARE0_PLUS_SECONDARY_COLOR_NV = _register_combiners.GL_SPARE0_PLUS_SECONDARY_COLOR_NV
GL_SCALE_BY_TWO_NV = _register_combiners.GL_SCALE_BY_TWO_NV
GL_SCALE_BY_FOUR_NV = _register_combiners.GL_SCALE_BY_FOUR_NV
GL_SCALE_BY_ONE_HALF_NV = _register_combiners.GL_SCALE_BY_ONE_HALF_NV
GL_BIAS_BY_NEGATIVE_ONE_HALF_NV = _register_combiners.GL_BIAS_BY_NEGATIVE_ONE_HALF_NV
GL_DISCARD_NV = _register_combiners.GL_DISCARD_NV
GL_COMBINER_INPUT_NV = _register_combiners.GL_COMBINER_INPUT_NV
GL_COMBINER_MAPPING_NV = _register_combiners.GL_COMBINER_MAPPING_NV
GL_COMBINER_COMPONENT_USAGE_NV = _register_combiners.GL_COMBINER_COMPONENT_USAGE_NV
GL_COMBINER_AB_DOT_PRODUCT_NV = _register_combiners.GL_COMBINER_AB_DOT_PRODUCT_NV
GL_COMBINER_CD_DOT_PRODUCT_NV = _register_combiners.GL_COMBINER_CD_DOT_PRODUCT_NV
GL_COMBINER_MUX_SUM_NV = _register_combiners.GL_COMBINER_MUX_SUM_NV
GL_COMBINER_SCALE_NV = _register_combiners.GL_COMBINER_SCALE_NV
GL_COMBINER_BIAS_NV = _register_combiners.GL_COMBINER_BIAS_NV
GL_COMBINER_AB_OUTPUT_NV = _register_combiners.GL_COMBINER_AB_OUTPUT_NV
GL_COMBINER_CD_OUTPUT_NV = _register_combiners.GL_COMBINER_CD_OUTPUT_NV
GL_COMBINER_SUM_OUTPUT_NV = _register_combiners.GL_COMBINER_SUM_OUTPUT_NV
GL_NUM_GENERAL_COMBINERS_NV = _register_combiners.GL_NUM_GENERAL_COMBINERS_NV
GL_COLOR_SUM_CLAMP_NV = _register_combiners.GL_COLOR_SUM_CLAMP_NV
GL_MAX_GENERAL_COMBINERS_NV = _register_combiners.GL_MAX_GENERAL_COMBINERS_NV

