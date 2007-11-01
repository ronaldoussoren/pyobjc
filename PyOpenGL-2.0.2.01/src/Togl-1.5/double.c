/* $Id: double.c,v 1.1 2001/05/14 22:55:19 twburton Exp $ */

/*
 * Togl - a Tk OpenGL widget
 * Copyright (C) 1996-1997  Brian Paul and Ben Bederson
 * See the LICENSE file for copyright details.
 */


/*
 * $Log: double.c,v $
 * Revision 1.1  2001/05/14 22:55:19  twburton
 * Add Togl
 *
 * Revision 1.1  1999/07/15 21:13:12  dacvs
 * Togl, again!
 *
 * Revision 1.7  1998/03/12 03:52:31  brianp
 * now sharing display lists between the widgets
 *
 * Revision 1.6  1997/09/16 02:17:10  brianp
 * Geza Groma's WIN32 changes
 *
 * Revision 1.5  1997/08/22 02:47:54  brianp
 * include togl.h first.  updated for Tcl/Tk 8.0
 *
 * Revision 1.4  1996/10/25 00:37:50  brianp
 * added print_string() wrapper for glCallLists()
 *
 * Revision 1.3  1996/10/23 23:39:56  brianp
 * moved glColor() before glRasterPos()
 *
 * Revision 1.2  1996/10/23 23:33:03  brianp
 * added text labels
 *
 * Revision 1.1  1996/10/23 23:15:49  brianp
 * Initial revision
 *
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


static GLuint FontBase;
static float xAngle = 0.0, yAngle = 0.0, zAngle = 0.0;
static GLfloat CornerX, CornerY, CornerZ;  /* where to print strings */


/*
 * Togl widget create callback.  This is called by Tcl/Tk when the widget has
 * been realized.  Here's where one may do some one-time context setup or
 * initializations.
 */
void create_cb( struct Togl *togl )
{
   FontBase = Togl_LoadBitmapFont( togl, TOGL_BITMAP_8_BY_13 );
   if (!FontBase) {
      printf("Couldn't load font!\n");
      exit(1);
   }
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
   glFrustum(-aspect, aspect, -1.0, 1.0, 1.0, 10.0);

   CornerX = -aspect;
   CornerY = -1.0;
   CornerZ = -1.1;

   /* Change back to model view transform for rendering */
   glMatrixMode(GL_MODELVIEW);
}



static void print_string( const char *s )
{
   glCallLists( strlen(s), GL_UNSIGNED_BYTE, s );
}


/*
 * Togl widget display callback.  This is called by Tcl/Tk when the widget's
 * contents have to be redrawn.  Typically, we clear the color and depth
 * buffers, render our objects, then swap the front/back color buffers.
 */
void display_cb( struct Togl *togl )
{
   static GLuint cubeList = 0;
   char *ident;

   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

   glLoadIdentity();	/* Reset modelview matrix to the identity matrix */
   glTranslatef(0.0, 0.0, -3.0);      /* Move the camera back three units */
   glRotatef(xAngle, 1.0, 0.0, 0.0);  /* Rotate by X, Y, and Z angles */
   glRotatef(yAngle, 0.0, 1.0, 0.0);
   glRotatef(zAngle, 0.0, 0.0, 1.0);
    
   glEnable( GL_DEPTH_TEST );

   if (!cubeList) {
      cubeList = glGenLists(1);
      glNewList(cubeList, GL_COMPILE);

      /* Front face */
      glBegin(GL_QUADS);
      glColor3f(0.0, 0.7, 0.1);	/* Green */
      glVertex3f(-1.0, 1.0, 1.0);
      glVertex3f(1.0, 1.0, 1.0);
      glVertex3f(1.0, -1.0, 1.0);
      glVertex3f(-1.0, -1.0, 1.0);
      /* Back face */
      glColor3f(0.9, 1.0, 0.0);   /* Yellow */
      glVertex3f(-1.0, 1.0, -1.0);
      glVertex3f(1.0, 1.0, -1.0);
      glVertex3f(1.0, -1.0, -1.0);
      glVertex3f(-1.0, -1.0, -1.0);
      /* Top side face */
      glColor3f(0.2, 0.2, 1.0);   /* Blue */
      glVertex3f(-1.0, 1.0, 1.0);
      glVertex3f(1.0, 1.0, 1.0);
      glVertex3f(1.0, 1.0, -1.0);
      glVertex3f(-1.0, 1.0, -1.0);
      /* Bottom side face */
      glColor3f(0.7, 0.0, 0.1);   /* Red */
      glVertex3f(-1.0, -1.0, 1.0);
      glVertex3f(1.0, -1.0, 1.0);
      glVertex3f(1.0, -1.0, -1.0);
      glVertex3f(-1.0, -1.0, -1.0);
      glEnd();

      glEndList();

   }
   glCallList(cubeList);
   
   glDisable( GL_DEPTH_TEST );
   glLoadIdentity();
   glColor3f( 1.0, 1.0, 1.0 );
   glRasterPos3f( CornerX, CornerY, CornerZ );
   glListBase( FontBase );
   ident = Togl_Ident( togl );
   if (strcmp(ident,"Single")==0) {
      print_string( "Single buffered" );
   }
   else {
      print_string( "Double buffered" );
   }
   Togl_SwapBuffers( togl );
}




int setXrot_cb( struct Togl *togl, int argc, char *argv[] )
{
   Tcl_Interp *interp = Togl_Interp(togl);

   /* error checking */
   if (argc != 3) {
      Tcl_SetResult( interp,
                     "wrong # args: should be \"pathName setXrot ?angle?\"",
                     TCL_STATIC );
      return TCL_ERROR;
   }

   xAngle = atof( argv[2] );
   
/* printf( "before %f ", xAngle ); */

   if ( xAngle < 0.0 ) {
     xAngle += 360.0;
   } else if ( xAngle > 360.0 ) {
     xAngle -= 360.0;
   }

/* printf( "after %f \n", xAngle ); */

   Togl_PostRedisplay( togl );

   /* Let result string equal value */
   strcpy( interp->result, argv[2] );
   return TCL_OK;
}



int setYrot_cb( struct Togl *togl, int argc, char *argv[] )
{
   Tcl_Interp *interp = Togl_Interp(togl);

   /* error checking */
   if (argc != 3) {
      Tcl_SetResult( interp,
                     "wrong # args: should be \"pathName setYrot ?angle?\"",
                     TCL_STATIC );
      return TCL_ERROR;
   }

   yAngle = atof( argv[2] );
   
   if ( yAngle < 0.0 ) {
     yAngle += 360.0;
   } else if ( yAngle > 360.0 ) {
     yAngle -= 360.0;
   }

   Togl_PostRedisplay(togl);

   /* Let result string equal value */
   strcpy( interp->result, argv[2] );
   return TCL_OK;
}

int getXrot_cb( ClientData clientData, Tcl_Interp *interp,
		int argc, char *argv[])
{
  sprintf( interp->result, "%d", (int)xAngle );
  return TCL_OK;
}

int getYrot_cb( ClientData clientData, Tcl_Interp *interp,
		int argc, char *argv[])
{
  sprintf( interp->result, "%d", (int)yAngle );
  return TCL_OK;
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

   /*
    * Make a new Togl widget command so the Tcl code can set a C variable.
    */
   
   Togl_CreateCommand( "setXrot", setXrot_cb );
   Togl_CreateCommand( "setYrot", setYrot_cb );

   /*
    * Call Tcl_CreateCommand for application-specific commands, if
    * they weren't already created by the init procedures called above.
    */
   
   Tcl_CreateCommand( interp, "getXrot", getXrot_cb, (ClientData)NULL,
                                                     (Tcl_CmdDeleteProc *)NULL );
   Tcl_CreateCommand( interp, "getYrot", getYrot_cb, (ClientData)NULL,
                                                     (Tcl_CmdDeleteProc *)NULL );
   /*
    * Specify a user-specific startup file to invoke if the application
    * is run interactively.  Typically the startup file is "~/.apprc"
    * where "app" is the name of the application.  If this line is deleted
    * then no user-specific startup file will be run under any conditions.
    */
#if (TCL_MAJOR_VERSION * 100 + TCL_MINOR_VERSION) >= 705
   Tcl_SetVar( interp, "tcl_rcFileName", "./double.tcl", TCL_GLOBAL_ONLY );
#else
   tcl_RcFileName = "./double.tcl";
#endif

   return TCL_OK;
}



int main( int argc, char *argv[] )
{
   Tk_Main( argc, argv, my_init );
   return 0;
}
