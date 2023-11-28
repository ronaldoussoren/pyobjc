from PyObjCTools.TestSupport import TestCase, min_os_level
from unittest import SkipTest
from PyObjCTest.dateint import OC_DateInt
from PyObjCTest.pythonset import OC_TestSet


import datetime
import time
import objc

NSKeyedArchiver = objc.lookUpClass("NSKeyedArchiver")
NSKeyedUnarchiver = objc.lookUpClass("NSKeyedUnarchiver")
NSArchiver = objc.lookUpClass("NSArchiver")
NSUnarchiver = objc.lookUpClass("NSUnarchiver")

NSDate = objc.lookUpClass("NSDate")
NSData = objc.lookUpClass("NSData")
OC_PythonDate = objc.lookUpClass("OC_PythonDate")
OC_BuiltinPythonDate = objc.lookUpClass("OC_BuiltinPythonDate")

# XXX: Move register calls to utility module
objc.registerMetaDataForSelector(
    b"NSKeyedArchiver",
    b"archivedDataWithRootObject:requiringSecureCoding:error:",
    {
        "arguments": {
            2 + 1: {"type": objc._C_NSBOOL},
            2 + 2: {"type_modifier": objc._C_OUT},
        }
    },
)
objc.registerMetaDataForSelector(
    b"NSKeyedUnarchiver",
    b"unarchivedObjectOfClass:fromData:error:",
    {"arguments": {2 + 2: {"type_modifier": objc._C_OUT}}},
)
objc.registerMetaDataForSelector(
    b"NSKeyedUnarchiver",
    b"unarchivedObjectOfClasses:fromData:error:",
    {"arguments": {2 + 2: {"type_modifier": objc._C_OUT}}},
)


# Start of epoch for NSDate
REFDATE = datetime.datetime(2001, 1, 1, 0, 0, 0, 0, datetime.timezone.utc)


def as_datetime(value):
    if isinstance(value, datetime.date) and not isinstance(value, datetime.datetime):
        return datetime.datetime.fromtimestamp(float(value.strftime("%s")))
    return value


class TestDateInObjC(TestCase):
    value = datetime.datetime.now() - datetime.timedelta(days=30)

    def test_proxy_class(self):
        if type(self.value) in (datetime.date, datetime.datetime):
            self.assertIs(OC_TestSet.classOf_(self.value), OC_BuiltinPythonDate)
        else:
            self.assertIs(OC_TestSet.classOf_(self.value), OC_PythonDate)

    def assert_same_timestamp(self, py, oc):
        if isinstance(self.value, datetime.date):
            # The conversion between datetime.date and NSDate
            # is less precise as I'd like, hence a fairly rough
            # check.
            self.assertLessEqual(abs(py - oc), 1)
        else:
            self.assertLessEqual(abs(py - oc), 0.5)

    def test_since1970(self):
        py = as_datetime(self.value).timestamp()
        oc = OC_DateInt.timeIntervalSince1970For_(self.value)
        self.assert_same_timestamp(py, oc)

    def test_sincerefdate(self):
        py = as_datetime(self.value).timestamp() - REFDATE.timestamp()
        oc = OC_DateInt.timeIntervalSinceReferenceDateFor_(self.value)
        self.assert_same_timestamp(py, oc)

    def test_since_now(self):
        if type(self.value) is datetime.date:
            raise SkipTest("Not relevant for datetime.date")
        py = self.value.timestamp() - datetime.datetime.now().timestamp()
        oc = OC_DateInt.timeIntervalSinceNowFor_(self.value)
        self.assertAlmostEqual(py, oc, places=1)

    def test_add_interval(self):
        seconds = 545.5
        py = as_datetime(self.value) + datetime.timedelta(seconds=seconds)
        oc = OC_DateInt.date_byAddingInterval_(self.value, seconds)
        self.assert_same_timestamp(
            py.timestamp(), OC_DateInt.timeIntervalSince1970For_(oc)
        )

    def test_add_old_interval(self):
        seconds = 545.5
        py = as_datetime(self.value) + datetime.timedelta(seconds=seconds)
        oc = OC_DateInt.date2_byAddingInterval_(self.value, seconds)
        self.assert_same_timestamp(
            py.timestamp(), OC_DateInt.timeIntervalSince1970For_(oc)
        )

    def test_compare(self):
        for offset in (-24 * 3600, 0, 24 * 3600):
            with self.subTest(offset=offset):
                value2 = self.value + datetime.timedelta(seconds=offset)
                v = OC_DateInt.compare_and_(value2, self.value)
                if offset < 0:
                    self.assertLess(v, 0)
                elif offset > 0:
                    self.assertGreater(v, 0)
                else:
                    self.assertEqual(v, 0)

    def test_earlier(self):
        for offset in (-10, 0, 10):
            with self.subTest(offset=offset):
                value2 = self.value + datetime.timedelta(seconds=offset)
                v = OC_DateInt.earlierOf_and_(value2, self.value)
                self.assertEqual(v, min(value2, self.value))

    def test_later(self):
        for offset in (-10, 0, 10):
            with self.subTest(offset=offset):
                value2 = self.value + datetime.timedelta(seconds=offset)
                v = OC_DateInt.laterOf_and_(value2, self.value)
                self.assertEqual(v, max(value2, self.value))

    def test_equal(self):
        for offset in (-10, 0, 10):
            with self.subTest(offset=offset):
                value2 = self.value + datetime.timedelta(seconds=offset)
                v = OC_DateInt.date_equalToDate_(value2, self.value)
                self.assertEqual(int(v), int(value2 == self.value))

    def test_roundtrip_through_keyedarchive(self):
        try:
            (
                blob,
                err,
            ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                self.value, False, None
            )
        except AttributeError:
            blob = NSKeyedArchiver.archivedDataWithRootObject_(self.value)
            err = None
        self.assertIs(err, None)
        self.assertIsInstance(blob, NSData)

        copy = NSKeyedUnarchiver.unarchiveObjectWithData_(blob)
        self.assertEqual(copy, self.value)

    def test_roundtrip_through_archive(self):
        blob = NSArchiver.archivedDataWithRootObject_(self.value)
        self.assertIsInstance(blob, NSData)

        copy = NSUnarchiver.unarchiveObjectWithData_(blob)
        self.assertEqual(copy, self.value)

    @min_os_level("10.13")
    def test_roundtrip_through_secure_keyedarchive(self):
        if (
            type(self.value) in (datetime.date, datetime.datetime)
            and getattr(self.value, "tzinfo", None) is None
        ):
            (
                blob,
                err,
            ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                self.value, True, None
            )
            self.assertIs(err, None)
            self.assertIsInstance(blob, NSData)

            copy = NSKeyedUnarchiver.unarchiveObjectWithData_(blob)
            self.assertEqual(copy, self.value)

        else:
            (
                blob,
                err,
            ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                self.value, True, None
            )
            self.assertIs(blob, None)
            self.assertIsNot(err, None)
            self.assertRegex(
                str(err),
                r"(Class 'OC_PythonDate' disallows secure)|(Class 'OC_PythonObject' does not adopt it)",
            )


class TestTZAwareDatetimeInObjC(TestDateInObjC):
    value = datetime.datetime.now().astimezone(
        tz=datetime.timezone.utc
    ) - datetime.timedelta(days=28)


class TestDate(TestDateInObjC):
    value = datetime.date.today()


class MyDateTime(datetime.datetime):
    pass


class TestDatimetimeSubclass(TestDateInObjC):
    value = MyDateTime.now()
    value.attr = 42


class TestInteractingWithNSDate(TestCase):
    def test_equal(self):
        seconds = int(time.time())

        oc = NSDate.dateWithTimeIntervalSince1970_(seconds)
        py = datetime.datetime.fromtimestamp(seconds)

        self.assertTrue(OC_DateInt.date_equalToDate_(oc, py))
        self.assertTrue(OC_DateInt.date_equalToDate_(py, oc))

    def test_earlier(self):
        seconds = time.time()

        oc = NSDate.dateWithTimeIntervalSince1970_(seconds)
        py = datetime.datetime.fromtimestamp(seconds + 7200)

        with self.subTest("py is later, ask oc"):
            v = OC_DateInt.earlierOf_and_(oc, py)
            self.assertIs(v, oc)

        with self.subTest("py is later, ask py"):
            v = OC_DateInt.earlierOf_and_(py, oc)
            self.assertIs(v, oc)

        oc = NSDate.dateWithTimeIntervalSince1970_(seconds)
        py = datetime.datetime.fromtimestamp(seconds - 7200)

        with self.subTest("py is earlier, ask oc"):
            v = OC_DateInt.earlierOf_and_(oc, py)
            self.assertIs(v, py)

        with self.subTest("py is earlier, ask py"):
            v = OC_DateInt.earlierOf_and_(py, oc)
            self.assertIs(v, py)

    def test_earlier_tz(self):
        seconds = time.time()

        oc = NSDate.dateWithTimeIntervalSince1970_(seconds)
        py = datetime.datetime.fromtimestamp(seconds + 7200, datetime.timezone.utc)

        with self.subTest("py is later, ask oc"):
            v = OC_DateInt.earlierOf_and_(oc, py)
            self.assertIs(v, oc)

        with self.subTest("py is later, ask py"):
            v = OC_DateInt.earlierOf_and_(py, oc)
            self.assertIs(v, oc)

        oc = NSDate.dateWithTimeIntervalSince1970_(seconds)
        py = datetime.datetime.fromtimestamp(seconds - 7200, datetime.timezone.utc)

        with self.subTest("py is earlier, ask oc"):
            v = OC_DateInt.earlierOf_and_(oc, py)
            self.assertIs(v, py)

        with self.subTest("py is earlier, ask py"):
            v = OC_DateInt.earlierOf_and_(py, oc)
            self.assertIs(v, py)
