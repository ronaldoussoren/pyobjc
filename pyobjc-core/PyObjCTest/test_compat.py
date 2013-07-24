from PyObjCTools.TestSupport import *

import objc

class TestCompatFunctions (TestCase):
    def test_verbose(self):
        orig = objc.options.verbose
        try:
            with filterWarnings("error", DeprecationWarning):
                self.assertRaises(DeprecationWarning, objc.setVerbose, False)
                self.assertRaises(DeprecationWarning, objc.getVerbose)

            with filterWarnings("ignore", DeprecationWarning):
                self.assertEqual(objc.getVerbose(), orig)

                objc.setVerbose(False)
                self.assertEqual(objc.options.verbose, False)
                self.assertEqual(objc.getVerbose(), False)

                objc.setVerbose(True)
                self.assertEqual(objc.options.verbose, True)
                self.assertEqual(objc.getVerbose(), True)

        finally:
            objc.options.verbose = orig

    def test_use_kvo(self):
        orig = objc.options.use_kvo
        try:
            with filterWarnings("error", DeprecationWarning):
                self.assertRaises(DeprecationWarning, objc.setUseKVOForSetattr, False)
                self.assertRaises(DeprecationWarning, objc.getUseKVOForSetattr)

            with filterWarnings("ignore", DeprecationWarning):
                self.assertEqual(objc.getUseKVOForSetattr(), orig)

                objc.setUseKVOForSetattr(False)
                self.assertEqual(objc.options.use_kvo, False)
                self.assertEqual(objc.getUseKVOForSetattr(), False)

                objc.setUseKVOForSetattr(True)
                self.assertEqual(objc.options.use_kvo, True)
                self.assertEqual(objc.getUseKVOForSetattr(), True)

        finally:
            objc.options.use_kvo = orig

    @onlyPython2
    def test_strbridge_enabled(self):
        orig = objc.options.strbridge_enabled
        try:
            with filterWarnings("error", DeprecationWarning):
                self.assertRaises(DeprecationWarning, objc.setStrBridgeEnabled, False)
                self.assertRaises(DeprecationWarning, objc.getStrBridgeEnabled)

            with filterWarnings("ignore", DeprecationWarning):
                self.assertEqual(objc.getStrBridgeEnabled(), orig)

                objc.setStrBridgeEnabled(False)
                self.assertEqual(objc.options.strbridge_enabled, False)
                self.assertEqual(objc.getStrBridgeEnabled(), False)

                objc.setStrBridgeEnabled(True)
                self.assertEqual(objc.options.strbridge_enabled, True)
                self.assertEqual(objc.getStrBridgeEnabled(), True)

        finally:
            objc.options.strbridge_enabled = orig

if __name__ == "__main__":
    main()
