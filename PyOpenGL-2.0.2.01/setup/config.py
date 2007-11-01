import distutils.command.config
from distutils.errors import *
from distutils.sysconfig import customize_compiler
from distutils.ccompiler import CompileError
from util import *


glu_body = '''
#ifdef _WIN32
#include <windows.h>
#endif
#ifdef __APPLE_CC__
#include <OpenGL/gl.h>
#include <OpenGL/glu.h>
#else
#include <GL/gl.h>
#include <GL/glu.h>
#endif
#ifdef GLU_VERSION_1_2
GLUnurbs *x;
GLUtesselator *y;
GLUquadric *z;
#endif
'''

texture_object_body = '''
#ifdef _WIN32
#include <windows.h>
#endif
#ifdef __APPLE_CC__
#include <OpenGL/gl.h>
#else
#include <GL/gl.h>
#endif
#ifndef GL_EXT_texture_object
void glAreTexturesResidentEXT (GLsizei n, const GLuint *textures, GLboolean *residences)
{
}
#endif
'''

class config(distutils.command.config.config):

	def run(self):
		self.output_dir = "" # Try by Jack
		self._check_compiler()
		customize_compiler(self.compiler)

		if not self.try_compile(glu_body):
			self.distribution.define_macros.append(('BAD_GLU_HEADER', None))

		if not self.try_compile(texture_object_body):
			self.distribution.define_macros.append(('GL_EXT_texture_object', 1))


	def try_compile (self, body, headers=None, include_dirs=None, lang="c"):
		"""Try to compile a source file built from 'body' and 'headers'.
		Return true on success, false otherwise.
		"""
		
		try:
			self._compile(body, headers, include_dirs, lang)
			ok = 1
		except CompileError:
			ok = 0
		
		return ok
