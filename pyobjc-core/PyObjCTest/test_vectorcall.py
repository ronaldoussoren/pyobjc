#
# This file is generated using Tools/generate-helpers-vector.py
#
#    ** DO NOT EDIT **
#
from PyObjCTools.TestSupport import TestCase
import objc
from objc import simd


# Needs to be replaced by minimal definitions for
# CGColor and CGColorSpace
import Quartz  # noqa: F401

from .vectorcall import OC_VectorCall


class NoObjCClass:
    @property
    def __pyobjc_object__(self):
        raise TypeError("Cannot proxy")


class NoBool:
    def __bool__(self):
        raise TypeError("no valid in boolean context")


NoObjCValueObject = NoObjCClass()

# Register full signatures for the helper methods

objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v16C", {"full_signature": b"<16C>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv16C", {"full_signature": b"<16C>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v2d", {"full_signature": b"<2d>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv2d", {"full_signature": b"<2d>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v2dd:", {"full_signature": b"<2d>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv2dd:", {"full_signature": b"<2d>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v2f", {"full_signature": b"<2f>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv2f", {"full_signature": b"<2f>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v2fQ:", {"full_signature": b"<2f>@:Q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv2fQ:", {"full_signature": b"<2f>@:Q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v2fd:", {"full_signature": b"<2f>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv2fd:", {"full_signature": b"<2f>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v2fq:", {"full_signature": b"<2f>@:q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv2fq:", {"full_signature": b"<2f>@:q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v2i", {"full_signature": b"<2i>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv2i", {"full_signature": b"<2i>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3dd:", {"full_signature": b"<3d>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3dd:", {"full_signature": b"<3d>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3f", {"full_signature": b"<3f>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3f", {"full_signature": b"<3f>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3fv2i:v2i:", {"full_signature": b"<3f>@:<2i><2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3fv2i:v2i:", {"full_signature": b"<3f>@:<2i><2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3fv3f:", {"full_signature": b"<3f>@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3fv3f:", {"full_signature": b"<3f>@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3fv3f:id:", {"full_signature": b"<3f>@:<3f>@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3fv3f:id:", {"full_signature": b"<3f>@:<3f>@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3fv4i:", {"full_signature": b"<3f>@:<4i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3fv4i:", {"full_signature": b"<3f>@:<4i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3fQ:", {"full_signature": b"<3f>@:Q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3fQ:", {"full_signature": b"<3f>@:Q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3fd:", {"full_signature": b"<3f>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3fd:", {"full_signature": b"<3f>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v4dd:", {"full_signature": b"<4d>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv4dd:", {"full_signature": b"<4d>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v4f", {"full_signature": b"<4f>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv4f", {"full_signature": b"<4f>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v4fd:", {"full_signature": b"<4f>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv4fd:", {"full_signature": b"<4f>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v4iv3f:", {"full_signature": b"<4i>@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv4iv3f:", {"full_signature": b"<4i>@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv2f:", {"full_signature": b"@@:<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv2f:", {"full_signature": b"@@:<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv2f:v2I:q:id:", {"full_signature": b"@@:<2f><2I>q@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv2f:v2I:q:id:", {"full_signature": b"@@:<2f><2I>q@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv2f:v2f:", {"full_signature": b"@@:<2f><2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv2f:v2f:", {"full_signature": b"@@:<2f><2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv2i:", {"full_signature": b"@@:<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv2i:", {"full_signature": b"@@:<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv2i:i:i:Z:", {"full_signature": b"@@:<2i>iiZ"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv2i:i:i:Z:", {"full_signature": b"@@:<2i>iiZ"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv2i:i:i:Z:Class:", {"full_signature": b"@@:<2i>iiZ#"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv2i:i:i:Z:Class:", {"full_signature": b"@@:<2i>iiZ#"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv3f:", {"full_signature": b"@@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv3f:", {"full_signature": b"@@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv3f:v2I:Z:Z:Z:q:id:", {"full_signature": b"@@:<3f><2I>ZZZq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsidv3f:v2I:Z:Z:Z:q:id:",
    {"full_signature": b"@@:<3f><2I>ZZZq@"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv3f:v2I:Z:Z:q:id:", {"full_signature": b"@@:<3f><2I>ZZq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv3f:v2I:Z:Z:q:id:", {"full_signature": b"@@:<3f><2I>ZZq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv3f:v2I:Z:q:id:", {"full_signature": b"@@:<3f><2I>Zq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv3f:v2I:Z:q:id:", {"full_signature": b"@@:<3f><2I>Zq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv3f:v2I:i:Z:q:id:", {"full_signature": b"@@:<3f><2I>iZq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv3f:v2I:i:Z:q:id:", {"full_signature": b"@@:<3f><2I>iZq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv3f:v2I:q:id:", {"full_signature": b"@@:<3f><2I>q@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv3f:v2I:q:id:", {"full_signature": b"@@:<3f><2I>q@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv3f:v3I:Z:q:id:", {"full_signature": b"@@:<3f><3I>Zq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv3f:v3I:Z:q:id:", {"full_signature": b"@@:<3f><3I>Zq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv3f:v3I:q:Z:id:", {"full_signature": b"@@:<3f><3I>qZ@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv3f:v3I:q:Z:id:", {"full_signature": b"@@:<3f><3I>qZ@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv3f:Q:Q:q:Z:Z:id:", {"full_signature": b"@@:<3f>QQqZZ@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv3f:Q:Q:q:Z:Z:id:", {"full_signature": b"@@:<3f>QQqZZ@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv3f:Z:q:id:", {"full_signature": b"@@:<3f>Zq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv3f:Z:q:id:", {"full_signature": b"@@:<3f>Zq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idv4f:", {"full_signature": b"@@:<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidv4f:", {"full_signature": b"@@:<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idid:v2d:v2d:v2i:Z:", {"full_signature": b"@@:@<2d><2d><2i>Z"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsidid:v2d:v2d:v2i:Z:",
    {"full_signature": b"@@:@<2d><2d><2i>Z"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idid:v2f:", {"full_signature": b"@@:@<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidid:v2f:", {"full_signature": b"@@:@<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idid:v3f:", {"full_signature": b"@@:@<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidid:v3f:", {"full_signature": b"@@:@<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idid:v4f:", {"full_signature": b"@@:@<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidid:v4f:", {"full_signature": b"@@:@<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idid:id:v2i:", {"full_signature": b"@@:@@<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidid:id:v2i:", {"full_signature": b"@@:@@<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idid:id:v2i:f:", {"full_signature": b"@@:@@<2i>f"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidid:id:v2i:f:", {"full_signature": b"@@:@@<2i>f"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idid:Q:v2f:", {"full_signature": b"@@:@Q<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidid:Q:v2f:", {"full_signature": b"@@:@Q<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idid:Q:v3f:", {"full_signature": b"@@:@Q<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidid:Q:v3f:", {"full_signature": b"@@:@Q<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idid:Q:v4f:", {"full_signature": b"@@:@Q<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidid:Q:v4f:", {"full_signature": b"@@:@Q<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"idid:Q:matrixfloat4x4:",
    {"full_signature": b"@@:@Q{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsidid:Q:matrixfloat4x4:",
    {"full_signature": b"@@:@Q{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idid:Z:id:v2i:q:Q:q:Z:", {"full_signature": b"@@:@Z@<2i>qQqZ"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsidid:Z:id:v2i:q:Q:q:Z:",
    {"full_signature": b"@@:@Z@<2i>qQqZ"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idid:q:v2i:f:f:f:f:", {"full_signature": b"@@:@q<2i>ffff"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidid:q:v2i:f:f:f:f:", {"full_signature": b"@@:@q<2i>ffff"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idid:q:v2i:f:f:f:f:f:", {"full_signature": b"@@:@q<2i>fffff"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidid:q:v2i:f:f:f:f:f:", {"full_signature": b"@@:@q<2i>fffff"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idid:GKBox:", {"full_signature": b"@@:@{GKBox=<3f><3f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidid:GKBox:", {"full_signature": b"@@:@{GKBox=<3f><3f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idid:GKQuad:", {"full_signature": b"@@:@{GKQuad=<2f><2f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidid:GKQuad:", {"full_signature": b"@@:@{GKQuad=<2f><2f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"idid:MDLAxisAlignedBoundingBox:f:",
    {"full_signature": b"@@:@{_MDLAxisAlignedBoundingBox=<3f><3f>}f"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsidid:MDLAxisAlignedBoundingBox:f:",
    {"full_signature": b"@@:@{_MDLAxisAlignedBoundingBox=<3f><3f>}f"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"idid:matrixfloat2x2:",
    {"full_signature": b"@@:@{_matrix_float2x2=[2<2f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsidid:matrixfloat2x2:",
    {"full_signature": b"@@:@{_matrix_float2x2=[2<2f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"idid:matrixfloat3x3:",
    {"full_signature": b"@@:@{_matrix_float3x3=[3<3f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsidid:matrixfloat3x3:",
    {"full_signature": b"@@:@{_matrix_float3x3=[3<3f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"idid:matrixfloat4x4:",
    {"full_signature": b"@@:@{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsidid:matrixfloat4x4:",
    {"full_signature": b"@@:@{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"idCGColor:CGColor:id:v2i:",
    {"full_signature": b"@@:^{CGColor=}^{CGColor=}@<2i>"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsidCGColor:CGColor:id:v2i:",
    {"full_signature": b"@@:^{CGColor=}^{CGColor=}@<2i>"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idf:v2f:v2f:", {"full_signature": b"@@:f<2f><2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidf:v2f:v2f:", {"full_signature": b"@@:f<2f><2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idf:v2f:v2f:Class:", {"full_signature": b"@@:f<2f><2f>#"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidf:v2f:v2f:Class:", {"full_signature": b"@@:f<2f><2f>#"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idf:v2f:Q:Q:Q:q:Z:id:", {"full_signature": b"@@:f<2f>QQQqZ@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidf:v2f:Q:Q:Q:q:Z:id:", {"full_signature": b"@@:f<2f>QQQqZ@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idf:v2f:Q:Q:q:Z:id:", {"full_signature": b"@@:f<2f>QQqZ@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidf:v2f:Q:Q:q:Z:id:", {"full_signature": b"@@:f<2f>QQqZ@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idf:id:v2i:i:q:Z:", {"full_signature": b"@@:f@<2i>iqZ"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidf:id:v2i:i:q:Z:", {"full_signature": b"@@:f@<2i>iqZ"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"idf:id:v2i:i:q:CGColor:CGColor:",
    {"full_signature": b"@@:f@<2i>iq^{CGColor=}^{CGColor=}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsidf:id:v2i:i:q:CGColor:CGColor:",
    {"full_signature": b"@@:f@<2i>iq^{CGColor=}^{CGColor=}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idf:id:v2i:q:", {"full_signature": b"@@:f@<2i>q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidf:id:v2i:q:", {"full_signature": b"@@:f@<2i>q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idf:f:id:v2i:", {"full_signature": b"@@:ff@<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidf:f:id:v2i:", {"full_signature": b"@@:ff@<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idGKBox:", {"full_signature": b"@@:{GKBox=<3f><3f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidGKBox:", {"full_signature": b"@@:{GKBox=<3f><3f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idGKBox:f:", {"full_signature": b"@@:{GKBox=<3f><3f>}f"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidGKBox:f:", {"full_signature": b"@@:{GKBox=<3f><3f>}f"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idGKQuad:", {"full_signature": b"@@:{GKQuad=<2f><2f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidGKQuad:", {"full_signature": b"@@:{GKQuad=<2f><2f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"idGKQuad:f:", {"full_signature": b"@@:{GKQuad=<2f><2f>}f"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsidGKQuad:f:", {"full_signature": b"@@:{GKQuad=<2f><2f>}f"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"idMDLVoxelIndexExtent:",
    {"full_signature": b"@@:{_MDLVoxelIndexExtent=<4i><4i>}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsidMDLVoxelIndexExtent:",
    {"full_signature": b"@@:{_MDLVoxelIndexExtent=<4i><4i>}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"idmatrixfloat4x4:",
    {"full_signature": b"@@:{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsidmatrixfloat4x4:",
    {"full_signature": b"@@:{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"idmatrixfloat4x4:Z:",
    {"full_signature": b"@@:{_matrix_float4x4=[4<4f>]}Z"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsidmatrixfloat4x4:Z:",
    {"full_signature": b"@@:{_matrix_float4x4=[4<4f>]}Z"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"Zv2i:id:id:id:id:", {"full_signature": b"Z@:<2i>@@@@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsZv2i:id:id:id:id:", {"full_signature": b"Z@:<2i>@@@@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"Zv2i:q:f:id:id:id:", {"full_signature": b"Z@:<2i>qf@@@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsZv2i:q:f:id:id:id:", {"full_signature": b"Z@:<2i>qf@@@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"Zv4i:Z:Z:Z:Z:", {"full_signature": b"Z@:<4i>ZZZZ"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsZv4i:Z:Z:Z:Z:", {"full_signature": b"Z@:<4i>ZZZZ"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"CGColorv3f:", {"full_signature": b"^{CGColor=}@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsCGColorv3f:", {"full_signature": b"^{CGColor=}@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"CGColorv3f:CGColorSpace:",
    {"full_signature": b"^{CGColor=}@:<3f>^{CGColorSpace=}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsCGColorv3f:CGColorSpace:",
    {"full_signature": b"^{CGColor=}@:<3f>^{CGColorSpace=}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"fv2f:", {"full_signature": b"f@:<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsfv2f:", {"full_signature": b"f@:<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"fv2i:", {"full_signature": b"f@:<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsfv2i:", {"full_signature": b"f@:<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vv2d:d:", {"full_signature": b"v@:<2d>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvv2d:d:", {"full_signature": b"v@:<2d>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vv2f:", {"full_signature": b"v@:<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvv2f:", {"full_signature": b"v@:<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vv2f:d:", {"full_signature": b"v@:<2f>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvv2f:d:", {"full_signature": b"v@:<2f>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vv3d:", {"full_signature": b"v@:<3d>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvv3d:", {"full_signature": b"v@:<3d>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vv3d:d:", {"full_signature": b"v@:<3d>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvv3d:d:", {"full_signature": b"v@:<3d>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vv3f:", {"full_signature": b"v@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvv3f:", {"full_signature": b"v@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vv3f:v3f:", {"full_signature": b"v@:<3f><3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvv3f:v3f:", {"full_signature": b"v@:<3f><3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vv3f:v3f:v3f:", {"full_signature": b"v@:<3f><3f><3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvv3f:v3f:v3f:", {"full_signature": b"v@:<3f><3f><3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vv3f:d:", {"full_signature": b"v@:<3f>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvv3f:d:", {"full_signature": b"v@:<3f>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vv4d:d:", {"full_signature": b"v@:<4d>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvv4d:d:", {"full_signature": b"v@:<4d>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vv4f:", {"full_signature": b"v@:<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvv4f:", {"full_signature": b"v@:<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vv4f:d:", {"full_signature": b"v@:<4f>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvv4f:d:", {"full_signature": b"v@:<4f>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vv4i:", {"full_signature": b"v@:<4i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvv4i:", {"full_signature": b"v@:<4i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vid:v2f:v2f:", {"full_signature": b"v@:@<2f><2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvid:v2f:v2f:", {"full_signature": b"v@:@<2f><2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vid:v2f:v2f:q:", {"full_signature": b"v@:@<2f><2f>q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvid:v2f:v2f:q:", {"full_signature": b"v@:@<2f><2f>q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vf:v2i:", {"full_signature": b"v@:f<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvf:v2i:", {"full_signature": b"v@:f<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"vMDLAxisAlignedBoundingBox:",
    {"full_signature": b"v@:{_MDLAxisAlignedBoundingBox=<3f><3f>}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsvMDLAxisAlignedBoundingBox:",
    {"full_signature": b"v@:{_MDLAxisAlignedBoundingBox=<3f><3f>}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"vMDLAxisAlignedBoundingBox:Z:",
    {"full_signature": b"v@:{_MDLAxisAlignedBoundingBox=<3f><3f>}Z"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsvMDLAxisAlignedBoundingBox:Z:",
    {"full_signature": b"v@:{_MDLAxisAlignedBoundingBox=<3f><3f>}Z"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"vmatrixdouble4x4:",
    {"full_signature": b"v@:{_matrix_double4x4=[4<4d>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsvmatrixdouble4x4:",
    {"full_signature": b"v@:{_matrix_double4x4=[4<4d>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"vmatrixdouble4x4:d:",
    {"full_signature": b"v@:{_matrix_double4x4=[4<4d>]}d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsvmatrixdouble4x4:d:",
    {"full_signature": b"v@:{_matrix_double4x4=[4<4d>]}d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"vmatrixfloat2x2:",
    {"full_signature": b"v@:{_matrix_float2x2=[2<2f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsvmatrixfloat2x2:",
    {"full_signature": b"v@:{_matrix_float2x2=[2<2f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"vmatrixfloat3x3:",
    {"full_signature": b"v@:{_matrix_float3x3=[3<3f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsvmatrixfloat3x3:",
    {"full_signature": b"v@:{_matrix_float3x3=[3<3f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"vmatrixfloat4x4:",
    {"full_signature": b"v@:{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsvmatrixfloat4x4:",
    {"full_signature": b"v@:{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"vmatrixfloat4x4:d:",
    {"full_signature": b"v@:{_matrix_float4x4=[4<4f>]}d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsvmatrixfloat4x4:d:",
    {"full_signature": b"v@:{_matrix_float4x4=[4<4f>]}d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"vsimdfloat4x4:",
    {"full_signature": b"v@:{_simd_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsvsimdfloat4x4:",
    {"full_signature": b"v@:{_simd_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vsimdquatd:d:", {"full_signature": b"v@:{_simd_quatd=<4d>}d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvsimdquatd:d:", {"full_signature": b"v@:{_simd_quatd=<4d>}d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vsimdquatf:", {"full_signature": b"v@:{_simd_quatf=<4f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvsimdquatf:", {"full_signature": b"v@:{_simd_quatf=<4f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"vsimdquatf:v3f:",
    {"full_signature": b"v@:{_simd_quatf=<4f>}<3f>"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsvsimdquatf:v3f:",
    {"full_signature": b"v@:{_simd_quatf=<4f>}<3f>"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"vsimdquatf:d:", {"full_signature": b"v@:{_simd_quatf=<4f>}d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsvsimdquatf:d:", {"full_signature": b"v@:{_simd_quatf=<4f>}d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"GKBox", {"full_signature": b"{GKBox=<3f><3f>}@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsGKBox", {"full_signature": b"{GKBox=<3f><3f>}@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"GKQuad", {"full_signature": b"{GKQuad=<2f><2f>}@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsGKQuad", {"full_signature": b"{GKQuad=<2f><2f>}@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"GKTriangleQ:", {"full_signature": b"{GKTriangle=[3<3f>]}@:Q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsGKTriangleQ:", {"full_signature": b"{GKTriangle=[3<3f>]}@:Q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"MDLAxisAlignedBoundingBox",
    {"full_signature": b"{_MDLAxisAlignedBoundingBox=<3f><3f>}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsMDLAxisAlignedBoundingBox",
    {"full_signature": b"{_MDLAxisAlignedBoundingBox=<3f><3f>}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"MDLAxisAlignedBoundingBoxv4i:",
    {"full_signature": b"{_MDLAxisAlignedBoundingBox=<3f><3f>}@:<4i>"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsMDLAxisAlignedBoundingBoxv4i:",
    {"full_signature": b"{_MDLAxisAlignedBoundingBox=<3f><3f>}@:<4i>"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"MDLAxisAlignedBoundingBoxd:",
    {"full_signature": b"{_MDLAxisAlignedBoundingBox=<3f><3f>}@:d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsMDLAxisAlignedBoundingBoxd:",
    {"full_signature": b"{_MDLAxisAlignedBoundingBox=<3f><3f>}@:d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"MDLVoxelIndexExtent",
    {"full_signature": b"{_MDLVoxelIndexExtent=<4i><4i>}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsMDLVoxelIndexExtent",
    {"full_signature": b"{_MDLVoxelIndexExtent=<4i><4i>}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"MPSAxisAlignedBoundingBox",
    {"full_signature": b"{_MPSAxisAlignedBoundingBox=<3f><3f>}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsMPSAxisAlignedBoundingBox",
    {"full_signature": b"{_MPSAxisAlignedBoundingBox=<3f><3f>}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"MPSImageHistogramInfo",
    {"full_signature": b"{_MPSImageHistogramInfo=QZ<4f><4f>}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsMPSImageHistogramInfo",
    {"full_signature": b"{_MPSImageHistogramInfo=QZ<4f><4f>}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"matrixdouble4x4",
    {"full_signature": b"{_matrix_double4x4=[4<4d>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsmatrixdouble4x4",
    {"full_signature": b"{_matrix_double4x4=[4<4d>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"matrixdouble4x4d:",
    {"full_signature": b"{_matrix_double4x4=[4<4d>]}@:d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsmatrixdouble4x4d:",
    {"full_signature": b"{_matrix_double4x4=[4<4d>]}@:d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"matrixfloat2x2",
    {"full_signature": b"{_matrix_float2x2=[2<2f>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsmatrixfloat2x2",
    {"full_signature": b"{_matrix_float2x2=[2<2f>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"matrixfloat3x3",
    {"full_signature": b"{_matrix_float3x3=[3<3f>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsmatrixfloat3x3",
    {"full_signature": b"{_matrix_float3x3=[3<3f>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"matrixfloat4x4",
    {"full_signature": b"{_matrix_float4x4=[4<4f>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsmatrixfloat4x4",
    {"full_signature": b"{_matrix_float4x4=[4<4f>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"matrixfloat4x4id:d:",
    {"full_signature": b"{_matrix_float4x4=[4<4f>]}@:@d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsmatrixfloat4x4id:d:",
    {"full_signature": b"{_matrix_float4x4=[4<4f>]}@:@d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"matrixfloat4x4d:",
    {"full_signature": b"{_matrix_float4x4=[4<4f>]}@:d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsmatrixfloat4x4d:",
    {"full_signature": b"{_matrix_float4x4=[4<4f>]}@:d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"simdfloat4x4", {"full_signature": b"{_simd_float4x4=[4<4f>]}@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clssimdfloat4x4",
    {"full_signature": b"{_simd_float4x4=[4<4f>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"simdfloat4x4simdfloat4x4:id:",
    {"full_signature": b"{_simd_float4x4=[4<4f>]}@:{_simd_float4x4=[4<4f>]}@"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clssimdfloat4x4simdfloat4x4:id:",
    {"full_signature": b"{_simd_float4x4=[4<4f>]}@:{_simd_float4x4=[4<4f>]}@"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"simdquatdd:", {"full_signature": b"{_simd_quatd=<4d>}@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clssimdquatdd:", {"full_signature": b"{_simd_quatd=<4d>}@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"simdquatf", {"full_signature": b"{_simd_quatf=<4f>}@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clssimdquatf", {"full_signature": b"{_simd_quatf=<4f>}@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"simdquatfd:", {"full_signature": b"{_simd_quatf=<4f>}@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clssimdquatfd:", {"full_signature": b"{_simd_quatf=<4f>}@:d"}
)


class TestVectorCall(TestCase):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.addTypeEqualityFunc(simd.matrix_float2x2, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.matrix_float3x3, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.matrix_float4x3, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.matrix_float4x4, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.matrix_double4x4, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.simd_quatf, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.simd_quatd, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.simd_float4x4, "assertMatrixEqual")

    def assertMatrixEqual(self, first, second, msg=None):
        self.assertEqual(type(first), type(second))
        if hasattr(first, "vector"):
            self.assertSequenceEqual(first.vector, second.vector, msg)
        else:
            self.assertSequenceEqual(first.columns, second.columns, msg)

    def test_v16C(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v16C, b"<16C>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v16C()
        self.assertEqual(
            rv,
            objc.simd.vector_uchar16(
                0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v16C("hello")

    def test_v2d(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v2d, b"<2d>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v2d()
        self.assertEqual(rv, objc.simd.vector_double2(0.0, 1.5))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v2d("hello")

    def test_v2dd_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v2dd_, b"<2d>")
        self.assertArgHasType(OC_VectorCall.v2dd_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v2dd_(-557000000000.0)
        self.assertEqual(rv, objc.simd.vector_double2(0.0, 1.5))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v2dd_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v2dd_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.v2dd_(None)

    def test_v2f(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v2f, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v2f()
        self.assertEqual(rv, objc.simd.vector_float2(0.0, 1.5))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v2f("hello")

    def test_v2fQ_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v2fQ_, b"<2f>")
        self.assertArgHasType(OC_VectorCall.v2fQ_, 0, b"Q")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v2fQ_(35184372088832)
        self.assertEqual(rv, objc.simd.vector_float2(0.0, 1.5))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], 35184372088832)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v2fQ_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v2fQ_(35184372088832, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.v2fQ_(None)

    def test_v2fd_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v2fd_, b"<2f>")
        self.assertArgHasType(OC_VectorCall.v2fd_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v2fd_(-557000000000.0)
        self.assertEqual(rv, objc.simd.vector_float2(0.0, 1.5))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v2fd_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v2fd_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.v2fd_(None)

    def test_v2fq_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v2fq_, b"<2f>")
        self.assertArgHasType(OC_VectorCall.v2fq_, 0, b"q")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v2fq_(-17592186044416)
        self.assertEqual(rv, objc.simd.vector_float2(0.0, 1.5))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -17592186044416)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v2fq_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v2fq_(-17592186044416, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.v2fq_(None)

    def test_v2i(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v2i, b"<2i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v2i()
        self.assertEqual(rv, objc.simd.vector_int2(0, 1))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v2i("hello")

    def test_v3dd_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v3dd_, b"<3d>")
        self.assertArgHasType(OC_VectorCall.v3dd_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v3dd_(-557000000000.0)
        self.assertEqual(rv, objc.simd.vector_double3(0.0, 1.5, 3.0))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v3dd_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v3dd_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.v3dd_(None)

    def test_v3f(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v3f, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v3f()
        self.assertEqual(rv, objc.simd.vector_float3(0.0, 1.5, 3.0))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v3f("hello")

    def test_v3fv2i_v2i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v3fv2i_v2i_, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v3fv2i_v2i_, 0, b"<2i>")
        self.assertArgHasType(OC_VectorCall.v3fv2i_v2i_, 1, b"<2i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v3fv2i_v2i_(objc.simd.vector_int2(0, 1), objc.simd.vector_int2(0, 1))
        self.assertEqual(rv, objc.simd.vector_float3(0.0, 1.5, 3.0))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_int2(0, 1))
        self.assertEqual(stored[1], objc.simd.vector_int2(0, 1))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v3fv2i_v2i_(objc.simd.vector_int2(0, 1))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v3fv2i_v2i_(
                objc.simd.vector_int2(0, 1), objc.simd.vector_int2(0, 1), "hello"
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.v3fv2i_v2i_(None, objc.simd.vector_int2(0, 1))

        with self.assertRaises((TypeError, ValueError)):
            oc.v3fv2i_v2i_(objc.simd.vector_int2(0, 1), None)

    def test_v3fv3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v3fv3f_, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v3fv3f_, 0, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v3fv3f_(objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(rv, objc.simd.vector_float3(0.0, 1.5, 3.0))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v3fv3f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v3fv3f_(objc.simd.vector_float3(0.0, 1.5, 3.0), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.v3fv3f_(None)

    def test_v3fv3f_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v3fv3f_id_, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v3fv3f_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v3fv3f_id_, 1, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v3fv3f_id_(objc.simd.vector_float3(0.0, 1.5, 3.0), "hello")
        self.assertEqual(rv, objc.simd.vector_float3(0.0, 1.5, 3.0))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v3fv3f_id_(objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v3fv3f_id_(objc.simd.vector_float3(0.0, 1.5, 3.0), "hello", "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.v3fv3f_id_(None, "hello")

        with self.assertRaises((TypeError, ValueError)):
            oc.v3fv3f_id_(objc.simd.vector_float3(0.0, 1.5, 3.0), NoObjCValueObject)

    def test_v3fv4i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v3fv4i_, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v3fv4i_, 0, b"<4i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v3fv4i_(objc.simd.vector_int4(0, 1, 2, 3))
        self.assertEqual(rv, objc.simd.vector_float3(0.0, 1.5, 3.0))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_int4(0, 1, 2, 3))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v3fv4i_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v3fv4i_(objc.simd.vector_int4(0, 1, 2, 3), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.v3fv4i_(None)

    def test_v3fQ_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v3fQ_, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v3fQ_, 0, b"Q")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v3fQ_(35184372088832)
        self.assertEqual(rv, objc.simd.vector_float3(0.0, 1.5, 3.0))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], 35184372088832)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v3fQ_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v3fQ_(35184372088832, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.v3fQ_(None)

    def test_v3fd_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v3fd_, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v3fd_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v3fd_(-557000000000.0)
        self.assertEqual(rv, objc.simd.vector_float3(0.0, 1.5, 3.0))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v3fd_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v3fd_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.v3fd_(None)

    def test_v4dd_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v4dd_, b"<4d>")
        self.assertArgHasType(OC_VectorCall.v4dd_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v4dd_(-557000000000.0)
        self.assertEqual(rv, objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v4dd_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v4dd_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.v4dd_(None)

    def test_v4f(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v4f, b"<4f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v4f()
        self.assertEqual(rv, objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v4f("hello")

    def test_v4fd_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v4fd_, b"<4f>")
        self.assertArgHasType(OC_VectorCall.v4fd_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v4fd_(-557000000000.0)
        self.assertEqual(rv, objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v4fd_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v4fd_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.v4fd_(None)

    def test_v4iv3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v4iv3f_, b"<4i>")
        self.assertArgHasType(OC_VectorCall.v4iv3f_, 0, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v4iv3f_(objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(rv, objc.simd.vector_int4(0, 1, 2, 3))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v4iv3f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.v4iv3f_(objc.simd.vector_float3(0.0, 1.5, 3.0), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.v4iv3f_(None)

    def test_idv2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv2f_, b"@")
        self.assertArgHasType(OC_VectorCall.idv2f_, 0, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv2f_(objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv2f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv2f_(objc.simd.vector_float2(0.0, 1.5), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv2f_(None)

    def test_idv2f_v2I_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv2f_v2I_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.idv2f_v2I_q_id_, 0, b"<2f>")
        self.assertArgHasType(OC_VectorCall.idv2f_v2I_q_id_, 1, b"<2I>")
        self.assertArgHasType(OC_VectorCall.idv2f_v2I_q_id_, 2, b"q")
        self.assertArgHasType(OC_VectorCall.idv2f_v2I_q_id_, 3, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv2f_v2I_q_id_(
            objc.simd.vector_float2(0.0, 1.5),
            objc.simd.vector_uint2(0, 1),
            -17592186044416,
            "hello",
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 4)
        self.assertEqual(stored[0], objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(stored[1], objc.simd.vector_uint2(0, 1))
        self.assertEqual(stored[2], -17592186044416)
        self.assertEqual(stored[3], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv2f_v2I_q_id_(
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_uint2(0, 1),
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv2f_v2I_q_id_(
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_uint2(0, 1),
                -17592186044416,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv2f_v2I_q_id_(
                None, objc.simd.vector_uint2(0, 1), -17592186044416, "hello"
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv2f_v2I_q_id_(
                objc.simd.vector_float2(0.0, 1.5), None, -17592186044416, "hello"
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv2f_v2I_q_id_(
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_uint2(0, 1),
                None,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv2f_v2I_q_id_(
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_uint2(0, 1),
                -17592186044416,
                NoObjCValueObject,
            )

    def test_idv2f_v2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv2f_v2f_, b"@")
        self.assertArgHasType(OC_VectorCall.idv2f_v2f_, 0, b"<2f>")
        self.assertArgHasType(OC_VectorCall.idv2f_v2f_, 1, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv2f_v2f_(
            objc.simd.vector_float2(0.0, 1.5), objc.simd.vector_float2(0.0, 1.5)
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(stored[1], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv2f_v2f_(objc.simd.vector_float2(0.0, 1.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv2f_v2f_(
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv2f_v2f_(None, objc.simd.vector_float2(0.0, 1.5))

        with self.assertRaises((TypeError, ValueError)):
            oc.idv2f_v2f_(objc.simd.vector_float2(0.0, 1.5), None)

    def test_idv2i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv2i_, b"@")
        self.assertArgHasType(OC_VectorCall.idv2i_, 0, b"<2i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv2i_(objc.simd.vector_int2(0, 1))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_int2(0, 1))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv2i_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv2i_(objc.simd.vector_int2(0, 1), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv2i_(None)

    def test_idv2i_i_i_Z_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv2i_i_i_Z_, b"@")
        self.assertArgHasType(OC_VectorCall.idv2i_i_i_Z_, 0, b"<2i>")
        self.assertArgHasType(OC_VectorCall.idv2i_i_i_Z_, 1, b"i")
        self.assertArgHasType(OC_VectorCall.idv2i_i_i_Z_, 2, b"i")
        self.assertArgHasType(OC_VectorCall.idv2i_i_i_Z_, 3, b"Z")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv2i_i_i_Z_(objc.simd.vector_int2(0, 1), -42, -42, False)
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 4)
        self.assertEqual(stored[0], objc.simd.vector_int2(0, 1))
        self.assertEqual(stored[1], -42)
        self.assertEqual(stored[2], -42)
        self.assertEqual(stored[3], False)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv2i_i_i_Z_(objc.simd.vector_int2(0, 1), -42, -42)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv2i_i_i_Z_(objc.simd.vector_int2(0, 1), -42, -42, False, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv2i_i_i_Z_(None, -42, -42, False)

        with self.assertRaises((TypeError, ValueError)):
            oc.idv2i_i_i_Z_(objc.simd.vector_int2(0, 1), None, -42, False)

        with self.assertRaises((TypeError, ValueError)):
            oc.idv2i_i_i_Z_(objc.simd.vector_int2(0, 1), -42, None, False)

        with self.assertRaises((TypeError, ValueError)):
            oc.idv2i_i_i_Z_(objc.simd.vector_int2(0, 1), -42, -42, NoBool())

    def test_idv2i_i_i_Z_Class_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv2i_i_i_Z_Class_, b"@")
        self.assertArgHasType(OC_VectorCall.idv2i_i_i_Z_Class_, 0, b"<2i>")
        self.assertArgHasType(OC_VectorCall.idv2i_i_i_Z_Class_, 1, b"i")
        self.assertArgHasType(OC_VectorCall.idv2i_i_i_Z_Class_, 2, b"i")
        self.assertArgHasType(OC_VectorCall.idv2i_i_i_Z_Class_, 3, b"Z")
        self.assertArgHasType(OC_VectorCall.idv2i_i_i_Z_Class_, 4, b"#")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv2i_i_i_Z_Class_(
            objc.simd.vector_int2(0, 1), -42, -42, False, objc.lookUpClass("NSObject")
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 5)
        self.assertEqual(stored[0], objc.simd.vector_int2(0, 1))
        self.assertEqual(stored[1], -42)
        self.assertEqual(stored[2], -42)
        self.assertEqual(stored[3], False)
        self.assertEqual(stored[4], objc.lookUpClass("NSObject"))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv2i_i_i_Z_Class_(objc.simd.vector_int2(0, 1), -42, -42, False)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv2i_i_i_Z_Class_(
                objc.simd.vector_int2(0, 1),
                -42,
                -42,
                False,
                objc.lookUpClass("NSObject"),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv2i_i_i_Z_Class_(None, -42, -42, False, objc.lookUpClass("NSObject"))

        with self.assertRaises((TypeError, ValueError)):
            oc.idv2i_i_i_Z_Class_(
                objc.simd.vector_int2(0, 1),
                None,
                -42,
                False,
                objc.lookUpClass("NSObject"),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv2i_i_i_Z_Class_(
                objc.simd.vector_int2(0, 1),
                -42,
                None,
                False,
                objc.lookUpClass("NSObject"),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv2i_i_i_Z_Class_(
                objc.simd.vector_int2(0, 1),
                -42,
                -42,
                NoBool(),
                objc.lookUpClass("NSObject"),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv2i_i_i_Z_Class_(objc.simd.vector_int2(0, 1), -42, -42, False, 42)

    def test_idv3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv3f_, b"@")
        self.assertArgHasType(OC_VectorCall.idv3f_, 0, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv3f_(objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_(objc.simd.vector_float3(0.0, 1.5, 3.0), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_(None)

    def test_idv3f_v2I_Z_Z_Z_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv3f_v2I_Z_Z_Z_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_Z_Z_q_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_Z_Z_q_id_, 1, b"<2I>")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_Z_Z_q_id_, 2, b"Z")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_Z_Z_q_id_, 3, b"Z")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_Z_Z_q_id_, 4, b"Z")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_Z_Z_q_id_, 5, b"q")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_Z_Z_q_id_, 6, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv3f_v2I_Z_Z_Z_q_id_(
            objc.simd.vector_float3(0.0, 1.5, 3.0),
            objc.simd.vector_uint2(0, 1),
            False,
            False,
            False,
            -17592186044416,
            "hello",
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 7)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], objc.simd.vector_uint2(0, 1))
        self.assertEqual(stored[2], False)
        self.assertEqual(stored[3], False)
        self.assertEqual(stored[4], False)
        self.assertEqual(stored[5], -17592186044416)
        self.assertEqual(stored[6], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_v2I_Z_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                False,
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_v2I_Z_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                False,
                -17592186044416,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_Z_Z_q_id_(
                None,
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                False,
                False,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                NoBool(),
                False,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                NoBool(),
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                NoBool(),
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                False,
                None,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                False,
                -17592186044416,
                NoObjCValueObject,
            )

    def test_idv3f_v2I_Z_Z_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv3f_v2I_Z_Z_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_Z_q_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_Z_q_id_, 1, b"<2I>")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_Z_q_id_, 2, b"Z")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_Z_q_id_, 3, b"Z")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_Z_q_id_, 4, b"q")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_Z_q_id_, 5, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv3f_v2I_Z_Z_q_id_(
            objc.simd.vector_float3(0.0, 1.5, 3.0),
            objc.simd.vector_uint2(0, 1),
            False,
            False,
            -17592186044416,
            "hello",
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 6)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], objc.simd.vector_uint2(0, 1))
        self.assertEqual(stored[2], False)
        self.assertEqual(stored[3], False)
        self.assertEqual(stored[4], -17592186044416)
        self.assertEqual(stored[5], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_v2I_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_v2I_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                -17592186044416,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_Z_q_id_(
                None,
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                False,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                NoBool(),
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                NoBool(),
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                None,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                -17592186044416,
                NoObjCValueObject,
            )

    def test_idv3f_v2I_Z_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv3f_v2I_Z_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_q_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_q_id_, 1, b"<2I>")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_q_id_, 2, b"Z")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_q_id_, 3, b"q")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_Z_q_id_, 4, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv3f_v2I_Z_q_id_(
            objc.simd.vector_float3(0.0, 1.5, 3.0),
            objc.simd.vector_uint2(0, 1),
            False,
            -17592186044416,
            "hello",
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 5)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], objc.simd.vector_uint2(0, 1))
        self.assertEqual(stored[2], False)
        self.assertEqual(stored[3], -17592186044416)
        self.assertEqual(stored[4], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_v2I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_v2I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                -17592186044416,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_q_id_(
                None, objc.simd.vector_uint2(0, 1), False, -17592186044416, "hello"
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                NoBool(),
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                None,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                -17592186044416,
                NoObjCValueObject,
            )

    def test_idv3f_v2I_i_Z_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv3f_v2I_i_Z_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_i_Z_q_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_i_Z_q_id_, 1, b"<2I>")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_i_Z_q_id_, 2, b"i")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_i_Z_q_id_, 3, b"Z")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_i_Z_q_id_, 4, b"q")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_i_Z_q_id_, 5, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv3f_v2I_i_Z_q_id_(
            objc.simd.vector_float3(0.0, 1.5, 3.0),
            objc.simd.vector_uint2(0, 1),
            -42,
            False,
            -17592186044416,
            "hello",
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 6)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], objc.simd.vector_uint2(0, 1))
        self.assertEqual(stored[2], -42)
        self.assertEqual(stored[3], False)
        self.assertEqual(stored[4], -17592186044416)
        self.assertEqual(stored[5], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_v2I_i_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -42,
                False,
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_v2I_i_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -42,
                False,
                -17592186044416,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_i_Z_q_id_(
                None, objc.simd.vector_uint2(0, 1), -42, False, -17592186044416, "hello"
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_i_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                -42,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_i_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                None,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_i_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -42,
                NoBool(),
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_i_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -42,
                False,
                None,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_i_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -42,
                False,
                -17592186044416,
                NoObjCValueObject,
            )

    def test_idv3f_v2I_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv3f_v2I_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_q_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_q_id_, 1, b"<2I>")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_q_id_, 2, b"q")
        self.assertArgHasType(OC_VectorCall.idv3f_v2I_q_id_, 3, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv3f_v2I_q_id_(
            objc.simd.vector_float3(0.0, 1.5, 3.0),
            objc.simd.vector_uint2(0, 1),
            -17592186044416,
            "hello",
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 4)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], objc.simd.vector_uint2(0, 1))
        self.assertEqual(stored[2], -17592186044416)
        self.assertEqual(stored[3], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_v2I_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_v2I_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -17592186044416,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_q_id_(
                None, objc.simd.vector_uint2(0, 1), -17592186044416, "hello"
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0), None, -17592186044416, "hello"
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                None,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v2I_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -17592186044416,
                NoObjCValueObject,
            )

    def test_idv3f_v3I_Z_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv3f_v3I_Z_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.idv3f_v3I_Z_q_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.idv3f_v3I_Z_q_id_, 1, b"<3I>")
        self.assertArgHasType(OC_VectorCall.idv3f_v3I_Z_q_id_, 2, b"Z")
        self.assertArgHasType(OC_VectorCall.idv3f_v3I_Z_q_id_, 3, b"q")
        self.assertArgHasType(OC_VectorCall.idv3f_v3I_Z_q_id_, 4, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv3f_v3I_Z_q_id_(
            objc.simd.vector_float3(0.0, 1.5, 3.0),
            objc.simd.vector_uint3(0, 1, 2),
            False,
            -17592186044416,
            "hello",
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 5)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], objc.simd.vector_uint3(0, 1, 2))
        self.assertEqual(stored[2], False)
        self.assertEqual(stored[3], -17592186044416)
        self.assertEqual(stored[4], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_v3I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                False,
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_v3I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                False,
                -17592186044416,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v3I_Z_q_id_(
                None, objc.simd.vector_uint3(0, 1, 2), False, -17592186044416, "hello"
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v3I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v3I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                NoBool(),
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v3I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                False,
                None,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v3I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                False,
                -17592186044416,
                NoObjCValueObject,
            )

    def test_idv3f_v3I_q_Z_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv3f_v3I_q_Z_id_, b"@")
        self.assertArgHasType(OC_VectorCall.idv3f_v3I_q_Z_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.idv3f_v3I_q_Z_id_, 1, b"<3I>")
        self.assertArgHasType(OC_VectorCall.idv3f_v3I_q_Z_id_, 2, b"q")
        self.assertArgHasType(OC_VectorCall.idv3f_v3I_q_Z_id_, 3, b"Z")
        self.assertArgHasType(OC_VectorCall.idv3f_v3I_q_Z_id_, 4, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv3f_v3I_q_Z_id_(
            objc.simd.vector_float3(0.0, 1.5, 3.0),
            objc.simd.vector_uint3(0, 1, 2),
            -17592186044416,
            False,
            "hello",
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 5)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], objc.simd.vector_uint3(0, 1, 2))
        self.assertEqual(stored[2], -17592186044416)
        self.assertEqual(stored[3], False)
        self.assertEqual(stored[4], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_v3I_q_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                -17592186044416,
                False,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_v3I_q_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                -17592186044416,
                False,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v3I_q_Z_id_(
                None, objc.simd.vector_uint3(0, 1, 2), -17592186044416, False, "hello"
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v3I_q_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v3I_q_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                None,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v3I_q_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                -17592186044416,
                NoBool(),
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_v3I_q_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                -17592186044416,
                False,
                NoObjCValueObject,
            )

    def test_idv3f_Q_Q_q_Z_Z_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv3f_Q_Q_q_Z_Z_id_, b"@")
        self.assertArgHasType(OC_VectorCall.idv3f_Q_Q_q_Z_Z_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.idv3f_Q_Q_q_Z_Z_id_, 1, b"Q")
        self.assertArgHasType(OC_VectorCall.idv3f_Q_Q_q_Z_Z_id_, 2, b"Q")
        self.assertArgHasType(OC_VectorCall.idv3f_Q_Q_q_Z_Z_id_, 3, b"q")
        self.assertArgHasType(OC_VectorCall.idv3f_Q_Q_q_Z_Z_id_, 4, b"Z")
        self.assertArgHasType(OC_VectorCall.idv3f_Q_Q_q_Z_Z_id_, 5, b"Z")
        self.assertArgHasType(OC_VectorCall.idv3f_Q_Q_q_Z_Z_id_, 6, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv3f_Q_Q_q_Z_Z_id_(
            objc.simd.vector_float3(0.0, 1.5, 3.0),
            35184372088832,
            35184372088832,
            -17592186044416,
            False,
            False,
            "hello",
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 7)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], 35184372088832)
        self.assertEqual(stored[2], 35184372088832)
        self.assertEqual(stored[3], -17592186044416)
        self.assertEqual(stored[4], False)
        self.assertEqual(stored[5], False)
        self.assertEqual(stored[6], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_Q_Q_q_Z_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                False,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_Q_Q_q_Z_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                False,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_Q_Q_q_Z_Z_id_(
                None,
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_Q_Q_q_Z_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                35184372088832,
                -17592186044416,
                False,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_Q_Q_q_Z_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                35184372088832,
                None,
                -17592186044416,
                False,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_Q_Q_q_Z_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                35184372088832,
                35184372088832,
                None,
                False,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_Q_Q_q_Z_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                35184372088832,
                35184372088832,
                -17592186044416,
                NoBool(),
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_Q_Q_q_Z_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                NoBool(),
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_Q_Q_q_Z_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                False,
                NoObjCValueObject,
            )

    def test_idv3f_Z_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv3f_Z_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.idv3f_Z_q_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.idv3f_Z_q_id_, 1, b"Z")
        self.assertArgHasType(OC_VectorCall.idv3f_Z_q_id_, 2, b"q")
        self.assertArgHasType(OC_VectorCall.idv3f_Z_q_id_, 3, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv3f_Z_q_id_(
            objc.simd.vector_float3(0.0, 1.5, 3.0), False, -17592186044416, "hello"
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 4)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], False)
        self.assertEqual(stored[2], -17592186044416)
        self.assertEqual(stored[3], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0), False, -17592186044416
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv3f_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                False,
                -17592186044416,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_Z_q_id_(None, False, -17592186044416, "hello")

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                NoBool(),
                -17592186044416,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0), False, None, "hello"
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idv3f_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                False,
                -17592186044416,
                NoObjCValueObject,
            )

    def test_idv4f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idv4f_, b"@")
        self.assertArgHasType(OC_VectorCall.idv4f_, 0, b"<4f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idv4f_(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv4f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idv4f_(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idv4f_(None)

    def test_idid_v2d_v2d_v2i_Z_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_v2d_v2d_v2i_Z_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_v2d_v2d_v2i_Z_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.idid_v2d_v2d_v2i_Z_, 1, b"<2d>")
        self.assertArgHasType(OC_VectorCall.idid_v2d_v2d_v2i_Z_, 2, b"<2d>")
        self.assertArgHasType(OC_VectorCall.idid_v2d_v2d_v2i_Z_, 3, b"<2i>")
        self.assertArgHasType(OC_VectorCall.idid_v2d_v2d_v2i_Z_, 4, b"Z")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_v2d_v2d_v2i_Z_(
            "hello",
            objc.simd.vector_double2(0.0, 1.5),
            objc.simd.vector_double2(0.0, 1.5),
            objc.simd.vector_int2(0, 1),
            False,
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 5)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], objc.simd.vector_double2(0.0, 1.5))
        self.assertEqual(stored[2], objc.simd.vector_double2(0.0, 1.5))
        self.assertEqual(stored[3], objc.simd.vector_int2(0, 1))
        self.assertEqual(stored[4], False)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_v2d_v2d_v2i_Z_(
                "hello",
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_int2(0, 1),
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_v2d_v2d_v2i_Z_(
                "hello",
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_int2(0, 1),
                False,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_v2d_v2d_v2i_Z_(
                NoObjCValueObject,
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_int2(0, 1),
                False,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_v2d_v2d_v2i_Z_(
                "hello",
                None,
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_int2(0, 1),
                False,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_v2d_v2d_v2i_Z_(
                "hello",
                objc.simd.vector_double2(0.0, 1.5),
                None,
                objc.simd.vector_int2(0, 1),
                False,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_v2d_v2d_v2i_Z_(
                "hello",
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_double2(0.0, 1.5),
                None,
                False,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_v2d_v2d_v2i_Z_(
                "hello",
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_int2(0, 1),
                NoBool(),
            )

    def test_idid_v2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_v2f_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_v2f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.idid_v2f_, 1, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_v2f_("hello", objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_v2f_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_v2f_("hello", objc.simd.vector_float2(0.0, 1.5), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_v2f_(NoObjCValueObject, objc.simd.vector_float2(0.0, 1.5))

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_v2f_("hello", None)

    def test_idid_v3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_v3f_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_v3f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.idid_v3f_, 1, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_v3f_("hello", objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_v3f_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_v3f_("hello", objc.simd.vector_float3(0.0, 1.5, 3.0), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_v3f_(NoObjCValueObject, objc.simd.vector_float3(0.0, 1.5, 3.0))

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_v3f_("hello", None)

    def test_idid_v4f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_v4f_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_v4f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.idid_v4f_, 1, b"<4f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_v4f_("hello", objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_v4f_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_v4f_("hello", objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_v4f_(NoObjCValueObject, objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_v4f_("hello", None)

    def test_idid_id_v2i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_id_v2i_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_id_v2i_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.idid_id_v2i_, 1, b"@")
        self.assertArgHasType(OC_VectorCall.idid_id_v2i_, 2, b"<2i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_id_v2i_("hello", "hello", objc.simd.vector_int2(0, 1))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 3)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], "hello")
        self.assertEqual(stored[2], objc.simd.vector_int2(0, 1))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_id_v2i_("hello", "hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_id_v2i_("hello", "hello", objc.simd.vector_int2(0, 1), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_id_v2i_(NoObjCValueObject, "hello", objc.simd.vector_int2(0, 1))

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_id_v2i_("hello", NoObjCValueObject, objc.simd.vector_int2(0, 1))

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_id_v2i_("hello", "hello", None)

    def test_idid_id_v2i_f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_id_v2i_f_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_id_v2i_f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.idid_id_v2i_f_, 1, b"@")
        self.assertArgHasType(OC_VectorCall.idid_id_v2i_f_, 2, b"<2i>")
        self.assertArgHasType(OC_VectorCall.idid_id_v2i_f_, 3, b"f")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_id_v2i_f_(
            "hello", "hello", objc.simd.vector_int2(0, 1), 2500000000.0
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 4)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], "hello")
        self.assertEqual(stored[2], objc.simd.vector_int2(0, 1))
        self.assertEqual(stored[3], 2500000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_id_v2i_f_("hello", "hello", objc.simd.vector_int2(0, 1))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_id_v2i_f_(
                "hello", "hello", objc.simd.vector_int2(0, 1), 2500000000.0, "hello"
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_id_v2i_f_(
                NoObjCValueObject, "hello", objc.simd.vector_int2(0, 1), 2500000000.0
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_id_v2i_f_(
                "hello", NoObjCValueObject, objc.simd.vector_int2(0, 1), 2500000000.0
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_id_v2i_f_("hello", "hello", None, 2500000000.0)

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_id_v2i_f_("hello", "hello", objc.simd.vector_int2(0, 1), None)

    def test_idid_Q_v2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_Q_v2f_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_Q_v2f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.idid_Q_v2f_, 1, b"Q")
        self.assertArgHasType(OC_VectorCall.idid_Q_v2f_, 2, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_Q_v2f_("hello", 35184372088832, objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 3)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], 35184372088832)
        self.assertEqual(stored[2], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_Q_v2f_("hello", 35184372088832)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_Q_v2f_(
                "hello", 35184372088832, objc.simd.vector_float2(0.0, 1.5), "hello"
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Q_v2f_(
                NoObjCValueObject, 35184372088832, objc.simd.vector_float2(0.0, 1.5)
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Q_v2f_("hello", None, objc.simd.vector_float2(0.0, 1.5))

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Q_v2f_("hello", 35184372088832, None)

    def test_idid_Q_v3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_Q_v3f_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_Q_v3f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.idid_Q_v3f_, 1, b"Q")
        self.assertArgHasType(OC_VectorCall.idid_Q_v3f_, 2, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_Q_v3f_(
            "hello", 35184372088832, objc.simd.vector_float3(0.0, 1.5, 3.0)
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 3)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], 35184372088832)
        self.assertEqual(stored[2], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_Q_v3f_("hello", 35184372088832)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_Q_v3f_(
                "hello", 35184372088832, objc.simd.vector_float3(0.0, 1.5, 3.0), "hello"
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Q_v3f_(
                NoObjCValueObject,
                35184372088832,
                objc.simd.vector_float3(0.0, 1.5, 3.0),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Q_v3f_("hello", None, objc.simd.vector_float3(0.0, 1.5, 3.0))

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Q_v3f_("hello", 35184372088832, None)

    def test_idid_Q_v4f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_Q_v4f_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_Q_v4f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.idid_Q_v4f_, 1, b"Q")
        self.assertArgHasType(OC_VectorCall.idid_Q_v4f_, 2, b"<4f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_Q_v4f_(
            "hello", 35184372088832, objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5)
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 3)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], 35184372088832)
        self.assertEqual(stored[2], objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_Q_v4f_("hello", 35184372088832)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_Q_v4f_(
                "hello",
                35184372088832,
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Q_v4f_(
                NoObjCValueObject,
                35184372088832,
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Q_v4f_("hello", None, objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Q_v4f_("hello", 35184372088832, None)

    def test_idid_Q_matrixfloat4x4_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_Q_matrixfloat4x4_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_Q_matrixfloat4x4_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.idid_Q_matrixfloat4x4_, 1, b"Q")
        self.assertArgHasType(
            OC_VectorCall.idid_Q_matrixfloat4x4_, 2, b"{_matrix_float4x4=[4<4f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_Q_matrixfloat4x4_(
            "hello",
            35184372088832,
            simd.matrix_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 3)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], 35184372088832)
        self.assertEqual(
            stored[2],
            simd.matrix_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_Q_matrixfloat4x4_("hello", 35184372088832)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_Q_matrixfloat4x4_(
                "hello",
                35184372088832,
                simd.matrix_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Q_matrixfloat4x4_(
                NoObjCValueObject,
                35184372088832,
                simd.matrix_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Q_matrixfloat4x4_(
                "hello",
                None,
                simd.matrix_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Q_matrixfloat4x4_("hello", 35184372088832, None)

    def test_idid_Z_id_v2i_q_Q_q_Z_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_Z_id_v2i_q_Q_q_Z_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_Z_id_v2i_q_Q_q_Z_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.idid_Z_id_v2i_q_Q_q_Z_, 1, b"Z")
        self.assertArgHasType(OC_VectorCall.idid_Z_id_v2i_q_Q_q_Z_, 2, b"@")
        self.assertArgHasType(OC_VectorCall.idid_Z_id_v2i_q_Q_q_Z_, 3, b"<2i>")
        self.assertArgHasType(OC_VectorCall.idid_Z_id_v2i_q_Q_q_Z_, 4, b"q")
        self.assertArgHasType(OC_VectorCall.idid_Z_id_v2i_q_Q_q_Z_, 5, b"Q")
        self.assertArgHasType(OC_VectorCall.idid_Z_id_v2i_q_Q_q_Z_, 6, b"q")
        self.assertArgHasType(OC_VectorCall.idid_Z_id_v2i_q_Q_q_Z_, 7, b"Z")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_Z_id_v2i_q_Q_q_Z_(
            "hello",
            False,
            "hello",
            objc.simd.vector_int2(0, 1),
            -17592186044416,
            35184372088832,
            -17592186044416,
            False,
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 8)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], False)
        self.assertEqual(stored[2], "hello")
        self.assertEqual(stored[3], objc.simd.vector_int2(0, 1))
        self.assertEqual(stored[4], -17592186044416)
        self.assertEqual(stored[5], 35184372088832)
        self.assertEqual(stored[6], -17592186044416)
        self.assertEqual(stored[7], False)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_Z_id_v2i_q_Q_q_Z_(
                "hello",
                False,
                "hello",
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                35184372088832,
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_Z_id_v2i_q_Q_q_Z_(
                "hello",
                False,
                "hello",
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                35184372088832,
                -17592186044416,
                False,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Z_id_v2i_q_Q_q_Z_(
                NoObjCValueObject,
                False,
                "hello",
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                35184372088832,
                -17592186044416,
                False,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Z_id_v2i_q_Q_q_Z_(
                "hello",
                NoBool(),
                "hello",
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                35184372088832,
                -17592186044416,
                False,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Z_id_v2i_q_Q_q_Z_(
                "hello",
                False,
                NoObjCValueObject,
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                35184372088832,
                -17592186044416,
                False,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Z_id_v2i_q_Q_q_Z_(
                "hello",
                False,
                "hello",
                None,
                -17592186044416,
                35184372088832,
                -17592186044416,
                False,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Z_id_v2i_q_Q_q_Z_(
                "hello",
                False,
                "hello",
                objc.simd.vector_int2(0, 1),
                None,
                35184372088832,
                -17592186044416,
                False,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Z_id_v2i_q_Q_q_Z_(
                "hello",
                False,
                "hello",
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                None,
                -17592186044416,
                False,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Z_id_v2i_q_Q_q_Z_(
                "hello",
                False,
                "hello",
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                35184372088832,
                None,
                False,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_Z_id_v2i_q_Q_q_Z_(
                "hello",
                False,
                "hello",
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                35184372088832,
                -17592186044416,
                NoBool(),
            )

    def test_idid_q_v2i_f_f_f_f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_, 1, b"q")
        self.assertArgHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_, 2, b"<2i>")
        self.assertArgHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_, 3, b"f")
        self.assertArgHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_, 4, b"f")
        self.assertArgHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_, 5, b"f")
        self.assertArgHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_, 6, b"f")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_q_v2i_f_f_f_f_(
            "hello",
            -17592186044416,
            objc.simd.vector_int2(0, 1),
            2500000000.0,
            2500000000.0,
            2500000000.0,
            2500000000.0,
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 7)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], -17592186044416)
        self.assertEqual(stored[2], objc.simd.vector_int2(0, 1))
        self.assertEqual(stored[3], 2500000000.0)
        self.assertEqual(stored[4], 2500000000.0)
        self.assertEqual(stored[5], 2500000000.0)
        self.assertEqual(stored[6], 2500000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_q_v2i_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_q_v2i_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_q_v2i_f_f_f_f_(
                NoObjCValueObject,
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_q_v2i_f_f_f_f_(
                "hello",
                None,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_q_v2i_f_f_f_f_(
                "hello",
                -17592186044416,
                None,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_q_v2i_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                None,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_q_v2i_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                None,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_q_v2i_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                None,
                2500000000.0,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_q_v2i_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                None,
            )

    def test_idid_q_v2i_f_f_f_f_f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_f_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_f_, 1, b"q")
        self.assertArgHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_f_, 2, b"<2i>")
        self.assertArgHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_f_, 3, b"f")
        self.assertArgHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_f_, 4, b"f")
        self.assertArgHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_f_, 5, b"f")
        self.assertArgHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_f_, 6, b"f")
        self.assertArgHasType(OC_VectorCall.idid_q_v2i_f_f_f_f_f_, 7, b"f")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_q_v2i_f_f_f_f_f_(
            "hello",
            -17592186044416,
            objc.simd.vector_int2(0, 1),
            2500000000.0,
            2500000000.0,
            2500000000.0,
            2500000000.0,
            2500000000.0,
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 8)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], -17592186044416)
        self.assertEqual(stored[2], objc.simd.vector_int2(0, 1))
        self.assertEqual(stored[3], 2500000000.0)
        self.assertEqual(stored[4], 2500000000.0)
        self.assertEqual(stored[5], 2500000000.0)
        self.assertEqual(stored[6], 2500000000.0)
        self.assertEqual(stored[7], 2500000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_q_v2i_f_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_q_v2i_f_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_q_v2i_f_f_f_f_f_(
                NoObjCValueObject,
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_q_v2i_f_f_f_f_f_(
                "hello",
                None,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_q_v2i_f_f_f_f_f_(
                "hello",
                -17592186044416,
                None,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_q_v2i_f_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                None,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_q_v2i_f_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                None,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_q_v2i_f_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                None,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_q_v2i_f_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                None,
                2500000000.0,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_q_v2i_f_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                None,
            )

    def test_idid_GKBox_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_GKBox_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_GKBox_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.idid_GKBox_, 1, b"{GKBox=<3f><3f>}")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_GKBox_(
            "hello",
            (
                objc.simd.vector_float3(1.0, 2.0, 3.0),
                objc.simd.vector_float3(4.0, 5.0, 6.0),
            ),
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(
            stored[1],
            (
                objc.simd.vector_float3(1.0, 2.0, 3.0),
                objc.simd.vector_float3(4.0, 5.0, 6.0),
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_GKBox_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_GKBox_(
                "hello",
                (
                    objc.simd.vector_float3(1.0, 2.0, 3.0),
                    objc.simd.vector_float3(4.0, 5.0, 6.0),
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_GKBox_(
                NoObjCValueObject,
                (
                    objc.simd.vector_float3(1.0, 2.0, 3.0),
                    objc.simd.vector_float3(4.0, 5.0, 6.0),
                ),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_GKBox_("hello", None)

    def test_idid_GKQuad_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_GKQuad_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_GKQuad_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.idid_GKQuad_, 1, b"{GKQuad=<2f><2f>}")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_GKQuad_(
            "hello",
            (objc.simd.vector_float2(9.0, 10.0), objc.simd.vector_float2(11.0, 12.0)),
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(
            stored[1],
            (objc.simd.vector_float2(9.0, 10.0), objc.simd.vector_float2(11.0, 12.0)),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_GKQuad_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_GKQuad_(
                "hello",
                (
                    objc.simd.vector_float2(9.0, 10.0),
                    objc.simd.vector_float2(11.0, 12.0),
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_GKQuad_(
                NoObjCValueObject,
                (
                    objc.simd.vector_float2(9.0, 10.0),
                    objc.simd.vector_float2(11.0, 12.0),
                ),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_GKQuad_("hello", None)

    def test_idid_MDLAxisAlignedBoundingBox_f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_MDLAxisAlignedBoundingBox_f_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_MDLAxisAlignedBoundingBox_f_, 0, b"@")
        self.assertArgHasType(
            OC_VectorCall.idid_MDLAxisAlignedBoundingBox_f_,
            1,
            b"{_MDLAxisAlignedBoundingBox=<3f><3f>}",
        )
        self.assertArgHasType(OC_VectorCall.idid_MDLAxisAlignedBoundingBox_f_, 2, b"f")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_MDLAxisAlignedBoundingBox_f_(
            "hello",
            (
                objc.simd.vector_float3(-8.0, -9.0, -10.0),
                objc.simd.vector_float3(-11.0, -12.0, -13.0),
            ),
            2500000000.0,
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 3)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(
            stored[1],
            (
                objc.simd.vector_float3(-8.0, -9.0, -10.0),
                objc.simd.vector_float3(-11.0, -12.0, -13.0),
            ),
        )
        self.assertEqual(stored[2], 2500000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_MDLAxisAlignedBoundingBox_f_(
                "hello",
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                ),
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_MDLAxisAlignedBoundingBox_f_(
                "hello",
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                ),
                2500000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_MDLAxisAlignedBoundingBox_f_(
                NoObjCValueObject,
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                ),
                2500000000.0,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_MDLAxisAlignedBoundingBox_f_("hello", None, 2500000000.0)

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_MDLAxisAlignedBoundingBox_f_(
                "hello",
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                ),
                None,
            )

    def test_idid_matrixfloat2x2_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_matrixfloat2x2_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_matrixfloat2x2_, 0, b"@")
        self.assertArgHasType(
            OC_VectorCall.idid_matrixfloat2x2_, 1, b"{_matrix_float2x2=[2<2f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_matrixfloat2x2_(
            "hello",
            simd.matrix_float2x2(
                (objc.simd.vector_float2(0.0, 1.5), objc.simd.vector_float2(0.0, 1.5))
            ),
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(
            stored[1],
            simd.matrix_float2x2(
                (objc.simd.vector_float2(0.0, 1.5), objc.simd.vector_float2(0.0, 1.5))
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_matrixfloat2x2_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_matrixfloat2x2_(
                "hello",
                simd.matrix_float2x2(
                    (
                        objc.simd.vector_float2(0.0, 1.5),
                        objc.simd.vector_float2(0.0, 1.5),
                    )
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_matrixfloat2x2_(
                NoObjCValueObject,
                simd.matrix_float2x2(
                    (
                        objc.simd.vector_float2(0.0, 1.5),
                        objc.simd.vector_float2(0.0, 1.5),
                    )
                ),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_matrixfloat2x2_("hello", None)

    def test_idid_matrixfloat3x3_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_matrixfloat3x3_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_matrixfloat3x3_, 0, b"@")
        self.assertArgHasType(
            OC_VectorCall.idid_matrixfloat3x3_, 1, b"{_matrix_float3x3=[3<3f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_matrixfloat3x3_(
            "hello",
            simd.matrix_float3x3(
                (
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                )
            ),
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(
            stored[1],
            simd.matrix_float3x3(
                (
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                )
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_matrixfloat3x3_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_matrixfloat3x3_(
                "hello",
                simd.matrix_float3x3(
                    (
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                    )
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_matrixfloat3x3_(
                NoObjCValueObject,
                simd.matrix_float3x3(
                    (
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                    )
                ),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_matrixfloat3x3_("hello", None)

    def test_idid_matrixfloat4x4_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idid_matrixfloat4x4_, b"@")
        self.assertArgHasType(OC_VectorCall.idid_matrixfloat4x4_, 0, b"@")
        self.assertArgHasType(
            OC_VectorCall.idid_matrixfloat4x4_, 1, b"{_matrix_float4x4=[4<4f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idid_matrixfloat4x4_(
            "hello",
            simd.matrix_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(
            stored[1],
            simd.matrix_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_matrixfloat4x4_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idid_matrixfloat4x4_(
                "hello",
                simd.matrix_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idid_matrixfloat4x4_(
                NoObjCValueObject,
                simd.matrix_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idid_matrixfloat4x4_("hello", None)

    def test_idCGColor_CGColor_id_v2i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idCGColor_CGColor_id_v2i_, b"@")
        self.assertArgHasType(
            OC_VectorCall.idCGColor_CGColor_id_v2i_, 0, b"^{CGColor=}"
        )
        self.assertArgHasType(
            OC_VectorCall.idCGColor_CGColor_id_v2i_, 1, b"^{CGColor=}"
        )
        self.assertArgHasType(OC_VectorCall.idCGColor_CGColor_id_v2i_, 2, b"@")
        self.assertArgHasType(OC_VectorCall.idCGColor_CGColor_id_v2i_, 3, b"<2i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idCGColor_CGColor_id_v2i_(
            "color!", "color!", "hello", objc.simd.vector_int2(0, 1)
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 4)
        self.assertEqual(stored[0], "color!")
        self.assertEqual(stored[1], "color!")
        self.assertEqual(stored[2], "hello")
        self.assertEqual(stored[3], objc.simd.vector_int2(0, 1))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idCGColor_CGColor_id_v2i_("color!", "color!", "hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idCGColor_CGColor_id_v2i_(
                "color!", "color!", "hello", objc.simd.vector_int2(0, 1), "hello"
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idCGColor_CGColor_id_v2i_(
                NoObjCValueObject, "color!", "hello", objc.simd.vector_int2(0, 1)
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idCGColor_CGColor_id_v2i_(
                "color!", NoObjCValueObject, "hello", objc.simd.vector_int2(0, 1)
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idCGColor_CGColor_id_v2i_(
                "color!", "color!", NoObjCValueObject, objc.simd.vector_int2(0, 1)
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idCGColor_CGColor_id_v2i_("color!", "color!", "hello", None)

    def test_idf_v2f_v2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idf_v2f_v2f_, b"@")
        self.assertArgHasType(OC_VectorCall.idf_v2f_v2f_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.idf_v2f_v2f_, 1, b"<2f>")
        self.assertArgHasType(OC_VectorCall.idf_v2f_v2f_, 2, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idf_v2f_v2f_(
            2500000000.0,
            objc.simd.vector_float2(0.0, 1.5),
            objc.simd.vector_float2(0.0, 1.5),
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 3)
        self.assertEqual(stored[0], 2500000000.0)
        self.assertEqual(stored[1], objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(stored[2], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_v2f_v2f_(2500000000.0, objc.simd.vector_float2(0.0, 1.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_v2f_v2f_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_v2f_(
                None,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_v2f_(2500000000.0, None, objc.simd.vector_float2(0.0, 1.5))

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_v2f_(2500000000.0, objc.simd.vector_float2(0.0, 1.5), None)

    def test_idf_v2f_v2f_Class_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idf_v2f_v2f_Class_, b"@")
        self.assertArgHasType(OC_VectorCall.idf_v2f_v2f_Class_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.idf_v2f_v2f_Class_, 1, b"<2f>")
        self.assertArgHasType(OC_VectorCall.idf_v2f_v2f_Class_, 2, b"<2f>")
        self.assertArgHasType(OC_VectorCall.idf_v2f_v2f_Class_, 3, b"#")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idf_v2f_v2f_Class_(
            2500000000.0,
            objc.simd.vector_float2(0.0, 1.5),
            objc.simd.vector_float2(0.0, 1.5),
            objc.lookUpClass("NSObject"),
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 4)
        self.assertEqual(stored[0], 2500000000.0)
        self.assertEqual(stored[1], objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(stored[2], objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(stored[3], objc.lookUpClass("NSObject"))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_v2f_v2f_Class_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_v2f_v2f_Class_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                objc.lookUpClass("NSObject"),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_v2f_Class_(
                None,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                objc.lookUpClass("NSObject"),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_v2f_Class_(
                2500000000.0,
                None,
                objc.simd.vector_float2(0.0, 1.5),
                objc.lookUpClass("NSObject"),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_v2f_Class_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                None,
                objc.lookUpClass("NSObject"),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_v2f_Class_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                42,
            )

    def test_idf_v2f_Q_Q_Q_q_Z_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idf_v2f_Q_Q_Q_q_Z_id_, b"@")
        self.assertArgHasType(OC_VectorCall.idf_v2f_Q_Q_Q_q_Z_id_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.idf_v2f_Q_Q_Q_q_Z_id_, 1, b"<2f>")
        self.assertArgHasType(OC_VectorCall.idf_v2f_Q_Q_Q_q_Z_id_, 2, b"Q")
        self.assertArgHasType(OC_VectorCall.idf_v2f_Q_Q_Q_q_Z_id_, 3, b"Q")
        self.assertArgHasType(OC_VectorCall.idf_v2f_Q_Q_Q_q_Z_id_, 4, b"Q")
        self.assertArgHasType(OC_VectorCall.idf_v2f_Q_Q_Q_q_Z_id_, 5, b"q")
        self.assertArgHasType(OC_VectorCall.idf_v2f_Q_Q_Q_q_Z_id_, 6, b"Z")
        self.assertArgHasType(OC_VectorCall.idf_v2f_Q_Q_Q_q_Z_id_, 7, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idf_v2f_Q_Q_Q_q_Z_id_(
            2500000000.0,
            objc.simd.vector_float2(0.0, 1.5),
            35184372088832,
            35184372088832,
            35184372088832,
            -17592186044416,
            False,
            "hello",
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 8)
        self.assertEqual(stored[0], 2500000000.0)
        self.assertEqual(stored[1], objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(stored[2], 35184372088832)
        self.assertEqual(stored[3], 35184372088832)
        self.assertEqual(stored[4], 35184372088832)
        self.assertEqual(stored[5], -17592186044416)
        self.assertEqual(stored[6], False)
        self.assertEqual(stored[7], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_Q_Q_Q_q_Z_id_(
                None,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                None,
                35184372088832,
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                None,
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                None,
                35184372088832,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                None,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                35184372088832,
                None,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                35184372088832,
                -17592186044416,
                NoBool(),
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                NoObjCValueObject,
            )

    def test_idf_v2f_Q_Q_q_Z_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idf_v2f_Q_Q_q_Z_id_, b"@")
        self.assertArgHasType(OC_VectorCall.idf_v2f_Q_Q_q_Z_id_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.idf_v2f_Q_Q_q_Z_id_, 1, b"<2f>")
        self.assertArgHasType(OC_VectorCall.idf_v2f_Q_Q_q_Z_id_, 2, b"Q")
        self.assertArgHasType(OC_VectorCall.idf_v2f_Q_Q_q_Z_id_, 3, b"Q")
        self.assertArgHasType(OC_VectorCall.idf_v2f_Q_Q_q_Z_id_, 4, b"q")
        self.assertArgHasType(OC_VectorCall.idf_v2f_Q_Q_q_Z_id_, 5, b"Z")
        self.assertArgHasType(OC_VectorCall.idf_v2f_Q_Q_q_Z_id_, 6, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idf_v2f_Q_Q_q_Z_id_(
            2500000000.0,
            objc.simd.vector_float2(0.0, 1.5),
            35184372088832,
            35184372088832,
            -17592186044416,
            False,
            "hello",
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 7)
        self.assertEqual(stored[0], 2500000000.0)
        self.assertEqual(stored[1], objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(stored[2], 35184372088832)
        self.assertEqual(stored[3], 35184372088832)
        self.assertEqual(stored[4], -17592186044416)
        self.assertEqual(stored[5], False)
        self.assertEqual(stored[6], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_v2f_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_v2f_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_Q_Q_q_Z_id_(
                None,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_Q_Q_q_Z_id_(
                2500000000.0,
                None,
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                None,
                35184372088832,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                None,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                None,
                False,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                -17592186044416,
                NoBool(),
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_v2f_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                NoObjCValueObject,
            )

    def test_idf_id_v2i_i_q_Z_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idf_id_v2i_i_q_Z_, b"@")
        self.assertArgHasType(OC_VectorCall.idf_id_v2i_i_q_Z_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.idf_id_v2i_i_q_Z_, 1, b"@")
        self.assertArgHasType(OC_VectorCall.idf_id_v2i_i_q_Z_, 2, b"<2i>")
        self.assertArgHasType(OC_VectorCall.idf_id_v2i_i_q_Z_, 3, b"i")
        self.assertArgHasType(OC_VectorCall.idf_id_v2i_i_q_Z_, 4, b"q")
        self.assertArgHasType(OC_VectorCall.idf_id_v2i_i_q_Z_, 5, b"Z")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idf_id_v2i_i_q_Z_(
            2500000000.0,
            "hello",
            objc.simd.vector_int2(0, 1),
            -42,
            -17592186044416,
            False,
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 6)
        self.assertEqual(stored[0], 2500000000.0)
        self.assertEqual(stored[1], "hello")
        self.assertEqual(stored[2], objc.simd.vector_int2(0, 1))
        self.assertEqual(stored[3], -42)
        self.assertEqual(stored[4], -17592186044416)
        self.assertEqual(stored[5], False)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_id_v2i_i_q_Z_(
                2500000000.0, "hello", objc.simd.vector_int2(0, 1), -42, -17592186044416
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_id_v2i_i_q_Z_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                False,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_i_q_Z_(
                None, "hello", objc.simd.vector_int2(0, 1), -42, -17592186044416, False
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_i_q_Z_(
                2500000000.0,
                NoObjCValueObject,
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                False,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_i_q_Z_(
                2500000000.0, "hello", None, -42, -17592186044416, False
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_i_q_Z_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                None,
                -17592186044416,
                False,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_i_q_Z_(
                2500000000.0, "hello", objc.simd.vector_int2(0, 1), -42, None, False
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_i_q_Z_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                NoBool(),
            )

    def test_idf_id_v2i_i_q_CGColor_CGColor_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idf_id_v2i_i_q_CGColor_CGColor_, b"@")
        self.assertArgHasType(OC_VectorCall.idf_id_v2i_i_q_CGColor_CGColor_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.idf_id_v2i_i_q_CGColor_CGColor_, 1, b"@")
        self.assertArgHasType(OC_VectorCall.idf_id_v2i_i_q_CGColor_CGColor_, 2, b"<2i>")
        self.assertArgHasType(OC_VectorCall.idf_id_v2i_i_q_CGColor_CGColor_, 3, b"i")
        self.assertArgHasType(OC_VectorCall.idf_id_v2i_i_q_CGColor_CGColor_, 4, b"q")
        self.assertArgHasType(
            OC_VectorCall.idf_id_v2i_i_q_CGColor_CGColor_, 5, b"^{CGColor=}"
        )
        self.assertArgHasType(
            OC_VectorCall.idf_id_v2i_i_q_CGColor_CGColor_, 6, b"^{CGColor=}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idf_id_v2i_i_q_CGColor_CGColor_(
            2500000000.0,
            "hello",
            objc.simd.vector_int2(0, 1),
            -42,
            -17592186044416,
            "color!",
            "color!",
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 7)
        self.assertEqual(stored[0], 2500000000.0)
        self.assertEqual(stored[1], "hello")
        self.assertEqual(stored[2], objc.simd.vector_int2(0, 1))
        self.assertEqual(stored[3], -42)
        self.assertEqual(stored[4], -17592186044416)
        self.assertEqual(stored[5], "color!")
        self.assertEqual(stored[6], "color!")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_id_v2i_i_q_CGColor_CGColor_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                "color!",
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_id_v2i_i_q_CGColor_CGColor_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                "color!",
                "color!",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_i_q_CGColor_CGColor_(
                None,
                "hello",
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                "color!",
                "color!",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_i_q_CGColor_CGColor_(
                2500000000.0,
                NoObjCValueObject,
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                "color!",
                "color!",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_i_q_CGColor_CGColor_(
                2500000000.0, "hello", None, -42, -17592186044416, "color!", "color!"
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_i_q_CGColor_CGColor_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                None,
                -17592186044416,
                "color!",
                "color!",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_i_q_CGColor_CGColor_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                -42,
                None,
                "color!",
                "color!",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_i_q_CGColor_CGColor_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                NoObjCValueObject,
                "color!",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_i_q_CGColor_CGColor_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                "color!",
                NoObjCValueObject,
            )

    def test_idf_id_v2i_q_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idf_id_v2i_q_, b"@")
        self.assertArgHasType(OC_VectorCall.idf_id_v2i_q_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.idf_id_v2i_q_, 1, b"@")
        self.assertArgHasType(OC_VectorCall.idf_id_v2i_q_, 2, b"<2i>")
        self.assertArgHasType(OC_VectorCall.idf_id_v2i_q_, 3, b"q")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idf_id_v2i_q_(
            2500000000.0, "hello", objc.simd.vector_int2(0, 1), -17592186044416
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 4)
        self.assertEqual(stored[0], 2500000000.0)
        self.assertEqual(stored[1], "hello")
        self.assertEqual(stored[2], objc.simd.vector_int2(0, 1))
        self.assertEqual(stored[3], -17592186044416)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_id_v2i_q_(2500000000.0, "hello", objc.simd.vector_int2(0, 1))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_id_v2i_q_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_q_(
                None, "hello", objc.simd.vector_int2(0, 1), -17592186044416
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_q_(
                2500000000.0,
                NoObjCValueObject,
                objc.simd.vector_int2(0, 1),
                -17592186044416,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_q_(2500000000.0, "hello", None, -17592186044416)

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_id_v2i_q_(2500000000.0, "hello", objc.simd.vector_int2(0, 1), None)

    def test_idf_f_id_v2i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idf_f_id_v2i_, b"@")
        self.assertArgHasType(OC_VectorCall.idf_f_id_v2i_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.idf_f_id_v2i_, 1, b"f")
        self.assertArgHasType(OC_VectorCall.idf_f_id_v2i_, 2, b"@")
        self.assertArgHasType(OC_VectorCall.idf_f_id_v2i_, 3, b"<2i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idf_f_id_v2i_(
            2500000000.0, 2500000000.0, "hello", objc.simd.vector_int2(0, 1)
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 4)
        self.assertEqual(stored[0], 2500000000.0)
        self.assertEqual(stored[1], 2500000000.0)
        self.assertEqual(stored[2], "hello")
        self.assertEqual(stored[3], objc.simd.vector_int2(0, 1))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_f_id_v2i_(2500000000.0, 2500000000.0, "hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idf_f_id_v2i_(
                2500000000.0,
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idf_f_id_v2i_(None, 2500000000.0, "hello", objc.simd.vector_int2(0, 1))

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_f_id_v2i_(2500000000.0, None, "hello", objc.simd.vector_int2(0, 1))

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_f_id_v2i_(
                2500000000.0,
                2500000000.0,
                NoObjCValueObject,
                objc.simd.vector_int2(0, 1),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.idf_f_id_v2i_(2500000000.0, 2500000000.0, "hello", None)

    def test_idGKBox_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idGKBox_, b"@")
        self.assertArgHasType(OC_VectorCall.idGKBox_, 0, b"{GKBox=<3f><3f>}")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idGKBox_(
            (
                objc.simd.vector_float3(1.0, 2.0, 3.0),
                objc.simd.vector_float3(4.0, 5.0, 6.0),
            )
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            (
                objc.simd.vector_float3(1.0, 2.0, 3.0),
                objc.simd.vector_float3(4.0, 5.0, 6.0),
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idGKBox_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idGKBox_(
                (
                    objc.simd.vector_float3(1.0, 2.0, 3.0),
                    objc.simd.vector_float3(4.0, 5.0, 6.0),
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idGKBox_(None)

    def test_idGKBox_f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idGKBox_f_, b"@")
        self.assertArgHasType(OC_VectorCall.idGKBox_f_, 0, b"{GKBox=<3f><3f>}")
        self.assertArgHasType(OC_VectorCall.idGKBox_f_, 1, b"f")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idGKBox_f_(
            (
                objc.simd.vector_float3(1.0, 2.0, 3.0),
                objc.simd.vector_float3(4.0, 5.0, 6.0),
            ),
            2500000000.0,
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(
            stored[0],
            (
                objc.simd.vector_float3(1.0, 2.0, 3.0),
                objc.simd.vector_float3(4.0, 5.0, 6.0),
            ),
        )
        self.assertEqual(stored[1], 2500000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idGKBox_f_(
                (
                    objc.simd.vector_float3(1.0, 2.0, 3.0),
                    objc.simd.vector_float3(4.0, 5.0, 6.0),
                )
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idGKBox_f_(
                (
                    objc.simd.vector_float3(1.0, 2.0, 3.0),
                    objc.simd.vector_float3(4.0, 5.0, 6.0),
                ),
                2500000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idGKBox_f_(None, 2500000000.0)

        with self.assertRaises((TypeError, ValueError)):
            oc.idGKBox_f_(
                (
                    objc.simd.vector_float3(1.0, 2.0, 3.0),
                    objc.simd.vector_float3(4.0, 5.0, 6.0),
                ),
                None,
            )

    def test_idGKQuad_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idGKQuad_, b"@")
        self.assertArgHasType(OC_VectorCall.idGKQuad_, 0, b"{GKQuad=<2f><2f>}")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idGKQuad_(
            (objc.simd.vector_float2(9.0, 10.0), objc.simd.vector_float2(11.0, 12.0))
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            (objc.simd.vector_float2(9.0, 10.0), objc.simd.vector_float2(11.0, 12.0)),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idGKQuad_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idGKQuad_(
                (
                    objc.simd.vector_float2(9.0, 10.0),
                    objc.simd.vector_float2(11.0, 12.0),
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idGKQuad_(None)

    def test_idGKQuad_f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idGKQuad_f_, b"@")
        self.assertArgHasType(OC_VectorCall.idGKQuad_f_, 0, b"{GKQuad=<2f><2f>}")
        self.assertArgHasType(OC_VectorCall.idGKQuad_f_, 1, b"f")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idGKQuad_f_(
            (objc.simd.vector_float2(9.0, 10.0), objc.simd.vector_float2(11.0, 12.0)),
            2500000000.0,
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(
            stored[0],
            (objc.simd.vector_float2(9.0, 10.0), objc.simd.vector_float2(11.0, 12.0)),
        )
        self.assertEqual(stored[1], 2500000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idGKQuad_f_(
                (
                    objc.simd.vector_float2(9.0, 10.0),
                    objc.simd.vector_float2(11.0, 12.0),
                )
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idGKQuad_f_(
                (
                    objc.simd.vector_float2(9.0, 10.0),
                    objc.simd.vector_float2(11.0, 12.0),
                ),
                2500000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idGKQuad_f_(None, 2500000000.0)

        with self.assertRaises((TypeError, ValueError)):
            oc.idGKQuad_f_(
                (
                    objc.simd.vector_float2(9.0, 10.0),
                    objc.simd.vector_float2(11.0, 12.0),
                ),
                None,
            )

    def test_idMDLVoxelIndexExtent_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idMDLVoxelIndexExtent_, b"@")
        self.assertArgHasType(
            OC_VectorCall.idMDLVoxelIndexExtent_, 0, b"{_MDLVoxelIndexExtent=<4i><4i>}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idMDLVoxelIndexExtent_(
            (
                objc.simd.vector_int4(100, 101, 102, 103),
                objc.simd.vector_int4(-20, -21, -22, -23),
            )
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            (
                objc.simd.vector_int4(100, 101, 102, 103),
                objc.simd.vector_int4(-20, -21, -22, -23),
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idMDLVoxelIndexExtent_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idMDLVoxelIndexExtent_(
                (
                    objc.simd.vector_int4(100, 101, 102, 103),
                    objc.simd.vector_int4(-20, -21, -22, -23),
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idMDLVoxelIndexExtent_(None)

    def test_idmatrixfloat4x4_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idmatrixfloat4x4_, b"@")
        self.assertArgHasType(
            OC_VectorCall.idmatrixfloat4x4_, 0, b"{_matrix_float4x4=[4<4f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idmatrixfloat4x4_(
            simd.matrix_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            )
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            simd.matrix_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idmatrixfloat4x4_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idmatrixfloat4x4_(
                simd.matrix_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idmatrixfloat4x4_(None)

    def test_idmatrixfloat4x4_Z_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.idmatrixfloat4x4_Z_, b"@")
        self.assertArgHasType(
            OC_VectorCall.idmatrixfloat4x4_Z_, 0, b"{_matrix_float4x4=[4<4f>]}"
        )
        self.assertArgHasType(OC_VectorCall.idmatrixfloat4x4_Z_, 1, b"Z")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.idmatrixfloat4x4_Z_(
            simd.matrix_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
            False,
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(
            stored[0],
            simd.matrix_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )
        self.assertEqual(stored[1], False)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idmatrixfloat4x4_Z_(
                simd.matrix_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                )
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.idmatrixfloat4x4_Z_(
                simd.matrix_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                False,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.idmatrixfloat4x4_Z_(None, False)

        with self.assertRaises((TypeError, ValueError)):
            oc.idmatrixfloat4x4_Z_(
                simd.matrix_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                NoBool(),
            )

    def test_Zv2i_id_id_id_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.Zv2i_id_id_id_id_, b"Z")
        self.assertArgHasType(OC_VectorCall.Zv2i_id_id_id_id_, 0, b"<2i>")
        self.assertArgHasType(OC_VectorCall.Zv2i_id_id_id_id_, 1, b"@")
        self.assertArgHasType(OC_VectorCall.Zv2i_id_id_id_id_, 2, b"@")
        self.assertArgHasType(OC_VectorCall.Zv2i_id_id_id_id_, 3, b"@")
        self.assertArgHasType(OC_VectorCall.Zv2i_id_id_id_id_, 4, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.Zv2i_id_id_id_id_(
            objc.simd.vector_int2(0, 1), "hello", "hello", "hello", "hello"
        )
        self.assertEqual(rv, False)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 5)
        self.assertEqual(stored[0], objc.simd.vector_int2(0, 1))
        self.assertEqual(stored[1], "hello")
        self.assertEqual(stored[2], "hello")
        self.assertEqual(stored[3], "hello")
        self.assertEqual(stored[4], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.Zv2i_id_id_id_id_(objc.simd.vector_int2(0, 1), "hello", "hello", "hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.Zv2i_id_id_id_id_(
                objc.simd.vector_int2(0, 1), "hello", "hello", "hello", "hello", "hello"
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.Zv2i_id_id_id_id_(None, "hello", "hello", "hello", "hello")

        with self.assertRaises((TypeError, ValueError)):
            oc.Zv2i_id_id_id_id_(
                objc.simd.vector_int2(0, 1),
                NoObjCValueObject,
                "hello",
                "hello",
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.Zv2i_id_id_id_id_(
                objc.simd.vector_int2(0, 1),
                "hello",
                NoObjCValueObject,
                "hello",
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.Zv2i_id_id_id_id_(
                objc.simd.vector_int2(0, 1),
                "hello",
                "hello",
                NoObjCValueObject,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.Zv2i_id_id_id_id_(
                objc.simd.vector_int2(0, 1),
                "hello",
                "hello",
                "hello",
                NoObjCValueObject,
            )

    def test_Zv2i_q_f_id_id_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.Zv2i_q_f_id_id_id_, b"Z")
        self.assertArgHasType(OC_VectorCall.Zv2i_q_f_id_id_id_, 0, b"<2i>")
        self.assertArgHasType(OC_VectorCall.Zv2i_q_f_id_id_id_, 1, b"q")
        self.assertArgHasType(OC_VectorCall.Zv2i_q_f_id_id_id_, 2, b"f")
        self.assertArgHasType(OC_VectorCall.Zv2i_q_f_id_id_id_, 3, b"@")
        self.assertArgHasType(OC_VectorCall.Zv2i_q_f_id_id_id_, 4, b"@")
        self.assertArgHasType(OC_VectorCall.Zv2i_q_f_id_id_id_, 5, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.Zv2i_q_f_id_id_id_(
            objc.simd.vector_int2(0, 1),
            -17592186044416,
            2500000000.0,
            "hello",
            "hello",
            "hello",
        )
        self.assertEqual(rv, False)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 6)
        self.assertEqual(stored[0], objc.simd.vector_int2(0, 1))
        self.assertEqual(stored[1], -17592186044416)
        self.assertEqual(stored[2], 2500000000.0)
        self.assertEqual(stored[3], "hello")
        self.assertEqual(stored[4], "hello")
        self.assertEqual(stored[5], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.Zv2i_q_f_id_id_id_(
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                2500000000.0,
                "hello",
                "hello",
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.Zv2i_q_f_id_id_id_(
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                2500000000.0,
                "hello",
                "hello",
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.Zv2i_q_f_id_id_id_(
                None, -17592186044416, 2500000000.0, "hello", "hello", "hello"
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.Zv2i_q_f_id_id_id_(
                objc.simd.vector_int2(0, 1),
                None,
                2500000000.0,
                "hello",
                "hello",
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.Zv2i_q_f_id_id_id_(
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                None,
                "hello",
                "hello",
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.Zv2i_q_f_id_id_id_(
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                2500000000.0,
                NoObjCValueObject,
                "hello",
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.Zv2i_q_f_id_id_id_(
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                2500000000.0,
                "hello",
                NoObjCValueObject,
                "hello",
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.Zv2i_q_f_id_id_id_(
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                2500000000.0,
                "hello",
                "hello",
                NoObjCValueObject,
            )

    def test_Zv4i_Z_Z_Z_Z_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.Zv4i_Z_Z_Z_Z_, b"Z")
        self.assertArgHasType(OC_VectorCall.Zv4i_Z_Z_Z_Z_, 0, b"<4i>")
        self.assertArgHasType(OC_VectorCall.Zv4i_Z_Z_Z_Z_, 1, b"Z")
        self.assertArgHasType(OC_VectorCall.Zv4i_Z_Z_Z_Z_, 2, b"Z")
        self.assertArgHasType(OC_VectorCall.Zv4i_Z_Z_Z_Z_, 3, b"Z")
        self.assertArgHasType(OC_VectorCall.Zv4i_Z_Z_Z_Z_, 4, b"Z")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.Zv4i_Z_Z_Z_Z_(
            objc.simd.vector_int4(0, 1, 2, 3), False, False, False, False
        )
        self.assertEqual(rv, False)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 5)
        self.assertEqual(stored[0], objc.simd.vector_int4(0, 1, 2, 3))
        self.assertEqual(stored[1], False)
        self.assertEqual(stored[2], False)
        self.assertEqual(stored[3], False)
        self.assertEqual(stored[4], False)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.Zv4i_Z_Z_Z_Z_(objc.simd.vector_int4(0, 1, 2, 3), False, False, False)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.Zv4i_Z_Z_Z_Z_(
                objc.simd.vector_int4(0, 1, 2, 3), False, False, False, False, "hello"
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.Zv4i_Z_Z_Z_Z_(None, False, False, False, False)

        with self.assertRaises((TypeError, ValueError)):
            oc.Zv4i_Z_Z_Z_Z_(
                objc.simd.vector_int4(0, 1, 2, 3), NoBool(), False, False, False
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.Zv4i_Z_Z_Z_Z_(
                objc.simd.vector_int4(0, 1, 2, 3), False, NoBool(), False, False
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.Zv4i_Z_Z_Z_Z_(
                objc.simd.vector_int4(0, 1, 2, 3), False, False, NoBool(), False
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.Zv4i_Z_Z_Z_Z_(
                objc.simd.vector_int4(0, 1, 2, 3), False, False, False, NoBool()
            )

    def test_CGColorv3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.CGColorv3f_, b"^{CGColor=}")
        self.assertArgHasType(OC_VectorCall.CGColorv3f_, 0, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.CGColorv3f_(objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(rv, "color!")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.CGColorv3f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.CGColorv3f_(objc.simd.vector_float3(0.0, 1.5, 3.0), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.CGColorv3f_(None)

    def test_CGColorv3f_CGColorSpace_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.CGColorv3f_CGColorSpace_, b"^{CGColor=}")
        self.assertArgHasType(OC_VectorCall.CGColorv3f_CGColorSpace_, 0, b"<3f>")
        self.assertArgHasType(
            OC_VectorCall.CGColorv3f_CGColorSpace_, 1, b"^{CGColorSpace=}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.CGColorv3f_CGColorSpace_(
            objc.simd.vector_float3(0.0, 1.5, 3.0), "colorspace!"
        )
        self.assertEqual(rv, "color!")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], "colorspace!")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.CGColorv3f_CGColorSpace_(objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.CGColorv3f_CGColorSpace_(
                objc.simd.vector_float3(0.0, 1.5, 3.0), "colorspace!", "hello"
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.CGColorv3f_CGColorSpace_(None, "colorspace!")

        with self.assertRaises((TypeError, ValueError)):
            oc.CGColorv3f_CGColorSpace_(
                objc.simd.vector_float3(0.0, 1.5, 3.0), NoObjCValueObject
            )

    def test_fv2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.fv2f_, b"f")
        self.assertArgHasType(OC_VectorCall.fv2f_, 0, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.fv2f_(objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(rv, 2500000000.0)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.fv2f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.fv2f_(objc.simd.vector_float2(0.0, 1.5), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.fv2f_(None)

    def test_fv2i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.fv2i_, b"f")
        self.assertArgHasType(OC_VectorCall.fv2i_, 0, b"<2i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.fv2i_(objc.simd.vector_int2(0, 1))
        self.assertEqual(rv, 2500000000.0)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_int2(0, 1))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.fv2i_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.fv2i_(objc.simd.vector_int2(0, 1), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.fv2i_(None)

    def test_vv2d_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vv2d_d_, b"v")
        self.assertArgHasType(OC_VectorCall.vv2d_d_, 0, b"<2d>")
        self.assertArgHasType(OC_VectorCall.vv2d_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vv2d_d_(objc.simd.vector_double2(0.0, 1.5), -557000000000.0)
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_double2(0.0, 1.5))
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv2d_d_(objc.simd.vector_double2(0.0, 1.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv2d_d_(objc.simd.vector_double2(0.0, 1.5), -557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vv2d_d_(None, -557000000000.0)

        with self.assertRaises((TypeError, ValueError)):
            oc.vv2d_d_(objc.simd.vector_double2(0.0, 1.5), None)

    def test_vv2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vv2f_, b"v")
        self.assertArgHasType(OC_VectorCall.vv2f_, 0, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vv2f_(objc.simd.vector_float2(0.0, 1.5))
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv2f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv2f_(objc.simd.vector_float2(0.0, 1.5), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vv2f_(None)

    def test_vv2f_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vv2f_d_, b"v")
        self.assertArgHasType(OC_VectorCall.vv2f_d_, 0, b"<2f>")
        self.assertArgHasType(OC_VectorCall.vv2f_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vv2f_d_(objc.simd.vector_float2(0.0, 1.5), -557000000000.0)
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv2f_d_(objc.simd.vector_float2(0.0, 1.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv2f_d_(objc.simd.vector_float2(0.0, 1.5), -557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vv2f_d_(None, -557000000000.0)

        with self.assertRaises((TypeError, ValueError)):
            oc.vv2f_d_(objc.simd.vector_float2(0.0, 1.5), None)

    def test_vv3d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vv3d_, b"v")
        self.assertArgHasType(OC_VectorCall.vv3d_, 0, b"<3d>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vv3d_(objc.simd.vector_double3(0.0, 1.5, 3.0))
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_double3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv3d_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv3d_(objc.simd.vector_double3(0.0, 1.5, 3.0), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vv3d_(None)

    def test_vv3d_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vv3d_d_, b"v")
        self.assertArgHasType(OC_VectorCall.vv3d_d_, 0, b"<3d>")
        self.assertArgHasType(OC_VectorCall.vv3d_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vv3d_d_(objc.simd.vector_double3(0.0, 1.5, 3.0), -557000000000.0)
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_double3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv3d_d_(objc.simd.vector_double3(0.0, 1.5, 3.0))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv3d_d_(
                objc.simd.vector_double3(0.0, 1.5, 3.0), -557000000000.0, "hello"
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vv3d_d_(None, -557000000000.0)

        with self.assertRaises((TypeError, ValueError)):
            oc.vv3d_d_(objc.simd.vector_double3(0.0, 1.5, 3.0), None)

    def test_vv3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vv3f_, b"v")
        self.assertArgHasType(OC_VectorCall.vv3f_, 0, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vv3f_(objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv3f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv3f_(objc.simd.vector_float3(0.0, 1.5, 3.0), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vv3f_(None)

    def test_vv3f_v3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vv3f_v3f_, b"v")
        self.assertArgHasType(OC_VectorCall.vv3f_v3f_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.vv3f_v3f_, 1, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vv3f_v3f_(
            objc.simd.vector_float3(0.0, 1.5, 3.0),
            objc.simd.vector_float3(0.0, 1.5, 3.0),
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv3f_v3f_(objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv3f_v3f_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vv3f_v3f_(None, objc.simd.vector_float3(0.0, 1.5, 3.0))

        with self.assertRaises((TypeError, ValueError)):
            oc.vv3f_v3f_(objc.simd.vector_float3(0.0, 1.5, 3.0), None)

    def test_vv3f_v3f_v3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vv3f_v3f_v3f_, b"v")
        self.assertArgHasType(OC_VectorCall.vv3f_v3f_v3f_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.vv3f_v3f_v3f_, 1, b"<3f>")
        self.assertArgHasType(OC_VectorCall.vv3f_v3f_v3f_, 2, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vv3f_v3f_v3f_(
            objc.simd.vector_float3(0.0, 1.5, 3.0),
            objc.simd.vector_float3(0.0, 1.5, 3.0),
            objc.simd.vector_float3(0.0, 1.5, 3.0),
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 3)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[2], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv3f_v3f_v3f_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_float3(0.0, 1.5, 3.0),
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv3f_v3f_v3f_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vv3f_v3f_v3f_(
                None,
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_float3(0.0, 1.5, 3.0),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.vv3f_v3f_v3f_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                objc.simd.vector_float3(0.0, 1.5, 3.0),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.vv3f_v3f_v3f_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
            )

    def test_vv3f_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vv3f_d_, b"v")
        self.assertArgHasType(OC_VectorCall.vv3f_d_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.vv3f_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vv3f_d_(objc.simd.vector_float3(0.0, 1.5, 3.0), -557000000000.0)
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv3f_d_(objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv3f_d_(objc.simd.vector_float3(0.0, 1.5, 3.0), -557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vv3f_d_(None, -557000000000.0)

        with self.assertRaises((TypeError, ValueError)):
            oc.vv3f_d_(objc.simd.vector_float3(0.0, 1.5, 3.0), None)

    def test_vv4d_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vv4d_d_, b"v")
        self.assertArgHasType(OC_VectorCall.vv4d_d_, 0, b"<4d>")
        self.assertArgHasType(OC_VectorCall.vv4d_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vv4d_d_(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5), -557000000000.0)
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5))
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv4d_d_(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv4d_d_(
                objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5), -557000000000.0, "hello"
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vv4d_d_(None, -557000000000.0)

        with self.assertRaises((TypeError, ValueError)):
            oc.vv4d_d_(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5), None)

    def test_vv4f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vv4f_, b"v")
        self.assertArgHasType(OC_VectorCall.vv4f_, 0, b"<4f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vv4f_(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv4f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv4f_(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vv4f_(None)

    def test_vv4f_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vv4f_d_, b"v")
        self.assertArgHasType(OC_VectorCall.vv4f_d_, 0, b"<4f>")
        self.assertArgHasType(OC_VectorCall.vv4f_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vv4f_d_(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5), -557000000000.0)
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv4f_d_(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv4f_d_(
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5), -557000000000.0, "hello"
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vv4f_d_(None, -557000000000.0)

        with self.assertRaises((TypeError, ValueError)):
            oc.vv4f_d_(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5), None)

    def test_vv4i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vv4i_, b"v")
        self.assertArgHasType(OC_VectorCall.vv4i_, 0, b"<4i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vv4i_(objc.simd.vector_int4(0, 1, 2, 3))
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_int4(0, 1, 2, 3))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv4i_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vv4i_(objc.simd.vector_int4(0, 1, 2, 3), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vv4i_(None)

    def test_vid_v2f_v2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vid_v2f_v2f_, b"v")
        self.assertArgHasType(OC_VectorCall.vid_v2f_v2f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.vid_v2f_v2f_, 1, b"<2f>")
        self.assertArgHasType(OC_VectorCall.vid_v2f_v2f_, 2, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vid_v2f_v2f_(
            "hello",
            objc.simd.vector_float2(0.0, 1.5),
            objc.simd.vector_float2(0.0, 1.5),
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 3)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(stored[2], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vid_v2f_v2f_("hello", objc.simd.vector_float2(0.0, 1.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vid_v2f_v2f_(
                "hello",
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vid_v2f_v2f_(
                NoObjCValueObject,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.vid_v2f_v2f_("hello", None, objc.simd.vector_float2(0.0, 1.5))

        with self.assertRaises((TypeError, ValueError)):
            oc.vid_v2f_v2f_("hello", objc.simd.vector_float2(0.0, 1.5), None)

    def test_vid_v2f_v2f_q_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vid_v2f_v2f_q_, b"v")
        self.assertArgHasType(OC_VectorCall.vid_v2f_v2f_q_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.vid_v2f_v2f_q_, 1, b"<2f>")
        self.assertArgHasType(OC_VectorCall.vid_v2f_v2f_q_, 2, b"<2f>")
        self.assertArgHasType(OC_VectorCall.vid_v2f_v2f_q_, 3, b"q")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vid_v2f_v2f_q_(
            "hello",
            objc.simd.vector_float2(0.0, 1.5),
            objc.simd.vector_float2(0.0, 1.5),
            -17592186044416,
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 4)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(stored[2], objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(stored[3], -17592186044416)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vid_v2f_v2f_q_(
                "hello",
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vid_v2f_v2f_q_(
                "hello",
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                -17592186044416,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vid_v2f_v2f_q_(
                NoObjCValueObject,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                -17592186044416,
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.vid_v2f_v2f_q_(
                "hello", None, objc.simd.vector_float2(0.0, 1.5), -17592186044416
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.vid_v2f_v2f_q_(
                "hello", objc.simd.vector_float2(0.0, 1.5), None, -17592186044416
            )

        with self.assertRaises((TypeError, ValueError)):
            oc.vid_v2f_v2f_q_(
                "hello",
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                None,
            )

    def test_vf_v2i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vf_v2i_, b"v")
        self.assertArgHasType(OC_VectorCall.vf_v2i_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.vf_v2i_, 1, b"<2i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vf_v2i_(2500000000.0, objc.simd.vector_int2(0, 1))
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], 2500000000.0)
        self.assertEqual(stored[1], objc.simd.vector_int2(0, 1))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vf_v2i_(2500000000.0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vf_v2i_(2500000000.0, objc.simd.vector_int2(0, 1), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vf_v2i_(None, objc.simd.vector_int2(0, 1))

        with self.assertRaises((TypeError, ValueError)):
            oc.vf_v2i_(2500000000.0, None)

    def test_vMDLAxisAlignedBoundingBox_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vMDLAxisAlignedBoundingBox_, b"v")
        self.assertArgHasType(
            OC_VectorCall.vMDLAxisAlignedBoundingBox_,
            0,
            b"{_MDLAxisAlignedBoundingBox=<3f><3f>}",
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vMDLAxisAlignedBoundingBox_(
            (
                objc.simd.vector_float3(-8.0, -9.0, -10.0),
                objc.simd.vector_float3(-11.0, -12.0, -13.0),
            )
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            (
                objc.simd.vector_float3(-8.0, -9.0, -10.0),
                objc.simd.vector_float3(-11.0, -12.0, -13.0),
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vMDLAxisAlignedBoundingBox_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vMDLAxisAlignedBoundingBox_(
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vMDLAxisAlignedBoundingBox_(None)

    def test_vMDLAxisAlignedBoundingBox_Z_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vMDLAxisAlignedBoundingBox_Z_, b"v")
        self.assertArgHasType(
            OC_VectorCall.vMDLAxisAlignedBoundingBox_Z_,
            0,
            b"{_MDLAxisAlignedBoundingBox=<3f><3f>}",
        )
        self.assertArgHasType(OC_VectorCall.vMDLAxisAlignedBoundingBox_Z_, 1, b"Z")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vMDLAxisAlignedBoundingBox_Z_(
            (
                objc.simd.vector_float3(-8.0, -9.0, -10.0),
                objc.simd.vector_float3(-11.0, -12.0, -13.0),
            ),
            False,
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(
            stored[0],
            (
                objc.simd.vector_float3(-8.0, -9.0, -10.0),
                objc.simd.vector_float3(-11.0, -12.0, -13.0),
            ),
        )
        self.assertEqual(stored[1], False)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vMDLAxisAlignedBoundingBox_Z_(
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                )
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vMDLAxisAlignedBoundingBox_Z_(
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                ),
                False,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vMDLAxisAlignedBoundingBox_Z_(None, False)

        with self.assertRaises((TypeError, ValueError)):
            oc.vMDLAxisAlignedBoundingBox_Z_(
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                ),
                NoBool(),
            )

    def test_vmatrixdouble4x4_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vmatrixdouble4x4_, b"v")
        self.assertArgHasType(
            OC_VectorCall.vmatrixdouble4x4_, 0, b"{_matrix_double4x4=[4<4d>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vmatrixdouble4x4_(
            simd.matrix_double4x4(
                (
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                )
            )
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            simd.matrix_double4x4(
                (
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vmatrixdouble4x4_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vmatrixdouble4x4_(
                simd.matrix_double4x4(
                    (
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vmatrixdouble4x4_(None)

    def test_vmatrixdouble4x4_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vmatrixdouble4x4_d_, b"v")
        self.assertArgHasType(
            OC_VectorCall.vmatrixdouble4x4_d_, 0, b"{_matrix_double4x4=[4<4d>]}"
        )
        self.assertArgHasType(OC_VectorCall.vmatrixdouble4x4_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vmatrixdouble4x4_d_(
            simd.matrix_double4x4(
                (
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                )
            ),
            -557000000000.0,
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(
            stored[0],
            simd.matrix_double4x4(
                (
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vmatrixdouble4x4_d_(
                simd.matrix_double4x4(
                    (
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    )
                )
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vmatrixdouble4x4_d_(
                simd.matrix_double4x4(
                    (
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                -557000000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vmatrixdouble4x4_d_(None, -557000000000.0)

        with self.assertRaises((TypeError, ValueError)):
            oc.vmatrixdouble4x4_d_(
                simd.matrix_double4x4(
                    (
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                None,
            )

    def test_vmatrixfloat2x2_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vmatrixfloat2x2_, b"v")
        self.assertArgHasType(
            OC_VectorCall.vmatrixfloat2x2_, 0, b"{_matrix_float2x2=[2<2f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vmatrixfloat2x2_(
            simd.matrix_float2x2(
                (objc.simd.vector_float2(0.0, 1.5), objc.simd.vector_float2(0.0, 1.5))
            )
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            simd.matrix_float2x2(
                (objc.simd.vector_float2(0.0, 1.5), objc.simd.vector_float2(0.0, 1.5))
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vmatrixfloat2x2_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vmatrixfloat2x2_(
                simd.matrix_float2x2(
                    (
                        objc.simd.vector_float2(0.0, 1.5),
                        objc.simd.vector_float2(0.0, 1.5),
                    )
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vmatrixfloat2x2_(None)

    def test_vmatrixfloat3x3_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vmatrixfloat3x3_, b"v")
        self.assertArgHasType(
            OC_VectorCall.vmatrixfloat3x3_, 0, b"{_matrix_float3x3=[3<3f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vmatrixfloat3x3_(
            simd.matrix_float3x3(
                (
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                )
            )
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            simd.matrix_float3x3(
                (
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                )
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vmatrixfloat3x3_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vmatrixfloat3x3_(
                simd.matrix_float3x3(
                    (
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                    )
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vmatrixfloat3x3_(None)

    def test_vmatrixfloat4x4_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vmatrixfloat4x4_, b"v")
        self.assertArgHasType(
            OC_VectorCall.vmatrixfloat4x4_, 0, b"{_matrix_float4x4=[4<4f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vmatrixfloat4x4_(
            simd.matrix_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            )
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            simd.matrix_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vmatrixfloat4x4_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vmatrixfloat4x4_(
                simd.matrix_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vmatrixfloat4x4_(None)

    def test_vmatrixfloat4x4_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vmatrixfloat4x4_d_, b"v")
        self.assertArgHasType(
            OC_VectorCall.vmatrixfloat4x4_d_, 0, b"{_matrix_float4x4=[4<4f>]}"
        )
        self.assertArgHasType(OC_VectorCall.vmatrixfloat4x4_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vmatrixfloat4x4_d_(
            simd.matrix_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
            -557000000000.0,
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(
            stored[0],
            simd.matrix_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vmatrixfloat4x4_d_(
                simd.matrix_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                )
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vmatrixfloat4x4_d_(
                simd.matrix_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                -557000000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vmatrixfloat4x4_d_(None, -557000000000.0)

        with self.assertRaises((TypeError, ValueError)):
            oc.vmatrixfloat4x4_d_(
                simd.matrix_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                None,
            )

    def test_vsimdfloat4x4_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vsimdfloat4x4_, b"v")
        self.assertArgHasType(
            OC_VectorCall.vsimdfloat4x4_, 0, b"{_simd_float4x4=[4<4f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vsimdfloat4x4_(
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            )
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vsimdfloat4x4_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vsimdfloat4x4_(
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vsimdfloat4x4_(None)

    def test_vsimdquatd_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vsimdquatd_d_, b"v")
        self.assertArgHasType(OC_VectorCall.vsimdquatd_d_, 0, b"{_simd_quatd=<4d>}")
        self.assertArgHasType(OC_VectorCall.vsimdquatd_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vsimdquatd_d_(
            simd.simd_quatd(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5)),
            -557000000000.0,
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(
            stored[0], simd.simd_quatd(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5))
        )
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vsimdquatd_d_(
                simd.simd_quatd(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5))
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vsimdquatd_d_(
                simd.simd_quatd(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5)),
                -557000000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vsimdquatd_d_(None, -557000000000.0)

        with self.assertRaises((TypeError, ValueError)):
            oc.vsimdquatd_d_(
                simd.simd_quatd(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5)), None
            )

    def test_vsimdquatf_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vsimdquatf_, b"v")
        self.assertArgHasType(OC_VectorCall.vsimdquatf_, 0, b"{_simd_quatf=<4f>}")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vsimdquatf_(
            simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0], simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vsimdquatf_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vsimdquatf_(
                simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5)), "hello"
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vsimdquatf_(None)

    def test_vsimdquatf_v3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vsimdquatf_v3f_, b"v")
        self.assertArgHasType(OC_VectorCall.vsimdquatf_v3f_, 0, b"{_simd_quatf=<4f>}")
        self.assertArgHasType(OC_VectorCall.vsimdquatf_v3f_, 1, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vsimdquatf_v3f_(
            simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5)),
            objc.simd.vector_float3(0.0, 1.5, 3.0),
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(
            stored[0], simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        )
        self.assertEqual(stored[1], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vsimdquatf_v3f_(
                simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vsimdquatf_v3f_(
                simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5)),
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vsimdquatf_v3f_(None, objc.simd.vector_float3(0.0, 1.5, 3.0))

        with self.assertRaises((TypeError, ValueError)):
            oc.vsimdquatf_v3f_(
                simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5)), None
            )

    def test_vsimdquatf_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.vsimdquatf_d_, b"v")
        self.assertArgHasType(OC_VectorCall.vsimdquatf_d_, 0, b"{_simd_quatf=<4f>}")
        self.assertArgHasType(OC_VectorCall.vsimdquatf_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.vsimdquatf_d_(
            simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5)),
            -557000000000.0,
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(
            stored[0], simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        )
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vsimdquatf_d_(
                simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.vsimdquatf_d_(
                simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5)),
                -557000000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.vsimdquatf_d_(None, -557000000000.0)

        with self.assertRaises((TypeError, ValueError)):
            oc.vsimdquatf_d_(
                simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5)), None
            )

    def test_GKBox(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.GKBox, b"{GKBox=<3f><3f>}")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.GKBox()
        self.assertEqual(
            rv,
            (
                objc.simd.vector_float3(1.0, 2.0, 3.0),
                objc.simd.vector_float3(4.0, 5.0, 6.0),
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.GKBox("hello")

    def test_GKQuad(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.GKQuad, b"{GKQuad=<2f><2f>}")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.GKQuad()
        self.assertEqual(
            rv,
            (objc.simd.vector_float2(9.0, 10.0), objc.simd.vector_float2(11.0, 12.0)),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.GKQuad("hello")

    def test_GKTriangleQ_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.GKTriangleQ_, b"{GKTriangle=[3<3f>]}")
        self.assertArgHasType(OC_VectorCall.GKTriangleQ_, 0, b"Q")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.GKTriangleQ_(35184372088832)
        self.assertEqual(
            rv,
            (
                (
                    objc.simd.vector_float3(-18.5, -19.5, -110.5),
                    objc.simd.vector_float3(-111.5, -112.5, -113.5),
                    objc.simd.vector_float3(-17.5, 11.5, 122.5),
                ),
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], 35184372088832)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.GKTriangleQ_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.GKTriangleQ_(35184372088832, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.GKTriangleQ_(None)

    def test_MDLAxisAlignedBoundingBox(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.MDLAxisAlignedBoundingBox,
            b"{_MDLAxisAlignedBoundingBox=<3f><3f>}",
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.MDLAxisAlignedBoundingBox()
        self.assertEqual(
            rv,
            (
                objc.simd.vector_float3(-8.0, -9.0, -10.0),
                objc.simd.vector_float3(-11.0, -12.0, -13.0),
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.MDLAxisAlignedBoundingBox("hello")

    def test_MDLAxisAlignedBoundingBoxv4i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.MDLAxisAlignedBoundingBoxv4i_,
            b"{_MDLAxisAlignedBoundingBox=<3f><3f>}",
        )
        self.assertArgHasType(OC_VectorCall.MDLAxisAlignedBoundingBoxv4i_, 0, b"<4i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.MDLAxisAlignedBoundingBoxv4i_(objc.simd.vector_int4(0, 1, 2, 3))
        self.assertEqual(
            rv,
            (
                objc.simd.vector_float3(-8.0, -9.0, -10.0),
                objc.simd.vector_float3(-11.0, -12.0, -13.0),
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_int4(0, 1, 2, 3))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.MDLAxisAlignedBoundingBoxv4i_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.MDLAxisAlignedBoundingBoxv4i_(objc.simd.vector_int4(0, 1, 2, 3), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.MDLAxisAlignedBoundingBoxv4i_(None)

    def test_MDLAxisAlignedBoundingBoxd_(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.MDLAxisAlignedBoundingBoxd_,
            b"{_MDLAxisAlignedBoundingBox=<3f><3f>}",
        )
        self.assertArgHasType(OC_VectorCall.MDLAxisAlignedBoundingBoxd_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.MDLAxisAlignedBoundingBoxd_(-557000000000.0)
        self.assertEqual(
            rv,
            (
                objc.simd.vector_float3(-8.0, -9.0, -10.0),
                objc.simd.vector_float3(-11.0, -12.0, -13.0),
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.MDLAxisAlignedBoundingBoxd_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.MDLAxisAlignedBoundingBoxd_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.MDLAxisAlignedBoundingBoxd_(None)

    def test_MDLVoxelIndexExtent(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.MDLVoxelIndexExtent, b"{_MDLVoxelIndexExtent=<4i><4i>}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.MDLVoxelIndexExtent()
        self.assertEqual(
            rv,
            (
                objc.simd.vector_int4(100, 101, 102, 103),
                objc.simd.vector_int4(-20, -21, -22, -23),
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.MDLVoxelIndexExtent("hello")

    def test_MPSAxisAlignedBoundingBox(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.MPSAxisAlignedBoundingBox,
            b"{_MPSAxisAlignedBoundingBox=<3f><3f>}",
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.MPSAxisAlignedBoundingBox()
        self.assertEqual(
            rv,
            (
                objc.simd.vector_float3(1.5, 2.5, 3.5),
                objc.simd.vector_float3(4.5, 5.5, 6.5),
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.MPSAxisAlignedBoundingBox("hello")

    def test_MPSImageHistogramInfo(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.MPSImageHistogramInfo, b"{_MPSImageHistogramInfo=QZ<4f><4f>}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.MPSImageHistogramInfo()
        self.assertEqual(
            rv,
            (
                4398046511104,
                True,
                objc.simd.vector_float4(1.0, 2.0, 3.0, 4.0),
                objc.simd.vector_float4(-1.0, -2.0, -3.0, -4.0),
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.MPSImageHistogramInfo("hello")

    def test_matrixdouble4x4(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.matrixdouble4x4, b"{_matrix_double4x4=[4<4d>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.matrixdouble4x4()
        self.assertEqual(
            rv,
            simd.matrix_double4x4(
                (
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.matrixdouble4x4("hello")

    def test_matrixdouble4x4d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.matrixdouble4x4d_, b"{_matrix_double4x4=[4<4d>]}"
        )
        self.assertArgHasType(OC_VectorCall.matrixdouble4x4d_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.matrixdouble4x4d_(-557000000000.0)
        self.assertEqual(
            rv,
            simd.matrix_double4x4(
                (
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.matrixdouble4x4d_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.matrixdouble4x4d_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.matrixdouble4x4d_(None)

    def test_matrixfloat2x2(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.matrixfloat2x2, b"{_matrix_float2x2=[2<2f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.matrixfloat2x2()
        self.assertEqual(
            rv,
            simd.matrix_float2x2(
                (objc.simd.vector_float2(0.0, 1.5), objc.simd.vector_float2(0.0, 1.5))
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.matrixfloat2x2("hello")

    def test_matrixfloat3x3(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.matrixfloat3x3, b"{_matrix_float3x3=[3<3f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.matrixfloat3x3()
        self.assertEqual(
            rv,
            simd.matrix_float3x3(
                (
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                )
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.matrixfloat3x3("hello")

    def test_matrixfloat4x4(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.matrixfloat4x4, b"{_matrix_float4x4=[4<4f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.matrixfloat4x4()
        self.assertEqual(
            rv,
            simd.matrix_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.matrixfloat4x4("hello")

    def test_matrixfloat4x4id_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.matrixfloat4x4id_d_, b"{_matrix_float4x4=[4<4f>]}"
        )
        self.assertArgHasType(OC_VectorCall.matrixfloat4x4id_d_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.matrixfloat4x4id_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.matrixfloat4x4id_d_("hello", -557000000000.0)
        self.assertEqual(
            rv,
            simd.matrix_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.matrixfloat4x4id_d_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.matrixfloat4x4id_d_("hello", -557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.matrixfloat4x4id_d_(NoObjCValueObject, -557000000000.0)

        with self.assertRaises((TypeError, ValueError)):
            oc.matrixfloat4x4id_d_("hello", None)

    def test_matrixfloat4x4d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.matrixfloat4x4d_, b"{_matrix_float4x4=[4<4f>]}"
        )
        self.assertArgHasType(OC_VectorCall.matrixfloat4x4d_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.matrixfloat4x4d_(-557000000000.0)
        self.assertEqual(
            rv,
            simd.matrix_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.matrixfloat4x4d_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.matrixfloat4x4d_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.matrixfloat4x4d_(None)

    def test_simdfloat4x4(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.simdfloat4x4, b"{_simd_float4x4=[4<4f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.simdfloat4x4()
        self.assertEqual(
            rv,
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.simdfloat4x4("hello")

    def test_simdfloat4x4simdfloat4x4_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.simdfloat4x4simdfloat4x4_id_, b"{_simd_float4x4=[4<4f>]}"
        )
        self.assertArgHasType(
            OC_VectorCall.simdfloat4x4simdfloat4x4_id_, 0, b"{_simd_float4x4=[4<4f>]}"
        )
        self.assertArgHasType(OC_VectorCall.simdfloat4x4simdfloat4x4_id_, 1, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.simdfloat4x4simdfloat4x4_id_(
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
            "hello",
        )
        self.assertEqual(
            rv,
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(
            stored[0],
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )
        self.assertEqual(stored[1], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.simdfloat4x4simdfloat4x4_id_(
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                )
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.simdfloat4x4simdfloat4x4_id_(
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.simdfloat4x4simdfloat4x4_id_(None, "hello")

        with self.assertRaises((TypeError, ValueError)):
            oc.simdfloat4x4simdfloat4x4_id_(
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                NoObjCValueObject,
            )

    def test_simdquatdd_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.simdquatdd_, b"{_simd_quatd=<4d>}")
        self.assertArgHasType(OC_VectorCall.simdquatdd_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.simdquatdd_(-557000000000.0)
        self.assertEqual(
            rv, simd.simd_quatd(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5))
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.simdquatdd_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.simdquatdd_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.simdquatdd_(None)

    def test_simdquatf(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.simdquatf, b"{_simd_quatf=<4f>}")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.simdquatf()
        self.assertEqual(
            rv, simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.simdquatf("hello")

    def test_simdquatfd_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.simdquatfd_, b"{_simd_quatf=<4f>}")
        self.assertArgHasType(OC_VectorCall.simdquatfd_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.simdquatfd_(-557000000000.0)
        self.assertEqual(
            rv, simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.simdquatfd_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            oc.simdquatfd_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            oc.simdquatfd_(None)
