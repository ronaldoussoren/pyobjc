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
    def doTinyURLService_userData_error_(self, pboard, data):
        try:
            types = [NSURLPboardType, NSStringPboardType]
            destType = pboard.availableTypeFromArray_(types)
            if destType is None:
                return ERROR(NSLocalizedString(
                        "Error: Pasteboard doesn't contain a string.",
                        "Pasteboard couldn't give string."
                    ))

            if destType == NSStringPboardType:
                urlString = pboard.stringForType_(destType)
                url = NSURL.URLWithString_(urlString.strip())
            else:
                url = NSURL.URLFromPasteboard_(pboard)

            urlString = url.absoluteString()
            
            res = getTinyURL(urlString.UTF8String())

            resURL = NSURL.URLWithString_(res)
            if resURL is None:
                return ERROR(NSLocalizedString(
                    "Error: Resultant URL was not well-formed.",
                    "URL not well-formed."
                ))
            pboard.declareTypes_owner_(types, None)
            resURL.writeToPasteboard_(pboard)
            pboard.setString_forType_(res, NSStringPboardType)
            return ERROR(None)
        except:
            traceback.print_exc()
            return ERROR(u'Exception, see traceback')

    doTinyURLService_userData_error_ = serviceSelector(
       doTinyURLService_userData_error_
    )

def main():
    serviceProvider = TinyURLService.alloc().init()
    NSRegisterServicesProvider(serviceProvider, u'TinyURLService')
    AppHelper.runConsoleEventLoop()

if __name__ == '__main__':
    main()
