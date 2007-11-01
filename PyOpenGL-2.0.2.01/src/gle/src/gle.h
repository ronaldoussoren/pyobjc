
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


#ifndef __GLE_H__
#define __GLE_H__

#if defined(__cplusplus) || defined(c_plusplus)
extern "C" {
#endif

/* some types */
#define __GLE_DOUBLE  1
#if __GLE_DOUBLE
typedef double gleDouble;
#else 
typedef float gleDouble;
#endif
typedef gleDouble gleAffine[2][3];

/* ====================================================== */

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

#ifdef GL_32
/* HACK for GL 3.2 -- needed because no way to tell if lighting is on.  */
#define TUBE_LIGHTING_ON	0x80000000

#define gleExtrusion		extrusion
#define gleSetJoinStyle		setjoinstyle
#define gleGetJoinStyle		getjoinstyle
#define glePolyCone		polycone
#define glePolyCylinder		polycylinder
#define	gleSuperExtrusion	super_extrusion
#define	gleTwistExtrusion	twist_extrusion
#define	gleSpiral		spiral
#define	gleLathe		lathe
#define	gleHelicoid		helicoid
#define	gleToroid		toroid
#define	gleScrew		screw

#endif /* GL_32 */

#ifdef _NO_PROTO		/* NO ANSI C PROTOTYPING */

extern int gleGetJoinStyle ();
extern void gleSetJoinStyle ();
extern void glePolyCone ();
extern void glePolyCylinder ();
extern void gleExtrusion ();
extern void gleSuperExtrusion ();
extern void gleTwistExtrusion ();
extern void gleSpiral ();
extern void gleLathe ();
extern void gleHelicoid ();
extern void gleToroid ();
extern void gleScrew ();

/* Rotation Utilities */
extern void rot_axis ();
extern void rot_about_axis ();
extern void rot_omega ();
extern void urot_axis ();
extern void urot_about_axis ();
extern void urot_omega ();

/* viewpoint functions */
extern void uview_direction ();
extern void uviewpoint ();

#else /* _NO_PROTO */		/* ANSI C PROTOTYPING */

/* control join style of the tubes */
extern int gleGetJoinStyle (void);
extern void gleSetJoinStyle (int style);	/* bitwise OR of flags */

/* control number of sides used to draw cylinders, cones */
extern int gleGetNumSides(void);
extern void gleSetNumSides(int slices); 

/* draw polyclinder, specified as a polyline */
extern void glePolyCylinder (int npoints,	/* num points in polyline */
                   gleDouble point_array[][3],	/* polyline vertces */
                   float color_array[][3],	/* colors at polyline verts */
                   gleDouble radius);		/* radius of polycylinder */

/* draw polycone, specified as a polyline with radii */
extern void glePolyCone (int npoints,	 /* numpoints in poly-line */
                   gleDouble point_array[][3],	/* polyline vertices */
                   float color_array[][3],	/* colors at polyline verts */
                   gleDouble radius_array[]); /* cone radii at polyline verts */

/* extrude arbitrary 2D contour along arbitrary 3D path */
extern void gleExtrusion (int ncp,         /* number of contour points */
                gleDouble contour[][2],     /* 2D contour */
                gleDouble cont_normal[][2], /* 2D contour normals */
                gleDouble up[3],            /* up vector for contour */
                int npoints,            /* numpoints in poly-line */
                gleDouble point_array[][3], /* polyline vertices */
                float color_array[][3]); /* colors at polyline verts */

/* extrude 2D contour, specifying local rotations (twists) */
extern void gleTwistExtrusion (int ncp,         /* number of contour points */
                gleDouble contour[][2],    /* 2D contour */
                gleDouble cont_normal[][2], /* 2D contour normals */
                gleDouble up[3],           /* up vector for contour */
                int npoints,           /* numpoints in poly-line */
                gleDouble point_array[][3],        /* polyline vertices */
                float color_array[][3],        /* color at polyline verts */
                gleDouble twist_array[]);   /* countour twists (in degrees) */

/* extrude 2D contour, specifying local affine tranformations */
extern void gleSuperExtrusion (int ncp,  /* number of contour points */
                gleDouble contour[][2],    /* 2D contour */
                gleDouble cont_normal[][2], /* 2D contour normals */
                gleDouble up[3],           /* up vector for contour */
                int npoints,           /* numpoints in poly-line */
                gleDouble point_array[][3],        /* polyline vertices */
                float color_array[][3],        /* color at polyline verts */
                gleDouble xform_array[][2][3]);   /* 2D contour xforms */

/* spiral moves contour along helical path by parallel transport */
extern void gleSpiral (int ncp,        /* number of contour points */
             gleDouble contour[][2],    /* 2D contour */
             gleDouble cont_normal[][2], /* 2D contour normals */
             gleDouble up[3],           /* up vector for contour */
             gleDouble startRadius,	/* spiral starts in x-y plane */
             gleDouble drdTheta,        /* change in radius per revolution */
             gleDouble startZ,		/* starting z value */
             gleDouble dzdTheta,        /* change in Z per revolution */
             gleDouble startXform[2][3], /* starting contour affine xform */
             gleDouble dXformdTheta[2][3], /* tangent change xform per revoln */
             gleDouble startTheta,	/* start angle in x-y plane */
             gleDouble sweepTheta);	/* degrees to spiral around */

/* lathe moves contour along helical path by helically shearing 3D space */
extern void gleLathe (int ncp,        /* number of contour points */
             gleDouble contour[][2],    /* 2D contour */
             gleDouble cont_normal[][2], /* 2D contour normals */
             gleDouble up[3],           /* up vector for contour */
             gleDouble startRadius,	/* spiral starts in x-y plane */
             gleDouble drdTheta,        /* change in radius per revolution */
             gleDouble startZ,		/* starting z value */
             gleDouble dzdTheta,        /* change in Z per revolution */
             gleDouble startXform[2][3], /* starting contour affine xform */
             gleDouble dXformdTheta[2][3], /* tangent change xform per revoln */
             gleDouble startTheta,	/* start angle in x-y plane */
             gleDouble sweepTheta);	/* degrees to spiral around */

/* similar to spiral, except contour is a circle */
extern void gleHelicoid (gleDouble rToroid, /* circle contour (torus) radius */
             gleDouble startRadius,	/* spiral starts in x-y plane */
             gleDouble drdTheta,        /* change in radius per revolution */
             gleDouble startZ,		/* starting z value */
             gleDouble dzdTheta,        /* change in Z per revolution */
             gleDouble startXform[2][3], /* starting contour affine xform */
             gleDouble dXformdTheta[2][3], /* tangent change xform per revoln */
             gleDouble startTheta,	/* start angle in x-y plane */
             gleDouble sweepTheta);	/* degrees to spiral around */

/* similar to lathe, except contour is a circle */
extern void gleToroid (gleDouble rToroid, /* circle contour (torus) radius */
             gleDouble startRadius,	/* spiral starts in x-y plane */
             gleDouble drdTheta,        /* change in radius per revolution */
             gleDouble startZ,		/* starting z value */
             gleDouble dzdTheta,        /* change in Z per revolution */
             gleDouble startXform[2][3], /* starting contour affine xform */
             gleDouble dXformdTheta[2][3], /* tangent change xform per revoln */
             gleDouble startTheta,	/* start angle in x-y plane */
             gleDouble sweepTheta);	/* degrees to spiral around */

/* draws a screw shape */
extern void gleScrew (int ncp,          /* number of contour points */
             gleDouble contour[][2],    /* 2D contour */
             gleDouble cont_normal[][2], /* 2D contour normals */
             gleDouble up[3],           /* up vector for contour */
             gleDouble startz,          /* start of segment */
             gleDouble endz,            /* end of segment */
             gleDouble twist);          /* number of rotations */

extern void gleTextureMode (int mode);

/* Rotation Utilities */
extern void rot_axis (gleDouble omega, gleDouble axis[3]);
extern void rot_about_axis (gleDouble angle, gleDouble axis[3]);
extern void rot_omega (gleDouble axis[3]);
extern void rot_prince (gleDouble omega, char axis);
extern void urot_axis (gleDouble m[4][4], gleDouble omega, gleDouble axis[3]);
extern void urot_about_axis (gleDouble m[4][4], gleDouble angle, gleDouble axis[3]);
extern void urot_omega (gleDouble m[4][4], gleDouble axis[3]);
extern void urot_prince (gleDouble m[4][4], gleDouble omega, char axis);

/* viewpoint functions */
extern void uview_direction (gleDouble m[4][4],	/* returned */
                        gleDouble v21[3],	/* input */
                        gleDouble up[3]);	/* input */

extern void uviewpoint (gleDouble m[4][4],	/* returned */
                   gleDouble v1[3],		/* input */
                   gleDouble v2[3],		/* input */
                   gleDouble up[3]);		/* input */

#endif /* _NO_PROTO */

#if defined(__cplusplus) || defined(c_plusplus)
};
#endif

#endif /* __GLE_H__ */
/* ================== END OF FILE ======================= */
