# // Code writen by: Vic Hollis 09/07/2003
# // I don't mind if you use this class in your own code. All I ask is 
# // that you give me credit for it if you do.  And plug NeHe while your
# // at it! :P  Thanks go to David Steere, Cameron Tidwell, Bert Sammons,
# // and Brannon Martindale for helping me test all the code!  Enjoy.
# //////////////////////////////////////////////////////////////////////
# // glCamera.h: interface for the glCamera class.
# //////////////////////////////////////////////////////////////////////
# 
# //////////////////////////////////////////////////////////////////////
# // Some minimal additions by rIO.Spinning Kids 
# // For testing flares against occluding objects.
# // Not using proprietary extensions, this is PURE OpenGL1.1
# //
# // Just call the IsOccluded function, passing it the glPoint to check
# //
# //////////////////////////////////////////////////////////////////////
#
# Ported to Python, PyOpenGL by Brian Leair 2004.
# The numarray python module can perform matrix math more effieciently 
# than direct python code. However, for this tutorial the differnce
# in performance isn't huge and it makes for a better tutorial to see
# the math operations directly.

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from glPoint import *
from glVector import *
from math import sqrt, fabs

import Numeric
import copy

class glCamera:
	# //////////// CONSTRUCTORS /////////////////////////////////////////
	def __init__ (self):
		# // Initalize all our member varibles.
		self.m_MaxPitchRate			= 0.0;
		self.m_MaxHeadingRate		= 0.0;
		self.m_HeadingDegrees		= 0.0;
		self.m_PitchDegrees			= 0.0;
		self.m_MaxForwardVelocity	= 0.0;
		self.m_ForwardVelocity		= 0.0;
		self.m_GlowTexture          = None;
		# bleair: NOTE that glCamera.cpp has a bug. m_BigGlowTexture isn't initialized.
		# Very minor bug because only in the case where we fail to get an earlier
		# texture will the class potentially read from the uninited memory. Most of
		# the time the field is assigned to straight away in InitGL ().
		self.m_BigGlowTexture       = None;
		self.m_HaloTexture			= None;
		self.m_StreakTexture		= None;
		self.m_MaxPointSize			= 0.0;
		self.m_Frustum = Numeric.zeros ( (6,4), 'f')

		self.m_LightSourcePos 		= glPoint ()
		self.m_Position = glPoint ()
		self.m_DirectionVector = glVector ()
		self.m_ptIntersect = glPoint ()




	def __del__ (self):
		self.release ()
		return

	def release (self):
		if (self.m_GlowTexture != None):
			glDeleteTextures (self.m_GlowTexture)
		if (self.m_HaloTexture != None):
			glDeleteTextures (self.m_HaloTexture)
		if (self.m_BigGlowTexture != None):
			glDeleteTextures (self.m_BigGlowTexture)
		if (self.m_StreakTexture != None):
			glDeleteTextures (self.m_StreakTexture)
		return

	def ChangePitch (self, degrees):
		if (fabs (degrees) < fabs (self.m_MaxPitchRate)):
			# // Our pitch is less than the max pitch rate that we 
			# // defined so lets increment it.
			self.m_PitchDegrees += degrees;
		else:
			# // Our pitch is greater than the max pitch rate that
			# // we defined so we can only increment our pitch by the 
			# // maximum allowed value.
			if(degrees < 0):
				# // We are pitching down so decrement
				self.m_PitchDegrees -= self.m_MaxPitchRate;
			else:
				# // We are pitching up so increment
				self.m_PitchDegrees += self.m_MaxPitchRate;

		# // We don't want our pitch to run away from us. Although it
		# // really doesn't matter I prefer to have my pitch degrees
		# // within the range of -360.0f to 360.0f
		if (self.m_PitchDegrees > 360.0):
			self.m_PitchDegrees -= 360.0;
		elif (self.m_PitchDegrees < -360.0):
			self.m_PitchDegrees += 360.0;

		return

	def ChangeHeading (self, degrees):
		if(fabs(degrees) < fabs(self.m_MaxHeadingRate)):
			# // Our Heading is less than the max heading rate that we 
			# // defined so lets increment it but first we must check
			# // to see if we are inverted so that our heading will not
			# // become inverted.
			if (self.m_PitchDegrees > 90 and self.m_PitchDegrees < 270 or 
				(self.m_PitchDegrees < -90 and self.m_PitchDegrees > -270)):
				self.m_HeadingDegrees -= degrees;
			else:
				self.m_HeadingDegrees += degrees;
		else:
			# // Our heading is greater than the max heading rate that
			# // we defined so we can only increment our heading by the 
			# // maximum allowed value.
			if(degrees < 0):
				# // Check to see if we are upside down.
				if ((self.m_PitchDegrees > 90 and self.m_PitchDegrees < 270) or
					(self.m_PitchDegrees < -90 and self.m_PitchDegrees > -270)):
					# // Ok we would normally decrement here but since we are upside
					# // down then we need to increment our heading
					self.m_HeadingDegrees += self.m_MaxHeadingRate;
				else:
					# // We are not upside down so decrement as usual
					self.m_HeadingDegrees -= self.m_MaxHeadingRate;
			else:
				# // Check to see if we are upside down.
				if (self.m_PitchDegrees > 90 and self.m_PitchDegrees < 270 or
					(self.m_PitchDegrees < -90 and self.m_PitchDegrees > -270)):
					# // Ok we would normally increment here but since we are upside
					# // down then we need to decrement our heading.
					self.m_HeadingDegrees -= self.m_MaxHeadingRate;
				else:
					# // We are not upside down so increment as usual.
					self.m_HeadingDegrees += self.m_MaxHeadingRate;
	
		# // We don't want our heading to run away from us either. Although it
		# // really doesn't matter I prefer to have my heading degrees
		# // within the range of -360.0f to 360.0f
		if(self.m_HeadingDegrees > 360.0):
			self.m_HeadingDegrees -= 360.0;
		elif(self.m_HeadingDegrees < -360.0):
			self.m_HeadingDegrees += 360.0;

		return

	# //////////// FUNCTIONS TO CHANGE CAMERA ORIENTATION AND SPEED /////
	def ChangeVelocity(self, vel):
		if(fabs(vel) < fabs(self.m_MaxForwardVelocity)):
			# // Our velocity is less than the max velocity increment that we 
			# // defined so lets increment it.
			self.m_ForwardVelocity += vel;
		else:
			# // Our velocity is greater than the max velocity increment that
			# // we defined so we can only increment our velocity by the 
			# // maximum allowed value.
			if(vel < 0):
				# // We are slowing down so decrement
				self.m_ForwardVelocity -= -self.m_MaxForwardVelocity;
			else:
				# // We are speeding up so increment
				self.m_ForwardVelocity += self.m_MaxForwardVelocity;

		return

	def UpdateFrustum(self):
		""" // I found this code here: http://www.markmorley.com/opengl/frustumculling.html
		// and decided to make it part of
		// the camera class just in case I might want to rotate
		// and translate the projection matrix. This code will
		// make sure that the Frustum is updated correctly but
		// this member is computational expensive with:
		// 82 muliplications, 72 additions, 24 divisions, and
		// 12 subtractions for a total of 190 operations. Ouch! """

		# /* Get the current PROJECTION matrix from OpenGL */
		proj = glGetFloatv( GL_PROJECTION_MATRIX);

		# /* Get the current MODELVIEW matrix from OpenGL */
		modl = glGetFloatv( GL_MODELVIEW_MATRIX);

		# /* Combine the two matrices (multiply projection by modelview) */
		# Careful, Note, that replication is simple scalars is OK, but replicate of objects
		# and lists is very bad.
		clip = [None,] * 16
		# clip = Numeric.zeros ( (16), 'f')
		clip[ 0] = modl[ 0] * proj[ 0] + modl[ 1] * proj[ 4] + modl[ 2] * proj[ 8] + modl[ 3] * proj[12];
		clip[ 1] = modl[ 0] * proj[ 1] + modl[ 1] * proj[ 5] + modl[ 2] * proj[ 9] + modl[ 3] * proj[13];
		clip[ 2] = modl[ 0] * proj[ 2] + modl[ 1] * proj[ 6] + modl[ 2] * proj[10] + modl[ 3] * proj[14];
		clip[ 3] = modl[ 0] * proj[ 3] + modl[ 1] * proj[ 7] + modl[ 2] * proj[11] + modl[ 3] * proj[15];

		clip[ 4] = modl[ 4] * proj[ 0] + modl[ 5] * proj[ 4] + modl[ 6] * proj[ 8] + modl[ 7] * proj[12];
		clip[ 5] = modl[ 4] * proj[ 1] + modl[ 5] * proj[ 5] + modl[ 6] * proj[ 9] + modl[ 7] * proj[13];
		clip[ 6] = modl[ 4] * proj[ 2] + modl[ 5] * proj[ 6] + modl[ 6] * proj[10] + modl[ 7] * proj[14];
		clip[ 7] = modl[ 4] * proj[ 3] + modl[ 5] * proj[ 7] + modl[ 6] * proj[11] + modl[ 7] * proj[15];

		clip[ 8] = modl[ 8] * proj[ 0] + modl[ 9] * proj[ 4] + modl[10] * proj[ 8] + modl[11] * proj[12];
		clip[ 9] = modl[ 8] * proj[ 1] + modl[ 9] * proj[ 5] + modl[10] * proj[ 9] + modl[11] * proj[13];
		clip[10] = modl[ 8] * proj[ 2] + modl[ 9] * proj[ 6] + modl[10] * proj[10] + modl[11] * proj[14];
		clip[11] = modl[ 8] * proj[ 3] + modl[ 9] * proj[ 7] + modl[10] * proj[11] + modl[11] * proj[15];

		clip[12] = modl[12] * proj[ 0] + modl[13] * proj[ 4] + modl[14] * proj[ 8] + modl[15] * proj[12];
		clip[13] = modl[12] * proj[ 1] + modl[13] * proj[ 5] + modl[14] * proj[ 9] + modl[15] * proj[13];
		clip[14] = modl[12] * proj[ 2] + modl[13] * proj[ 6] + modl[14] * proj[10] + modl[15] * proj[14];
		clip[15] = modl[12] * proj[ 3] + modl[13] * proj[ 7] + modl[14] * proj[11] + modl[15] * proj[15];

		# ### Use a shortened name to reference to our camera's Frustum (does 
		# ### not copy anything, just a ref to make code less wordy
		Frustum = self.m_Frustum

		# /* Extract the numbers for the RIGHT plane */
		Frustum[0][0] = clip[ 3] - clip[ 0];
		Frustum[0][1] = clip[ 7] - clip[ 4];
		Frustum[0][2] = clip[11] - clip[ 8];
		Frustum[0][3] = clip[15] - clip[12];

    	# /* Normalize the result */
		t = (sqrt( Frustum[0][0] * Frustum[0][0] + \
		Frustum[0][1] * Frustum[0][1] + Frustum[0][2] * Frustum[0][2] ));
		Frustum[0][0] /= t;
		Frustum[0][1] /= t;
		Frustum[0][2] /= t;
		Frustum[0][3] /= t;

		# /* Extract the numbers for the LEFT plane */
		Frustum[1][0] = clip[ 3] + clip[ 0];
		Frustum[1][1] = clip[ 7] + clip[ 4];
		Frustum[1][2] = clip[11] + clip[ 8];
		Frustum[1][3] = clip[15] + clip[12];

		# /* Normalize the result */
		t = sqrt( Frustum[1][0] * Frustum[1][0] + Frustum[1][1] * Frustum[1][1] + Frustum[1][2] * Frustum[1][2] );
		Frustum[1][0] /= t;
		Frustum[1][1] /= t;
		Frustum[1][2] /= t;
		Frustum[1][3] /= t;

		# /* Extract the BOTTOM plane */
		Frustum[2][0] = clip[ 3] + clip[ 1];
		Frustum[2][1] = clip[ 7] + clip[ 5];
		Frustum[2][2] = clip[11] + clip[ 9];
		Frustum[2][3] = clip[15] + clip[13];

		# /* Normalize the result */
		t = sqrt( Frustum[2][0] * Frustum[2][0] + Frustum[2][1] * Frustum[2][1] + Frustum[2][2] * Frustum[2][2] );
		Frustum[2][0] /= t;
		Frustum[2][1] /= t;
		Frustum[2][2] /= t;
		Frustum[2][3] /= t;

		# /* Extract the TOP plane */
		Frustum[3][0] = clip[ 3] - clip[ 1];
		Frustum[3][1] = clip[ 7] - clip[ 5];
		Frustum[3][2] = clip[11] - clip[ 9];
		Frustum[3][3] = clip[15] - clip[13];

    	# /* Normalize the result */
		t = sqrt( Frustum[3][0] * Frustum[3][0] + Frustum[3][1] * Frustum[3][1] + Frustum[3][2] * Frustum[3][2] )
		Frustum[3][0] /= t;
		Frustum[3][1] /= t;
		Frustum[3][2] /= t;
		Frustum[3][3] /= t;

 		# /* Extract the FAR plane */
 		Frustum[4][0] = clip[ 3] - clip[ 2];
 		Frustum[4][1] = clip[ 7] - clip[ 6];
 		Frustum[4][2] = clip[11] - clip[10];
		Frustum[4][3] = clip[15] - clip[14];

		# /* Normalize the result */
 		t = sqrt( Frustum[4][0] * Frustum[4][0] + Frustum[4][1] * Frustum[4][1] + Frustum[4][2] * Frustum[4][2] )
 		Frustum[4][0] /= t;
 		Frustum[4][1] /= t;
 		Frustum[4][2] /= t;
 		Frustum[4][3] /= t;

 		# /* Extract the NEAR plane */
 		Frustum[5][0] = clip[ 3] + clip[ 2];
 		Frustum[5][1] = clip[ 7] + clip[ 6];
 		Frustum[5][2] = clip[11] + clip[10];
 		Frustum[5][3] = clip[15] + clip[14];

 		# /* Normalize the result */
 		t = sqrt( Frustum[5][0] * Frustum[5][0] + Frustum[5][1] * Frustum[5][1] + Frustum[5][2] * Frustum[5][2] );
 		Frustum[5][0] /= t;
 		Frustum[5][1] /= t;
 		Frustum[5][2] /= t;
 		Frustum[5][3] /= t;

		return

	# //////////// FUNCTIONS TO UPDATE THE FRUSTUM //////////////////////
	def UpdateFrustumFaster (self):
		""" // This is the much faster version of the above member 
		// function, however the speed increase is not gained 
		// without a cost. If you rotate or translate the projection
		// matrix then this member will not work correctly. That is acceptable
		// in my book considering I very rarely do such a thing.
		// This function has far fewer operations in it and I 
		// shaved off 2 square root functions by passing in the
		// near and far values. This member has:
		// 38 muliplications, 28 additions, 24 divisions, and
		// 12 subtractions for a total of 102 operations. Still hurts
		// but at least it is decent now. In practice this will 
		// run about 2 times faster than the above function. """

		# /* Get the current PROJECTION matrix from OpenGL */
		proj = glGetFloatv( GL_PROJECTION_MATRIX);
	
		# /* Get the current MODELVIEW matrix from OpenGL */
		modl = glGetFloatv( GL_MODELVIEW_MATRIX);
	
		# /* Combine the two matrices (multiply projection by modelview) 
	   	# but keep in mind this function will only work if you do NOT
	   	# rotate or translate your projection matrix                  */
		clip = [0,] * 16
		modl_row1 = modl [0]
		clip[ 0] = modl [0] [0] * proj[0][0];
		clip[ 1] = modl  [0][ 1] * proj[1][1];
		clip[ 2] = modl [0][ 2] * proj[2][2] + modl_row1[ 3] * proj[3][2]
		clip[ 3] = modl [0][ 2] * proj[2][3]
	
		modl_row2 = modl [1]
		clip[ 4] = modl_row2[ 0] * proj[0][0]
		clip[ 5] = modl_row2[ 1] * proj[1][1]
		clip[ 6] = modl_row2[ 2] * proj[2][2] + modl_row2[ 3] * proj[3][2]
		clip[ 7] = modl_row2[ 2] * proj[2][3]
	
		modl_row3 = modl [2]
		clip[ 8] = modl_row3[ 0] * proj[0][0];
		clip[ 9] = modl_row3[ 1] * proj[1][1]
		clip[10] = modl_row3[2] * proj[2][2] + modl_row3[3] * proj[3][2]
		clip[11] = modl_row3[2] * proj[2][3]
	
		modl_row4 = modl [3]
		clip[12] = modl_row4[0] * proj[0][0]
		clip[13] = modl_row4[1] * proj[1][1]
		clip[14] = modl_row4[2] * proj[2][2] + modl_row4[3] * proj[3][2]
		clip[15] = modl_row4[2] * proj[2][3]
	
		# ### Use a shortened name to reference to our camera's Frustum (does 
		# ### not copy anything, just a ref to make code less wordy
		Frustum = self.m_Frustum

		# /* Extract the numbers for the RIGHT plane */
		Frustum[0][0] = clip[ 3] - clip[ 0];
		Frustum[0][1] = clip[ 7] - clip[ 4];
		Frustum[0][2] = clip[11] - clip[ 8];
		Frustum[0][3] = clip[15] - clip[12];
	
		# /* Normalize the result */
		t = sqrt( (Frustum[0][0] * Frustum[0][0]) + (Frustum[0][1] * Frustum[0][1]) + (Frustum[0][2] * Frustum[0][2]) );
		Frustum[0][0] /= t;
		Frustum[0][1] /= t;
		Frustum[0][2] /= t;
		Frustum[0][3] /= t;
	
 		# /* Extract the numbers for the LEFT plane */
 		Frustum[1][0] = clip[ 3] + clip[ 0];
 		Frustum[1][1] = clip[ 7] + clip[ 4];
 		Frustum[1][2] = clip[11] + clip[ 8];
 		Frustum[1][3] = clip[15] + clip[12];
	
    	# /* Normalize the result */
 		t = sqrt( Frustum[1][0] * Frustum[1][0] + Frustum[1][1] * Frustum[1][1] + Frustum[1][2] * Frustum[1][2] );
 		Frustum[1][0] /= t;
 		Frustum[1][1] /= t;
 		Frustum[1][2] /= t;
 		Frustum[1][3] /= t;
	
		# /* Extract the BOTTOM plane */
		Frustum[2][0] = clip[ 3] + clip[ 1];
		Frustum[2][1] = clip[ 7] + clip[ 5];
		Frustum[2][2] = clip[11] + clip[ 9];
		Frustum[2][3] = clip[15] + clip[13];
	
    	# /* Normalize the result */
		t = sqrt( Frustum[2][0] * Frustum[2][0] + Frustum[2][1] * Frustum[2][1] + Frustum[2][2] * Frustum[2][2] );
		Frustum[2][0] /= t;
		Frustum[2][1] /= t;
		Frustum[2][2] /= t;
		Frustum[2][3] /= t;
	
    	# /* Extract the TOP plane */
 		Frustum[3][0] = clip[ 3] - clip[ 1];
 		Frustum[3][1] = clip[ 7] - clip[ 5];
 		Frustum[3][2] = clip[11] - clip[ 9];
 		Frustum[3][3] = clip[15] - clip[13];
	
    	# /* Normalize the result */
 		t = sqrt( Frustum[3][0] * Frustum[3][0] + Frustum[3][1] * Frustum[3][1] + Frustum[3][2] * Frustum[3][2] );
 		Frustum[3][0] /= t;
 		Frustum[3][1] /= t;
 		Frustum[3][2] /= t;
 		Frustum[3][3] /= t;
	
    	# /* Extract the FAR plane */
 		Frustum[4][0] = clip[ 3] - clip[ 2];
 		Frustum[4][1] = clip[ 7] - clip[ 6];
 		Frustum[4][2] = clip[11] - clip[10];
 		Frustum[4][3] = clip[15] - clip[14];
	
    	# /* Normalize the result */
 		t = sqrt( (Frustum[4][0] * Frustum[4][0]) + (Frustum[4][1] * Frustum[4][1]) + (Frustum[4][2] * Frustum[4][2]) );
 		Frustum[4][0] /= t;
 		Frustum[4][1] /= t;
 		Frustum[4][2] /= t;
 		Frustum[4][3] /= t;
	
    	# /* Extract the NEAR plane */
 		Frustum[5][0] = clip[ 3] + clip[ 2];
 		Frustum[5][1] = clip[ 7] + clip[ 6];
 		Frustum[5][2] = clip[11] + clip[10];
 		Frustum[5][3] = clip[15] + clip[14];
	
 		# /* Normalize the result */
 		t = sqrt( Frustum[5][0] * Frustum[5][0] + Frustum[5][1] * Frustum[5][1] + Frustum[5][2] * Frustum[5][2] );
 		Frustum[5][0] /= t;
 		Frustum[5][1] /= t;
 		Frustum[5][2] /= t;
 		Frustum[5][3] /= t;

		return
	
	

	# //////////// FRUSTUM TESTING FUNCTIONS ////////////////////////////
	def SphereInFrustum(self, p, Radius):
		""" // This member function checks to see if a sphere is in
			// the viewing volume.   """

		Frustum = self.m_Frustum
		# // The idea here is the same as the PointInFrustum function.
		if (Radius != 0):
			for i in xrange (6):
			# // If the point is outside of the plane then its not in the viewing volume.
				if(Frustum[i][0] * p.x + Frustum[i][1] * p.y + Frustum[i][2] * p.z + Frustum[i][3] <= -Radius):
					return(False);
		else:
			# // The idea here is the same as the PointInFrustum function.
			for i in xrange (6):
				# // If the point is outside of the plane then its not in the viewing volume.
				if(Frustum[i][0] * p.x + Frustum[i][1] * p.y + Frustum[i][2] * p.z + Frustum[i][3] <= 0):
					return(False);

		return(True);

	def PointInFrustum(self, x,y,z):
		""" // This member fuction checks to see if a point is in
			// the viewing volume. """

		# // The idea behind this algorithum is that if the point
		# // is inside all 6 clipping planes then it is inside our
		# // viewing volume so we can return true.

		Frustum = self.m_Frustum
		# // Loop through all our clipping planes
		for i in xrange (6):
			# // If the point is outside of the plane then its not in the viewing volume.
			if(Frustum[i][0] * x + Frustum[i][1] * y + Frustum[i][2] * z + Frustum[i][3] <= 0):
				return(False);

		return(True);

	# /////////// OCCLUSION TESTING FUNCTIONS ///////////////////////////
	def IsOccluded (self, p):
		# // Now we will ask OGL to project some geometry for us using the gluProject function.
		# // Practically we ask OGL to guess where a point in space will be projected in our current viewport,
		# // using arbitrary viewport and transform matrices we pass to the function.
		# // If we pass to the function the current matrices  (retrievede with the glGet funcs)
		# // we will have the real position on screen where the dot will be drawn.
		# // The interesting part is that we also get a Z value back, this means that 
		# // reading the REAL buffer for Z values we can discover if the flare is in front or
		# // if it's occluded by some objects.
		# ### This function should be a flat function, not a function of the camera as we
		# ### use the immediate GL rendering state entirely.


		# ### Viewport is the rectangle of window pixels that OpenGL is rasterizing into.
		viewport = glGetIntegerv (GL_VIEWPORT);						# //get actual viewport
  		mvmatrix = glGetDoublev (GL_MODELVIEW_MATRIX);				# //get actual model view matrix
  		projmatrix = glGetDoublev (GL_PROJECTION_MATRIX);			# //get actual projiection matrix

		# // this asks OGL to guess the 2d position of a 3d point inside the viewport
		winx, winy, winz = gluProject(p.x, p.y, p.z, mvmatrix, projmatrix, viewport)
		flareZ = winz;

		# // we read back one pixel from th depth buffer (exactly where our flare should be drawn)
		glPixelStorei(GL_PACK_ALIGNMENT, 1)

		# PyOpenGL 2.0.1.07 bug, Only the type clarified function works.
		# bufferZ = glReadPixels(int(winx), int(winy),1,1,GL_DEPTH_COMPONENT, GL_FLOAT)
		bufferZ = glReadPixelsf(int(winx), int(winy),1,1,GL_DEPTH_COMPONENT)

		# // if the buffer Z is lower than our flare guessed Z then don't draw 
		# // this means there is something in front of our flare
		if (bufferZ [0] [0] < flareZ):
			return True;
		else:
			return False;

	# //////////// FUNCTIONS TO RENDER LENS FLARES //////////////////////
	def RenderLensFlare(self):
		# // Draw the flare only If the light source is in our line of sight (inside the Frustum)
		if (self.SphereInFrustum(self.m_LightSourcePos, 1.0) == True):

			# Vector pointing from the light's position toward the camera's position (the camera might
			# be pointing elsewhere, this vector is pointing from the light to the camera)
			self.vLightSourceToCamera = self.m_Position - self.m_LightSourcePos;		# // Lets compute the vector that points to the camera from
																						# // the light source.

			Length = self.vLightSourceToCamera.Magnitude () 						# // Save the length we will need it in a minute

			# Move down our look-toward direction vector. Move down the look-toward the same dist. as the
			# distance between camera and the light.
			intersect = self.m_DirectionVector * Length
			self.m_ptIntersect = glPoint (intersect.i, intersect.j, intersect.k)
																		# // Now lets find an point along the cameras direction
																		# // vector that we can use as an intersection point. 
																		# // Lets translate down this vector the same distance
																		# // that the camera is away from the light source.
			ptIntersect = self.m_ptIntersect
			# Did the motion in the correct direction above, now translate the intersection position 
			# relative to our camera location.
			ptIntersect += self.m_Position;


			self.vLightSourceToIntersect = ptIntersect - self.m_LightSourcePos;		# // Lets compute the vector that points to the Intersect
																	# // point from the light source
					
			Length = self.vLightSourceToIntersect.Magnitude();		# // Save the length we will need it later.
			self.vLightSourceToIntersect.Normalize();				# // Normalize the vector so its unit length
			vLightSourceToIntersect = self.vLightSourceToIntersect
		
			glEnable(GL_BLEND);										# // You should already know what this does
			glBlendFunc(GL_SRC_ALPHA, GL_ONE);						# // You should already know what this does
			glDisable(GL_DEPTH_TEST);								# // You should already know what this does
			glEnable(GL_TEXTURE_2D);								# // You should already know what this does
			
			# /////////// Differenet Color Glows & Streaks /////////////////////
			# //RenderBigGlow(1.0f, 1.0f, 1.0f, 1.0f, m_LightSourcePos, 1.0f);
			# //RenderStreaks(1.0f, 1.0f, 0.8f, 1.0f, m_LightSourcePos, 0.7f);
			# //
			# //RenderBigGlow(1.0f, 0.9f, 1.0f, 1.0f, m_LightSourcePos, 1.0f);
			# //RenderStreaks(1.0f, 0.9f, 1.0f, 1.0f, m_LightSourcePos, 0.7f);
			# //////////////////////////////////////////////////////////////////


			# //########################## NEW STUFF ##################################

			if (not self.IsOccluded(self.m_LightSourcePos)):		#	//Check if the center of the flare is occluded
				# // Render the large hazy glow
				self.RenderBigGlow(0.60, 0.60, 0.8, 1.0, self.m_LightSourcePos, 16.0);
				# // Render the streaks
				self.RenderStreaks(0.60, 0.60, 0.8, 1.0, self.m_LightSourcePos, 16.0);
				# // Render the small Glow
				self.RenderGlow(0.8, 0.8, 1.0, 0.5, self.m_LightSourcePos, 3.5);

				pt = glPoint (vLightSourceToIntersect * (Length * 0.1));	# // Lets compute a point that is 20%
				pt += self.m_LightSourcePos;								# // away from the light source in the
																			# // direction of the intersection point.
		
				self.RenderGlow(0.9, 0.6, 0.4, 0.5, pt, 0.6);					# // Render the small Glow

				pt = glPoint (vLightSourceToIntersect * (Length * 0.15));	# // Lets compute a point that is 30%
				pt += self.m_LightSourcePos;								# // away from the light source in the
																			# // direction of the intersection point.		
		
				self.RenderHalo(0.8, 0.5, 0.6, 0.5, pt, 1.7);					# // Render the a Halo
		
				pt = glPoint (vLightSourceToIntersect * (Length * 0.175));			# // Lets compute a point that is 35%
				pt += self.m_LightSourcePos;								# // away from the light source in the
																			# // direction of the intersection point.		
		
				self.RenderHalo(0.9, 0.2, 0.1, 0.5, pt, 0.83);					# // Render the a Halo

				pt = glPoint (vLightSourceToIntersect * (Length * 0.285));			# // Lets compute a point that is 57%
				pt += self.m_LightSourcePos;								# // away from the light source in the
																			# // direction of the intersection point.		
		
				self.RenderHalo(0.7, 0.7, 0.4, 0.5, pt, 1.6);					# // Render the a Halo
		
				pt = glPoint (vLightSourceToIntersect * (Length * 0.2755));			# // Lets compute a point that is 55.1%
				pt += self.m_LightSourcePos;								# // away from the light source in the
																			# // direction of the intersection point.		
		
				self.RenderGlow(0.9, 0.9, 0.2, 0.5, pt, 0.8);					# // Render the small Glow

				pt = glPoint (vLightSourceToIntersect * (Length * 0.4775));			# // Lets compute a point that is 95.5%
				pt += self.m_LightSourcePos;								# // away from the light source in the
																			# // direction of the intersection point.		
		
				self.RenderGlow(0.93, 0.82, 0.73, 0.5, pt, 1.0);					# // Render the small Glow
		
				pt = glPoint (vLightSourceToIntersect * (Length * 0.49));				# // Lets compute a point that is 98%
				pt += self.m_LightSourcePos;								# // away from the light source in the
																			# // direction of the intersection point.		
		
				self.RenderHalo(0.7, 0.6, 0.5, 0.5, pt, 1.4);					# // Render the a Halo

				pt = glPoint (vLightSourceToIntersect * (Length * 0.65));				# // Lets compute a point that is 130%
				pt += self.m_LightSourcePos;								# // away from the light source in the
																			# // direction of the intersection point.		
		
				self.RenderGlow(0.7, 0.8, 0.3, 0.5, pt, 1.8);					# // Render the small Glow
		
				pt = glPoint (vLightSourceToIntersect * (Length * 0.63));				# // Lets compute a point that is 126%
				pt += self.m_LightSourcePos;								# // away from the light source in the
																			# // direction of the intersection point.		
		
				self.RenderGlow(0.4, 0.3, 0.2, 0.5, pt, 1.4);					# // Render the small Glow

				pt = glPoint (vLightSourceToIntersect * (Length * 0.8));				# // Lets compute a point that is 160%
				pt += self.m_LightSourcePos;								# // away from the light source in the
																			# // direction of the intersection point.		
		
				self.RenderHalo(0.7, 0.5, 0.5, 0.5, pt, 1.4);					# // Render the a Halo
		
				pt = glPoint (vLightSourceToIntersect * (Length * 0.7825));			# // Lets compute a point that is 156.5%
				pt += self.m_LightSourcePos;								# // away from the light source in the
																			# // direction of the intersection point.

				self.RenderGlow(0.8, 0.5, 0.1, 0.5, pt, 0.6);					# // Render the small Glow

				pt = glPoint (vLightSourceToIntersect * (Length * 1.0));				# // Lets compute a point that is 200%
				pt += self.m_LightSourcePos;								# // away from the light source in the
																			# // direction of the intersection point.		
		
				self.RenderHalo(0.5, 0.5, 0.7, 0.5, pt, 1.7);					# // Render the a Halo
		
				pt = glPoint (vLightSourceToIntersect * (Length * 0.975));			# // Lets compute a point that is 195%
				pt += self.m_LightSourcePos;								# // away from the light source in the
																			# // direction of the intersection point.		
		
				self.RenderGlow(0.4, 0.1, 0.9, 0.5, pt, 2.0);					# // Render the small Glow

			glDisable(GL_BLEND );											# // You should already know what this does
			glEnable(GL_DEPTH_TEST);										# // You should already know what this does
			glDisable(GL_TEXTURE_2D);										# // You should already know what this does
		return

	def RenderHalo (self, r, g, b, a, p, scale):
		self.RenderFlareTexture (self.m_HaloTexture, r, g, b, a, p, scale)
		return

	def RenderGlow (self, r, g, b, a, p, scale):
		self.RenderFlareTexture (self.m_GlowTexture, r, g, b, a, p, scale)
		return

	def RenderBigGlow (self, r, g, b, a, p, scale):
		self.RenderFlareTexture (self.m_BigGlowTexture, r, g, b, a, p, scale)
		return

	def RenderStreaks (self, r, g, b, a, p, scale):
		self.RenderFlareTexture (self.m_StreakTexture, r, g, b, a, p, scale)
		return

	def RenderFlareTexture (self, tex_ID, r, g, b, a, p, scale):
		# bleair: Duplicate functions all the same except for the texture to bind to.

		q = []
		q.append (glPoint ())
		q.append (glPoint ())
		q.append (glPoint ())
		q.append (glPoint ())
		# // Basically we are just going to make a 2D box
		# // from four points we don't need a z coord because
		# // we are rotating the camera by the inverse so the 
		# // texture mapped quads will always face us.

		q[0].x = (p.x - scale);											# // Set the x coordinate -scale units from the center point.
		q[0].y = (p.y - scale);											# // Set the y coordinate -scale units from the center point.
		
		q[1].x = (p.x - scale);											# // Set the x coordinate -scale units from the center point.
		q[1].y = (p.y + scale);											# // Set the y coordinate scale units from the center point.
		
		q[2].x = (p.x + scale);											# // Set the x coordinate scale units from the center point.
		q[2].y = (p.y - scale);											# // Set the y coordinate -scale units from the center point.
		
		q[3].x = (p.x + scale);											# // Set the x coordinate scale units from the center point.
		q[3].y = (p.y + scale);											# // Set the y coordinate scale units from the center point.
		
		glPushMatrix();													# // Save the model view matrix
		glTranslatef(p.x, p.y, p.z);									# // Translate to our point
		glRotatef(-self.m_HeadingDegrees, 0.0, 1.0, 0.0);
		glRotatef(-self.m_PitchDegrees, 1.0, 0.0, 0.0);
		glBindTexture(GL_TEXTURE_2D, tex_ID);							# // Bind to the Big Glow texture
		glColor4f(r, g, b, a);											# // Set the color since the texture is a gray scale
	
		glBegin(GL_TRIANGLE_STRIP);										# // Draw the Big Glow on a Triangle Strip
		glTexCoord2f(0.0, 0.0);					
		glVertex2f(q[0].x, q[0].y);
		glTexCoord2f(0.0, 1.0);
		glVertex2f(q[1].x, q[1].y);
		glTexCoord2f(1.0, 0.0);
		glVertex2f(q[2].x, q[2].y);
		glTexCoord2f(1.0, 1.0);
		glVertex2f(q[3].x, q[3].y);
		glEnd();										
		glPopMatrix();													# // Restore the model view matrix
		return




	def SetPrespective (self):
		# Matrix = [0] * 16 					# // A (list) array to hold the model view matrix.

		# However the MODELVIEW was oriented, we now rotate it based upon our Camer object's state.
		# // Going to use glRotate to calculate our direction vector
		glRotatef(self.m_HeadingDegrees, 0.0, 1.0, 0.0);		# turn your head left/right (around y axe)
		glRotatef(self.m_PitchDegrees, 1.0, 0.0, 0.0);			# nod your head up/down (around x axe)

		# // Get the resulting matrix from OpenGL it will have our
		# // direction vector in the 3rd row.
		Matrix = glGetFloatv(GL_MODELVIEW_MATRIX);

		# // Get the direction vector from the matrix. Element 10 must
		# // be inverted!
		self.m_DirectionVector.i = Matrix[2] [0]	#[8];
		self.m_DirectionVector.j = Matrix[2] [1]	#[9];
		self.m_DirectionVector.k = -Matrix[2] [2] 	#[10];

		# #### bleair: no need to do this as this. Previous rotates already here (because
		# #### all invocations have the modelview at identity.
		# #### Suspect this was just a bit of code that was mvoed up and not deleted here.
		# // Ok erase the results of the last computation.
		glLoadIdentity();

		# // Rotate the scene to get the right orientation.
		glRotatef(self.m_PitchDegrees, 1.0, 0.0, 0.0);
		glRotatef(self.m_HeadingDegrees, 0.0, 1.0, 0.0);

		# // A vector to hold our cameras direction * the forward velocity
		# // we don't want to destory the Direction vector by using it instead.
		# // Scale the direction by our speed.
		v = copy.copy (self.m_DirectionVector);
		v *= self.m_ForwardVelocity;

		# // Increment our position by the vector
		self.m_Position.x += v.i;
		self.m_Position.y += v.j;
		self.m_Position.z += v.k;

		# // Translate to our new position.
		glTranslatef(-self.m_Position.x, -self.m_Position.y, -self.m_Position.z);
		return
		

"""
	//////////// MEMBER VARIBLES //////////////////////////////////////
	glVector vLightSourceToCamera, vLightSourceToIntersect;
	glPoint ptIntersect, pt;
	GLsizei m_WindowHeight;
	GLsizei m_WindowWidth;
	GLuint m_StreakTexture;
	GLuint m_HaloTexture;
	GLuint m_GlowTexture;
	GLuint m_BigGlowTexture;
	GLfloat m_MaxPointSize;
	GLfloat m_Frustum[6][4];
	glPoint m_LightSourcePos;
	GLfloat m_MaxPitchRate;
	GLfloat m_MaxHeadingRate;
	GLfloat m_HeadingDegrees;
	GLfloat m_PitchDegrees;
	GLfloat m_MaxForwardVelocity;
	GLfloat m_ForwardVelocity;
	glPoint m_Position;
	glVector m_DirectionVector;
"""

