# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _fragment_shader

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


__version__ = _fragment_shader.__version__
__date__ = _fragment_shader.__date__
__api_version__ = _fragment_shader.__api_version__
__author__ = _fragment_shader.__author__
__doc__ = _fragment_shader.__doc__

glGenFragmentShadersATI = _fragment_shader.glGenFragmentShadersATI

glBindFragmentShaderATI = _fragment_shader.glBindFragmentShaderATI

glDeleteFragmentShaderATI = _fragment_shader.glDeleteFragmentShaderATI

glBeginFragmentShaderATI = _fragment_shader.glBeginFragmentShaderATI

glEndFragmentShaderATI = _fragment_shader.glEndFragmentShaderATI

glPassTexCoordATI = _fragment_shader.glPassTexCoordATI

glSampleMapATI = _fragment_shader.glSampleMapATI

glColorFragmentOp1ATI = _fragment_shader.glColorFragmentOp1ATI

glColorFragmentOp2ATI = _fragment_shader.glColorFragmentOp2ATI

glColorFragmentOp3ATI = _fragment_shader.glColorFragmentOp3ATI

glAlphaFragmentOp1ATI = _fragment_shader.glAlphaFragmentOp1ATI

glAlphaFragmentOp2ATI = _fragment_shader.glAlphaFragmentOp2ATI

glAlphaFragmentOp3ATI = _fragment_shader.glAlphaFragmentOp3ATI

glSetFragmentShaderConstantATI = _fragment_shader.glSetFragmentShaderConstantATI
GL_FRAGMENT_SHADER_ATI = _fragment_shader.GL_FRAGMENT_SHADER_ATI
GL_REG_0_ATI = _fragment_shader.GL_REG_0_ATI
GL_REG_1_ATI = _fragment_shader.GL_REG_1_ATI
GL_REG_2_ATI = _fragment_shader.GL_REG_2_ATI
GL_REG_3_ATI = _fragment_shader.GL_REG_3_ATI
GL_REG_4_ATI = _fragment_shader.GL_REG_4_ATI
GL_REG_5_ATI = _fragment_shader.GL_REG_5_ATI
GL_REG_6_ATI = _fragment_shader.GL_REG_6_ATI
GL_REG_7_ATI = _fragment_shader.GL_REG_7_ATI
GL_REG_8_ATI = _fragment_shader.GL_REG_8_ATI
GL_REG_9_ATI = _fragment_shader.GL_REG_9_ATI
GL_REG_10_ATI = _fragment_shader.GL_REG_10_ATI
GL_REG_11_ATI = _fragment_shader.GL_REG_11_ATI
GL_REG_12_ATI = _fragment_shader.GL_REG_12_ATI
GL_REG_13_ATI = _fragment_shader.GL_REG_13_ATI
GL_REG_14_ATI = _fragment_shader.GL_REG_14_ATI
GL_REG_15_ATI = _fragment_shader.GL_REG_15_ATI
GL_REG_16_ATI = _fragment_shader.GL_REG_16_ATI
GL_REG_17_ATI = _fragment_shader.GL_REG_17_ATI
GL_REG_18_ATI = _fragment_shader.GL_REG_18_ATI
GL_REG_19_ATI = _fragment_shader.GL_REG_19_ATI
GL_REG_20_ATI = _fragment_shader.GL_REG_20_ATI
GL_REG_21_ATI = _fragment_shader.GL_REG_21_ATI
GL_REG_22_ATI = _fragment_shader.GL_REG_22_ATI
GL_REG_23_ATI = _fragment_shader.GL_REG_23_ATI
GL_REG_24_ATI = _fragment_shader.GL_REG_24_ATI
GL_REG_25_ATI = _fragment_shader.GL_REG_25_ATI
GL_REG_26_ATI = _fragment_shader.GL_REG_26_ATI
GL_REG_27_ATI = _fragment_shader.GL_REG_27_ATI
GL_REG_28_ATI = _fragment_shader.GL_REG_28_ATI
GL_REG_29_ATI = _fragment_shader.GL_REG_29_ATI
GL_REG_30_ATI = _fragment_shader.GL_REG_30_ATI
GL_REG_31_ATI = _fragment_shader.GL_REG_31_ATI
GL_CON_0_ATI = _fragment_shader.GL_CON_0_ATI
GL_CON_1_ATI = _fragment_shader.GL_CON_1_ATI
GL_CON_2_ATI = _fragment_shader.GL_CON_2_ATI
GL_CON_3_ATI = _fragment_shader.GL_CON_3_ATI
GL_CON_4_ATI = _fragment_shader.GL_CON_4_ATI
GL_CON_5_ATI = _fragment_shader.GL_CON_5_ATI
GL_CON_6_ATI = _fragment_shader.GL_CON_6_ATI
GL_CON_7_ATI = _fragment_shader.GL_CON_7_ATI
GL_CON_8_ATI = _fragment_shader.GL_CON_8_ATI
GL_CON_9_ATI = _fragment_shader.GL_CON_9_ATI
GL_CON_10_ATI = _fragment_shader.GL_CON_10_ATI
GL_CON_11_ATI = _fragment_shader.GL_CON_11_ATI
GL_CON_12_ATI = _fragment_shader.GL_CON_12_ATI
GL_CON_13_ATI = _fragment_shader.GL_CON_13_ATI
GL_CON_14_ATI = _fragment_shader.GL_CON_14_ATI
GL_CON_15_ATI = _fragment_shader.GL_CON_15_ATI
GL_CON_16_ATI = _fragment_shader.GL_CON_16_ATI
GL_CON_17_ATI = _fragment_shader.GL_CON_17_ATI
GL_CON_18_ATI = _fragment_shader.GL_CON_18_ATI
GL_CON_19_ATI = _fragment_shader.GL_CON_19_ATI
GL_CON_20_ATI = _fragment_shader.GL_CON_20_ATI
GL_CON_21_ATI = _fragment_shader.GL_CON_21_ATI
GL_CON_22_ATI = _fragment_shader.GL_CON_22_ATI
GL_CON_23_ATI = _fragment_shader.GL_CON_23_ATI
GL_CON_24_ATI = _fragment_shader.GL_CON_24_ATI
GL_CON_25_ATI = _fragment_shader.GL_CON_25_ATI
GL_CON_26_ATI = _fragment_shader.GL_CON_26_ATI
GL_CON_27_ATI = _fragment_shader.GL_CON_27_ATI
GL_CON_28_ATI = _fragment_shader.GL_CON_28_ATI
GL_CON_29_ATI = _fragment_shader.GL_CON_29_ATI
GL_CON_30_ATI = _fragment_shader.GL_CON_30_ATI
GL_CON_31_ATI = _fragment_shader.GL_CON_31_ATI
GL_MOV_ATI = _fragment_shader.GL_MOV_ATI
GL_ADD_ATI = _fragment_shader.GL_ADD_ATI
GL_MUL_ATI = _fragment_shader.GL_MUL_ATI
GL_SUB_ATI = _fragment_shader.GL_SUB_ATI
GL_DOT3_ATI = _fragment_shader.GL_DOT3_ATI
GL_DOT4_ATI = _fragment_shader.GL_DOT4_ATI
GL_MAD_ATI = _fragment_shader.GL_MAD_ATI
GL_LERP_ATI = _fragment_shader.GL_LERP_ATI
GL_CND_ATI = _fragment_shader.GL_CND_ATI
GL_CND0_ATI = _fragment_shader.GL_CND0_ATI
GL_DOT2_ADD_ATI = _fragment_shader.GL_DOT2_ADD_ATI
GL_SECONDARY_INTERPOLATOR_ATI = _fragment_shader.GL_SECONDARY_INTERPOLATOR_ATI
GL_NUM_FRAGMENT_REGISTERS_ATI = _fragment_shader.GL_NUM_FRAGMENT_REGISTERS_ATI
GL_NUM_FRAGMENT_CONSTANTS_ATI = _fragment_shader.GL_NUM_FRAGMENT_CONSTANTS_ATI
GL_NUM_PASSES_ATI = _fragment_shader.GL_NUM_PASSES_ATI
GL_NUM_INSTRUCTIONS_PER_PASS_ATI = _fragment_shader.GL_NUM_INSTRUCTIONS_PER_PASS_ATI
GL_NUM_INSTRUCTIONS_TOTAL_ATI = _fragment_shader.GL_NUM_INSTRUCTIONS_TOTAL_ATI
GL_NUM_INPUT_INTERPOLATOR_COMPONENTS_ATI = _fragment_shader.GL_NUM_INPUT_INTERPOLATOR_COMPONENTS_ATI
GL_NUM_LOOPBACK_COMPONENTS_ATI = _fragment_shader.GL_NUM_LOOPBACK_COMPONENTS_ATI
GL_COLOR_ALPHA_PAIRING_ATI = _fragment_shader.GL_COLOR_ALPHA_PAIRING_ATI
GL_SWIZZLE_STR_ATI = _fragment_shader.GL_SWIZZLE_STR_ATI
GL_SWIZZLE_STQ_ATI = _fragment_shader.GL_SWIZZLE_STQ_ATI
GL_SWIZZLE_STR_DR_ATI = _fragment_shader.GL_SWIZZLE_STR_DR_ATI
GL_SWIZZLE_STQ_DQ_ATI = _fragment_shader.GL_SWIZZLE_STQ_DQ_ATI
GL_SWIZZLE_STRQ_ATI = _fragment_shader.GL_SWIZZLE_STRQ_ATI
GL_SWIZZLE_STRQ_DQ_ATI = _fragment_shader.GL_SWIZZLE_STRQ_DQ_ATI
GL_RED_BIT_ATI = _fragment_shader.GL_RED_BIT_ATI
GL_GREEN_BIT_ATI = _fragment_shader.GL_GREEN_BIT_ATI
GL_BLUE_BIT_ATI = _fragment_shader.GL_BLUE_BIT_ATI
GL_2X_BIT_ATI = _fragment_shader.GL_2X_BIT_ATI
GL_4X_BIT_ATI = _fragment_shader.GL_4X_BIT_ATI
GL_8X_BIT_ATI = _fragment_shader.GL_8X_BIT_ATI
GL_HALF_BIT_ATI = _fragment_shader.GL_HALF_BIT_ATI
GL_QUARTER_BIT_ATI = _fragment_shader.GL_QUARTER_BIT_ATI
GL_EIGHTH_BIT_ATI = _fragment_shader.GL_EIGHTH_BIT_ATI
GL_SATURATE_BIT_ATI = _fragment_shader.GL_SATURATE_BIT_ATI
GL_COMP_BIT_ATI = _fragment_shader.GL_COMP_BIT_ATI
GL_NEGATE_BIT_ATI = _fragment_shader.GL_NEGATE_BIT_ATI
GL_BIAS_BIT_ATI = _fragment_shader.GL_BIAS_BIT_ATI

glInitFragmentShaderATI = _fragment_shader.glInitFragmentShaderATI

__info = _fragment_shader.__info

