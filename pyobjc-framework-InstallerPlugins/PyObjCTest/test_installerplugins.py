'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import InstallerPlugins

class TestInstallerPlugins (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(InstallerPlugins, 'InstallerSection') )
        self.assert_( isinstance(InstallerPlugins.InstallerSection, objc.objc_class) )

        self.assert_( hasattr(InstallerPlugins, 'InstallerPane') )
        self.assert_( isinstance(InstallerPlugins.InstallerPane, objc.objc_class) )


    def testValues(self):
        self.assert_( hasattr(InstallerPlugins, 'InstallerDirectionBackward') )
        self.assert_( isinstance(InstallerPlugins.InstallerDirectionBackward, (int, long)) )
        self.assertEquals(InstallerPlugins.InstallerDirectionBackward, 1)

    def testVariables(self):
        self.assert_( hasattr(InstallerPlugins, 'InstallerState_Choice_Identifier') )
        self.assert_( isinstance(InstallerPlugins.InstallerState_Choice_Identifier, unicode) )

        self.assert_( hasattr(InstallerPlugins, 'InstallerState_Choice_CustomLocation') )
        self.assert_( isinstance(InstallerPlugins.InstallerState_Choice_CustomLocation, unicode) )


if __name__ == "__main__":
    unittest.main()

