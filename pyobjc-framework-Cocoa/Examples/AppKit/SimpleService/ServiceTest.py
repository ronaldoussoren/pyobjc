import objc
from Foundation import *
from AppKit import *
import objc

def serviceSelector(fn):
    # this is the signature of service selectors
    return objc.selector(fn, signature="v@:@@o^@")

def ERROR(s):
    #NSLog(u"ERROR: %s" % (s,))
    return s

class ServiceTest(NSObject):

    @serviceSelector
    def doOpenFileService_userData_error_(self, pboard, data, error):
        #NSLog(u"doOpenFileService_userData_error_(%r, %r)" % (pboard, data,))
        try:
            types = pboard.types()
            pboardString = None
            if NSStringPboardType in types:
                pboardString = pboard.stringForType_(NSStringPboardType)
            if pboardString is None:
                return ERROR(NSLocalizedString(
                    "Error: Pasteboard doesn't contain a string.",
                    "Pasteboard couldn't give string."
                ))

            if not NSWorkspace.sharedWorkspace().openFile_(pboardString):
                return ERROR(NSLocalizedString(
                    "Error: Couldn't open file %s.",
                    "Couldn't perform service operation for file %s."
                ) % pboardString)

            return ERROR(None)
        except:
            import traceback
            traceback.print_exc()
            return ERROR(u'Exception, see traceback')


    @serviceSelector
    def doCapitalizeService_userData_error_(self, pboard, data, err):
        #NSLog(u"doCapitalizeService_userData_error_(%r, %r)" % (pboard, data,))
        try:
            types = pboard.types()
            pboardString = None
            if NSStringPboardType in types:
                pboardString = pboard.stringForType_(NSStringPboardType)
            if pboardString is None:
                return ERROR(NSLocalizedString(
                    "Error: Pasteboard doesn't contain a string.",
                    "Pasteboard couldn't give string."
                ))

            newString = NSString.capitalizedString(pboardString)

            if not newString:
                return ERROR(NSLocalizedString(
                    "Error: Couldn't capitalize string %s.",
                    "Couldn't perform service operation for string %s."
                ) % pboardString)

            types = [NSStringPboardType]
            pboard.declareTypes_owner_([NSStringPboardType], None)
            pboard.setString_forType_(newString, NSStringPboardType)
            return ERROR(None)
        except:
            import traceback
            traceback.print_exc()
            return ERROR(u'Exception, see traceback')
