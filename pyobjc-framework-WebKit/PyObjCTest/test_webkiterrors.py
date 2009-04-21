
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebKitErrors (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(WebKitErrorDomain, unicode)
        self.failUnlessIsInstance(WebKitErrorMIMETypeKey, unicode)
        self.failUnlessIsInstance(WebKitErrorPlugInNameKey, unicode)
        self.failUnlessIsInstance(WebKitErrorPlugInPageURLStringKey, unicode)

        self.failUnlessEqual(WebKitErrorCannotShowMIMEType, 100)
        self.failUnlessEqual(WebKitErrorCannotShowURL, 101)
        self.failUnlessEqual(WebKitErrorFrameLoadInterruptedByPolicyChange, 102)
        self.failUnlessEqual(WebKitErrorCannotFindPlugIn, 200)
        self.failUnlessEqual(WebKitErrorCannotLoadPlugIn, 201)
        self.failUnlessEqual(WebKitErrorJavaUnavailable, 202)




if __name__ == "__main__":
    main()
