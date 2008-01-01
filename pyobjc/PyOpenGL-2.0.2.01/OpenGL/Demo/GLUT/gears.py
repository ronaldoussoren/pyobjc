#!/usr/bin/env python2.3
# * 3-D gear wheels.  This program is in the public domain.
# * Brian Paul
# * Conversion to GLUT by Mark J. Kilgard 
# conversion to Python using PyOpenGL with frame rates ala glxgears
# Peter Barth
     
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys, time 
from math import sin,cos,sqrt,pi

def gear(inner_radius, outer_radius, width, teeth, tooth_depth):
    r0 = inner_radius
    r1 = outer_radius - tooth_depth/2.0
    r2 = outer_radius + tooth_depth/2.0    
    da = 2.0*pi / teeth / 4.0
    
    glShadeModel(GL_FLAT)  
    glNormal3f(0.0, 0.0, 1.0)

    # draw front face
    glBegin(GL_QUAD_STRIP)
    for i in range(teeth + 1):
        angle = i * 2.0 * pi / teeth
        glVertex3f(r0*cos(angle), r0*sin(angle), width*0.5)
        glVertex3f(r1*cos(angle), r1*sin(angle), width*0.5)
        glVertex3f(r0*cos(angle), r0*sin(angle), width*0.5)
        glVertex3f(r1*cos(angle+3*da), r1*sin(angle+3*da), width*0.5)
    glEnd()

    # draw front sides of teeth
    glBegin(GL_QUADS)
    da = 2.0*pi / teeth / 4.0
    for i in range(teeth):
        angle = i * 2.0*pi / teeth
        glVertex3f(r1*cos(angle),      r1*sin(angle),      width*0.5)
        glVertex3f(r2*cos(angle+da),   r2*sin(angle+da),   width*0.5)
        glVertex3f(r2*cos(angle+2*da), r2*sin(angle+2*da), width*0.5)
        glVertex3f(r1*cos(angle+3*da), r1*sin(angle+3*da), width*0.5)
    glEnd()

    glNormal3f(0.0, 0.0, -1.0)

    # draw back face
    glBegin(GL_QUAD_STRIP)
    for i in range(teeth + 1):
        angle = i * 2.0*pi / teeth
        glVertex3f(r1*cos(angle), r1*sin(angle), -width*0.5)
        glVertex3f(r0*cos(angle), r0*sin(angle), -width*0.5)
        glVertex3f(r1*cos(angle+3*da), r1*sin(angle+3*da),-width*0.5)
        glVertex3f(r0*cos(angle), r0*sin(angle), -width*0.5)
    glEnd()

    # draw back sides of teeth
    glBegin(GL_QUADS)
    da = 2.0*pi / teeth / 4.0
    for i in range(teeth):
        angle = i * 2.0*pi / teeth        
        glVertex3f(r1*cos(angle+3*da), r1*sin(angle+3*da),-width*0.5)
        glVertex3f(r2*cos(angle+2*da), r2*sin(angle+2*da),-width*0.5)
        glVertex3f(r2*cos(angle+da),   r2*sin(angle+da),  -width*0.5)
        glVertex3f(r1*cos(angle),      r1*sin(angle),     -width*0.5)
    glEnd()

    # draw outward faces of teeth
    glBegin(GL_QUAD_STRIP);
    for i in range(teeth):
        angle = i * 2.0*pi / teeth        
        glVertex3f(r1*cos(angle), r1*sin(angle),  width*0.5)
        glVertex3f(r1*cos(angle), r1*sin(angle), -width*0.5)
        u = r2*cos(angle+da) - r1*cos(angle)
        v = r2*sin(angle+da) - r1*sin(angle)
        len = sqrt(u*u + v*v)
        u = u / len
        v = v / len
        glNormal3f(v, -u, 0.0)
        glVertex3f(r2*cos(angle+da),   r2*sin(angle+da),   width*0.5)
        glVertex3f(r2*cos(angle+da),   r2*sin(angle+da),  -width*0.5)
        glNormal3f(cos(angle), sin(angle), 0.0)
        glVertex3f(r2*cos(angle+2*da), r2*sin(angle+2*da), width*0.5)
        glVertex3f(r2*cos(angle+2*da), r2*sin(angle+2*da),-width*0.5)
        u = r1*cos(angle+3*da) - r2*cos(angle+2*da)
        v = r1*sin(angle+3*da) - r2*sin(angle+2*da)
        glNormal3f(v, -u, 0.0)
        glVertex3f(r1*cos(angle+3*da), r1*sin(angle+3*da), width*0.5)
        glVertex3f(r1*cos(angle+3*da), r1*sin(angle+3*da),-width*0.5)
        glNormal3f(cos(angle), sin(angle), 0.0)

    glVertex3f(r1*cos(0), r1*sin(0), width*0.5)
    glVertex3f(r1*cos(0), r1*sin(0), -width*0.5)

    glEnd()

    glShadeModel(GL_SMOOTH)

    # draw inside radius cylinder
    glBegin(GL_QUAD_STRIP)
    for i in range(teeth + 1):
        angle = i * 2.0*pi / teeth;
        glNormal3f(-cos(angle), -sin(angle), 0.0)
        glVertex3f(r0*cos(angle), r0*sin(angle), -width*0.5)
        glVertex3f(r0*cos(angle), r0*sin(angle), width*0.5)
    glEnd()


(view_rotx,view_roty,view_rotz)=(20.0, 30.0, 0.0)
(gear1, gear2, gear3) = (0,0,0)
angle = 0.0


tStart = t0 = time.time()
frames = 0
rotationRate = 1.01

def framerate():
    global t0, frames
    t = time.time()
    frames += 1
    if t - t0 >= 5.0:
        seconds = t - t0
        fps = frames/seconds
        print "%.0f frames in %3.1f seconds = %6.3f FPS" % (frames,seconds,fps)
        t0 = t
        frames = 0


def draw():
    rotationRate = (time.time() - tStart) * 1.05
    angle = (2 * pi) * ((time.time() - tStart)*rotationRate)# * rotationRate
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(view_rotx, 1.0, 0.0, 0.0)
    glRotatef(view_roty, 0.0, 1.0, 0.0)
    glRotatef(view_rotz, 0.0, 0.0, 1.0)

    glPushMatrix()
    glTranslatef(-3.0, -2.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)
    glCallList(gear1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.1, -2.0, 0.0)
    glRotatef(-2.0*angle-9.0, 0.0, 0.0, 1.0)
    glCallList(gear2)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-3.1, 4.2, 0.0)
    glRotatef(-2.0*angle-25.0, 0.0, 0.0, 1.0)
    glCallList(gear3)
    glPopMatrix()

    glPopMatrix()

    glutSwapBuffers()

    framerate()
    
def idle():
    global angle
    angle += 2.0
    glutPostRedisplay()
    

# change view angle, exit upon ESC
def key(k, x, y):
    global view_rotz

    if k == 'z':
        view_rotz += 5.0
    elif k == 'Z':
        view_rotz -= 5.0
    elif ord(k) == 27: # Escape
        sys.exit(0)
    else:
        return
    glutPostRedisplay()


# change view angle
def special(k, x, y):
    global view_rotx, view_roty, view_rotz
    
    if k == GLUT_KEY_UP:
        view_rotx += 5.0
    elif k == GLUT_KEY_DOWN:
        view_rotx -= 5.0
    elif k == GLUT_KEY_LEFT:
        view_roty += 5.0
    elif k == GLUT_KEY_RIGHT:
        view_roty -= 5.0
    else:
        return
    glutPostRedisplay()


# new window size or exposure
def reshape(width, height):
    h = float(height) / float(width);
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1.0, 1.0, -h, h, 5.0, 60.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -40.0)

def init():
    global gear1, gear2, gear3
    
    pos = (5.0, 5.0, 10.0, 0.0)
    red = (0.8, 0.1, 0.0, 1.0)
    green = (0.0, 0.8, 0.2, 1.0)
    blue = (0.2, 0.2, 1.0, 1.0)

    glLightfv(GL_LIGHT0, GL_POSITION, pos)
    glEnable(GL_CULL_FACE)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)

    # make the gears
    gear1 = glGenLists(1)
    glNewList(gear1, GL_COMPILE)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red)
    gear(1.0, 4.0, 1.0, 20, 0.7)
    glEndList()
    
    gear2 = glGenLists(1)
    glNewList(gear2, GL_COMPILE)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, green)
    gear(0.5, 2.0, 2.0, 10, 0.7)
    glEndList()

    gear3 = glGenLists(1)
    glNewList(gear3, GL_COMPILE)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, blue)
    gear(1.3, 2.0, 0.5, 10, 0.7)
    glEndList()

    glEnable(GL_NORMALIZE)

def visible(vis):
    if vis == GLUT_VISIBLE:
        glutIdleFunc(idle)
    else:
        glutIdleFunc(None)


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

    glutInitWindowPosition(0, 0)
    glutInitWindowSize(300, 300)
    glutCreateWindow("pyGears")
    init()
    
    glutDisplayFunc(draw)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(key)
    glutSpecialFunc(special)
    glutVisibilityFunc(visible)

    if "-info" in sys.argv:
        print "GL_RENDERER   = ", glGetString(GL_RENDERER)
        print "GL_VERSION    = ", glGetString(GL_VERSION)
        print "GL_VENDOR     = ", glGetString(GL_VENDOR)
        print "GL_EXTENSIONS = ", glGetString(GL_EXTENSIONS)

    glutMainLoop()
    
