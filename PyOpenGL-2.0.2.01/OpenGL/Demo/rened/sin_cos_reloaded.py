#!/usr/bin/env python

"""
file: sin_cos_reloaded
purpose: doing the orbiting, matrix camera effect.

Press 1,2,3 to change which cube is orbited around.

Uses sin, and cos, with the time as input to those to generate the positions
 of the camera as it orbits around the objects.


"""


import time
import math
from math import cos, sin

import pygame

from pygame.locals import *

import sys, os

from OpenGL.GL import *
from OpenGL.GLU import *

import OpenGL.GLUT



import traceback

pygame.init()

HAS_QUIT = 0


MODEL_POS = (0.5, 0.5, 0.5)
MODEL_POS2 = (1.5, 1.5, 1.5)
MODEL_POS3 = (.5, .0, .0)



class TheApp:

    def __init__(self):


	self.window = 0
	self.xrot =0.
	self.yrot =0.
	self.zrot =0.

	self.frames = 0

	self.ESCAPE = '\033'
	self._debug_level = 1

        self.pos = MODEL_POS






        
    def _debug(self, x, debug_level = 0):
        """
	"""
	if self._debug_level > debug_level:
	    print x



    def Display(self, *args):
        pass

	self._debug("running display", 4)
	glClearColor(1.0, 1.0, 1.0, 0.0);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	#glClear(GL_COLOR_BUFFER_BIT)
	#glClear(GL_DEPTH_BUFFER_BIT)


        # we should be in matrix mode here.
	glLoadIdentity()

        # an extra 5 fps on a gf2 duron 850.
        #   probably lots more on a non t&l card.

	self.ChangeCameraPosition()
	self.DisplayLights()

	self.DisplayModels()

    def get_pos_to_orbit(self):
        return self.pos

    def ChangeCameraPosition(self):
        """ This changes the camera position.  
              Depending on the transform type, it may not update it.
        """
        
        # This is the orbit around the winning avatar.


        glLoadIdentity()

        model_pos = self.get_pos_to_orbit()

        ax,ay,az = model_pos


        rotate_counter = self.total_elapsed_time * 3

        # distance to raise the camera.
        raise_by = 1.0

        bx = 10. * sin(rotate_counter)
        by = 0. + raise_by
        bz = 10. * cos(rotate_counter)

        cx, cy, cz = ax+bx, ay+by, az+bz


        gluLookAt (cx, cy, cz,
                   ax, ay +raise_by, az,
                   0.0, 1.0, 0.0)
        #glRotatef(90, -1.0, 0.,0.)






    def DisplayModels(self):


        self.ChangeCameraPosition()

        #TODO: translate to position of model, and draw.
        mx, my, mz = MODEL_POS
        glColor3f(1.0, 0., 0.)
        glTranslatef(mx, my, mz)
        OpenGL.GLUT.glutSolidCube(1.0)
        glTranslatef(-mx, -my, -mz)

        mx, my, mz = MODEL_POS2
        glColor3f(0.0, 1., 0.)
        glTranslatef(mx, my, mz)
        OpenGL.GLUT.glutSolidCube(1.0)
        glTranslatef(-mx, -my, -mz)

        mx, my, mz = MODEL_POS3
        glColor3f(0.0, 0., 1.)
        glTranslatef(mx, my, mz)
        OpenGL.GLUT.glutSolidCube(1.0)
        glTranslatef(-mx, -my, -mz)

    def DisplayLights(self):
        """
	"""

	# light attributes
	light_ambient  = [ 0.3, 0.3, 0.3, 1.0 ]
	light_diffuse  = [ 0.52, 0.5, 0.5, 1.0 ]
	light_specular = [ 0.1, 0.1, 0.1, 1.0 ]

	# setup the light attributes
	glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
	glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

	# set the light position
	lightPosition = [ 0.0, -1.0, 1.0, 1.0 ]
	glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)



    def Init(self):
        pass


    def InitDisplay(self, height, width):
	global HAS_QUIT
        self._debug("initializing display")

        if not HAS_QUIT:
	    pygame.quit()
	pygame.init()

	HAS_QUIT = 0
	
        #display_flags = DOUBLEBUF | OPENGL | FULLSCREEN
        display_flags = DOUBLEBUF | OPENGL 

	if pygame.display.mode_ok((width, height), display_flags ):
	    self.screen = pygame.display.set_mode((width, height), display_flags)
	else:
	    raise ValueError("error initializing display, can not get mode")
	
        pygame.display.set_caption("sin and cos reloaded")

    




    def Load(self):
        """ Place to load stuff.  duh!
	"""

	self._debug("loading")
        


    def Stop(self):
        """
	"""
	global HAS_QUIT

	pygame.quit()
	#pygame.display.quit()

	HAS_QUIT = 1




    def Start(self):
        """ """
	self._debug("starting")


	width, height = 640, 480
	#width, height = 1024, 768

	self.width = width
	self.height= height



        self.InitDisplay(height, width)

	self.Load()




    def HandleEvents(self, event_list):

        for event in event_list:
	    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
		self.Stop()
		return 0
	    if event.type == KEYDOWN and event.key == K_1:
                self.pos = MODEL_POS
	    if event.type == KEYDOWN and event.key == K_2:
                self.pos = MODEL_POS2
	    if event.type == KEYDOWN and event.key == K_3:
                self.pos = MODEL_POS3


        return 1


    def SetupProjection(self):
    	# set the projection transformation
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

	#TODO: replace the glu call with something else.
	#gluPerspective(45.0, float(width) / height, scale * 50.0, scale * 1000.0)
	#gluPerspective(45.0, float(self.width) / float(self.height), 5.0, 1000.0)
        self.zNear = 5.0
	self.zFar = 300.0
        self.buffer_calc_a = self.zFar / ( self.zFar - self.zNear )
        self.buffer_calc_b = self.zFar * self.zNear / ( self.zNear - self.zFar )



	gluPerspective(45.0, 
	               float(self.width) / float(self.height), 
		       self.zNear,
		       self.zFar)

	self.gl_projection_matrix = glGetFloatv(GL_PROJECTION_MATRIX)





	# set the model transformation
	glMatrixMode(GL_MODELVIEW)



    def Loop(self):

        # A little bit of stupid optimization.
	#  I wish python could do this automatically.

	pygame_display_flip = pygame.display.flip
	pygame_event_poll= pygame.event.poll
	pygame_event_get = pygame.event.get
	self_HandleEvents = self.HandleEvents

	last_time = time.time()

        # sets up the projection matrix.
	self.SetupProjection()

        self.total_elapsed_time = 0.


	while 1:

	    current_time = time.time()
	    elapsed_time = current_time - last_time
            self.total_elapsed_time += elapsed_time


	    event_list = pygame_event_get()

            if not self_HandleEvents(event_list):
                break

            self.Display()

            pygame_display_flip()

	    self.frames +=1

            # how to handle elapsed time with paused?
	    last_time = current_time








def main():


    a = TheApp()
    t1 = time.time()


    # for testing that the game can be started and stopped 100 times.
    #for x in range(100):
    for x in range(1):
        t1 = time.time()
	a.Start()
        t2 = time.time()
        load_time = t2 - t1

        print "load_time: %s seconds" % load_time

	try:
	    a.Loop()
	except:
	    traceback.print_exc(sys.stderr)
	    print "Cleaning up."
	    a.Stop()

    total_time = time.time() - t1
    print "time:%s frames:%s frames/time:%s" % (total_time, a.frames, a.frames/total_time)







if(__name__ == "__main__"):

    #pygame.key.set_repeat(500, 30)

    if "profile" in sys.argv:
        

        import hotshot
        import hotshot.stats
        import tempfile
        import os

        profile_data_fname= tempfile.mktemp("prf")
        

        try:
            prof = hotshot.Profile(profile_data_fname)
            prof.run('main()')

            del prof

            s = hotshot.stats.load(profile_data_fname)
            print "cumulative\n\n"
            s.sort_stats('cumulative').print_stats()
            print "By time.\n\n"
            s.sort_stats('time').print_stats()

            del s
        finally:
            # clean up the temporary file name.
            os.remove(profile_data_fname)

    else:
	main()
 






