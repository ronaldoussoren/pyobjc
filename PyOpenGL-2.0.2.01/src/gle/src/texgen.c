
/*
 * texgen.c
 *
 * FUNCTION:
 * Implement a 'graphics context' for the GLE subsystem.
 * For the most part, this is for a big texture mapping hack.
 *
 * HISTORY:
 * Created by Linas Vepstas April 1994
 * general cleanup December 1995
 */

#ifdef __APPLE_CC__
#include <sys/types.h> /* Darwin has a bug that doesn't define u_short in */
#include <sys/malloc.h> /* malloc.h, so we have to get it through stdio.h. */
#else
#include <malloc.h>
#endif
#include <math.h>

#include "gle.h"
#include "port.h"
#include "tube_gc.h"

/* ======================================================= */
/* should really make this an adaptive algorithm ... */
#define _POLYCYL_TESS   20
static void setup_circle (gleGC *gc, int nslices);

gleGC *_gle_gc = 0x0;

gleGC *
gleCreateGC (void)
{
   gleGC * retval = (gleGC *) malloc (sizeof (gleGC));

   retval -> bgn_gen_texture = 0x0;
   retval -> n3f_gen_texture = 0x0;
   retval -> n3d_gen_texture = 0x0;
   retval -> v3f_gen_texture = 0x0;
   retval -> v3d_gen_texture = 0x0;
   retval -> end_gen_texture = 0x0;

   retval -> save_bgn_gen_texture = 0x0;
   retval -> save_n3f_gen_texture = 0x0;
   retval -> save_n3d_gen_texture = 0x0;
   retval -> save_v3f_gen_texture = 0x0;
   retval -> save_v3d_gen_texture = 0x0;
   retval -> save_end_gen_texture = 0x0;

   retval -> join_style = TUBE_JN_ANGLE | TUBE_JN_CAP | TUBE_NORM_FACET;

   retval -> slices = 0;
   retval -> circle = 0x0;
   retval -> norm = 0x0;
   setup_circle (retval, _POLYCYL_TESS);

   retval -> ncp = 0;
   retval -> npoints = 0;

   retval -> num_vert = 0;
   retval -> segment_number = 0;
   retval -> segment_length = 0.0;
   retval -> accum_seg_len = 0.0;
   retval -> prev_x = 0.0;
   retval -> prev_y = 0.0;

   return retval;
}

/* ======================================================= */
/* setup_circle is used to avoid excessive mallocs and frees
 * when drawing polycylinders and polycones */

static void
setup_circle (gleGC *gc, int nslices)
{
   int i;
   double c, s;

   if (!gc) return;
   if (0 > nslices) return;
   if (nslices == gc->slices) return;

   if (nslices > gc->slices) {
      gc->circle = (gleTwoVec *) realloc (gc->circle,
                                          sizeof(gleTwoVec)*2*nslices);
      gc->norm = &(gc->circle)[nslices];
   }

   s = sin (2.0*M_PI/ ((double) nslices));
   c = cos (2.0*M_PI/ ((double) nslices));

   gc->norm [0][0] = 1.0;
   gc->norm [0][1] = 0.0;

   /* compute a perfect unit circle, using recursion relations */
   for (i=1; i<nslices; i++) {
      gc->norm [i][0] = gc->norm[i-1][0] * c - gc->norm[i-1][1] * s;
      gc->norm [i][1] = gc->norm[i-1][0] * s + gc->norm[i-1][1] * c;
   }

  gc->slices = nslices;
}

int
gleGetNumSides(void)
{
  INIT_GC();
  return (_gle_gc->slices);
}

void
gleSetNumSides(int nslices)
{
  INIT_GC();
  setup_circle (_gle_gc, nslices);
}

/* ======================================================= */

#define segment_number (_gle_gc -> segment_number)
#define segment_length (_gle_gc -> segment_length)
#define accum_seg_len (_gle_gc -> accum_seg_len)
#define num_vert  (_gle_gc -> num_vert)
#define prev_x  (_gle_gc -> prev_x)
#define prev_y  (_gle_gc -> prev_y)

/* ======================================================= */

static double save_nx = 0.0;
static double save_ny = 0.0;
static double save_nz = 0.0;

static void save_normal (double *v) {
   save_nx = v[0];
   save_ny = v[1];
   save_nz = v[2];
}

/* ======================================================= */

static void bgn_sphere_texgen (int inext, double len) {
   segment_number = inext - 1;
   segment_length = len;
   num_vert = 0;
}

/* ======================================================= */
/*
 * this routine assumes that the vertex passed in has been normalized
 * (i.e. is of unit length)
 */
static void sphere_texgen (double x, double y, double z,
                           int jcnt, int which_end)
{
   double theta, phi;

   /* let phi and theta range fro 0 to 1 */
   phi = 0.5 * atan2 (x, y) / M_PI;
   phi += 0.5;

   theta = 1.0 - acos (z) / M_PI;

   /* if first vertex, merely record the texture coords */
   if (num_vert == 0) {
      prev_x = phi;
      prev_y = theta;
      num_vert ++;
   } else {

      /* if texture coordinates changed radically, wrap them */
      if ((prev_y - theta) > 0.6) {
         theta +=1.0;
      } else if ((prev_y - theta) < -0.6) {
         theta -=1.0;
      } /* else no-op */
      prev_y = theta;


      /* if texture coordinates changed radically, wrap them */
      if ((prev_x - phi) > 0.6) {
         phi +=1.0;
      } else if ((prev_x - phi) < -0.6) {
         phi -=1.0;
      } /* else no-op */
      prev_x = phi;

   }

   T2F_D (phi, theta);
}

/* ======================================================= */
/* mappers */

static void vertex_sphere_texgen_v (double *v, int jcnt, int which_end)  {
   double x = v[0]; double y = v[1]; double z = v[2];
   double r;

   r = 1.0 / sqrt (x*x + y*y + z*z);
   x *= r;
   y *= r;
   z *= r;
   sphere_texgen (x, y, z, jcnt, which_end);
}

static void normal_sphere_texgen_v (double *v, int jcnt, int which_end)  {
   sphere_texgen (save_nx, save_ny, save_nz, jcnt, which_end);
}

static void vertex_sphere_model_v (double *v, int jcnt, int which_end) {
   double x = _gle_gc->contour[jcnt][0];
   double y = _gle_gc->contour[jcnt][1];
   double z = v[2];
   double r;

   r = 1.0 / sqrt (x*x + y*y + z*z);
   x *= r;
   y *= r;
   z *= r;
   sphere_texgen (x, y, z, jcnt, which_end);
}

static void normal_sphere_model_v (double *v, int jcnt, int which_end) {
   if (!(_gle_gc -> cont_normal)) return;
   sphere_texgen (_gle_gc->cont_normal[jcnt][0],
                _gle_gc->cont_normal[jcnt][1], 0.0, jcnt, which_end);
}

/* ======================================================= */

static void bgn_z_texgen (int inext, double len) {

   /* accumulate the previous length */
   accum_seg_len += segment_length;

   /* save current values */
   segment_number = inext - 1;
   segment_length = len;

   /* reset counter on first segment */
   if (1 >= segment_number) accum_seg_len = 0.0;

   num_vert = 0;
}

/* ======================================================= */

static void cylinder_texgen (double x, double y, double z,
                             int jcnt, int which_end)
{
   double phi;

   /* let phi and theta range fro 0 to 1 */
   phi = 0.5 * atan2 (x, y) / M_PI;
   phi += 0.5;

   /* if first vertex, merely record the texture coords */
   if (num_vert == 0) {
      prev_x = phi;
      num_vert ++;
   } else {
      /* if texture coordinates changed radically, wrap them */
      if ((prev_x - phi) > 0.6) {
         phi +=1.0;
      } else if ((prev_x - phi) < -0.6) {
         phi -=1.0;
      } /* else no-op */
      prev_x = phi;
   }

   if (FRONT == which_end) {
      T2F_D (phi, accum_seg_len);
   }
   if (BACK == which_end) {
      T2F_D (phi, accum_seg_len + segment_length);
   }
}

/* ======================================================= */
/* mappers */

static void vertex_cylinder_texgen_v (double *v, int jcnt, int which_end) {
   double x = v[0]; double y = v[1]; double z = v[2];
   double r;

   r = 1.0 / sqrt (x*x + y*y);
   x *= r;
   y *= r;
   cylinder_texgen (x, y, z, jcnt, which_end);
}

static void normal_cylinder_texgen_v (double *v, int jcnt, int which_end) {
   cylinder_texgen (save_nx, save_ny, save_nz, jcnt, which_end);
}

static void vertex_cylinder_model_v (double *v, int jcnt, int which_end) {
   double x = _gle_gc->contour[jcnt][0];
   double y = _gle_gc->contour[jcnt][1];
   double z = v[2];
   double r;

   r = 1.0 / sqrt (x*x + y*y);
   x *= r;
   y *= r;
   cylinder_texgen (x, y, z, jcnt, which_end);
}

static void normal_cylinder_model_v (double *v, int jcnt, int which_end) {
   if (!(_gle_gc -> cont_normal)) return;
   cylinder_texgen (_gle_gc->cont_normal[jcnt][0],
                _gle_gc->cont_normal[jcnt][1], 0.0, jcnt, which_end);
}

/* ======================================================= */

static void flat_texgen (double x, double y, double z,
                             int jcnt, int which_end)
{
   if (FRONT == which_end) {
      T2F_D (x, accum_seg_len);
   }
   if (BACK == which_end) {
      T2F_D (x, accum_seg_len + segment_length);
   }
}

/* ======================================================= */


static void vertex_flat_texgen_v (double *v, int jcnt, int which_end) {
   flat_texgen (v[0], v[1], v[2], jcnt, which_end);
}

static void normal_flat_texgen_v (double *v, int jcnt, int which_end) {
   flat_texgen (save_nx, save_ny, save_nz, jcnt, which_end);
}

static void vertex_flat_model_v (double *v, int jcnt, int which_end) {
   flat_texgen (_gle_gc->contour[jcnt][0],
                _gle_gc->contour[jcnt][1], v[2], jcnt, which_end);
}

static void normal_flat_model_v (double *v, int jcnt, int which_end) {
   if (!(_gle_gc -> cont_normal)) return;
   flat_texgen (_gle_gc->cont_normal[jcnt][0],
                _gle_gc->cont_normal[jcnt][1], 0.0, jcnt, which_end);
}

/* ======================================================= */

void gleTextureMode (int mode) {

   INIT_GC();

   /* enable textureing by restoring the mode */
   _gle_gc -> bgn_gen_texture = _gle_gc -> save_bgn_gen_texture;
   _gle_gc -> n3f_gen_texture = _gle_gc -> save_n3f_gen_texture;
   _gle_gc -> n3d_gen_texture = _gle_gc -> save_n3d_gen_texture;
   _gle_gc -> v3f_gen_texture = _gle_gc -> save_v3f_gen_texture;
   _gle_gc -> v3d_gen_texture = _gle_gc -> save_v3d_gen_texture;
   _gle_gc -> end_gen_texture = _gle_gc -> save_end_gen_texture;

   switch (mode&GLE_TEXTURE_STYLE_MASK) {

      case GLE_TEXTURE_VERTEX_FLAT:
         _gle_gc -> bgn_gen_texture = bgn_z_texgen;
         _gle_gc -> v3d_gen_texture = vertex_flat_texgen_v;
         _gle_gc -> n3d_gen_texture = 0x0;
         break;

      case GLE_TEXTURE_NORMAL_FLAT:
         _gle_gc -> bgn_gen_texture = bgn_z_texgen;
         _gle_gc -> v3d_gen_texture = normal_flat_texgen_v;
         _gle_gc -> n3d_gen_texture = save_normal;
         break;

      case GLE_TEXTURE_VERTEX_MODEL_FLAT:
         _gle_gc -> bgn_gen_texture = bgn_z_texgen;
         _gle_gc -> v3d_gen_texture = vertex_flat_model_v;
         _gle_gc -> n3d_gen_texture = 0x0;
         break;

      case GLE_TEXTURE_NORMAL_MODEL_FLAT:
         _gle_gc -> bgn_gen_texture = bgn_z_texgen;
         _gle_gc -> v3d_gen_texture = normal_flat_model_v;
         _gle_gc -> n3d_gen_texture = 0x0;
         break;

      case GLE_TEXTURE_VERTEX_CYL:
         _gle_gc -> bgn_gen_texture = bgn_z_texgen;
         _gle_gc -> v3d_gen_texture = vertex_cylinder_texgen_v;
         _gle_gc -> n3d_gen_texture = 0x0;
         break;

      case GLE_TEXTURE_NORMAL_CYL:
         _gle_gc -> bgn_gen_texture = bgn_z_texgen;
         _gle_gc -> v3d_gen_texture = normal_cylinder_texgen_v;
         _gle_gc -> n3d_gen_texture = save_normal;
         break;

      case GLE_TEXTURE_VERTEX_MODEL_CYL:
         _gle_gc -> bgn_gen_texture = bgn_z_texgen;
         _gle_gc -> v3d_gen_texture = vertex_cylinder_model_v;
         _gle_gc -> n3d_gen_texture = 0x0;
         break;

      case GLE_TEXTURE_NORMAL_MODEL_CYL:
         _gle_gc -> bgn_gen_texture = bgn_z_texgen;
         _gle_gc -> v3d_gen_texture = normal_cylinder_model_v;
         _gle_gc -> n3d_gen_texture = 0x0;
         break;

      case GLE_TEXTURE_VERTEX_SPH:
         _gle_gc -> bgn_gen_texture = bgn_sphere_texgen;
         _gle_gc -> v3d_gen_texture = vertex_sphere_texgen_v;
         _gle_gc -> n3d_gen_texture = 0x0;
         break;

      case GLE_TEXTURE_NORMAL_SPH:
         _gle_gc -> bgn_gen_texture = bgn_sphere_texgen;
         _gle_gc -> v3d_gen_texture = normal_sphere_texgen_v;
         _gle_gc -> n3d_gen_texture = save_normal;
         break;

      case GLE_TEXTURE_VERTEX_MODEL_SPH:
         _gle_gc -> bgn_gen_texture = bgn_sphere_texgen;
         _gle_gc -> v3d_gen_texture = vertex_sphere_model_v;
         _gle_gc -> n3d_gen_texture = 0x0;
         break;

      case GLE_TEXTURE_NORMAL_MODEL_SPH:
         _gle_gc -> bgn_gen_texture = bgn_sphere_texgen;
         _gle_gc -> v3d_gen_texture = normal_sphere_model_v;
         _gle_gc -> n3d_gen_texture = 0x0;
         break;

      default:
         break;
   }

   /* disable texturing, and save the mode */
   if (!(mode & GLE_TEXTURE_ENABLE)) {
      _gle_gc -> save_bgn_gen_texture = _gle_gc -> bgn_gen_texture;
      _gle_gc -> save_n3f_gen_texture = _gle_gc -> n3f_gen_texture;
      _gle_gc -> save_n3d_gen_texture = _gle_gc -> n3d_gen_texture;
      _gle_gc -> save_v3f_gen_texture = _gle_gc -> v3f_gen_texture;
      _gle_gc -> save_v3d_gen_texture = _gle_gc -> v3d_gen_texture;
      _gle_gc -> save_end_gen_texture = _gle_gc -> end_gen_texture;

      _gle_gc -> bgn_gen_texture = 0x0;
      _gle_gc -> n3f_gen_texture = 0x0;
      _gle_gc -> n3d_gen_texture = 0x0;
      _gle_gc -> v3f_gen_texture = 0x0;
      _gle_gc -> v3d_gen_texture = 0x0;
      _gle_gc -> end_gen_texture = 0x0;
   }
}

/* ================== END OF FILE ========================= */
