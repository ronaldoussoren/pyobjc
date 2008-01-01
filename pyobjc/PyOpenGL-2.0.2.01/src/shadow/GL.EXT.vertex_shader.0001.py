# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _vertex_shader

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


__version__ = _vertex_shader.__version__
__date__ = _vertex_shader.__date__
__api_version__ = _vertex_shader.__api_version__
__author__ = _vertex_shader.__author__
__doc__ = _vertex_shader.__doc__

glBeginVertexShaderEXT = _vertex_shader.glBeginVertexShaderEXT

glEndVertexShaderEXT = _vertex_shader.glEndVertexShaderEXT

glBindVertexShaderEXT = _vertex_shader.glBindVertexShaderEXT

glGenVertexShadersEXT = _vertex_shader.glGenVertexShadersEXT

glDeleteVertexShaderEXT = _vertex_shader.glDeleteVertexShaderEXT

glShaderOp1EXT = _vertex_shader.glShaderOp1EXT

glShaderOp2EXT = _vertex_shader.glShaderOp2EXT

glShaderOp3EXT = _vertex_shader.glShaderOp3EXT

glSwizzleEXT = _vertex_shader.glSwizzleEXT

glWriteMaskEXT = _vertex_shader.glWriteMaskEXT

glInsertComponentEXT = _vertex_shader.glInsertComponentEXT

glExtractComponentEXT = _vertex_shader.glExtractComponentEXT

glGenSymbolsEXT = _vertex_shader.glGenSymbolsEXT

glSetInvariantEXT = _vertex_shader.glSetInvariantEXT

glSetLocalConstantEXT = _vertex_shader.glSetLocalConstantEXT

glVariantbvEXT = _vertex_shader.glVariantbvEXT

glVariantsvEXT = _vertex_shader.glVariantsvEXT

glVariantivEXT = _vertex_shader.glVariantivEXT

glVariantfvEXT = _vertex_shader.glVariantfvEXT

glVariantdvEXT = _vertex_shader.glVariantdvEXT

glVariantubvEXT = _vertex_shader.glVariantubvEXT

glVariantusvEXT = _vertex_shader.glVariantusvEXT

glVariantuivEXT = _vertex_shader.glVariantuivEXT

glVariantPointerEXT = _vertex_shader.glVariantPointerEXT

glEnableVariantClientStateEXT = _vertex_shader.glEnableVariantClientStateEXT

glDisableVariantClientStateEXT = _vertex_shader.glDisableVariantClientStateEXT

glBindLightParameterEXT = _vertex_shader.glBindLightParameterEXT

glBindMaterialParameterEXT = _vertex_shader.glBindMaterialParameterEXT

glBindTexGenParameterEXT = _vertex_shader.glBindTexGenParameterEXT

glBindTextureUnitParameterEXT = _vertex_shader.glBindTextureUnitParameterEXT

glBindParameterEXT = _vertex_shader.glBindParameterEXT

glIsVariantEnabledEXT = _vertex_shader.glIsVariantEnabledEXT

glGetVariantBooleanvEXT = _vertex_shader.glGetVariantBooleanvEXT

glGetVariantIntegervEXT = _vertex_shader.glGetVariantIntegervEXT

glGetVariantFloatvEXT = _vertex_shader.glGetVariantFloatvEXT

glGetVariantPointervEXT = _vertex_shader.glGetVariantPointervEXT

glGetInvariantBooleanvEXT = _vertex_shader.glGetInvariantBooleanvEXT

glGetInvariantIntegervEXT = _vertex_shader.glGetInvariantIntegervEXT

glGetInvariantFloatvEXT = _vertex_shader.glGetInvariantFloatvEXT

glGetLocalConstantBooleanvEXT = _vertex_shader.glGetLocalConstantBooleanvEXT

glGetLocalConstantIntegervEXT = _vertex_shader.glGetLocalConstantIntegervEXT

glGetLocalConstantFloatvEXT = _vertex_shader.glGetLocalConstantFloatvEXT
GL_VERTEX_SHADER_EXT = _vertex_shader.GL_VERTEX_SHADER_EXT
GL_VERTEX_SHADER_BINDING_EXT = _vertex_shader.GL_VERTEX_SHADER_BINDING_EXT
GL_OP_INDEX_EXT = _vertex_shader.GL_OP_INDEX_EXT
GL_OP_NEGATE_EXT = _vertex_shader.GL_OP_NEGATE_EXT
GL_OP_DOT3_EXT = _vertex_shader.GL_OP_DOT3_EXT
GL_OP_DOT4_EXT = _vertex_shader.GL_OP_DOT4_EXT
GL_OP_MUL_EXT = _vertex_shader.GL_OP_MUL_EXT
GL_OP_ADD_EXT = _vertex_shader.GL_OP_ADD_EXT
GL_OP_MADD_EXT = _vertex_shader.GL_OP_MADD_EXT
GL_OP_FRAC_EXT = _vertex_shader.GL_OP_FRAC_EXT
GL_OP_MAX_EXT = _vertex_shader.GL_OP_MAX_EXT
GL_OP_MIN_EXT = _vertex_shader.GL_OP_MIN_EXT
GL_OP_SET_GE_EXT = _vertex_shader.GL_OP_SET_GE_EXT
GL_OP_SET_LT_EXT = _vertex_shader.GL_OP_SET_LT_EXT
GL_OP_CLAMP_EXT = _vertex_shader.GL_OP_CLAMP_EXT
GL_OP_FLOOR_EXT = _vertex_shader.GL_OP_FLOOR_EXT
GL_OP_ROUND_EXT = _vertex_shader.GL_OP_ROUND_EXT
GL_OP_EXP_BASE_2_EXT = _vertex_shader.GL_OP_EXP_BASE_2_EXT
GL_OP_LOG_BASE_2_EXT = _vertex_shader.GL_OP_LOG_BASE_2_EXT
GL_OP_POWER_EXT = _vertex_shader.GL_OP_POWER_EXT
GL_OP_RECIP_EXT = _vertex_shader.GL_OP_RECIP_EXT
GL_OP_RECIP_SQRT_EXT = _vertex_shader.GL_OP_RECIP_SQRT_EXT
GL_OP_SUB_EXT = _vertex_shader.GL_OP_SUB_EXT
GL_OP_CROSS_PRODUCT_EXT = _vertex_shader.GL_OP_CROSS_PRODUCT_EXT
GL_OP_MULTIPLY_MATRIX_EXT = _vertex_shader.GL_OP_MULTIPLY_MATRIX_EXT
GL_OP_MOV_EXT = _vertex_shader.GL_OP_MOV_EXT
GL_OUTPUT_VERTEX_EXT = _vertex_shader.GL_OUTPUT_VERTEX_EXT
GL_OUTPUT_COLOR0_EXT = _vertex_shader.GL_OUTPUT_COLOR0_EXT
GL_OUTPUT_COLOR1_EXT = _vertex_shader.GL_OUTPUT_COLOR1_EXT
GL_OUTPUT_TEXTURE_COORD0_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD0_EXT
GL_OUTPUT_TEXTURE_COORD1_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD1_EXT
GL_OUTPUT_TEXTURE_COORD2_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD2_EXT
GL_OUTPUT_TEXTURE_COORD3_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD3_EXT
GL_OUTPUT_TEXTURE_COORD4_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD4_EXT
GL_OUTPUT_TEXTURE_COORD5_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD5_EXT
GL_OUTPUT_TEXTURE_COORD6_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD6_EXT
GL_OUTPUT_TEXTURE_COORD7_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD7_EXT
GL_OUTPUT_TEXTURE_COORD8_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD8_EXT
GL_OUTPUT_TEXTURE_COORD9_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD9_EXT
GL_OUTPUT_TEXTURE_COORD10_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD10_EXT
GL_OUTPUT_TEXTURE_COORD11_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD11_EXT
GL_OUTPUT_TEXTURE_COORD12_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD12_EXT
GL_OUTPUT_TEXTURE_COORD13_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD13_EXT
GL_OUTPUT_TEXTURE_COORD14_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD14_EXT
GL_OUTPUT_TEXTURE_COORD15_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD15_EXT
GL_OUTPUT_TEXTURE_COORD16_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD16_EXT
GL_OUTPUT_TEXTURE_COORD17_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD17_EXT
GL_OUTPUT_TEXTURE_COORD18_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD18_EXT
GL_OUTPUT_TEXTURE_COORD19_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD19_EXT
GL_OUTPUT_TEXTURE_COORD20_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD20_EXT
GL_OUTPUT_TEXTURE_COORD21_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD21_EXT
GL_OUTPUT_TEXTURE_COORD22_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD22_EXT
GL_OUTPUT_TEXTURE_COORD23_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD23_EXT
GL_OUTPUT_TEXTURE_COORD24_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD24_EXT
GL_OUTPUT_TEXTURE_COORD25_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD25_EXT
GL_OUTPUT_TEXTURE_COORD26_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD26_EXT
GL_OUTPUT_TEXTURE_COORD27_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD27_EXT
GL_OUTPUT_TEXTURE_COORD28_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD28_EXT
GL_OUTPUT_TEXTURE_COORD29_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD29_EXT
GL_OUTPUT_TEXTURE_COORD30_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD30_EXT
GL_OUTPUT_TEXTURE_COORD31_EXT = _vertex_shader.GL_OUTPUT_TEXTURE_COORD31_EXT
GL_OUTPUT_FOG_EXT = _vertex_shader.GL_OUTPUT_FOG_EXT
GL_SCALAR_EXT = _vertex_shader.GL_SCALAR_EXT
GL_VECTOR_EXT = _vertex_shader.GL_VECTOR_EXT
GL_MATRIX_EXT = _vertex_shader.GL_MATRIX_EXT
GL_VARIANT_EXT = _vertex_shader.GL_VARIANT_EXT
GL_INVARIANT_EXT = _vertex_shader.GL_INVARIANT_EXT
GL_LOCAL_CONSTANT_EXT = _vertex_shader.GL_LOCAL_CONSTANT_EXT
GL_LOCAL_EXT = _vertex_shader.GL_LOCAL_EXT
GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT = _vertex_shader.GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT
GL_MAX_VERTEX_SHADER_VARIANTS_EXT = _vertex_shader.GL_MAX_VERTEX_SHADER_VARIANTS_EXT
GL_MAX_VERTEX_SHADER_INVARIANTS_EXT = _vertex_shader.GL_MAX_VERTEX_SHADER_INVARIANTS_EXT
GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = _vertex_shader.GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT
GL_MAX_VERTEX_SHADER_LOCALS_EXT = _vertex_shader.GL_MAX_VERTEX_SHADER_LOCALS_EXT
GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT = _vertex_shader.GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT
GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT = _vertex_shader.GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = _vertex_shader.GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT
GL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT = _vertex_shader.GL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT = _vertex_shader.GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT
GL_VERTEX_SHADER_INSTRUCTIONS_EXT = _vertex_shader.GL_VERTEX_SHADER_INSTRUCTIONS_EXT
GL_VERTEX_SHADER_VARIANTS_EXT = _vertex_shader.GL_VERTEX_SHADER_VARIANTS_EXT
GL_VERTEX_SHADER_INVARIANTS_EXT = _vertex_shader.GL_VERTEX_SHADER_INVARIANTS_EXT
GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = _vertex_shader.GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT
GL_VERTEX_SHADER_LOCALS_EXT = _vertex_shader.GL_VERTEX_SHADER_LOCALS_EXT
GL_VERTEX_SHADER_OPTIMIZED_EXT = _vertex_shader.GL_VERTEX_SHADER_OPTIMIZED_EXT
GL_X_EXT = _vertex_shader.GL_X_EXT
GL_Y_EXT = _vertex_shader.GL_Y_EXT
GL_Z_EXT = _vertex_shader.GL_Z_EXT
GL_W_EXT = _vertex_shader.GL_W_EXT
GL_NEGATIVE_X_EXT = _vertex_shader.GL_NEGATIVE_X_EXT
GL_NEGATIVE_Y_EXT = _vertex_shader.GL_NEGATIVE_Y_EXT
GL_NEGATIVE_Z_EXT = _vertex_shader.GL_NEGATIVE_Z_EXT
GL_NEGATIVE_W_EXT = _vertex_shader.GL_NEGATIVE_W_EXT
GL_ZERO_EXT = _vertex_shader.GL_ZERO_EXT
GL_ONE_EXT = _vertex_shader.GL_ONE_EXT
GL_NEGATIVE_ONE_EXT = _vertex_shader.GL_NEGATIVE_ONE_EXT
GL_NORMALIZED_RANGE_EXT = _vertex_shader.GL_NORMALIZED_RANGE_EXT
GL_FULL_RANGE_EXT = _vertex_shader.GL_FULL_RANGE_EXT
GL_CURRENT_VERTEX_EXT = _vertex_shader.GL_CURRENT_VERTEX_EXT
GL_MVP_MATRIX_EXT = _vertex_shader.GL_MVP_MATRIX_EXT
GL_VARIANT_VALUE_EXT = _vertex_shader.GL_VARIANT_VALUE_EXT
GL_VARIANT_DATATYPE_EXT = _vertex_shader.GL_VARIANT_DATATYPE_EXT
GL_VARIANT_ARRAY_STRIDE_EXT = _vertex_shader.GL_VARIANT_ARRAY_STRIDE_EXT
GL_VARIANT_ARRAY_TYPE_EXT = _vertex_shader.GL_VARIANT_ARRAY_TYPE_EXT
GL_VARIANT_ARRAY_EXT = _vertex_shader.GL_VARIANT_ARRAY_EXT
GL_VARIANT_ARRAY_POINTER_EXT = _vertex_shader.GL_VARIANT_ARRAY_POINTER_EXT
GL_INVARIANT_VALUE_EXT = _vertex_shader.GL_INVARIANT_VALUE_EXT
GL_INVARIANT_DATATYPE_EXT = _vertex_shader.GL_INVARIANT_DATATYPE_EXT
GL_LOCAL_CONSTANT_VALUE_EXT = _vertex_shader.GL_LOCAL_CONSTANT_VALUE_EXT
GL_LOCAL_CONSTANT_DATATYPE_EXT = _vertex_shader.GL_LOCAL_CONSTANT_DATATYPE_EXT

glInitVertexShaderEXT = _vertex_shader.glInitVertexShaderEXT

__info = _vertex_shader.__info

