import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/NV/texture_shader2.txt'
__api_version__ = 0x100


GL_DOT_PRODUCT_TEXTURE_3D_NV =                 0x86EF

GL_HILO_NV =                                   0x86F4
GL_DSDT_NV =                                   0x86F5
GL_DSDT_MAG_NV =                               0x86F6
GL_DSDT_MAG_VIB_NV =                           0x86F7

GL_UNSIGNED_INT_S8_S8_8_8_NV =                 0x86DA 
GL_UNSIGNED_INT_8_8_S8_S8_REV_NV =             0x86DB 

GL_SIGNED_RGBA_NV =                            0x86FB
GL_SIGNED_RGBA8_NV =                           0x86FC
GL_SIGNED_RGB_NV =                             0x86FE
GL_SIGNED_RGB8_NV =                            0x86FF
GL_SIGNED_LUMINANCE_NV =                       0x8701
GL_SIGNED_LUMINANCE8_NV =                      0x8702
GL_SIGNED_LUMINANCE_ALPHA_NV =                 0x8703
GL_SIGNED_LUMINANCE8_ALPHA8_NV =               0x8704
GL_SIGNED_ALPHA_NV =                           0x8705
GL_SIGNED_ALPHA8_NV =                          0x8706
GL_SIGNED_INTENSITY_NV =                       0x8707
GL_SIGNED_INTENSITY8_NV =                      0x8708
GL_SIGNED_RGB_UNSIGNED_ALPHA_NV =              0x870C
GL_SIGNED_RGB8_UNSIGNED_ALPHA8_NV =            0x870D

GL_HILO16_NV =                                 0x86F8
GL_SIGNED_HILO_NV =                            0x86F9
GL_SIGNED_HILO16_NV =                          0x86FA
GL_DSDT8_NV =                                  0x8709
GL_DSDT8_MAG8_NV =                             0x870A
GL_DSDT_MAG_INTENSITY_NV =                     0x86DC
GL_DSDT8_MAG8_INTENSITY8_NV =                  0x870B


def glInitTextureShader2NV():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_NV_texture_shader2")

glInitTexShader2NV = glInitTextureShader2NV

def __info():
	if glInitTextureShader2NV():
		return []
