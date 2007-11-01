/*
# BUILD sources []
# BUILD api_version_check 0
# BUILD libs ['GLUT']
# BUILD include_dirs []
*/
#include "../config.h"

#if GLUT_XLIB_IMPLEMENTATION >= 20 || FREEGLUT_VERSION_2_0
#include "_GLUT.0014.inc"
#elif GLUT_XLIB_IMPLEMENTATION >= 13 || FREEGLUT_VERSION_2_0
#include "_GLUT.000d.inc"
#elif GLUT_XLIB_IMPLEMENTATION >= 11 || FREEGLUT_VERSION_2_0
#include "_GLUT.000b.inc"
#elif GLUT_XLIB_IMPLEMENTATION >= 9 || FREEGLUT_VERSION_2_0
#include "_GLUT.0009.inc"
#elif GLUT_XLIB_IMPLEMENTATION >= 7 || FREEGLUT_VERSION_2_0
#include "_GLUT.0007.inc"
#elif GLUT_XLIB_IMPLEMENTATION >= 5 || FREEGLUT_VERSION_2_0
#include "_GLUT.0005.inc"
#elif GLUT_XLIB_IMPLEMENTATION >= 2 || FREEGLUT_VERSION_2_0
#include "_GLUT.0002.inc"
#else
#include "_GLUT.0001.inc"
#endif
