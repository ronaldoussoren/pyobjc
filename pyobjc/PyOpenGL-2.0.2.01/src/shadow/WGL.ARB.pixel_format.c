/*
# BUILD gl_platforms ['WGL']
# BUILD sources []
# BUILD api_version_check 0
# BUILD libs ['gdi32']
# BUILD include_dirs []
*/
#include "src/config.h"

#include <stdio.h>

int main(int argc, char **argv)
{
	FILE *f = fopen("api_version", "w");
	fprintf(f, "256");
	fclose(f);
	return 0;
}
