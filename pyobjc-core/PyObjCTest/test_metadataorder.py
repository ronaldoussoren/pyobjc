import objc
from .metadataorder import (
    OC_MetadataOrder,
    OC_MetadataOrderChild1,
    OC_MetadataOrderChild2,
    OC_MetadataOrderGrandchild,
)
from .fnd import NSObject
from PyObjCTools.TestSupport import TestCase

objc.registerMetaDataForSelector(
    b"NSObject",
    b"metaProtoValue",
    {"retval": {"type": objc._C_NSBOOL}},
)

# No registrations for metadataorder1

# metadataorder2: Registered on NSObject (only)
objc.registerMetaDataForSelector(
    b"NSObject",
    b"metadataorder2",
    {"retval": {"type": objc._C_NSBOOL}},
)

# metadataorder3: registered on more specific before NSObject
objc.registerMetaDataForSelector(
    b"OC_MetadataOrderChild1",
    b"metadataorder3",
    {"retval": {"type": objc._C_NSBOOL}},
)

objc.registerMetaDataForSelector(
    b"NSObject",
    b"metadataorder3",
    {"retval": {"type": objc._C_CHAR_AS_INT}},
)

# metadataorder4: registered on NSObject before more specific
objc.registerMetaDataForSelector(
    b"NSObject",
    b"metadataorder4",
    {"retval": {"type": objc._C_CHAR_AS_TEXT}},
)

objc.registerMetaDataForSelector(
    b"OC_MetadataOrderChild2",
    b"metadataorder4",
    {"retval": {"type": objc._C_CHAR_AS_INT}},
)


class OC_TestMetadataOrder1(NSObject):
    def metaProtoValue(self):
        return 1


class OC_TestMetadataOrder2(NSObject):
    __pyobjc_protocols__ = [objc.protocolNamed("OC_MetaDataProto")]

    def metaProtoValue(self):
        return 1


class TestProtocolImpact(TestCase):
    def test_without_protocol(self):
        self.assertResultIsBOOL(OC_TestMetadataOrder1.metaProtoValue)

    def test_with_protocol(self):
        self.assertResultIsBOOL(OC_TestMetadataOrder2.metaProtoValue)


class TestRegistrationOrder(TestCase):
    def test_no_metadata(self):
        self.assertResultHasType(OC_MetadataOrder.metadataorder1, objc._C_CHR)
        self.assertResultHasType(OC_MetadataOrderChild1.metadataorder1, objc._C_CHR)
        self.assertResultHasType(OC_MetadataOrderChild2.metadataorder1, objc._C_CHR)
        self.assertResultHasType(OC_MetadataOrderGrandchild.metadataorder1, objc._C_CHR)

    def test_registered_for_nsobject(self):
        self.assertResultHasType(OC_MetadataOrder.metadataorder2, objc._C_NSBOOL)
        self.assertResultHasType(OC_MetadataOrderChild1.metadataorder2, objc._C_NSBOOL)
        self.assertResultHasType(OC_MetadataOrderChild2.metadataorder2, objc._C_NSBOOL)
        self.assertResultHasType(
            OC_MetadataOrderGrandchild.metadataorder2, objc._C_NSBOOL
        )

    def test_registered_for_nsobject_after_class(self):
        self.assertResultHasType(OC_MetadataOrder.metadataorder3, objc._C_CHAR_AS_INT)
        self.assertResultHasType(OC_MetadataOrderChild1.metadataorder3, objc._C_NSBOOL)
        self.assertResultHasType(
            OC_MetadataOrderChild2.metadataorder3, objc._C_CHAR_AS_INT
        )
        self.assertResultHasType(
            OC_MetadataOrderGrandchild.metadataorder3, objc._C_NSBOOL
        )

    def test_registered_for_child_before_parent(self):
        self.assertResultHasType(OC_MetadataOrder.metadataorder4, objc._C_CHAR_AS_TEXT)
        self.assertResultHasType(
            OC_MetadataOrderChild1.metadataorder4, objc._C_CHAR_AS_TEXT
        )
        self.assertResultHasType(
            OC_MetadataOrderChild2.metadataorder4, objc._C_CHAR_AS_INT
        )
        self.assertResultHasType(
            OC_MetadataOrderGrandchild.metadataorder4, objc._C_CHAR_AS_TEXT
        )
