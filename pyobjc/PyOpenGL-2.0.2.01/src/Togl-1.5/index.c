/* $Id: index.c,v 1.1 2001/05/14 22:55:19 twburton Exp $ */

/*
 * Togl - a Tk OpenGL widget
 * Copyright (C) 1996-1997  Brian Paul and Ben Bederson
 * See the LICENSE file for copyright details.
 */


/*
 * $Log: index.c,v $
 * Revision 1.1  2001/05/14 22:55:19  twburton
 * Add Togl
 *
 * Revision 1.1  1999/07/15 21:13:12  dacvs
 * Togl, again!
 *
 * Revision 1.5  1997/09/16 02:20:02  brianp
 * Geza Groma's changes
 *
 * Revision 1.4  1997/08/22 02:47:54  brianp
 * include togl.h first.  updated for Tcl/Tk 8.0
 *
 * Revision 1.3  1997/04/11 01:43:39  brianp
 * set shademodel to flag, disable dithering
 *
 * Revision 1.2  1997/04/11 01:37:34  brianp
 * added a timer to rotate the triangles
 *
 * Revision 1.1  1996/10/23 23:15:40  brianp
 * Initial revision
 *
 */


/*
 * An example Togl program using color-index mode.
 */


#include "togl.h"
#include <stdlib.h>
#include <string.h>
#include <tcl.h>
#include <tk.h>


/*
 * The following variable is a special hack that is needed in order for
 * Sun shared libraries to be used for Tcl.
 */
extern int matherr();
int *tclDummyMathPtr = (int *) matherr;


/* Our color indexes: */
unsigned long black, red, green, blue;

/* Rotation angle */
static float Angle = 0.0;



/*
 * Togl widget create callback.  This is called by Tcl/Tk when the widget has
 * been realized.  Here's where one may do some one-time context setup or
 * initializations.
 */
void create_cb( struct Togl *togl )
{
   /* allocate color indexes */
   black = Togl_AllocColor( togl, 0.0, 0.0, 0.0 );
   red   = Togl_AllocColor( togl, 1.0, 0.0, 0.0 );
   green = Togl_AllocColor( togl, 0.0, 1.0, 0.0 );
   blue  = Togl_AllocColor( togl, 0.0, 0.0, 1.0 );

   /* If we were using a private read/write colormap we'd setup our color
    * table with something like this:
    */
/*
   black = 1;   Togl_SetColor( togl, black, 0.0, 0.0, 0.0 );
   red   = 2;   Togl_SetColor( togl, red,   1.0, 0.0, 0.0 );
   green = 3;   Togl_SetColor( togl, green, 0.0, 1.0, 0.0 );
   blue  = 4;   Togl_SetColor( togl, blue,  0.0, 0.0, 1.0 );
*/

   glShadeModel(GL_FLAT);
   glDisable(GL_DITHER);
}


/*
 * Togl widget reshape callback.  This is called by Tcl/Tk when the widget
 * has been resized.  Typically, we call glViewport and perhaps setup the
 * projection matrix.
 */
void reshape_cb( struct Togl *togl )
{
   int width = Togl_Width( togl );
   int height = Togl_Height( togl );
   float aspect = (float) width / (float) height;

   glViewport( 0, 0, width, height );

   /* Set up projection transform */
   glMatrixMode(GL_PROJECTION);
   glLoadIdentity();
   glOrtho( -aspect, aspect, -1.0, 1.0, -1.0, 1.0 );

   /* Change back to model view transform for rendering */
   glMatrixMode(GL_MODELVIEW);
}



/*
 * Togl widget display callback.  This is called by Tcl/Tk when the widget's
 * contents have to be redrawn.  Typically, we clear the color and depth
 * buffers, render our objects, then swap the front/back color buffers.
 */
void display_cb( struct Togl *togl )
{
   glClearIndex( black );
   glClear(GL_COLOR_BUFFER_BIT);

   glPushMatrix();
   glTranslatef(0.3, -0.3, 0.0);
   glRotatef(Angle, 0.0, 0.0, 1.0);
   glIndexi( red );
   glBegin( GL_TRIANGLES );
   glVertex2f( -0.5, -0.3 );
   glVertex2f(  0.5, -0.3 );
   glVertex2f(  0.0,  0.6 );
   glEnd();
   glPopMatrix();

   glPushMatrix();
   glRotatef(Angle, 0.0, 0.0, 1.0);
   glIndexi( green );
   glBegin( GL_TRIANGLES );
   glVertex2f( -0.5, -0.3 );
   glVertex2f(  0.5, -0.3 );
   glVertex2f(  0.0,  0.6 );
   glEnd();
   glPopMatrix();

   glPushMatrix();
   glTranslatef(-0.3, 0.3, 0.0);
   glRotatef(Angle, 0.0, 0.0, 1.0);
   glIndexi( blue );
   glBegin( GL_TRIANGLES );
   glVertex2f( -0.5, -0.3 );
   glVertex2f(  0.5, -0.3 );
   glVertex2f(  0.0,  0.6 );
   glEnd();
   glPopMatrix();

   glFlush();
   Togl_SwapBuffers(togl);
}



void timer_cb( struct Togl *togl )
{
   Angle += 5.0;
   Togl_PostRedisplay(togl);
}


#if defined(WIN32)
EXTERN int		TkConsoleInit(Tcl_Interp *interp);
#endif /* WIN32 */

/*
 * Called by Tk_Main() to let me initialize the modules (Togl) I will need.
 */
int my_init( Tcl_Interp *interp )
{
   /*
    * Initialize Tcl, Tk, and the Togl widget module.
    */
   if (Tcl_Init(interp) == TCL_ERROR) {
      return TCL_ERROR;
   }
   if (Tk_Init(interp) == TCL_ERROR) {
      return TCL_ERROR;
   }

#ifdef WIN32
    /*
     * Set up a console window. Delete the following statement if you do not need that.
     */
    if (TkConsoleInit(interp) == TCL_ERROR) {
	   return TCL_ERROR;
    }
#endif /* WIN32 */

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
   Togl_TimerFunc( timer_cb );

   /*
    * Make a new Togl widget command so the Tcl code can set a C variable.
    */
   /* NONE */

   /*
    * Call Tcl_CreateCommand for application-specific commands, if
    * they weren't already created by the init procedures called above.
    */
   /*NOTHING*/

   /*
    * Specify a user-specific startup file to invoke if the application
    * is run interactively.  Typically the startup file is "~/.apprc"
    * where "app" is the name of the application.  If this line is deleted
    * then no user-specific startup file will be run under any conditions.
    */
#if (TCL_MAJOR_VERSION * 100 + TCL_MINOR_VERSION) >= 705
   Tcl_SetVar( interp, "tcl_rcFileName", "./index.tcl", TCL_GLOBAL_ONLY );
#else
   tcl_RcFileName = "./index.tcl";
#endif

   return TCL_OK;
}



int main( int argc, char *argv[] )
{
   Tk_Main( argc, argv, my_init );
   return 0;
}
