from PyObjCTools.TestSupport import *

import objc._bridgesupport as bridgesupport
import os
import re

try:
    basestring
except NameError:
    basestring = str

IDENTIFIER=re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

class TestSystemBridgeSupport (TestCase):

    def iter_framework_dir(self, framework_dir):
        for dn in os.listdir(framework_dir):
            fn = os.path.join(framework_dir, dn, 'Resources', 'BridgeSupport', dn.replace('.framework', '.bridgesupport'))
            if os.path.exists(fn):
                yield fn

            fn = os.path.join(framework_dir, dn, 'Frameworks')
            if os.path.exists(fn):
                for item in self.iter_framework_dir(fn):
                    yield item

    def iter_system_bridgesupport_files(self):
        for item in self.iter_framework_dir('/System/Library/Frameworks'):
            yield item

    def test_system_bridgesupport(self):
        for fn in self.iter_system_bridgesupport_files():
            with open(fn, 'r') as fp:
                xmldata = fp.read()

            self.assert_valid_bridgesupport(os.path.basename(fn).split('.')[0], xmldata)



    def assertIsIdenfier(self, value):
        m = IDENTIFIER.match(value)
        if m is None:
            self.fail("'%s' is not an identifier"%(value,))

    def assert_valid_bridgesupport(self, framework_name, xmldata):
        print framework_name
        prs = bridgesupport._BridgeSupportParser(xmldata, framework_name)

        for item in prs.ctypes:
            # XXX: validate items
            pass

        for name, typestr, magic in pfs.constants:
            self.assertIsInstance(name, basestring)
            self.assertIsInstance(typestr, bytes)
            self.assertIsInstance(magic, bool)

            self.assertEqual(len(objc.splitSig(typestr)), 1)

        for name, orig in prs.func_aliases:
            self.assertIsInstance(name, basestring)
            self.assertIsInstance(orig, basestring)
            self.assertIsIdentifier(name)

        for info in prs.functions:
            # XXX: validate item
            pass

        for info in prs.informal_protocols:
            # XXX: validate item
            pass

        for info in prs.meta:
            # XXX: validate class metadata
            pass

        for name, typestr in prs.opaque:
            self.assertIsInstance(name, basestring)
            self.assertIsInstance(typestr, bytes)

            self.assertEqual(len(objc.splitSig(typestr)), 1)

        for name, typestr in prs.structs:
            self.assertIsInstance(name, basestring)
            self.assertIsInstance(typestr, bytes)

            self.assertEqual(len(objc.splitSig(typestr)), 1)

        # XXX: Is there anything to do w.r.t. validating prs.values? 
        prs.values


if __name__ == "__main__":
    main()
