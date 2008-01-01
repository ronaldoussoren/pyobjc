/*
# BUILD sources []
# BUILD api_version_check 0
# BUILD include_dirs []
*/
#include "../config.h"

#if defined(GL_VERSION_1_1)
#include "GL._GL__init__.0101.inc"
#else
#include "GL._GL__init__.0100.inc"
#endif
