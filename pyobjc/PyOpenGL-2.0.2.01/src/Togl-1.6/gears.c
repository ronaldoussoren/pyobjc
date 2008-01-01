/* gears.c */

/*
 * 3-D gear wheels.  This program is in the public domain.
 *
 * Brian Paul
 *
 *
 * Modified to work under Togl as a widget for TK 1997
 *
 * Philip Quaife
 *
*/

#include "togl.h"
#include <math.h>
#include <stdlib.h>
#include <tcl.h>
#include <tk.h>
#include <GL/glu.h>

#ifndef M_PI
#  define M_PI 3.14159265
#endif

struct WHIRLYGIZMO {
	GLint	Gear1,Gear2,Gear3;
	GLfloat	Rotx,Roty,Rotz;
	GLfloat	Angle;
	int	Height,Width;
	};

/*
 * Draw a gear wheel.  You'll probably want to call this function when
 * building a display list since we do a lot of trig here.
 *
 * Input:  inner_radius - radius of hole at center
 *         outer_radius - radius at center of teeth
 *         width - width of gear
 *         teeth - number of teeth
 *         tooth_depth - depth of tooth
 */
static void gear( GLfloat inner_radius, GLfloat outer_radius, GLfloat width,
		  GLint teeth, GLfloat tooth_depth )
{
   GLint i;
   GLfloat r0, r1, r2;
   GLfloat angle, da;
   GLfloat u, v, len;

   r0 = inner_radius;
   r1 = outer_radius - tooth_depth/2.0;
   r2 = outer_radius + tooth_depth/2.0;

   da = 2.0*M_PI / teeth / 4.0;

   glShadeModel( GL_FLAT );

   glNormal3f( 0.0, 0.0, 1.0 );

   /* draw front face */
   glBegin( GL_QUAD_STRIP );
   for (i=0;i<=teeth;i++) {
      angle = i * 2.0*M_PI / teeth;
      glVertex3f( r0*cos(angle), r0*sin(angle), width*0.5 );
      glVertex3f( r1*cos(angle), r1*sin(angle), width*0.5 );
      glVertex3f( r0*cos(angle), r0*sin(angle), width*0.5 );
      glVertex3f( r1*cos(angle+3*da), r1*sin(angle+3*da), width*0.5 );
   }
   glEnd();

   /* draw front sides of teeth */
   glBegin( GL_QUADS );
   da = 2.0*M_PI / teeth / 4.0;
   for (i=0;i<teeth;i++) {
      angle = i * 2.0*M_PI / teeth;

      glVertex3f( r1*cos(angle),      r1*sin(angle),      width*0.5 );
      glVertex3f( r2*cos(angle+da),   r2*sin(angle+da),   width*0.5 );
      glVertex3f( r2*cos(angle+2*da), r2*sin(angle+2*da), width*0.5 );
      glVertex3f( r1*cos(angle+3*da), r1*sin(angle+3*da), width*0.5 );
   }
   glEnd();


   glNormal3f( 0.0, 0.0, -1.0 );

   /* draw back face */
   glBegin( GL_QUAD_STRIP );
   for (i=0;i<=teeth;i++) {
      angle = i * 2.0*M_PI / teeth;
      glVertex3f( r1*cos(angle), r1*sin(angle), -width*0.5 );
      glVertex3f( r0*cos(angle), r0*sin(angle), -width*0.5 );
      glVertex3f( r1*cos(angle+3*da), r1*sin(angle+3*da), -width*0.5 );
      glVertex3f( r0*cos(angle), r0*sin(angle), -width*0.5 );
   }
   glEnd();

   /* draw back sides of teeth */
   glBegin( GL_QUADS );
   da = 2.0*M_PI / teeth / 4.0;
   for (i=0;i<teeth;i++) {
      angle = i * 2.0*M_PI / teeth;

      glVertex3f( r1*cos(angle+3*da), r1*sin(angle+3*da), -width*0.5 );
      glVertex3f( r2*cos(angle+2*da), r2*sin(angle+2*da), -width*0.5 );
      glVertex3f( r2*cos(angle+da),   r2*sin(angle+da),   -width*0.5 );
      glVertex3f( r1*cos(angle),      r1*sin(angle),      -width*0.5 );
   }
   glEnd();


   /* draw outward faces of teeth */
   glBegin( GL_QUAD_STRIP );
   for (i=0;i<teeth;i++) {
      angle = i * 2.0*M_PI / teeth;

      glVertex3f( r1*cos(angle),      r1*sin(angle),       width*0.5 );
      glVertex3f( r1*cos(angle),      r1*sin(angle),      -width*0.5 );
      u = r2*cos(angle+da) - r1*cos(angle);
      v = r2*sin(angle+da) - r1*sin(angle);
      len = sqrt( u*u + v*v );
      u /= len;
      v /= len;
      glNormal3f( v, -u, 0.0 );
      glVertex3f( r2*cos(angle+da),   r2*sin(angle+da),    width*0.5 );
      glVertex3f( r2*cos(angle+da),   r2*sin(angle+da),   -width*0.5 );
      glNormal3f( cos(angle), sin(angle), 0.0 );
      glVertex3f( r2*cos(angle+2*da), r2*sin(angle+2*da),  width*0.5 );
      glVertex3f( r2*cos(angle+2*da), r2*sin(angle+2*da), -width*0.5 );
      u = r1*cos(angle+3*da) - r2*cos(angle+2*da);
      v = r1*sin(angle+3*da) - r2*sin(angle+2*da);
      glNormal3f( v, -u, 0.0 );
      glVertex3f( r1*cos(angle+3*da), r1*sin(angle+3*da),  width*0.5 );
      glVertex3f( r1*cos(angle+3*da), r1*sin(angle+3*da), -width*0.5 );
      glNormal3f( cos(angle), sin(angle), 0.0 );
   }

   glVertex3f( r1*cos(0), r1*sin(0), width*0.5 );
   glVertex3f( r1*cos(0), r1*sin(0), -width*0.5 );

   glEnd();


   glShadeModel( GL_SMOOTH );

   /* draw inside radius cylinder */
   glBegin( GL_QUAD_STRIP );
   for (i=0;i<=teeth;i++) {
      angle = i * 2.0*M_PI / teeth;
      glNormal3f( -cos(angle), -sin(angle), 0.0 );
      glVertex3f( r0*cos(angle), r0*sin(angle), -width*0.5 );
      glVertex3f( r0*cos(angle), r0*sin(angle), width*0.5 );
   }
   glEnd();
      
}

/*
static GLfloat view_rotx=20.0, view_roty=30.0, view_rotz=0.0;
static GLint gear1, gear2, gear3;
static GLfloat angle = 0.0;
*/
static GLuint limit;
static GLuint count = 1;

static GLubyte polycolor[4] = {255, 255, 255, 255};

static void draw( struct Togl *togl )
{
   struct WHIRLYGIZMO *Wg;
   glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT );

   Wg = Togl_GetClientData(togl);
   glDisable(GL_TEXTURE_2D); 
   glPushMatrix();
   glRotatef( Wg->Rotx, 1.0, 0.0, 0.0 );
   glRotatef( Wg->Roty, 0.0, 1.0, 0.0 );
   glRotatef( Wg->Rotz, 0.0, 0.0, 1.0 );

   glPushMatrix();
   glTranslatef( -3.0, -2.0, 0.0 );
   glRotatef( Wg->Angle, 0.0, 0.0, 1.0 );
   glEnable(GL_DEPTH_TEST);
   glCallList(Wg->Gear1);
   glEnable(GL_DEPTH_TEST);
   glPopMatrix();

   glPushMatrix();
   glTranslatef( 3.1, -2.0, 0.0 );
   glRotatef( -2.0*Wg->Angle-9.0, 0.0, 0.0, 1.0 );
   glCallList(Wg->Gear2);
   glPopMatrix();

   glPushMatrix();
   glTranslatef( -3.1, 4.2, 0.0 );
   glRotatef( -2.0*Wg->Angle-25.0, 0.0, 0.0, 1.0 );
   glCallList(Wg->Gear3);
   glPopMatrix();

   glPopMatrix();

   Togl_SwapBuffers(togl);

}



static void zap( struct Togl *togl )
{
   struct WHIRLYGIZMO *Wg;

   Wg = Togl_GetClientData(togl);
   free(Wg);
}


static void idle( struct Togl *togl )
{
   struct WHIRLYGIZMO *Wg;

   Wg = Togl_GetClientData(togl);
   Wg->Angle += 2.0;
   Togl_PostRedisplay(togl);
}


/* change view angle, exit upon ESC */
/* 
static GLenum key(int k, GLenum mask)
{
   switch (k) {
      case TK_UP:
         view_rotx += 5.0;
	 return GL_TRUE;
      case TK_DOWN:
         view_rotx -= 5.0;
	 return GL_TRUE;
      case TK_LEFT:
         view_roty += 5.0;
	 return GL_TRUE;
      case TK_RIGHT:
         view_roty -= 5.0;
	 return GL_TRUE;
      case TK_z:
	 view_rotz += 5.0;
	 return GL_TRUE;
      case TK_Z:
	 view_rotz -= 5.0;
	 return GL_TRUE;
   }
   return GL_FALSE;
}
*/

/* new window size or exposure */
static void reshape( struct Togl *togl)
{
   struct WHIRLYGIZMO *Wg;
   int width, height ;
   width = Togl_Width(togl);
   height = Togl_Height(togl);
   glViewport(0, 0, (GLint)width, (GLint)height);
   glMatrixMode(GL_PROJECTION);
   glLoadIdentity();
   if (width>height) {
      GLfloat w = (GLfloat) width / (GLfloat) height;
      glFrustum( -w, w, -1.0, 1.0, 5.0, 60.0 );
   }
   else {
      GLfloat h = (GLfloat) height / (GLfloat) width;
      glFrustum( -1.0, 1.0, -h, h, 5.0, 60.0 );
   }

   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();
   glTranslatef( 0.0, 0.0, -40.0 );
   glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT );

}


static void init( struct Togl *togl )
{
   struct WHIRLYGIZMO *Wg;

   static GLfloat red[4] = {0.8, 0.1, 0.0, 1.0 };
   static GLfloat green[4] = {0.0, 0.8, 0.2, 1.0 };
   static GLfloat blue[4] = {0.2, 0.2, 1.0, 1.0 };
   static GLfloat pos[4] = {5.0, 5.0, 10.0, 0.0 };
   glLightfv( GL_LIGHT0, GL_POSITION, pos );
   glEnable( GL_CULL_FACE );
   glEnable( GL_LIGHTING );
   glEnable( GL_LIGHT0 );
   glEnable( GL_DEPTH_TEST );
   /* make the gears */
   Wg = malloc(sizeof(*Wg));
   if( ! Wg ) {
      Tcl_SetResult( Togl_Interp(togl),
          "\"Cannot allocate client data for widget\"",
          TCL_STATIC );
   }
   Wg->Gear1 = glGenLists(1);
   glNewList(Wg->Gear1, GL_COMPILE);
   glMaterialfv( GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red );
   gear( 1.0, 4.0, 1.0, 20, 0.7 );
   glEndList();

   Wg->Gear2 = glGenLists(1);
   glNewList(Wg->Gear2, GL_COMPILE);
   glMaterialfv( GL_FRONT, GL_AMBIENT_AND_DIFFUSE, green );
   gear( 0.5, 2.0, 2.0, 10, 0.7 );
   glEndList();

   Wg->Gear3 = glGenLists(1);
   glNewList(Wg->Gear3, GL_COMPILE);
   glMaterialfv( GL_FRONT, GL_AMBIENT_AND_DIFFUSE, blue );
   gear( 1.3, 2.0, 0.5, 10, 0.7 );
   glEndList();

   glEnable( GL_NORMALIZE );
   Wg->Height = Togl_Height(togl);
   Wg->Width  = Togl_Width(togl);
   Wg->Angle = 0.0;
   Wg->Rotx = 0.0;
   Wg->Roty = 0.0;
   Wg->Rotz = 0.0;
   Togl_SetClientData(togl,(ClientData)Wg);
}

int position( struct Togl *togl, int argc, char *argv[] )
{
   struct WHIRLYGIZMO *Wg;
   Tcl_Interp *interp = Togl_Interp(togl);
   char Result[100];

   Wg = Togl_GetClientData(togl);
   /* error checking */
   if (argc != 2) {
      Tcl_SetResult( interp,
                     "wrong # args: should be \"pathName \"",
                     TCL_STATIC );
      return TCL_ERROR;
   }

   /* Let result string equal value */
    sprintf(Result,"%g %g",Wg->Roty,Wg->Rotx);
    
     Tcl_SetResult( interp,
                     Result,
                     TCL_VOLATILE );
   return TCL_OK;
}

int rotate( struct Togl *togl, int argc, char *argv[] )
{
   struct WHIRLYGIZMO *Wg;
   Tcl_Interp *interp = Togl_Interp(togl);

   Wg = Togl_GetClientData(togl);
   /* error checking */
   if (argc != 4) {
      Tcl_SetResult( interp,
                     "wrong # args: should be \"pathName xrot yrot\"",
                     TCL_STATIC );
      return TCL_ERROR;
   }

   Wg->Roty = atof( argv[2] );
   Wg->Rotx = atof(argv[3] );
   Togl_PostRedisplay(togl);

   /* Let result string equal value */
   strcpy( interp->result, argv[2] );
   return TCL_OK;
}

EXPORT(int,Gears_Init)(Tcl_Interp *interp) 
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
   Togl_CreateFunc( init );
   Togl_DestroyFunc( zap );
   Togl_DisplayFunc( draw );
   Togl_ReshapeFunc( reshape );
   Togl_TimerFunc(  idle );
   Togl_CreateCommand("rotate",rotate);
   Togl_CreateCommand("position",position);
   return TCL_OK;
}
