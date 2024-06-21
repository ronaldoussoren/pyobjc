from PyObjCTools.TestSupport import TestCase

import Carbon


class TestHIToolbox_CarbonEvents(TestCase):
    def test_structs(self):
        v = Carbon.EventHotKeyID()
        self.assertIsInstance(v.signature, int)
        self.assertIsInstance(v.id, int)

    def test_types(self):
        self.assertIsOpaquePointer(Carbon.EventHotKeyRef)

    def test_enum(self):
        self.assertEqual(Carbon.kEventHotKeyNoOptions, 0)
        self.assertEqual(Carbon.kEventHotKeyExclusive, 1 << 0)

        self.assertEqual(Carbon.kHIHotKeyModeAllEnabled, 0)
        self.assertEqual(Carbon.kHIHotKeyModeAllDisabled, 1 << 0)
        self.assertEqual(Carbon.kHIHotKeyModeAllDisabledExceptUniversalAccess, 1 << 1)

    def test_constants(self):
        self.assertEqual(Carbon.kHISymbolicHotKeyCode, "kHISymbolicHotKeyCode")
        self.assertEqual(
            Carbon.kHISymbolicHotKeyModifiers, "kHISymbolicHotKeyModifiers"
        )
        self.assertEqual(Carbon.kHISymbolicHotKeyEnabled, "kHISymbolicHotKeyEnabled")

    def test_functions(self):
        self.assertArgIsOut(Carbon.RegisterEventHotKey, 5)
        Carbon.UnregisterEventHotKey

        self.assertArgIsOut(Carbon.CopySymbolicHotKeys, 0)
        self.assertArgIsCFRetained(Carbon.CopySymbolicHotKeys, 0)

        self.assertResultHasType(Carbon.PushSymbolicHotKeyMode, b"q")
        self.assertArgHasType(Carbon.PopSymbolicHotKeyMode, 0, b"q")
