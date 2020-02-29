from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSURLAuthenticationChallenge(NSObject):
    def testProtocols(self):
        objc.protocolNamed("NSURLAuthenticationChallengeSender")


if __name__ == "__main__":
    main()
