/*
# BUILD gl_platforms ['WGL']
# BUILD sources []
# BUILD api_version_check 1
# BUILD libs ['gdi32']
# BUILD include_dirs []
*/
#include "src/config.h"

#include <stdio.h>

int main(int argc, char **argv)
{
	FILE *f = fopen("api_version", "w");
#if WINVER >= 0x400
	fprintf(f, "1024");
#else
#error "Do not know how to compile WGL.WGL__init__ for API version < 0x0400"
#endif
	fclose(f);
	return 0;
}
