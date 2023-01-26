import warnings

import objc
import copy
import pickle
from PyObjCTools.TestSupport import TestCase


class TestOptionVarious(TestCase):
    def test_option_creation(self):
        with self.assertRaisesRegex(
            TypeError, "cannot create 'objc._OptionsType' instances"
        ):
            type(objc.options)()

        with self.assertRaisesRegex(TypeError, "Cannot call this method"):
            copy.copy(objc.options)

        with self.assertRaisesRegex(TypeError, "Cannot call this method"):
            pickle.dumps(objc.options)


class TestCompatFunctions(TestCase):
    def test_verbose(self):
        orig = objc.options.verbose
        try:
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                objc.setVerbose(False)
                objc.getVerbose()

            self.assertEqual(len(w), 2)
            self.assertEqual(w[0].category, DeprecationWarning)
            self.assertEqual(w[1].category, DeprecationWarning)

            with warnings.catch_warnings(record=True):
                warnings.simplefilter("ignore")
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
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                objc.setUseKVOForSetattr(orig)
                objc.getUseKVOForSetattr()
            self.assertEqual(len(w), 2)
            self.assertEqual(w[0].category, DeprecationWarning)
            self.assertEqual(w[1].category, DeprecationWarning)

            with warnings.catch_warnings(record=True):
                warnings.simplefilter("ignore")
                self.assertEqual(objc.getUseKVOForSetattr(), orig)

                objc.setUseKVOForSetattr(False)
                self.assertEqual(objc.options.use_kvo, False)
                self.assertEqual(objc.getUseKVOForSetattr(), False)

                objc.setUseKVOForSetattr(True)
                self.assertEqual(objc.options.use_kvo, True)
                self.assertEqual(objc.getUseKVOForSetattr(), True)

        finally:
            objc.options.use_kvo = orig
