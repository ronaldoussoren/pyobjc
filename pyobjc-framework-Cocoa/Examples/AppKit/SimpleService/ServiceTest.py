import Cocoa
import objc

def serviceSelector(fn):
    # this is the signature of service selectors
    return objc.selector(fn, signature=b"v@:@@o^@")

def ERROR(s):
    #NSLog(u"ERROR: %s", s)
    return s

class ServiceTest(Cocoa.NSObject):

    @serviceSelector
    def doOpenFileService_userData_error_(self, pboard, data, error):
        try:
            types = pboard.types()
            pboardString = None
            if Cocoa.NSStringPboardType in types:
                pboardString = pboard.stringForType_(Cocoa.NSStringPboardType)
            if pboardString is None:
                return ERROR(Cocoa.NSLocalizedString(
                    "Error: Pasteboard doesn't contain a string.",
                    "Pasteboard couldn't give string."
                ))

            if not Cocoa.NSWorkspace.sharedWorkspace().openFile_(pboardString):
                return ERROR(Cocoa.NSLocalizedString(
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
        #NSLog(u"doCapitalizeService_userData_error_(%s, %s)", pboard, data)
        try:
            types = pboard.types()
            pboardString = None
            if Cocoa.NSStringPboardType in types:
                pboardString = pboard.stringForType_(Cocoa.NSStringPboardType)
            if pboardString is None:
                return ERROR(Cocoa.NSLocalizedString(
                    "Error: Pasteboard doesn't contain a string.",
                    "Pasteboard couldn't give string."
                ))

            newString = Cocoa.NSString.capitalizedString(pboardString)

            if not newString:
                return ERROR(Cocoa.NSLocalizedString(
                    "Error: Couldn't capitalize string %s.",
                    "Couldn't perform service operation for string %s."
                ) % pboardString)

            types = [Cocoa.NSStringPboardType]
            pboard.declareTypes_owner_([Cocoa.NSStringPboardType], None)
            pboard.setString_forType_(newString, Cocoa.NSStringPboardType)
            return ERROR(None)
        except:
            import traceback
            traceback.print_exc()
            return ERROR(u'Exception, see traceback')
