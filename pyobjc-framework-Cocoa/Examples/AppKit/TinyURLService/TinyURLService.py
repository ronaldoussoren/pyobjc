import traceback
import urllib
import urllib2

import Cocoa
import objc
from PyObjCTools import AppHelper


def serviceSelector(fn):
    # this is the signature of service selectors
    return objc.selector(fn, signature=b"v@:@@o^@")


def ERROR(s):
    # NSLog("ERROR: %s", s)
    return s


NAME = "TinyURLService-0.0"
TINYURL_API = "http://tinyurl.com/api-create.php"


def getTinyURL(url):
    data = urllib.urlencode({"url": url, "source": NAME})
    return urllib2.urlopen(TINYURL_API, data).read().decode("utf-8")


class TinyURLService(Cocoa.NSObject):
    @serviceSelector
    def doTinyURLService_userData_error_(self, pboard, data, error):
        # Mail.app in 10.4.1 doesn't do NSURLPboardType correctly!
        # Probably elsewhere too, so we just use strings.
        try:
            types = pboard.types()
            url = None

            if Cocoa.NSStringPboardType in types:
                urlString = pboard.stringForType_(Cocoa.NSStringPboardType)
                url = Cocoa.NSURL.URLWithString_(urlString.strip())
                if url is None:
                    return ERROR(
                        Cocoa.NSLocalizedString(
                            "Error: Given URL was not well-formed.",
                            "Given URL not well-formed.",
                        )
                    )

            if url is None:
                return ERROR(
                    Cocoa.NSLocalizedString(
                        "Error: Pasteboard doesn't contain a valid URL.",
                        "Pasteboard doesn't contain a valid URL.",
                    )
                )

            urlString = url.absoluteString()

            res = getTinyURL(urlString.UTF8String())

            resURL = Cocoa.NSURL.URLWithString_(res)
            if resURL is None:
                return ERROR(
                    Cocoa.NSLocalizedString(
                        "Error: Resultant URL was not well-formed.",
                        "Resultant URL not well-formed.",
                    )
                )
            pboard.declareTypes_owner_([Cocoa.NSStringPboardType], None)
            pboard.setString_forType_(resURL.absoluteString(), Cocoa.NSStringPboardType)
            return ERROR(None)
        except:  # noqa: E722, B001
            traceback.print_exc()
            return ERROR("Exception, see traceback")


def main():
    serviceProvider = TinyURLService.alloc().init()
    Cocoa.NSRegisterServicesProvider(serviceProvider, "TinyURLService")
    AppHelper.runConsoleEventLoop()


if __name__ == "__main__":
    main()
