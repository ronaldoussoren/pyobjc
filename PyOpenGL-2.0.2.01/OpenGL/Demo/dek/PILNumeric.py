# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

## This isn't really a PyOpenGL demo, but it's a nice
## example of how Numeric, Tkinter, and PIL can be used 
## together to create all sorts of images.
try:
    import Numeric
except:
    print "This demo requires the Numeric Extension, sorry."
    import sys
    sys.exit()
import FFT
import Tkinter
import Image
import ImageTk
import sys

w = 256
h = 256

    
def demo():
    data = Numeric.arrayrange(w*h)

##    fftdata = FFT.fft(data)
##    fftdata2 = FFT.fft(data2)
##    fftdata3 = (fftdata + fftdata2) / 2.
##    invfftdata = FFT.inverse_fft(fftdata3)
##    data = invfftdata.real
    data = data.astype('l')

    im = Image.new("RGBA", (w, h))
    print len(data.tostring("raw", "RGBX", 0, -1))
    print len(im.tostring("raw", "RGBX", 0, -1))
    im.fromstring(data.tostring("raw", "RGBX", 0, -1),"raw", "RGBX", 0, -1)

    root = Tkinter.Tk()
    image = ImageTk.PhotoImage(im)
    x = Tkinter.Label(root, image=image)
    x.pack()

    root.mainloop()
