/* $Id: texture.c,v 1.1 2003/02/14 20:18:20 mcfletch Exp $ */

/*
 * Togl - a Tk OpenGL widget
 * Copyright (C) 1996-1997  Brian Paul and Ben Bederson
 * See the LICENSE file for copyright details.
 */


/*
 * $Log: texture.c,v $
 * Revision 1.1  2003/02/14 20:18:20  mcfletch
 * Switch to TOGL 1.6 (from CVS) which should support Tk 8.4 (and earlier versions as well)
 *
 * Revision 1.6  2001/12/20 13:59:31  beskow
 * Improved error-handling in togl.c in case of window creation failure
 * Added pkgIndex target to makefile
 * Updated documentation to reflect stubs-interface (Togl.html + new README.stubs)
 * Added tk8.4a3 headers
 * Removed obsolete Tk internal headers
 *
 * Revision 1.2  2001/04/18 13:27:03  Administrator
 * Fixed windows build system
 *
 * Revision 1.1.1.1  2001/02/15 16:32:28  beskow
 * imported sources
 *
 * Revision 1.4  1997/09/16 02:21:10  brianp
 * Geza Groma's changes
 *
 * Revision 1.3  1997/08/22 02:47:54  brianp
 * include togl.h first.  updated for Tcl/Tk 8.0
 *
 * Revision 1.2  1997/02/16 01:24:53  brianp
 * removed some unused variables
 *
 * Revision 1.1  1996/10/23 23:15:33  brianp
 * Initial revision
 *
 */


/*
 * An example Togl program demonstrating texture mapping
 */



#include "togl.h"
#include <stdlib.h>
#include <string.h>
#include <tcl.h>
#include <tk.h>
#include <GL/glu.h>
#include "image.h"



/*
 * The following variable is a special hack that is needed in order for
 * Sun shared libraries to be used for Tcl.
 */
#ifdef SUN
extern int matherr();
int *tclDummyMathPtr = (int *) matherr;
#endif

#define CHECKER 0
#define FACE 1
#define TREE 2


static GLenum minfilter = GL_NEAREST_MIPMAP_LINEAR;
static GLenum magfilter = GL_LINEAR;
static GLenum swrap = GL_REPEAT;
static GLenum twrap = GL_REPEAT;
static GLenum envmode = GL_MODULATE;
static GLubyte polycolor[4] = {255, 255, 255, 255};
static int image = CHECKER;
static GLfloat coord_scale = 1.0;
static GLfloat xrot = 0.0;
static GLfloat yrot = 0.0;
static GLfloat scale = 1.0;

static GLint width, height;

static GLboolean blend = GL_FALSE;


   
/*
 * Load a texture image.  n is one of CHECKER, FACE or TREE.
 */
void texture_image( int n )
{
   if (n==CHECKER) {
#define WIDTH 64
#define HEIGHT 64
      GLubyte teximage[WIDTH*HEIGHT][4];
      int i, j;

      for (i=0;i<HEIGHT;i++) {
         for (j=0;j<WIDTH;j++) {
            GLubyte value;
            value = ((i/4+j/4)%2) ? 0xff : 0x00;
            teximage[i*WIDTH+j][0] = value;
            teximage[i*WIDTH+j][1] = value;
            teximage[i*WIDTH+j][2] = value;
            teximage[i*WIDTH+j][3] = value;
         }
      }

      glEnable( GL_TEXTURE_2D );
      gluBuild2DMipmaps( GL_TEXTURE_2D, 4, WIDTH, HEIGHT,
                         GL_RGBA, GL_UNSIGNED_BYTE, teximage );
      blend = GL_FALSE;

#undef WIDTH
#undef HEIGHT
   }
   else if (n==FACE) {
      TK_RGBImageRec *img = tkRGBImageLoad("ben.rgb");
      if (img) {
         glEnable( GL_TEXTURE_2D );
         glPixelStorei( GL_UNPACK_ALIGNMENT, 1 );
         gluBuild2DMipmaps( GL_TEXTURE_2D, img->sizeZ, img->sizeX, img->sizeY,
                            img->sizeZ==3 ? GL_RGB : GL_RGBA,
                            GL_UNSIGNED_BYTE, img->data );

         blend = GL_TRUE;
      }
   }
   else if (n==TREE) {
      TK_RGBImageRec *img = tkRGBImageLoad("tree2.rgba");
      if (img) {
         glEnable( GL_TEXTURE_2D );
         glPixelStorei( GL_UNPACK_ALIGNMENT, 1 );
         gluBuild2DMipmaps( GL_TEXTURE_2D, img->sizeZ, img->sizeX, img->sizeY,
                            img->sizeZ==3 ? GL_RGB : GL_RGBA,
                            GL_UNSIGNED_BYTE, img->data );

         blend = GL_TRUE;
      }
   }
   else {
      abort();
   }
}


/*
 * Togl widget create callback.  This is called by Tcl/Tk when the widget has
 * been realized.  Here's where one may do some one-time context setup or
 * initializations.
 */
void create_cb( struct Togl *togl )
{
   glEnable(GL_DEPTH_TEST);    /* Enable depth buffering */

   texture_image( CHECKER );

   glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, magfilter );
   glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, minfilter );
}


/*
 * Togl widget reshape callback.  This is called by Tcl/Tk when the widget
 * has been resized.  Typically, we call glViewport and perhaps setup the
 * projection matrix.
 */
void reshape_cb( struct Togl *togl )
{
   width = Togl_Width( togl );
   height = Togl_Height( togl );

   glViewport( 0, 0, width, height );

}


static void check_error( char *where )
{
   GLenum error;

   while (1) {
      error = glGetError();
      if (error==GL_NO_ERROR) {
         break;
      }
      printf("OpenGL error near %s: %s\n", where, gluErrorString( error ) );
   }
}



/*
 * Togl widget display callback.  This is called by Tcl/Tk when the widget's
 * contents have to be redrawn.  Typically, we clear the color and depth
 * buffers, render our objects, then swap the front/back color buffers.
 */
void display_cb( struct Togl *togl )
{
   float aspect = (float) width / (float) height;

   check_error("begin display\n");

   glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT );

   /* Draw background image */
   glMatrixMode( GL_PROJECTION );
   glLoadIdentity();
   glMatrixMode( GL_MODELVIEW );
   glLoadIdentity();

   glDisable( GL_TEXTURE_2D );
   glDisable( GL_DEPTH_TEST );
   glBegin( GL_POLYGON );
   glColor3f( 0.0, 0.0, 0.3 );   glVertex2f( -1.0, -1.0 );
   glColor3f( 0.0, 0.0, 0.3 );   glVertex2f(  1.0, -1.0 );
   glColor3f( 0.0, 0.0, 0.9 );   glVertex2f(  1.0,  1.0 );
   glColor3f( 0.0, 0.0, 0.9 );   glVertex2f( -1.0,  1.0 );
   glEnd();
   
   /* draw textured object */
   glMatrixMode(GL_PROJECTION);
   glLoadIdentity();
   glFrustum( -aspect, aspect, -1.0, 1.0, 2.0, 10.0 );
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();
   glTranslatef( 0.0, 0.0, -5.0 );
   glScalef( scale, scale, scale );
   glRotatef( yrot, 0.0, 1.0, 0.0 );
   glRotatef( xrot, 1.0, 0.0, 0.0 );

   glEnable( GL_DEPTH_TEST );
   glEnable( GL_TEXTURE_2D );
   glColor4ubv( polycolor );

   if (blend) {
      glBlendFunc( GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA );
      glEnable( GL_BLEND );
   }

   glBegin( GL_POLYGON );
   glTexCoord2f( 0.0, 0.0 );                   glVertex2f( -1.0, -1.0 );
   glTexCoord2f( coord_scale, 0.0 );           glVertex2f(  1.0, -1.0 );
   glTexCoord2f( coord_scale, coord_scale );   glVertex2f(  1.0,  1.0 );
   glTexCoord2f( 0.0, coord_scale );           glVertex2f( -1.0,  1.0 );
   glEnd();

   glDisable( GL_BLEND );

   Togl_SwapBuffers( togl );
}



/*
 * Called when a magnification filter radio button is pressed.
 */
int magfilter_cb( struct Togl *togl, int argc, char *argv[] )
{
   Tcl_Interp *interp = Togl_Interp(togl);

   if (strcmp(argv[2],"GL_NEAREST")==0) {
      magfilter = GL_NEAREST;
   }
   else if (strcmp(argv[2],"GL_LINEAR")==0) {
      magfilter = GL_LINEAR;
   }
   else {
      Tcl_SetResult( interp, "unknown magnification filter type", TCL_STATIC );
      return TCL_ERROR;
   }

   glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, magfilter );
   Togl_PostRedisplay( togl );

   return TCL_OK;
}



/*
 * Called when a minification filter radio button is pressed.
 */
int minfilter_cb( struct Togl *togl, int argc, char *argv[] )
{
   Tcl_Interp *interp = Togl_Interp(togl);

   if (strcmp(argv[2],"GL_NEAREST")==0) {
      minfilter = GL_NEAREST;
   }
   else if (strcmp(argv[2],"GL_LINEAR")==0) {
      minfilter = GL_LINEAR;
   }
   else if (strcmp(argv[2],"GL_NEAREST_MIPMAP_NEAREST")==0) {
      minfilter = GL_NEAREST_MIPMAP_NEAREST;
   }
   else if (strcmp(argv[2],"GL_LINEAR_MIPMAP_NEAREST")==0) {
      minfilter = GL_LINEAR_MIPMAP_NEAREST;
   }
   else if (strcmp(argv[2],"GL_NEAREST_MIPMAP_LINEAR")==0) {
      minfilter = GL_NEAREST_MIPMAP_LINEAR;
   }
   else if (strcmp(argv[2],"GL_LINEAR_MIPMAP_LINEAR")==0) {
      minfilter = GL_LINEAR_MIPMAP_LINEAR;
   }
   else {
      Tcl_SetResult( interp, "unknown minification filter type", TCL_STATIC );
      return TCL_ERROR;
   }

   glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, minfilter );
   Togl_PostRedisplay( togl );

   return TCL_OK;
}




int xrot_cb( struct Togl *togl, int argc, char *argv[] )
{
   Tcl_Interp *interp = Togl_Interp(togl);

   /* error checking */
   if (argc != 3) {
      Tcl_SetResult( interp,
                     "wrong # args: should be \"pathName setXrot ?angle?\"",
                     TCL_STATIC );
      return TCL_ERROR;
   }

   xrot = atof( argv[2] );

   Togl_PostRedisplay(togl);

   /* Let result string equal value */
   strcpy( interp->result, argv[2] );
   return TCL_OK;
}



int yrot_cb( struct Togl *togl, int argc, char *argv[] )
{
   Tcl_Interp *interp = Togl_Interp(togl);

   /* error checking */
   if (argc != 3) {
      Tcl_SetResult( interp,
                     "wrong # args: should be \"pathName setYrot ?angle?\"",
                     TCL_STATIC );
      return TCL_ERROR;
   }

   yrot = atof( argv[2] );

   Togl_PostRedisplay(togl);

   /* Let result string equal value */
   strcpy( interp->result, argv[2] );
   return TCL_OK;
}


int scale_cb( struct Togl *togl, int argc, char *argv[] )
{
   Tcl_Interp *interp = Togl_Interp(togl);

   /* error checking */
   if (argc != 3) {
      Tcl_SetResult( interp,
                     "wrong # args: should be \"pathName scale ?value?\"",
                     TCL_STATIC );
      return TCL_ERROR;
   }

   scale = atof( argv[2] );

   Togl_PostRedisplay(togl);

   /* Let result string equal value */
   strcpy( interp->result, argv[2] );
   return TCL_OK;
}



/*
 * Called when S texture coordinate wrapping is changed.
 */
int swrap_cb( struct Togl *togl, int argc, char *argv[] )
{
   Tcl_Interp *interp = Togl_Interp(togl);

   /* error checking */
   if (argc != 3) {
      Tcl_SetResult( interp,
                     "wrong # args: should be \"pathName swrap ?mode?\"",
                     TCL_STATIC );
      return TCL_ERROR;
   }

   if (strcmp(argv[2],"GL_CLAMP")==0) {
      swrap = GL_CLAMP;
   }
   else if (strcmp(argv[2],"GL_REPEAT")==0) {
      swrap = GL_REPEAT;
   }
   else {
      Tcl_SetResult( interp, "unknown wrap value", TCL_STATIC );
      return TCL_ERROR;
   }

   glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, swrap );
   Togl_PostRedisplay(togl);

   /* Let result string equal value */
   strcpy( interp->result, argv[2] );
   return TCL_OK;
}


/*
 * Called when T texture coordinate wrapping is changed.
 */
int twrap_cb( struct Togl *togl, int argc, char *argv[] )
{
   Tcl_Interp *interp = Togl_Interp(togl);

   /* error checking */
   if (argc != 3) {
      Tcl_SetResult( interp,
                     "wrong # args: should be \"pathName twrap ?mode?\"",
                     TCL_STATIC );
      return TCL_ERROR;
   }

   if (strcmp(argv[2],"GL_CLAMP")==0) {
      twrap = GL_CLAMP;
   }
   else if (strcmp(argv[2],"GL_REPEAT")==0) {
      twrap = GL_REPEAT;
   }
   else {
      Tcl_SetResult( interp, "unknown wrap value", TCL_STATIC );
      return TCL_ERROR;
   }

   glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, twrap );
   Togl_PostRedisplay(togl);

   /* Let result string equal value */
   strcpy( interp->result, argv[2] );
   return TCL_OK;
}



/*
 * Called when the texture environment mode is changed.
 */
int envmode_cb( struct Togl *togl, int argc, char *argv[] )
{
   Tcl_Interp *interp = Togl_Interp(togl);

   /* error checking */
   if (argc != 3) {
      Tcl_SetResult( interp,
                     "wrong # args: should be \"pathName envmode ?mode?\"",
                     TCL_STATIC );
      return TCL_ERROR;
   }

   if (strcmp(argv[2],"GL_MODULATE")==0) {
      envmode = GL_MODULATE;
   }
   else if (strcmp(argv[2],"GL_DECAL")==0) {
      envmode = GL_DECAL;
   }
   else if (strcmp(argv[2],"GL_BLEND")==0) {
      envmode = GL_BLEND;
   }
   else {
      Tcl_SetResult( interp, "unknown texture env mode", TCL_STATIC );
      return TCL_ERROR;
   }

   glTexEnvi( GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, envmode );
   Togl_PostRedisplay(togl);

   /* Let result string equal value */
   strcpy( interp->result, argv[2] );
   return TCL_OK;
}



/*
 * Called when the polygon color is changed.
 */
int polycolor_cb( struct Togl *togl, int argc, char *argv[] )
{
   Tcl_Interp *interp = Togl_Interp(togl);

   /* error checking */
   if (argc != 5) {
      Tcl_SetResult( interp,
                "wrong # args: should be \"pathName polycolor ?r? ?g? ?b?\"",
                TCL_STATIC );
      return TCL_ERROR;
   }

   polycolor[0] = atoi( argv[2] );
   polycolor[1] = atoi( argv[3] );
   polycolor[2] = atoi( argv[4] );

   Togl_PostRedisplay(togl);

   /* Let result string equal value */
   strcpy( interp->result, argv[2] );
   return TCL_OK;
}



/*
 * Called when the texture image is to be changed
 */
int image_cb( struct Togl *togl, int argc, char *argv[] )
{
   Tcl_Interp *interp = Togl_Interp(togl);

   /* error checking */
   if (argc != 3) {
      Tcl_SetResult( interp,
                "wrong # args: should be \"pathName image ?name?\"",
                TCL_STATIC );
      return TCL_ERROR;
   }

   if (strcmp(argv[2],"CHECKER")==0) {
      texture_image( CHECKER );
   }
   else if (strcmp(argv[2],"FACE")==0) {
      texture_image( FACE );
   }
   else if (strcmp(argv[2],"TREE")==0) {
      texture_image( TREE );
   }
   else {
      Tcl_SetResult( interp, "unknown texture image", TCL_STATIC );
      return TCL_ERROR;
   }

   Togl_PostRedisplay(togl);

   /* Let result string equal value */
   strcpy( interp->result, argv[2] );
   return TCL_OK;
}



/*
 * Called when the texture coordinate scale is changed.
 */
int coord_scale_cb( struct Togl *togl, int argc, char *argv[] )
{
   Tcl_Interp *interp = Togl_Interp(togl);
   float s;

   /* error checking */
   if (argc != 3) {
      Tcl_SetResult( interp,
                "wrong # args: should be \"pathName coord_scale ?scale?\"",
                TCL_STATIC );
      return TCL_ERROR;
   }

   s = atof( argv[2] );
   if (s>0.0 && s<10.0) {
      coord_scale = s;
      Togl_PostRedisplay(togl);
   }

   /* Let result string equal value */
   strcpy( interp->result, argv[2] );
   return TCL_OK;
}



EXPORT(int,Texture_Init)( Tcl_Interp *interp )
{
   /*
    * Initialize Tcl, Tk, and the Togl widget module.
    */
#ifdef USE_TCL_STUBS
  if (Tcl_InitStubs(interp, "8.1", 0) == NULL) {return TCL_ERROR;}
#endif
#ifdef USE_TK_STUBS
  if (Tk_InitStubs(interp, "8.1", 0) == NULL) {return TCL_ERROR;}
#endif

   if (Togl_Init(interp) == TCL_ERROR) {
      return TCL_ERROR;
   }

   /*
    * Specify the C callback functions for widget creation, display,
    * and reshape.
    */
   Togl_CreateFunc( create_cb );
   Togl_DisplayFunc( display_cb );
   Togl_ReshapeFunc( reshape_cb );

   /*
    * Make a new Togl widget command so the Tcl code can set a C variable.
    */
   Togl_CreateCommand( "min_filter", minfilter_cb );
   Togl_CreateCommand( "mag_filter", magfilter_cb );
   Togl_CreateCommand( "xrot", xrot_cb );
   Togl_CreateCommand( "yrot", yrot_cb );
   Togl_CreateCommand( "scale", scale_cb );
   Togl_CreateCommand( "swrap", swrap_cb );
   Togl_CreateCommand( "twrap", twrap_cb );
   Togl_CreateCommand( "envmode", envmode_cb );
   Togl_CreateCommand( "polycolor", polycolor_cb );
   Togl_CreateCommand( "image", image_cb );
   Togl_CreateCommand( "coord_scale", coord_scale_cb );

   /*
    * Call Tcl_CreateCommand for application-specific commands, if
    * they weren't already created by the init procedures called above.
    */

   return TCL_OK;
}
