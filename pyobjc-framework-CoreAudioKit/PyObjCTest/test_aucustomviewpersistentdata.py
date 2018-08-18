from PyObjCTools.TestSupport import *

import CoreAudioKit

class TestAUCustomViewPersistentData (TestCase):
    def testProtocols(self):
        objc.protocolNamed('AUCustomViewPersistentData')

if __name__ == "__main__":
    main()
