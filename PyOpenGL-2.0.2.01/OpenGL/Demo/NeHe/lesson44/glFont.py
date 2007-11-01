# glFont.py -- SImple font class that uses a single texture represent 16x16 tiles
# for a font.
# // Code writen by: Vic Hollis 09/07/2003
# // I don't mind if you use this class in your own code. All I ask is 
# // that you give me and Giuseppe D'Agata credit for it if you do.  
# // And plug NeHe while your at it! :P  Thanks go to Giuseppe D'Agata
# // for the code that this class is based off of. Thanks Enjoy.
# //////////////////////////////////////////////////////////////////////
# // glFont.cpp: implementation of the glFont class.
# //////////////////////////////////////////////////////////////////////

from OpenGL.GL import *

class glFont:
	def __init__ (self):
		self.m_FontTexture = 0
		self.m_ListBase = 0

	def __del__ (self):
		self.release ()
		return

	def release (self):
		""" We've made a separate resoruce-deallocation method
			so that the client can return system resources when the
			want to explcitly. Python will eventually garbage collect,
			once all refs to the object go away. This method
			allows the client to retain the object, and yet free up the
			gl resources. 
		"""
		if (self.m_FontTexture != 0):
			glDeleteTextures (self.m_FontTexture)
		if (self.m_ListBase != 0):
			glDeleteLists (self.m_ListBase, 256)
		return

	def SetFontTexture (self, tex):
		if (tex != 0):												# // If the texture is valid
			self.m_FontTexture = tex;								# // Set the font texture
		else:
			# Client should not pass an invalid texture.
			raise RuntimeError, "SetFontTexture passed invalid texture (ID == 0)"
		return

	def BuildFont (self, Scale):
		self.m_ListBase=glGenLists(256);							# // Creating 256 Display Lists
		if (self.m_FontTexture != 0):
			glBindTexture(GL_TEXTURE_2D, self.m_FontTexture);		# // Select Our Font Texture
			for loop in xrange (256):							 	# // Loop Through All 256 Lists
				cx=float(loop%16)/16.0;								# // X Position Of Current Character
				cy=float(loop/16)/16.0;								# // Y Position Of Current Character

				glNewList(self.m_ListBase+loop,GL_COMPILE);			# // Start Building A List
				# List start
				glBegin(GL_QUADS);									# // Use A Quad For Each Character
				glTexCoord2f(cx, 1 - cy - 0.0625);					# // Texture Coord (Bottom Left)
				glVertex2f(0,0);									# // Vertex Coord (Bottom Left)
				glTexCoord2f(cx + 0.0625, 1 - cy - 0.0625);			# // Texture Coord (Bottom Right)
				glVertex2f(16 * Scale,0);							# // Vertex Coord (Bottom Right)
				glTexCoord2f(cx + 0.0625, 1 - cy);					# // Texture Coord (Top Right)
				glVertex2f(16 * Scale, 16 * Scale);					# // Vertex Coord (Top Right)
				glTexCoord2f(cx, 1 - cy);							# // Texture Coord (Top Left)
				glVertex2f(0, 16 * Scale);							# // Vertex Coord (Top Left)
				glEnd();											# // Done Building Our Quad (Character)
				glTranslated(10*Scale,0,0);							# // Move To The Right Of The Character
				glEndList();										# // Done Building The Display List
				# List end

	def glPrintf (self, x,y, set, text):
		glEnable(GL_TEXTURE_2D);									# // Enable 2d Textures
		glEnable(GL_BLEND);											# // Enable Blending
		glBlendFunc(GL_SRC_COLOR, GL_ONE_MINUS_SRC_COLOR);
		glBindTexture(GL_TEXTURE_2D, self.m_FontTexture);			# // Select Our Font Texture
		glDisable(GL_DEPTH_TEST);									# // Disables Depth Testing
		glMatrixMode(GL_PROJECTION);								# // Select The Projection Matrix
		glPushMatrix();												# // Store The Projection Matrix
		glLoadIdentity();											# // Reset The Projection Matrix
		glOrtho(0,self.m_WindowWidth,0,self.m_WindowHeight,-1,1);	# // Set Up An Ortho Screen
		glMatrixMode(GL_MODELVIEW);									# // Select The Modelview Matrix
		glPushMatrix();												# // Store The Modelview Matrix
		glLoadIdentity();											# // Reset The Modelview Matrix
		glTranslated(x,y,0);										# // Position The Text (0,0 - Bottom Left)
		glListBase(self.m_ListBase-32+(128*set));					# // Choose The Font Set (0 or 1)
		# glCallLists(len(text),GL_BYTE,text);						# // Write The Text To The Screen
		# function can figure out the count and TYP
		glCallLists(text);											# // Write The Text To The Screen
		glMatrixMode(GL_PROJECTION);								# // Select The Projection Matrix
		glPopMatrix();												# // Restore The Old Projection Matrix
		glMatrixMode(GL_MODELVIEW);									# // Select The Modelview Matrix
		glPopMatrix();												# // Restore The Old Projection Matrix
		glEnable(GL_DEPTH_TEST);
		glDisable(GL_BLEND);
		glDisable(GL_TEXTURE_2D);
		return

	def SetWindowSize (self, width, height):
		self.m_WindowWidth = width
		self.m_WindowHeight = height
		return

	def GetTexture (self):
		return self.m_FontTexture

	def GetListBase (self):
		return self.m_ListBase


