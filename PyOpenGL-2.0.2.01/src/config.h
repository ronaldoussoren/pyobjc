#include <Python.h>

#if PY_VERSION_HEX < 0x01060000
#define PySequence_Size PySequence_Length
#define PyObject_Del(obj)
#endif

#if PY_VERSION_HEX < 0x02000000
extern int PyString_AsStringAndSize(PyObject *obj, char **s, int *len);

/* Python 1.5 doesn't define these and Python 1.6 defines buggy ones */
#undef PyMem_New
#define PyMem_New(type, n) ((type *)PyMem_Malloc((n) * sizeof(type)))
#undef PyMem_Resize
#define PyMem_Resize(p, type, n) ((type *)PyMem_Realloc(((ANY*)p), (n) * sizeof(type)))
#undef PyMem_Del
#define PyMem_Del(p) PyMem_Free((ANY*)p)
#endif


#if defined(WGL_PLATFORM) /* Windows */

#include <windows.h>

/* Do extension definitions define the C prototype
   or just the enumerants? */
#define EXT_DEFINES_PROTO 0

/* A function which returns true if the current
   context is valid */
#define CurrentContextIsValid() wglGetCurrentContext()

/* Get a hash code (long) corresponding to the
   current context */
#define GetCurrentContext() ((long)wglGetCurrentContext())

/* Does the platform have a dynamic extension loading
   mechanism? */
#define HAS_DYNAMIC_EXT 1

#elif defined(AGL_PLATFORM) /* Mac OS9, OS-X and DJGPP (for some reason) */

#define APIENTRY
#define CALLBACK

#ifndef __DJGPP__ /* OS9/X */
#define EXT_DEFINES_PROTO 1
#define HAS_DYNAMIC_EXT 0
#define CurrentContextIsValid() aglGetCurrentContext()
#define GetCurrentContext() ((long)aglGetCurrentContext())
#define GL_GLEXT_PROTOTYPES 1
#else /* DOS/DJGPP */
#define EXT_DEFINES_PROTO 1
#define CurrentContextIsValid() DMesaGetCurrentContext()
#define GetCurrentContext() ((long)DMesaGetCurrentContext())
#define HAS_DYNAMIC_EXT 1
#define NUMERIC 1
#endif

#elif defined(CGL_PLATFORM) /* Mac OSX */

#import <mach-o/dyld.h>
#import <stdlib.h>
#import <string.h>

#define APIENTRY
#define CALLBACK
#define EXT_DEFINES_PROTO 1
#define HAS_DYNAMIC_EXT 1
#define CurrentContextIsValid() CGLGetCurrentContext()
#define GetCurrentContext() ((long)CGLGetCurrentContext())
#define GL_GLEXT_PROTOTYPES 1

#elif defined(GLX_PLATFORM) /* X-Windows */

#define APIENTRY
#define CALLBACK
#define EXT_DEFINES_PROTO 1
#define CurrentContextIsValid() glXGetCurrentContext()
#define GetCurrentContext() ((long)glXGetCurrentContext())
#define GL_GLEXT_PROTOTYPES 1
#include <GL/glx.h>

#ifdef GLX_ARB_get_proc_address
#define HAS_DYNAMIC_EXT 1
#else
#define HAS_DYNAMIC_EXT 0
#endif

#else

#error "I don't know how to compile for your platform!  Look at the porting notes."

#endif

#ifdef CGL_PLATFORM
#include <OpenGL/gl.h>
#include <OpenGL/glu.h>
#include <glut.h>
#else
#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>
#endif

#ifndef APIENTRY
/* GLUT undefines APIENTRY for some crazy reason */
#define APIENTRY
#endif

/* Used alot and the the lib was really written for GL 1.1 initially */
#ifndef GL_VERSION_1_1
#define GL_DOUBLE                         0x140A
#endif

#ifdef GL_VERSION_1_1
/* Mesa 2.0 and 2.1 are missing some GLenums */

#ifndef GL_FEEDBACK_BUFFER_POINTER
#define GL_FEEDBACK_BUFFER_POINTER        0x0DF0
#endif

#ifndef GL_FEEDBACK_BUFFER_SIZE
#define GL_FEEDBACK_BUFFER_SIZE           0x0DF1
#endif

#ifndef GL_FEEDBACK_BUFFER_TYPE
#define GL_FEEDBACK_BUFFER_TYPE           0x0DF2
#endif

#ifndef GL_SELECTION_BUFFER_POINTER
#define GL_SELECTION_BUFFER_POINTER       0x0DF3
#endif

#ifndef GL_SELECTION_BUFFER_SIZE
#define GL_SELECTION_BUFFER_SIZE          0x0DF4
#endif

#if defined(GL_SGIS_multitexture) && !defined(GL_MAX_TEXTURE_UNITS_SGIS)
#define GL_MAX_TEXTURE_UNITS_SGIS          0x84E2
#endif

#endif

#ifdef BAD_GLU_HEADER
#undef GLU_VERSION_1_2
#endif

#ifndef GLU_VERSION_1_2
/* Don't use typedefs in case they are already defined */
#define GLUquadric GLUquadricObj
#define GLUnurbs GLUnurbsObj
#define GLUtesselator GLUtriangulatorObj
#endif

#include <math.h>
#include <limits.h>
#include <float.h>
#include <string.h>

#ifdef NUMERIC
#include <arrayobject.h>
#endif
