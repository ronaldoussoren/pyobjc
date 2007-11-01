/*
# BUILD gl_platforms ['WGL']
# BUILD sources []
# BUILD api_version_check 1
# BUILD libs ['gdi32']
# BUILD include_dirs []
*/
#include "../config.h"

#if WINVER >= 0x400
#include "WGL._WGL__init__.0400.inc"
#else
#error "Do not know how to compile WGL._WGL__init__ for API version < 0x0400"
#endif
