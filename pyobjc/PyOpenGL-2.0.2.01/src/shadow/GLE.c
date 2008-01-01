/*
# BUILD sources ['src/gle/src/rot_prince.c', 'src/gle/src/ex_cut_round.c', 'src/gle/src/ex_raw.c', 'src/gle/src/extrude.c', 'src/gle/src/intersect.c', 'src/gle/src/qmesh.c', 'src/gle/src/ex_angle.c', 'src/gle/src/rotate.c', 'src/gle/src/round_cap.c', 'src/gle/src/segment.c', 'src/gle/src/texgen.c', 'src/gle/src/urotate.c', 'src/gle/src/view.c']
# BUILD api_version_check 0
# BUILD include_dirs ['src/gle/src']
*/
#include "src/config.h"
#include <gle.h>

#include <stdio.h>

int main(int argc, char **argv)
{
	FILE *f = fopen("api_version", "w");
	fprintf(f, "768");
	fclose(f);
	return 0;
}
