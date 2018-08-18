from PyObjCTools.TestSupport import *

import CoreServices

class TestDriverServices (TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(not hasattr(CoreServices, name), "%r exposed in bindings"%(name,))

    def test_not_wrapped(self):
        self.assert_not_wrapped('durationMicrosecond')
        self.assert_not_wrapped('durationMillisecond')
        self.assert_not_wrapped('durationSecond')
        self.assert_not_wrapped('durationMinute')
        self.assert_not_wrapped('durationHour')
        self.assert_not_wrapped('durationDay')
        self.assert_not_wrapped('durationNoWait')
        self.assert_not_wrapped('durationForever')
        self.assert_not_wrapped('UpTime')
        self.assert_not_wrapped('AbsoluteToNanoseconds')
        self.assert_not_wrapped('AbsoluteToDuration')
        self.assert_not_wrapped('NanosecondsToAbsolute')
        self.assert_not_wrapped('DurationToAbsolute')
        self.assert_not_wrapped('AddAbsoluteToAbsolute')
        self.assert_not_wrapped('SubAbsoluteFromAbsolute')
        self.assert_not_wrapped('AddNanosecondsToAbsolute')
        self.assert_not_wrapped('AddDurationToAbsolute')
        self.assert_not_wrapped('SubNanosecondsFromAbsolute')
        self.assert_not_wrapped('SubDurationFromAbsolute')
        self.assert_not_wrapped('AbsoluteDeltaToNanoseconds')
        self.assert_not_wrapped('AbsoluteDeltaToDuration')
        self.assert_not_wrapped('DurationToNanoseconds')
        self.assert_not_wrapped('NanosecondsToDuration')


if __name__ == "__main__":
    main()
