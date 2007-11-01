#	A quick and simple opengl font library that uses GNU freetype2, written
#	and distributed as part of a tutorial for nehe.gamedev.net.
#	Sven Olsen, 2003
#	Translated to PyOpenGL by Brian Leair, 2004
# 
#



# import freetype
# We are going to use Python Image Library's font handling
# From PIL 1.1.4:
import ImageFont
from OpenGL.GL import *
from OpenGL.GLU import *


# Python 2.2 defines these directly
try:
	True
except NameError:
	True = 1==1
	False = 1==0


def is_font_available (ft, facename):
	""" Returns true if FreeType can find the requested face name 
		Pass the basname of the font e.g. "arial" or "times new roman"
	"""
	if (facename in ft.available_fonts ()):
		return True
	return False


def next_p2 (num):
	""" If num isn't a power of 2, will return the next higher power of two """
	rval = 1
	while (rval<num):
		rval <<= 1
	return rval



def make_dlist (ft, ch, list_base, tex_base_list):
	""" Given an integer char code, build a GL texture into texture_array,
		build a GL display list for display list number display_list_base + ch.
		Populate the glTexture for the integer ch and construct a display
		list that renders the texture for ch.
		Note, that display_list_base and texture_base are supposed
		to be preallocated for 128 consecutive display lists and and 
		array of textures.
	"""

	# //The first thing we do is get FreeType to render our character
	# //into a bitmap.  This actually requires a couple of FreeType commands:
	# //Load the Glyph for our character.
	# //Move the face's glyph into a Glyph object.
	# //Convert the glyph to a bitmap.
	# //This reference will make accessing the bitmap easier
	# - This is the 2 dimensional Numeric array

	# Use our helper function to get the widths of
	# the bitmap data that we will need in order to create
	# our texture.
	glyph = ft.getmask (chr (ch))
	glyph_width, glyph_height = glyph.size 
	# We are using PIL's wrapping for FreeType. As a result, we don't have 
	# direct access to glyph.advance or other attributes, so we add a 1 pixel pad.
	width = next_p2 (glyph_width + 1)
	height = next_p2 (glyph_height + 1)


	# python GL will accept lists of integers or strings, but not Numeric arrays
	# so, we buildup a string for our glyph's texture from the Numeric bitmap 

	# Here we fill in the data for the expanded bitmap.
	# Notice that we are using two channel bitmap (one for
	# luminocity and one for alpha), but we assign
	# both luminocity and alpha to the value that we
	# find in the FreeType bitmap. 
	# We use the ?: operator so that value which we use
	# will be 0 if we are in the padding zone, and whatever
	# is the the Freetype bitmap otherwise.
	expanded_data = ""
	for j in xrange (height):
		for i in xrange (width):
			if (i >= glyph_width) or (j >= glyph_height):
				value = chr (0)
				expanded_data += value
				expanded_data += value
			else:
				value = chr (glyph.getpixel ((i, j)))
				expanded_data += value
				expanded_data += value

	# -------------- Build the gl texture ------------

	# Now we just setup some texture paramaters.
	ID = glGenTextures (1)
	tex_base_list [ch] = ID
	glBindTexture (GL_TEXTURE_2D, ID)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

	border = 0
	# Here we actually create the texture itself, notice
	# that we are using GL_LUMINANCE_ALPHA to indicate that
	# we are using 2 channel data.
	glTexImage2D( GL_TEXTURE_2D, 0, GL_RGBA, width, height,
		border, GL_LUMINANCE_ALPHA, GL_UNSIGNED_BYTE, expanded_data )

	# With the texture created, we don't need to expanded data anymore
	expanded_data = None



	# --- Build the gl display list that draws the texture for this character ---

	# So now we can create the display list
	glNewList (list_base + ch, GL_COMPILE)

	if (ch == ord (" ")):
		glyph_advance = glyph_width
		glTranslatef(glyph_advance, 0, 0)
		glEndList()
	else:

		glBindTexture (GL_TEXTURE_2D, ID)

		glPushMatrix()

		# // first we need to move over a little so that
		# // the character has the right amount of space
		# // between it and the one before it.
		# glyph_left = glyph.bbox [0]
		# glTranslatef(glyph_left, 0, 0)

		# // Now we move down a little in the case that the
		# // bitmap extends past the bottom of the line 
		# // this is only true for characters like 'g' or 'y'.
		# glyph_descent = glyph.decent
		# glTranslatef(0, glyph_descent, 0)

		# //Now we need to account for the fact that many of
		# //our textures are filled with empty padding space.
		# //We figure what portion of the texture is used by 
		# //the actual character and store that information in 
		# //the x and y variables, then when we draw the
		# //quad, we will only reference the parts of the texture
		# //that we contain the character itself.
		x=float (glyph_width) / float (width)
		y=float (glyph_height) / float (height)

		# //Here we draw the texturemaped quads.
		# //The bitmap that we got from FreeType was not 
		# //oriented quite like we would like it to be,
		# //so we need to link the texture to the quad
		# //so that the result will be properly aligned.
		glBegin(GL_QUADS)
		glTexCoord2f(0,0), glVertex2f(0,glyph_height)
		glTexCoord2f(0,y), glVertex2f(0,0)
		glTexCoord2f(x,y), glVertex2f(glyph_width,0)
		glTexCoord2f(x,0), glVertex2f(glyph_width, glyph_height)
		glEnd()
		glPopMatrix()

		# Note, PIL's FreeType interface hides the advance from us.
		# Normal PIL clients are rendering an entire string through FreeType, not
		# a single character at a time like we are doing here.
		# Because the advance value is hidden from we will advance
		# the "pen" based upon the rendered glyph's width. This is imperfect.
		glTranslatef(glyph_width + 0.75, 0, 0)

		# //increment the raster position as if we were a bitmap font.
		# //(only needed if you want to calculate text length)
		# //glBitmap(0,0,0,0,face->glyph->advance.x >> 6,0,NULL)

		# //Finnish the display list
		glEndList()

	return

# /// A fairly straight forward function that pushes
# /// a projection matrix that will make object world 
# /// coordinates identical to window coordinates.
def pushScreenCoordinateMatrix():
	glPushAttrib(GL_TRANSFORM_BIT)
	viewport = glGetIntegerv(GL_VIEWPORT)
	glMatrixMode(GL_PROJECTION)
	glPushMatrix()
	glLoadIdentity()
	gluOrtho2D(viewport[0],viewport[2],viewport[1],viewport[3])
	glPopAttrib()
	return


# Pops the projection matrix without changing the current
# MatrixMode.
def pop_projection_matrix():
	glPushAttrib(GL_TRANSFORM_BIT)
	glMatrixMode(GL_PROJECTION)
	glPopMatrix()
	glPopAttrib()
	return


class font_data:
	def __init__ (self, facename, pixel_height):
		# We haven't yet allocated textures or display lists
		self.m_allocated = False
		self.m_font_height = pixel_height
		self.m_facename = facename

		# Try to obtain the FreeType font
		try:
			ft = ImageFont.truetype (facename, pixel_height)
		except:
			raise ValueError, "Unable to locate true type font '%s'" % (facename)

		# Here we ask opengl to allocate resources for
		# all the textures and displays lists which we
		# are about to create.  
		self.m_list_base = glGenLists (128)

		# Consturct a list of 128 elements. This
		# list will be assigned the texture IDs we create for each glyph
		self.textures = [None] * 128

		# This is where we actually create each of the fonts display lists.
		for i in xrange (128):
			make_dlist (ft, i, self.m_list_base, self.textures);

		self.m_allocated = True


		# //We don't need the face information now that the display
		# //lists have been created, so we free the assosiated resources.
		# Note: Don't need this, as python will decref and dealloc the ft for us.
		ft = None
		return

	def glPrint (self, x, y, string):
		"""
		# ///Much like Nehe's glPrint function, but modified to work
		# ///with freetype fonts.
		"""
		# We want a coordinate system where things coresponding to window pixels.
		pushScreenCoordinateMatrix()
	
		# //We make the height about 1.5* that of
		h = float (self.m_font_height) / 0.63		
	
		# If There's No Text
		# Do Nothing
		if (string == None):
			pop_projection_matrix()
			return
		if (string == ""):
			pop_projection_matrix()
			return

		# //Here is some code to split the text that we have been
		# //given into a set of lines.  
		# //This could be made much neater by using
		# //a regular expression library such as the one avliable from
		# //boost.org (I've only done it out by hand to avoid complicating
		# //this tutorial with unnecessary library dependencies).
		# //Note: python string object has convenience method for this :)
		lines = string.split ("\n")

		glPushAttrib(GL_LIST_BIT | GL_CURRENT_BIT  | GL_ENABLE_BIT | GL_TRANSFORM_BIT)
		glMatrixMode(GL_MODELVIEW)
		glDisable(GL_LIGHTING)
		glEnable(GL_TEXTURE_2D)
		glDisable(GL_DEPTH_TEST)
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

		glListBase(self.m_list_base)
		modelview_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)

		# //This is where the text display actually happens.
		# //For each line of text we reset the modelview matrix
		# //so that the line's text will start in the correct position.
		# //Notice that we need to reset the matrix, rather than just translating
		# //down by h. This is because when each character is
		# //draw it modifies the current matrix so that the next character
		# //will be drawn immediatly after it.  
		for i in xrange (len (lines)):
			line = lines [i]

			glPushMatrix ()
			glLoadIdentity ()
			glTranslatef (x,y-h*i,0);
			glMultMatrixf (modelview_matrix);

			# //  The commented out raster position stuff can be useful if you need to
			# //  know the length of the text that you are creating.
			# //  If you decide to use it make sure to also uncomment the glBitmap command
			# //  in make_dlist().
			# //	glRasterPos2f(0,0);
			glCallLists (line)
			# //	rpos = glGetFloatv (GL_CURRENT_RASTER_POSITION)
			# //	float len=x-rpos[0];
			glPopMatrix()

		glPopAttrib()
		pop_projection_matrix()
		return

	def release (self):
		""" Release the gl resources for this Face.
			(This provides the functionality of KillFont () and font_data::clean ()
		"""
		if (self.m_allocated):
			# Free up the glTextures and the display lists for our face
			glDeleteLists ( self.m_list_base, 128);
			for ID in self.textures:
				glDeleteTextures (ID);
			# Extra defensive. Clients that continue to try and use this object
			# will now trigger exceptions.
			self.list_base = None
			self.m_allocated = False
		return

	def __del__ (self):
		""" Python destructor for when no more refs to this Face object """
		self.release ()
		return


# Unit Test harness if this python module is run directly.
if __name__ == "__main__":
	print "testing availability of freetype font arial\n"
	ft = ImageFont.truetype ("arial.ttf", 15)
	if ft:
		print "Found the TrueType font 'arial.ttf'"
	else:
		print "faild to find the TrueTYpe font 'arial'\n"
