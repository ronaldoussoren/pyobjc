/*
# BUILD api_versions [0x300]
# BUILD headers ['gle.h']
# BUILD sources ['src/gle/src/rot_prince.c',\
                 'src/gle/src/ex_cut_round.c',\
                 'src/gle/src/ex_raw.c',\
                 'src/gle/src/extrude.c',\
                 'src/gle/src/intersect.c',\
                 'src/gle/src/qmesh.c',\
                 'src/gle/src/ex_angle.c',\
                 'src/gle/src/rotate.c',\
                 'src/gle/src/round_cap.c',\
                 'src/gle/src/segment.c',\
                 'src/gle/src/texgen.c',\
                 'src/gle/src/urotate.c',\
                 'src/gle/src/view.c']
# BUILD include_dirs ['src/gle/src']
*/

%module GLE

#define __version__ "$Revision: 1.19.4.1 $"
#define __date__ "$Date: 2004/11/14 23:23:50 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "This module provides support for the GLE (Tubing and Extrusion) Library.\n\
Function prototypes are identical to that of the C binding with the small\n\
difference that passing array lengths explicity is not needed.\n\
\n\
Documentation:\n\
    GLE homepage:  http:\057\057linas.org/gle/\n\
    Man Pages:  http:\057\057pyopengl.sourceforge.net/documentation/ref/gle.html"

%{
/**
 *
 * GLE Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/

/*
 * gle.h
 *
 * FUNCTION:
 * Tubing and Extrusion header file.
 * This file provides protypes and defines for the extrusion 
 * and tubing primitives.
 *
 * HISTORY:
 * Copyright (c) Linas Vepstas 1990, 1991
 */
%}

%include util.inc

%include gl_exception_handler.inc

typedef double gleDouble;

/* ====================================================== */

/* control join style of the tubes */
int gleGetJoinStyle (void);
DOC(gleGetJoinStyle, "gleGetJoinStyle() -> style")

void gleSetJoinStyle (int style);	/* bitwise OR of flags */
DOC(gleSetJoinStyle, "gleSetJoinStyle(style) -> None")

/* control number of sides used to draw cylinders, cones */
int gleGetNumSides(void);
DOC(gleGetNumSides, "gleGetNumSides() -> sides")

void gleSetNumSides(int slices); 
DOC(gleSetNumSides, "gleSetNumSides(slices) -> None")

/* draw polyclinder, specified as a polyline */
void glePolyCylinder (int d_0_0,	/* num points in polyline */
                   const gleDouble *point_array,	/* polyline vertces */
                   const float *color_array,	/* colors at polyline verts */
                   gleDouble radius);		/* radius of polycylinder */
DOC(glePolyCylinder, "glePolyCylinder(point_array[][3], color_array[][3], radius) -> None")

/* draw polycone, specified as a polyline with radii */
void glePolyCone (int d_0_0,	 /* numpoints in poly-line */
                   const gleDouble *point_array,	/* polyline vertices */
                   const float *color_array,	/* colors at polyline verts */
                   const gleDouble *radius_array); /* cone radii at polyline verts */
DOC(glePolyCone, "glePolyCone(point_array[][3], color_array[][3], radius_array[])")

/* extrude arbitrary 2D contour along arbitrary 3D path */
void gleExtrusion (int d_0_0,         /* number of contour points */
                const gleDouble *contour,     /* 2D contour */
                const gleDouble *cont_normal, /* 2D contour normals */
                const gleDouble *up,            /* up vector for contour */
                int d_6_0,            /* numpoints in poly-line */
                const gleDouble *point_array, /* polyline vertices */
                const float *color_array); /* colors at polyline verts */
DOC(gleExtrusion, "gleExtrusion(contour[][2], cont_normal[][2], up[3], point_array[][3], color_array[][3]) -> None")

/* extrude 2D contour, specifying local rotations (twists) */
void gleTwistExtrusion (int d_0_0,         /* number of contour points */
                const gleDouble *contour,    /* 2D contour */
                const gleDouble *cont_normal, /* 2D contour normals */
                const gleDouble *up,           /* up vector for contour */
                int d_6_0,           /* numpoints in poly-line */
                const gleDouble *point_array,        /* polyline vertices */
                const float *color_array,        /* color at polyline verts */
                const gleDouble *twist_array);   /* countour twists (in degrees) */
DOC(gleTwistExtrusion, "gleTwistExtrusion(contour[][2], cont_normal[][2], up[3], point_array[][3], color_array[][3], twist_array[]) -> None")

/* extrude 2D contour, specifying local affine tranformations */
void gleSuperExtrusion (int d_0_0,  /* number of contour points */
                const gleDouble *contour,    /* 2D contour */
                const gleDouble *cont_normal, /* 2D contour normals */
                const gleDouble *up,           /* up vector for contour */
                int d_6_0,           /* numpoints in poly-line */
                const gleDouble *point_array,        /* polyline vertices */
                const float *color_array,        /* color at polyline verts */
                const gleDouble *xform_array);   /* 2D contour xforms */
DOC(gleSuperExtrusion, "gleSuperExtrusion(contour[][2], cont_normal[][2], up[3], point_array[][3], color_array[][3], xform_array[][2][3]) -> None")

/* spiral moves contour along helical path by parallel transport */
void gleSpiral (int d_0_0,        /* number of contour points */
             const gleDouble *contour,    /* 2D contour */
             const gleDouble *cont_normal, /* 2D contour normals */
             const gleDouble *up,           /* up vector for contour */
             gleDouble startRadius,	/* spiral starts in x-y plane */
             gleDouble drdTheta,        /* change in radius per revolution */
             gleDouble startZ,		/* starting z value */
             gleDouble dzdTheta,        /* change in Z per revolution */
             const gleDouble *startXform, /* starting contour affine xform */
             const gleDouble *dXformdTheta, /* tangent change xform per revoln */
             gleDouble startTheta,	/* start angle in x-y plane */
             gleDouble sweepTheta);	/* degrees to spiral around */
DOC(gleSpiral, "gleSpiral(contour[][2], cont_normal[][3], up[3], startRadius, drdTheta, startZ, dzdTheta, startXform[2][3], dXformdTheta[2][3], startTheta, sweepTheta) -> None")

/* lathe moves contour along helical path by helically shearing 3D space */
void gleLathe (int d_0_0,        /* number of contour points */
             const gleDouble *contour,    /* 2D contour */
             const gleDouble *cont_normal, /* 2D contour normals */
             const gleDouble *up,           /* up vector for contour */
             gleDouble startRadius,	/* spiral starts in x-y plane */
             gleDouble drdTheta,        /* change in radius per revolution */
             gleDouble startZ,		/* starting z value */
             gleDouble dzdTheta,        /* change in Z per revolution */
             const gleDouble *startXform, /* starting contour affine xform */
             const gleDouble *dXformdTheta, /* tangent change xform per revoln */
             gleDouble startTheta,	/* start angle in x-y plane */
             gleDouble sweepTheta);	/* degrees to spiral around */
DOC(gleLathe, "gleLathe(contour[][2], cont_normal[][2], up[3], startRadius, drdTheta, startZ, dzdTheta, startXform[2][3], dXformdTheta[2][3], startTheta, sweepTheta) -> None")

/* similar to spiral, except contour is a circle */
void gleHelicoid (gleDouble rToroid, /* circle contour (torus) radius */
             gleDouble startRadius,	/* spiral starts in x-y plane */
             gleDouble drdTheta,        /* change in radius per revolution */
             gleDouble startZ,		/* starting z value */
             gleDouble dzdTheta,        /* change in Z per revolution */
             const gleDouble *startXform, /* starting contour affine xform */
             const gleDouble *dXformdTheta, /* tangent change xform per revoln */
             gleDouble startTheta,	/* start angle in x-y plane */
             gleDouble sweepTheta);	/* degrees to spiral around */
DOC(gleHelicoid, "gleHelicoid(rToroid, startRadius, drdTheta, startZ, dzdTheta, startXform[2][3], dXformdTheta[2][3], startTheta, sweepTheta) -> None")

/* similar to lathe, except contour is a circle */
void gleToroid (gleDouble rToroid, /* circle contour (torus) radius */
             gleDouble startRadius,	/* spiral starts in x-y plane */
             gleDouble drdTheta,        /* change in radius per revolution */
             gleDouble startZ,		/* starting z value */
             gleDouble dzdTheta,        /* change in Z per revolution */
             const gleDouble *startXform, /* starting contour affine xform */
             const gleDouble *dXformdTheta, /* tangent change xform per revoln */
             gleDouble startTheta,	/* start angle in x-y plane */
             gleDouble sweepTheta);	/* degrees to spiral around */
DOC(gleToroid, "gleToroid(rToroid, startRadius, drdTheta, startZ, dzdTheta, startXform[2][3], dXformdTheta[2][3], startTheta, sweepTheta) -> None")

/* draws a screw shape */
void gleScrew (int d_0_0,          /* number of contour points */
             const gleDouble *contour,    /* 2D contour */
             const gleDouble *cont_normal, /* 2D contour normals */
             const gleDouble *up,           /* up vector for contour */
             gleDouble startz,          /* start of segment */
             gleDouble endz,            /* end of segment */
             gleDouble twist);          /* number of rotations */
DOC(gleScrew, "gleScrew(contour[][2], cont_normal[][2], up[3], startz, endz, twist) -> None")

void gleTextureMode (int mode);
DOC(gleTextureMode, "gleTextureMode(mode) -> None")


%{
PyObject *__info()
{
	return PyList_New(0);
}
%}

PyObject *__info();


/* defines for tubing join styles */
#define TUBE_JN_RAW          0x1
#define TUBE_JN_ANGLE        0x2
#define TUBE_JN_CUT          0x3
#define TUBE_JN_ROUND        0x4
#define TUBE_JN_MASK         0xf    /* mask bits */
#define TUBE_JN_CAP          0x10

/* determine how normal vectors are to be handled */
#define TUBE_NORM_FACET      0x100
#define TUBE_NORM_EDGE       0x200
#define TUBE_NORM_PATH_EDGE  0x400 /* for spiral, lathe, helix primitives */
#define TUBE_NORM_MASK       0xf00    /* mask bits */

/* closed or open countours */
#define TUBE_CONTOUR_CLOSED	0x1000

#define GLE_TEXTURE_ENABLE	0x10000
#define GLE_TEXTURE_STYLE_MASK	0xff
#define GLE_TEXTURE_VERTEX_FLAT		1
#define GLE_TEXTURE_NORMAL_FLAT		2
#define GLE_TEXTURE_VERTEX_CYL		3
#define GLE_TEXTURE_NORMAL_CYL		4
#define GLE_TEXTURE_VERTEX_SPH		5
#define GLE_TEXTURE_NORMAL_SPH		6
#define GLE_TEXTURE_VERTEX_MODEL_FLAT	7
#define GLE_TEXTURE_NORMAL_MODEL_FLAT	8
#define GLE_TEXTURE_VERTEX_MODEL_CYL	9
#define GLE_TEXTURE_NORMAL_MODEL_CYL	10
#define GLE_TEXTURE_VERTEX_MODEL_SPH	11
#define GLE_TEXTURE_NORMAL_MODEL_SPH	12


