from Foundation import *
import objc


class MyObject (NSObject):

	def encodeWithCoder_(self, coder):
		#super(MyObject, self).encodeWithCoder_(coder)
		#coder.encodeFloat_(2.3)
		coder.encodeValueOfObjCType_at_(objc._objc._C_INT, 2)
	

print 1
data = NSMutableData.data()
print 2
archiver = NSArchiver.alloc()
print 3
archiver = archiver.initForWritingWithMutableData_(data)
print 4
archiver.encodeObject_(MyObject.alloc().init())
print 5
result = data.writeToFile_atomically_("archive.bin", True)
print 6

del archiver
