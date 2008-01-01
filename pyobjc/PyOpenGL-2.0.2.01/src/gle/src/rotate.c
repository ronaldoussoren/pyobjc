/* 
 * MODULE NAME: rotate.c
 *
 * FUNCTION:
 * This module contains three different routines that compute rotation
 * matricies and load them into GL.
 * Detailed description is provided below.
 *
 * DEPENDENCIES:
 * The routines call GL matrix routines.
 *
 * HISTORY:
 * Developed & written, Linas Vepstas, Septmeber 1991
 * Double precision port, March 1993
 *
 * DETAILED DESCRIPTION:
 * This module contains three routines:
 * --------------------------------------------------------------------
 *
 * void urot_about_axis (float m[4][4],      --- returned
 *                       float angle,        --- input 
 *                       float axis[3])      --- input
 * Computes a rotation matrix.
 * The rotation is around the the direction specified by the argument
 * argument axis[3].  User may specify vector which is not of unit
 * length.  The angle of rotation is specified in degrees, and is in the
 * right-handed direction.
 *
 * void rot_about_axis (float angle,        --- input 
 *                      float axis[3])      --- input
 * Same as above routine, except that the matrix is multiplied into the
 * GL matrix stack.
 *
 * --------------------------------------------------------------------
 *
 * void urot_axis (float m[4][4],      --- returned
 *                 float omega,        --- input
 *                 float axis[3])      --- input
 * Same as urot_about_axis(), but angle specified in radians.
 * It is assumed that the argument axis[3] is a vector of unit length.
 * If it is not of unit length, the returned matrix will not be correct.
 *
 * void rot_axis (float omega,        --- input
 *                float axis[3])      --- input
 * Same as above routine, except that the matrix is multiplied into the
 * GL matrix stack.
 *
 * --------------------------------------------------------------------
 *
 * void urot_omega (float m[4][4],       --- returned
 *                  float omega[3])      --- input
 * same as urot_axis(), but the angle is taken as the length of the
 * vector omega[3]
 *
 * void rot_omega (float omega[3])      --- input
 * Same as above routine, except that the matrix is multiplied into the
 * GL matrix stack.
 *
 * --------------------------------------------------------------------
 */

#include "gle.h"
#include "port.h"
   
/* ========================================================== */

void rot_axis (gleDouble omega, 		/* input */
               gleDouble axis[3])		/* input */
{
   gleDouble m[4][4];

   urot_axis (m, omega, axis);
   MULTMATRIX (m);

}

/* ========================================================== */

void rot_about_axis (gleDouble angle, 		/* input */
                     gleDouble axis[3])		/* input */
{
   gleDouble m[4][4];

   urot_about_axis (m, angle, axis);
   MULTMATRIX (m);
}

/* ========================================================== */

void rot_omega (gleDouble axis[3])		/* input */
{
   gleDouble m[4][4];

   urot_omega (m, axis);
   MULTMATRIX(m);
}

/* ========================================================== */
