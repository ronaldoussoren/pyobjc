'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import InputMethodKit

class TestInputMethodKit (unittest.TestCase):
    def testClasses(self):

        self.assert_( hasattr(InputMethodKit, 'IMKInputController') )
        self.assert_( isinstance(InputMethodKit.IMKInputController, objc.objc_class) )

        # 10.5
        self.assert_( hasattr(InputMethodKit, 'IMKCandidates') )
        self.assert_( isinstance(InputMethodKit.IMKCandidates, objc.objc_class) )
    def testValues(self):
        self.assert_( hasattr(InputMethodKit, 'kIMKScrollingGridCandidatePanel') )
        self.assert_( isinstance(InputMethodKit.kIMKScrollingGridCandidatePanel, (int, long)) )
        self.assertEquals(InputMethodKit.kIMKScrollingGridCandidatePanel, 2)

    def testVariables(self):
        self.assert_( hasattr(InputMethodKit, 'IMKCandidatesOpacityAttributeName') )
        self.assert_( isinstance(InputMethodKit.IMKCandidatesOpacityAttributeName, unicode) )

    def testProtocols(self):
        self.assert_( hasattr(InputMethodKit, 'protocols') )
        self.assert_( hasattr(InputMethodKit.protocols, 'IMKServerInput') )
        self.assert_( isinstance(InputMethodKit.protocols.IMKServerInput, objc.informal_protocol) )



if __name__ == "__main__":
    unittest.main()

