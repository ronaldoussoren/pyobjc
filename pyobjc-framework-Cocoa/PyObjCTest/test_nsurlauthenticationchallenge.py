from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSURLAuthenticationChallenge (NSObject):
    def testProtocols(self):
        objc.protocolNamed('NSURLAuthenticationChallengeSender')


if __name__ == "__main__":
    main()
