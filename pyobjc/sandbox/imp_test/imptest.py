#
# XXX - this needs to be made safe...
#
from Foundation import *
import objc
initWithString_relativeToURL_ = NSURL.instanceMethodForSelector_('initWithString:relativeToURL:')
URLWithString_ = NSURL.pyobjc_classMethods.methodForSelector_('URLWithString:')
class NSURL(objc.Category(NSURL)):
    def URLWithString_(cls, URLString):
        print 'URLWithString_'
        return URLWithString_(cls, u'http://slashdot.org')
    URLWithString_ = classmethod(URLWithString_)

    def initWithString_relativeToURL_(self, URLString, baseURL):
        print URLString
        print baseURL
        return initWithString_relativeToURL_(self, u'about:blank', None)

print NSURL.alloc().initWithString_(u'http://slashdot.org')
print NSURL.URLWithString_(u'http://undefined.org')
