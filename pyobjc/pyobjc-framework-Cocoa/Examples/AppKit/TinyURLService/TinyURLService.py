from Foundation import *
from AppKit import *
from PyObjCTools import AppHelper
import objc
import traceback
import urllib
import urllib2

def serviceSelector(fn):
    # this is the signature of service selectors
    return objc.selector(fn, signature="v@:@@o^@")

def ERROR(s):
    #NSLog(u"ERROR: %s" % (s,))
    return s

NAME = 'TinyURLService-0.0'
TINYURL_API = 'http://tinyurl.com/api-create.php'
def getTinyURL(url):
    data = urllib.urlencode(dict(url=url, source=NAME))
    return urllib2.urlopen(TINYURL_API, data).read().decode('utf-8')

class TinyURLService(NSObject):

    @serviceSelector
    def doTinyURLService_userData_error_(self, pboard, data, error):
        # Mail.app in 10.4.1 doesn't do NSURLPboardType correctly!
        # Probably elsewhere too, so we just use strings.
        try:
            #NSLog(u'doTinyURLService: %r' % (pboard,))
            types = pboard.types()
            url = None

            
            if NSStringPboardType in types:
                #NSLog(u'getting NSStringPboardType')
                urlString = pboard.stringForType_(NSStringPboardType)
                #NSLog(u'NSStringPboardType: %r' % (urlString,))
                url = NSURL.URLWithString_(urlString.strip())
                if url is None:
                    #NSLog(u'urlString was %r' % (urlString,))
                    return ERROR(NSLocalizedString(
                        "Error: Given URL was not well-formed.",
                        "Given URL not well-formed."
                    ))

            if url is None:
                return ERROR(NSLocalizedString(
                        "Error: Pasteboard doesn't contain a valid URL.",
                        "Pasteboard doesn't contain a valid URL.",
                    ))


            urlString = url.absoluteString()
            #NSLog(u'urlString = %r' % (urlString,))
            
            res = getTinyURL(urlString.UTF8String())

            #NSLog(u'res = %r' % (res,))
            resURL = NSURL.URLWithString_(res)
            #NSLog(u'resURL = %r' % (resURL,))
            if resURL is None:
                NSLog(u'res was %r' % (res,))
                return ERROR(NSLocalizedString(
                    "Error: Resultant URL was not well-formed.",
                    "Resultant URL not well-formed."
                ))
            pboard.declareTypes_owner_([NSStringPboardType], None)
            pboard.setString_forType_(resURL.absoluteString(), NSStringPboardType)
            return ERROR(None)
        except:
            traceback.print_exc()
            return ERROR(u'Exception, see traceback')


def main():
    serviceProvider = TinyURLService.alloc().init()
    NSRegisterServicesProvider(serviceProvider, u'TinyURLService')
    AppHelper.runConsoleEventLoop()

if __name__ == '__main__':
    main()
