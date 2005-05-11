import os
global x
try:
    x += 1
except NameError:
    x = 0
print x
print __name__
print "hi"
print "INJECTED! pid: %d" % (os.getpid(),)
