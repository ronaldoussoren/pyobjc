/********************************************************************\
 * acconfig.h -- configuration defines for gle                      *
 * Copyright (C) 2000 Linas Vepstas (linas@linas.org)               *
\********************************************************************/


#ifndef __GLE_CONFIG_H__
#define __GLE_CONFIG_H__

#if defined(_WIN32)
#undef WIN32
#define WIN32 1
#endif

/* Build for OpenGL by default, and not for old IrisGL aka GL 3.2 */
#define  OPENGL_10 1
#undef   GL_32

/* Disable debugging stuff (debugging replaces GL output with printfs) */
#undef   DEBUG_OUTPUT

/* Do we have a lenient tesselator? */
#undef  LENIENT_TESSELATOR
#define DELICATE_TESSELATOR 1

/* Enable texture mapping by default. */
#define AUTO_TEXTURE 1

/* assume a modern C compiler */
#undef FUNKY_C


#endif
