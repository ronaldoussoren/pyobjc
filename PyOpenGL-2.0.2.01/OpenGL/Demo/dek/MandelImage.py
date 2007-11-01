#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

## This isn't really a PyOpenGL demo, but it's a nice
## example of how Numeric, Tkinter, and PIL can be used 
## together to create all sorts of images.
## In this case, it's the Mandelbrot set.
## i used the Numerical python text example, but modified it to
## work with PIL

try:
		import Numeric
except:
		print "This demo requires the Numeric extension, sorry."
		import sys
		sys.exit()
import FFT
import Tkinter
import Image
import ImageTk
import sys

w = 256
h = 256

class Test:
	def draw(self,LowX, HighX, LowY, HighY, maxiter=30):
		xx=Numeric.arange(LowX,HighX,(HighX-LowX)/w*2)
		yy=Numeric.arange(HighY,LowY,(LowY-HighY)/h*2)*1j
		c=Numeric.ravel(xx+yy[:,Numeric.NewAxis])
		z=Numeric.zeros(c.shape,Numeric.Complex)
		output=Numeric.resize(Numeric.array(0,),c.shape)

		for iter in range(maxiter):
			print "iter",iter
			z=z*z+c
			finished=Numeric.greater(abs(z),2.0)
			c=Numeric.where(finished,0+0j,c)
			z=Numeric.where(finished,0+0j,z)
			output=Numeric.where(finished,iter,output)

		## scale output a bit to make it brighter
##      output * output * 1000
		output = (output + (256*output) + (256**2)*output)*8
		self.mandel = output.tostring()#"raw", "RGBX", 0, -1)
		print len(self.mandel)

	def createImage(self):
		self.im = Image.new("RGB", (w/2,h/2))
		self.draw(-2.1, 0.7, -1.2, 1.2)
		print len(self.im.tostring("raw", "RGBX", 0, -1))
		self.im.fromstring(self.mandel, "raw", "RGBX", 0, -1)

	def createLabel(self):
		self.image = ImageTk.PhotoImage(self.im)
		self.label = Tkinter.Label(self.root, image=self.image)
		self.label.pack()
		
		
	def __init__(self):
		self.root = Tkinter.Tk()
		self.i = 0
		self.createImage()
		self.createLabel()
		self.root.mainloop()

demo = Test

if __name__ == '__main__':
	demo()

