/*
# BUILD sources []
# BUILD api_version_check 0
# BUILD include_dirs []
*/
#include "src/config.h"

#include <stdio.h>

int main(int argc, char **argv)
{
	FILE *f = fopen("api_version", "w");
	fprintf(f, "283");
	fclose(f);
	return 0;
}
