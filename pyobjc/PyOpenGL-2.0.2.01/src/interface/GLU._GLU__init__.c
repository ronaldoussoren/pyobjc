/*
# BUILD sources []
# BUILD api_version_check 0
# BUILD include_dirs []
*/
#include "../config.h"

#if defined(GLU_VERSION_1_3)
#include "GLU._GLU__init__.0103.inc"
#elif defined(GLU_VERSION_1_2)
#include "GLU._GLU__init__.0102.inc"
#elif defined(GLU_VERSION_1_1)
#include "GLU._GLU__init__.0101.inc"
#else
#include "GLU._GLU__init__.0100.inc"
#endif
