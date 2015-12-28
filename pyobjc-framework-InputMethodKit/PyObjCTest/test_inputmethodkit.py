'''
Some simple tests to check that the framework is properly wrapped.
'''
from PyObjCTools.TestSupport import *
import objc
import InputMethodKit

class TestInputMethodKit (TestCase):
    def testClasses(self):

        self.assertTrue( hasattr(InputMethodKit, 'IMKInputController') )
        self.assertTrue( isinstance(InputMethodKit.IMKInputController, objc.objc_class) )

        # 10.5
        self.assertTrue( hasattr(InputMethodKit, 'IMKCandidates') )
        self.assertTrue( isinstance(InputMethodKit.IMKCandidates, objc.objc_class) )
    def testValues(self):
        self.assertTrue( hasattr(InputMethodKit, 'kIMKScrollingGridCandidatePanel') )
        self.assertTrue( isinstance(InputMethodKit.kIMKScrollingGridCandidatePanel, (int, long)) )
        self.assertEquals(InputMethodKit.kIMKScrollingGridCandidatePanel, 2)

    def testVariables(self):
        self.assertTrue( hasattr(InputMethodKit, 'IMKCandidatesOpacityAttributeName') )
        self.assertTrue( isinstance(InputMethodKit.IMKCandidatesOpacityAttributeName, unicode) )

    #def testProtocols(self):
        #self.assertFalse( hasattr(InputMethodKit, 'protocols') )
        #self.assertTrue( hasattr(InputMethodKit.protocols, 'IMKServerInput') )
        #self.assertTrue( isinstance(InputMethodKit.protocols.IMKServerInput, objc.informal_protocol) )

    def testProtocols2(self):
        objc.protocolNamed('IMKMouseHandling')
        objc.protocolNamed('IMKStateSetting')



if __name__ == "__main__":
    main()
