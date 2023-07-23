from PyObjCTools.TestSupport import TestCase

import Cinematic


class TestCNCinematicError(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Cinematic.CNCinematicErrorCode)
        self.assertEqual(Cinematic.CNCinematicErrorCodeUnknown, 1)
        self.assertEqual(Cinematic.CNCinematicErrorCodeUnreadable, 2)
        self.assertEqual(Cinematic.CNCinematicErrorCodeIncomplete, 3)
        self.assertEqual(Cinematic.CNCinematicErrorCodeMalformed, 4)
        self.assertEqual(Cinematic.CNCinematicErrorCodeUnsupported, 5)
        self.assertEqual(Cinematic.CNCinematicErrorCodeIncompatible, 6)
        self.assertEqual(Cinematic.CNCinematicErrorCodeCancelled, 7)
