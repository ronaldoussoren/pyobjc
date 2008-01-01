/*
# BUILD sources []
# BUILD api_version_check 0
# BUILD libs ['GLUT']
# BUILD include_dirs []
*/
#include "src/config.h"

#include <stdio.h>

int main(int argc, char **argv)
{
	FILE *f = fopen("api_version", "w");
#if GLUT_XLIB_IMPLEMENTATION >= 20 || FREEGLUT_VERSION_2_0
	fprintf(f, "20");
#elif GLUT_XLIB_IMPLEMENTATION >= 13 || FREEGLUT_VERSION_2_0
	fprintf(f, "13");
#elif GLUT_XLIB_IMPLEMENTATION >= 11 || FREEGLUT_VERSION_2_0
	fprintf(f, "11");
#elif GLUT_XLIB_IMPLEMENTATION >= 9 || FREEGLUT_VERSION_2_0
	fprintf(f, "9");
#elif GLUT_XLIB_IMPLEMENTATION >= 7 || FREEGLUT_VERSION_2_0
	fprintf(f, "7");
#elif GLUT_XLIB_IMPLEMENTATION >= 5 || FREEGLUT_VERSION_2_0
	fprintf(f, "5");
#elif GLUT_XLIB_IMPLEMENTATION >= 2 || FREEGLUT_VERSION_2_0
	fprintf(f, "2");
#else
	fprintf(f, "1");
#endif
	fclose(f);
	return 0;
}
