#
# This file is generated using Tools/generate-helpers-vector.py
#
#    ** DO NOT EDIT **
#
from PyObjCTools.TestSupport import TestCase
import objc
from objc import simd

from .vectorcall import OC_VectorCall


class Fake:
    @property
    def __pyobjc_object__(self):
        raise TypeError("Cannot proxy")


NoObjCValueObject = Fake()

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
    b"OC_VectorCall", b"v2d:d:", {"full_signature": b"<2d>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv2d:d:", {"full_signature": b"<2d>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v2f", {"full_signature": b"<2f>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv2f", {"full_signature": b"<2f>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v2f:Q:", {"full_signature": b"<2f>@:Q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv2f:Q:", {"full_signature": b"<2f>@:Q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v2f:d:", {"full_signature": b"<2f>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv2f:d:", {"full_signature": b"<2f>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v2f:q:", {"full_signature": b"<2f>@:q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv2f:q:", {"full_signature": b"<2f>@:q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v2i", {"full_signature": b"<2i>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv2i", {"full_signature": b"<2i>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3d:d:", {"full_signature": b"<3d>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3d:d:", {"full_signature": b"<3d>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3f", {"full_signature": b"<3f>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3f", {"full_signature": b"<3f>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3f:v2i:v2i:", {"full_signature": b"<3f>@:<2i><2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3f:v2i:v2i:", {"full_signature": b"<3f>@:<2i><2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3f:v3f:", {"full_signature": b"<3f>@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3f:v3f:", {"full_signature": b"<3f>@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3f:v3f:id:", {"full_signature": b"<3f>@:<3f>@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3f:v3f:id:", {"full_signature": b"<3f>@:<3f>@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3f:v4i:", {"full_signature": b"<3f>@:<4i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3f:v4i:", {"full_signature": b"<3f>@:<4i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3f:Q:", {"full_signature": b"<3f>@:Q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3f:Q:", {"full_signature": b"<3f>@:Q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v3f:d:", {"full_signature": b"<3f>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv3f:d:", {"full_signature": b"<3f>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v4d:d:", {"full_signature": b"<4d>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv4d:d:", {"full_signature": b"<4d>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v4f", {"full_signature": b"<4f>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv4f", {"full_signature": b"<4f>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v4f:d:", {"full_signature": b"<4f>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv4f:d:", {"full_signature": b"<4f>@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v4i:v3f:", {"full_signature": b"<4i>@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv4i:v3f:", {"full_signature": b"<4i>@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v2f:", {"full_signature": b"@@:<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v2f:", {"full_signature": b"@@:<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v2f:v2I:q:id:", {"full_signature": b"@@:<2f><2I>q@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v2f:v2I:q:id:", {"full_signature": b"@@:<2f><2I>q@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v2f:v2f:", {"full_signature": b"@@:<2f><2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v2f:v2f:", {"full_signature": b"@@:<2f><2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v2i:", {"full_signature": b"@@:<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v2i:", {"full_signature": b"@@:<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v2i:i:i:Z:", {"full_signature": b"@@:<2i>iiZ"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v2i:i:i:Z:", {"full_signature": b"@@:<2i>iiZ"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v2i:i:i:Z:Class:", {"full_signature": b"@@:<2i>iiZ#"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v2i:i:i:Z:Class:", {"full_signature": b"@@:<2i>iiZ#"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v3f:", {"full_signature": b"@@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v3f:", {"full_signature": b"@@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v3f:v2I:Z:Z:Z:q:id:", {"full_signature": b"@@:<3f><2I>ZZZq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsid:v3f:v2I:Z:Z:Z:q:id:",
    {"full_signature": b"@@:<3f><2I>ZZZq@"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v3f:v2I:Z:Z:q:id:", {"full_signature": b"@@:<3f><2I>ZZq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v3f:v2I:Z:Z:q:id:", {"full_signature": b"@@:<3f><2I>ZZq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v3f:v2I:Z:q:id:", {"full_signature": b"@@:<3f><2I>Zq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v3f:v2I:Z:q:id:", {"full_signature": b"@@:<3f><2I>Zq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v3f:v2I:i:Z:q:id:", {"full_signature": b"@@:<3f><2I>iZq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v3f:v2I:i:Z:q:id:", {"full_signature": b"@@:<3f><2I>iZq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v3f:v2I:q:id:", {"full_signature": b"@@:<3f><2I>q@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v3f:v2I:q:id:", {"full_signature": b"@@:<3f><2I>q@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v3f:v3I:Z:q:id:", {"full_signature": b"@@:<3f><3I>Zq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v3f:v3I:Z:q:id:", {"full_signature": b"@@:<3f><3I>Zq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v3f:v3I:q:Z:id:", {"full_signature": b"@@:<3f><3I>qZ@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v3f:v3I:q:Z:id:", {"full_signature": b"@@:<3f><3I>qZ@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v3f:Q:Q:q:Z:Z:id:", {"full_signature": b"@@:<3f>QQqZZ@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v3f:Q:Q:q:Z:Z:id:", {"full_signature": b"@@:<3f>QQqZZ@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v3f:Z:q:id:", {"full_signature": b"@@:<3f>Zq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v3f:Z:q:id:", {"full_signature": b"@@:<3f>Zq@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:v4f:", {"full_signature": b"@@:<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:v4f:", {"full_signature": b"@@:<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:id:v2d:v2d:v2i:Z:", {"full_signature": b"@@:@<2d><2d><2i>Z"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsid:id:v2d:v2d:v2i:Z:",
    {"full_signature": b"@@:@<2d><2d><2i>Z"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:id:v2f:", {"full_signature": b"@@:@<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:id:v2f:", {"full_signature": b"@@:@<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:id:v3f:", {"full_signature": b"@@:@<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:id:v3f:", {"full_signature": b"@@:@<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:id:v4f:", {"full_signature": b"@@:@<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:id:v4f:", {"full_signature": b"@@:@<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:id:id:v2i:", {"full_signature": b"@@:@@<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:id:id:v2i:", {"full_signature": b"@@:@@<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:id:id:v2i:f:", {"full_signature": b"@@:@@<2i>f"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:id:id:v2i:f:", {"full_signature": b"@@:@@<2i>f"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:id:Q:v2f:", {"full_signature": b"@@:@Q<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:id:Q:v2f:", {"full_signature": b"@@:@Q<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:id:Q:v3f:", {"full_signature": b"@@:@Q<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:id:Q:v3f:", {"full_signature": b"@@:@Q<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:id:Q:v4f:", {"full_signature": b"@@:@Q<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:id:Q:v4f:", {"full_signature": b"@@:@Q<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"id:id:Q:matrix_float4x4:",
    {"full_signature": b"@@:@Q{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsid:id:Q:matrix_float4x4:",
    {"full_signature": b"@@:@Q{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:id:Z:id:v2i:q:Q:q:Z:", {"full_signature": b"@@:@Z@<2i>qQqZ"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsid:id:Z:id:v2i:q:Q:q:Z:",
    {"full_signature": b"@@:@Z@<2i>qQqZ"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:id:q:v2i:f:f:f:f:", {"full_signature": b"@@:@q<2i>ffff"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:id:q:v2i:f:f:f:f:", {"full_signature": b"@@:@q<2i>ffff"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:id:q:v2i:f:f:f:f:f:", {"full_signature": b"@@:@q<2i>fffff"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsid:id:q:v2i:f:f:f:f:f:",
    {"full_signature": b"@@:@q<2i>fffff"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:id:GKBox:", {"full_signature": b"@@:@{GKBox=<3f><3f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:id:GKBox:", {"full_signature": b"@@:@{GKBox=<3f><3f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:id:GKQuad:", {"full_signature": b"@@:@{GKQuad=<2f><2f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:id:GKQuad:", {"full_signature": b"@@:@{GKQuad=<2f><2f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"id:id:MDLAxisAlignedBoundingBox:f:",
    {"full_signature": b"@@:@{_MDLAxisAlignedBoundingBox=<3f><3f>}f"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsid:id:MDLAxisAlignedBoundingBox:f:",
    {"full_signature": b"@@:@{_MDLAxisAlignedBoundingBox=<3f><3f>}f"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"id:id:matrix_float2x2:",
    {"full_signature": b"@@:@{_matrix_float2x2=[2<2f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsid:id:matrix_float2x2:",
    {"full_signature": b"@@:@{_matrix_float2x2=[2<2f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"id:id:matrix_float3x3:",
    {"full_signature": b"@@:@{_matrix_float3x3=[3<3f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsid:id:matrix_float3x3:",
    {"full_signature": b"@@:@{_matrix_float3x3=[3<3f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"id:id:matrix_float4x4:",
    {"full_signature": b"@@:@{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsid:id:matrix_float4x4:",
    {"full_signature": b"@@:@{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"id:CGColor:CGColor:id:v2i:",
    {"full_signature": b"@@:^{CGColor=}^{CGColor=}@<2i>"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsid:CGColor:CGColor:id:v2i:",
    {"full_signature": b"@@:^{CGColor=}^{CGColor=}@<2i>"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:f:v2f:v2f:", {"full_signature": b"@@:f<2f><2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:f:v2f:v2f:", {"full_signature": b"@@:f<2f><2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:f:v2f:v2f:Class:", {"full_signature": b"@@:f<2f><2f>#"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:f:v2f:v2f:Class:", {"full_signature": b"@@:f<2f><2f>#"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:f:v2f:Q:Q:Q:q:Z:id:", {"full_signature": b"@@:f<2f>QQQqZ@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsid:f:v2f:Q:Q:Q:q:Z:id:",
    {"full_signature": b"@@:f<2f>QQQqZ@"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:f:v2f:Q:Q:q:Z:id:", {"full_signature": b"@@:f<2f>QQqZ@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:f:v2f:Q:Q:q:Z:id:", {"full_signature": b"@@:f<2f>QQqZ@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:f:id:v2i:i:q:Z:", {"full_signature": b"@@:f@<2i>iqZ"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:f:id:v2i:i:q:Z:", {"full_signature": b"@@:f@<2i>iqZ"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"id:f:id:v2i:i:q:CGColor:CGColor:",
    {"full_signature": b"@@:f@<2i>iq^{CGColor=}^{CGColor=}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsid:f:id:v2i:i:q:CGColor:CGColor:",
    {"full_signature": b"@@:f@<2i>iq^{CGColor=}^{CGColor=}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:f:id:v2i:q:", {"full_signature": b"@@:f@<2i>q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:f:id:v2i:q:", {"full_signature": b"@@:f@<2i>q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:f:f:id:v2i:", {"full_signature": b"@@:ff@<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:f:f:id:v2i:", {"full_signature": b"@@:ff@<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:GKBox:", {"full_signature": b"@@:{GKBox=<3f><3f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:GKBox:", {"full_signature": b"@@:{GKBox=<3f><3f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:GKBox:f:", {"full_signature": b"@@:{GKBox=<3f><3f>}f"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:GKBox:f:", {"full_signature": b"@@:{GKBox=<3f><3f>}f"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:GKQuad:", {"full_signature": b"@@:{GKQuad=<2f><2f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:GKQuad:", {"full_signature": b"@@:{GKQuad=<2f><2f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"id:GKQuad:f:", {"full_signature": b"@@:{GKQuad=<2f><2f>}f"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsid:GKQuad:f:", {"full_signature": b"@@:{GKQuad=<2f><2f>}f"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"id:MDLVoxelIndexExtent:",
    {"full_signature": b"@@:{_MDLVoxelIndexExtent=<4i><4i>}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsid:MDLVoxelIndexExtent:",
    {"full_signature": b"@@:{_MDLVoxelIndexExtent=<4i><4i>}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"id:matrix_float4x4:",
    {"full_signature": b"@@:{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsid:matrix_float4x4:",
    {"full_signature": b"@@:{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"id:matrix_float4x4:Z:",
    {"full_signature": b"@@:{_matrix_float4x4=[4<4f>]}Z"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsid:matrix_float4x4:Z:",
    {"full_signature": b"@@:{_matrix_float4x4=[4<4f>]}Z"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"Z:v2i:id:id:id:id:", {"full_signature": b"Z@:<2i>@@@@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsZ:v2i:id:id:id:id:", {"full_signature": b"Z@:<2i>@@@@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"Z:v2i:q:f:id:id:id:", {"full_signature": b"Z@:<2i>qf@@@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsZ:v2i:q:f:id:id:id:", {"full_signature": b"Z@:<2i>qf@@@"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"Z:v4i:Z:Z:Z:Z:", {"full_signature": b"Z@:<4i>ZZZZ"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsZ:v4i:Z:Z:Z:Z:", {"full_signature": b"Z@:<4i>ZZZZ"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"CGColor:v3f:", {"full_signature": b"^{CGColor=}@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsCGColor:v3f:", {"full_signature": b"^{CGColor=}@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"CGColor:v3f:CGColorSpace:",
    {"full_signature": b"^{CGColor=}@:<3f>^{CGColorSpace=}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsCGColor:v3f:CGColorSpace:",
    {"full_signature": b"^{CGColor=}@:<3f>^{CGColorSpace=}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"f:v2f:", {"full_signature": b"f@:<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsf:v2f:", {"full_signature": b"f@:<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"f:v2i:", {"full_signature": b"f@:<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsf:v2i:", {"full_signature": b"f@:<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:v2d:d:", {"full_signature": b"v@:<2d>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:v2d:d:", {"full_signature": b"v@:<2d>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:v2f:", {"full_signature": b"v@:<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:v2f:", {"full_signature": b"v@:<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:v2f:d:", {"full_signature": b"v@:<2f>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:v2f:d:", {"full_signature": b"v@:<2f>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:v3d:", {"full_signature": b"v@:<3d>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:v3d:", {"full_signature": b"v@:<3d>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:v3d:d:", {"full_signature": b"v@:<3d>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:v3d:d:", {"full_signature": b"v@:<3d>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:v3f:", {"full_signature": b"v@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:v3f:", {"full_signature": b"v@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:v3f:v3f:", {"full_signature": b"v@:<3f><3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:v3f:v3f:", {"full_signature": b"v@:<3f><3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:v3f:v3f:v3f:", {"full_signature": b"v@:<3f><3f><3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:v3f:v3f:v3f:", {"full_signature": b"v@:<3f><3f><3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:v3f:d:", {"full_signature": b"v@:<3f>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:v3f:d:", {"full_signature": b"v@:<3f>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:v4d:d:", {"full_signature": b"v@:<4d>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:v4d:d:", {"full_signature": b"v@:<4d>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:v4f:", {"full_signature": b"v@:<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:v4f:", {"full_signature": b"v@:<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:v4f:d:", {"full_signature": b"v@:<4f>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:v4f:d:", {"full_signature": b"v@:<4f>d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:v4i:", {"full_signature": b"v@:<4i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:v4i:", {"full_signature": b"v@:<4i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:id:v2f:v2f:", {"full_signature": b"v@:@<2f><2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:id:v2f:v2f:", {"full_signature": b"v@:@<2f><2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:id:v2f:v2f:q:", {"full_signature": b"v@:@<2f><2f>q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:id:v2f:v2f:q:", {"full_signature": b"v@:@<2f><2f>q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:f:v2i:", {"full_signature": b"v@:f<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:f:v2i:", {"full_signature": b"v@:f<2i>"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"v:MDLAxisAlignedBoundingBox:",
    {"full_signature": b"v@:{_MDLAxisAlignedBoundingBox=<3f><3f>}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsv:MDLAxisAlignedBoundingBox:",
    {"full_signature": b"v@:{_MDLAxisAlignedBoundingBox=<3f><3f>}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"v:MDLAxisAlignedBoundingBox:Z:",
    {"full_signature": b"v@:{_MDLAxisAlignedBoundingBox=<3f><3f>}Z"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsv:MDLAxisAlignedBoundingBox:Z:",
    {"full_signature": b"v@:{_MDLAxisAlignedBoundingBox=<3f><3f>}Z"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"v:matrix_double4x4:",
    {"full_signature": b"v@:{_matrix_double4x4=[4<4d>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsv:matrix_double4x4:",
    {"full_signature": b"v@:{_matrix_double4x4=[4<4d>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"v:matrix_double4x4:d:",
    {"full_signature": b"v@:{_matrix_double4x4=[4<4d>]}d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsv:matrix_double4x4:d:",
    {"full_signature": b"v@:{_matrix_double4x4=[4<4d>]}d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"v:matrix_float2x2:",
    {"full_signature": b"v@:{_matrix_float2x2=[2<2f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsv:matrix_float2x2:",
    {"full_signature": b"v@:{_matrix_float2x2=[2<2f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"v:matrix_float3x3:",
    {"full_signature": b"v@:{_matrix_float3x3=[3<3f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsv:matrix_float3x3:",
    {"full_signature": b"v@:{_matrix_float3x3=[3<3f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"v:matrix_float4x4:",
    {"full_signature": b"v@:{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsv:matrix_float4x4:",
    {"full_signature": b"v@:{_matrix_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"v:matrix_float4x4:d:",
    {"full_signature": b"v@:{_matrix_float4x4=[4<4f>]}d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsv:matrix_float4x4:d:",
    {"full_signature": b"v@:{_matrix_float4x4=[4<4f>]}d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"v:simd_float4x4:",
    {"full_signature": b"v@:{_simd_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsv:simd_float4x4:",
    {"full_signature": b"v@:{_simd_float4x4=[4<4f>]}"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:simd_quatd:d:", {"full_signature": b"v@:{_simd_quatd=<4d>}d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsv:simd_quatd:d:",
    {"full_signature": b"v@:{_simd_quatd=<4d>}d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:simd_quatf:", {"full_signature": b"v@:{_simd_quatf=<4f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clsv:simd_quatf:", {"full_signature": b"v@:{_simd_quatf=<4f>}"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"v:simd_quatf:v3f:",
    {"full_signature": b"v@:{_simd_quatf=<4f>}<3f>"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsv:simd_quatf:v3f:",
    {"full_signature": b"v@:{_simd_quatf=<4f>}<3f>"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"v:simd_quatf:d:", {"full_signature": b"v@:{_simd_quatf=<4f>}d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsv:simd_quatf:d:",
    {"full_signature": b"v@:{_simd_quatf=<4f>}d"},
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
    b"OC_VectorCall", b"GKTriangle:Q:", {"full_signature": b"{GKTriangle=[3<3f>]}@:Q"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsGKTriangle:Q:",
    {"full_signature": b"{GKTriangle=[3<3f>]}@:Q"},
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
    b"MDLAxisAlignedBoundingBox:v4i:",
    {"full_signature": b"{_MDLAxisAlignedBoundingBox=<3f><3f>}@:<4i>"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsMDLAxisAlignedBoundingBox:v4i:",
    {"full_signature": b"{_MDLAxisAlignedBoundingBox=<3f><3f>}@:<4i>"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"MDLAxisAlignedBoundingBox:d:",
    {"full_signature": b"{_MDLAxisAlignedBoundingBox=<3f><3f>}@:d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsMDLAxisAlignedBoundingBox:d:",
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
    b"matrix_double4x4",
    {"full_signature": b"{_matrix_double4x4=[4<4d>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsmatrix_double4x4",
    {"full_signature": b"{_matrix_double4x4=[4<4d>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"matrix_double4x4:d:",
    {"full_signature": b"{_matrix_double4x4=[4<4d>]}@:d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsmatrix_double4x4:d:",
    {"full_signature": b"{_matrix_double4x4=[4<4d>]}@:d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"matrix_float2x2",
    {"full_signature": b"{_matrix_float2x2=[2<2f>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsmatrix_float2x2",
    {"full_signature": b"{_matrix_float2x2=[2<2f>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"matrix_float3x3",
    {"full_signature": b"{_matrix_float3x3=[3<3f>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsmatrix_float3x3",
    {"full_signature": b"{_matrix_float3x3=[3<3f>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"matrix_float4x4",
    {"full_signature": b"{_matrix_float4x4=[4<4f>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsmatrix_float4x4",
    {"full_signature": b"{_matrix_float4x4=[4<4f>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"matrix_float4x4:id:d:",
    {"full_signature": b"{_matrix_float4x4=[4<4f>]}@:@d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsmatrix_float4x4:id:d:",
    {"full_signature": b"{_matrix_float4x4=[4<4f>]}@:@d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"matrix_float4x4:d:",
    {"full_signature": b"{_matrix_float4x4=[4<4f>]}@:d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clsmatrix_float4x4:d:",
    {"full_signature": b"{_matrix_float4x4=[4<4f>]}@:d"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"simd_float4x4",
    {"full_signature": b"{_simd_float4x4=[4<4f>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clssimd_float4x4",
    {"full_signature": b"{_simd_float4x4=[4<4f>]}@:"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"simd_float4x4:simd_float4x4:id:",
    {"full_signature": b"{_simd_float4x4=[4<4f>]}@:{_simd_float4x4=[4<4f>]}@"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall",
    b"clssimd_float4x4:simd_float4x4:id:",
    {"full_signature": b"{_simd_float4x4=[4<4f>]}@:{_simd_float4x4=[4<4f>]}@"},
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"simd_quatd:d:", {"full_signature": b"{_simd_quatd=<4d>}@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clssimd_quatd:d:", {"full_signature": b"{_simd_quatd=<4d>}@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"simd_quatf", {"full_signature": b"{_simd_quatf=<4f>}@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clssimd_quatf", {"full_signature": b"{_simd_quatf=<4f>}@:"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"simd_quatf:d:", {"full_signature": b"{_simd_quatf=<4f>}@:d"}
)
objc.registerMetaDataForSelector(
    b"OC_VectorCall", b"clssimd_quatf:d:", {"full_signature": b"{_simd_quatf=<4f>}@:d"}
)


class TestVectorCall(TestCase):
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

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v16C()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v16C("hello")

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

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v2d()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v2d("hello")

    def test_v2d_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v2d_d_, b"<2d>")
        self.assertArgHasType(OC_VectorCall.v2d_d_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v2d_d_(-557000000000.0)
        self.assertEqual(rv, objc.simd.vector_double2(0.0, 1.5))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v2d_d_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v2d_d_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v2d_d_(None)

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

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v2f()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v2f("hello")

    def test_v2f_Q_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v2f_Q_, b"<2f>")
        self.assertArgHasType(OC_VectorCall.v2f_Q_, 0, b"Q")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v2f_Q_(35184372088832)
        self.assertEqual(rv, objc.simd.vector_float2(0.0, 1.5))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], 35184372088832)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v2f_Q_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v2f_Q_(35184372088832, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v2f_Q_(None)

    def test_v2f_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v2f_d_, b"<2f>")
        self.assertArgHasType(OC_VectorCall.v2f_d_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v2f_d_(-557000000000.0)
        self.assertEqual(rv, objc.simd.vector_float2(0.0, 1.5))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v2f_d_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v2f_d_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v2f_d_(None)

    def test_v2f_q_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v2f_q_, b"<2f>")
        self.assertArgHasType(OC_VectorCall.v2f_q_, 0, b"q")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v2f_q_(-17592186044416)
        self.assertEqual(rv, objc.simd.vector_float2(0.0, 1.5))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -17592186044416)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v2f_q_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v2f_q_(-17592186044416, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v2f_q_(None)

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

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v2i()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v2i("hello")

    def test_v3d_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v3d_d_, b"<3d>")
        self.assertArgHasType(OC_VectorCall.v3d_d_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v3d_d_(-557000000000.0)
        self.assertEqual(rv, objc.simd.vector_double3(0.0, 1.5, 3.0))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3d_d_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3d_d_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v3d_d_(None)

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

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3f()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3f("hello")

    def test_v3f_v2i_v2i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v3f_v2i_v2i_, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v3f_v2i_v2i_, 0, b"<2i>")
        self.assertArgHasType(OC_VectorCall.v3f_v2i_v2i_, 1, b"<2i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v3f_v2i_v2i_(objc.simd.vector_int2(0, 1), objc.simd.vector_int2(0, 1))
        self.assertEqual(rv, objc.simd.vector_float3(0.0, 1.5, 3.0))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_int2(0, 1))
        self.assertEqual(stored[1], objc.simd.vector_int2(0, 1))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3f_v2i_v2i_(objc.simd.vector_int2(0, 1))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3f_v2i_v2i_(
                objc.simd.vector_int2(0, 1), objc.simd.vector_int2(0, 1), "hello"
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v3f_v2i_v2i_(None, objc.simd.vector_int2(0, 1))

        with self.assertRaises(TypeError):
            self.v3f_v2i_v2i_(objc.simd.vector_int2(0, 1), None)

    def test_v3f_v3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v3f_v3f_, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v3f_v3f_, 0, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v3f_v3f_(objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(rv, objc.simd.vector_float3(0.0, 1.5, 3.0))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3f_v3f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3f_v3f_(objc.simd.vector_float3(0.0, 1.5, 3.0), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v3f_v3f_(None)

    def test_v3f_v3f_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v3f_v3f_id_, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v3f_v3f_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v3f_v3f_id_, 1, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v3f_v3f_id_(objc.simd.vector_float3(0.0, 1.5, 3.0), "hello")
        self.assertEqual(rv, objc.simd.vector_float3(0.0, 1.5, 3.0))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3f_v3f_id_(objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3f_v3f_id_(objc.simd.vector_float3(0.0, 1.5, 3.0), "hello", "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v3f_v3f_id_(None, "hello")

        with self.assertRaises(TypeError):
            self.v3f_v3f_id_(objc.simd.vector_float3(0.0, 1.5, 3.0), NoObjCValueObject)

    def test_v3f_v4i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v3f_v4i_, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v3f_v4i_, 0, b"<4i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v3f_v4i_(objc.simd.vector_int4(0, 1, 2, 3))
        self.assertEqual(rv, objc.simd.vector_float3(0.0, 1.5, 3.0))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_int4(0, 1, 2, 3))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3f_v4i_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3f_v4i_(objc.simd.vector_int4(0, 1, 2, 3), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v3f_v4i_(None)

    def test_v3f_Q_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v3f_Q_, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v3f_Q_, 0, b"Q")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v3f_Q_(35184372088832)
        self.assertEqual(rv, objc.simd.vector_float3(0.0, 1.5, 3.0))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], 35184372088832)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3f_Q_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3f_Q_(35184372088832, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v3f_Q_(None)

    def test_v3f_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v3f_d_, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v3f_d_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v3f_d_(-557000000000.0)
        self.assertEqual(rv, objc.simd.vector_float3(0.0, 1.5, 3.0))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3f_d_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v3f_d_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v3f_d_(None)

    def test_v4d_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v4d_d_, b"<4d>")
        self.assertArgHasType(OC_VectorCall.v4d_d_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v4d_d_(-557000000000.0)
        self.assertEqual(rv, objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v4d_d_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v4d_d_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v4d_d_(None)

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

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v4f()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v4f("hello")

    def test_v4f_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v4f_d_, b"<4f>")
        self.assertArgHasType(OC_VectorCall.v4f_d_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v4f_d_(-557000000000.0)
        self.assertEqual(rv, objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v4f_d_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v4f_d_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v4f_d_(None)

    def test_v4i_v3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v4i_v3f_, b"<4i>")
        self.assertArgHasType(OC_VectorCall.v4i_v3f_, 0, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v4i_v3f_(objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(rv, objc.simd.vector_int4(0, 1, 2, 3))

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v4i_v3f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v4i_v3f_(objc.simd.vector_float3(0.0, 1.5, 3.0), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v4i_v3f_(None)

    def test_id_v2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v2f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v2f_, 0, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v2f_(objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v2f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v2f_(objc.simd.vector_float2(0.0, 1.5), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_v2f_(None)

    def test_id_v2f_v2I_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v2f_v2I_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v2f_v2I_q_id_, 0, b"<2f>")
        self.assertArgHasType(OC_VectorCall.id_v2f_v2I_q_id_, 1, b"<2I>")
        self.assertArgHasType(OC_VectorCall.id_v2f_v2I_q_id_, 2, b"q")
        self.assertArgHasType(OC_VectorCall.id_v2f_v2I_q_id_, 3, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v2f_v2I_q_id_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v2f_v2I_q_id_(
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_uint2(0, 1),
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v2f_v2I_q_id_(
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_uint2(0, 1),
                -17592186044416,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_v2f_v2I_q_id_(
                None, objc.simd.vector_uint2(0, 1), -17592186044416, "hello"
            )

        with self.assertRaises(TypeError):
            self.id_v2f_v2I_q_id_(
                objc.simd.vector_float2(0.0, 1.5), None, -17592186044416, "hello"
            )

        with self.assertRaises(TypeError):
            self.id_v2f_v2I_q_id_(
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_uint2(0, 1),
                None,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v2f_v2I_q_id_(
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_uint2(0, 1),
                -17592186044416,
                NoObjCValueObject,
            )

    def test_id_v2f_v2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v2f_v2f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v2f_v2f_, 0, b"<2f>")
        self.assertArgHasType(OC_VectorCall.id_v2f_v2f_, 1, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v2f_v2f_(
            objc.simd.vector_float2(0.0, 1.5), objc.simd.vector_float2(0.0, 1.5)
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(stored[1], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v2f_v2f_(objc.simd.vector_float2(0.0, 1.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v2f_v2f_(
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_v2f_v2f_(None, objc.simd.vector_float2(0.0, 1.5))

        with self.assertRaises(TypeError):
            self.id_v2f_v2f_(objc.simd.vector_float2(0.0, 1.5), None)

    def test_id_v2i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v2i_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v2i_, 0, b"<2i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v2i_(objc.simd.vector_int2(0, 1))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_int2(0, 1))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v2i_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v2i_(objc.simd.vector_int2(0, 1), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_v2i_(None)

    def test_id_v2i_i_i_Z_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v2i_i_i_Z_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v2i_i_i_Z_, 0, b"<2i>")
        self.assertArgHasType(OC_VectorCall.id_v2i_i_i_Z_, 1, b"i")
        self.assertArgHasType(OC_VectorCall.id_v2i_i_i_Z_, 2, b"i")
        self.assertArgHasType(OC_VectorCall.id_v2i_i_i_Z_, 3, b"Z")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v2i_i_i_Z_(objc.simd.vector_int2(0, 1), -42, -42, False)
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 4)
        self.assertEqual(stored[0], objc.simd.vector_int2(0, 1))
        self.assertEqual(stored[1], -42)
        self.assertEqual(stored[2], -42)
        self.assertEqual(stored[3], False)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v2i_i_i_Z_(objc.simd.vector_int2(0, 1), -42, -42)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v2i_i_i_Z_(objc.simd.vector_int2(0, 1), -42, -42, False, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_v2i_i_i_Z_(None, -42, -42, False)

        with self.assertRaises(TypeError):
            self.id_v2i_i_i_Z_(objc.simd.vector_int2(0, 1), None, -42, False)

        with self.assertRaises(TypeError):
            self.id_v2i_i_i_Z_(objc.simd.vector_int2(0, 1), -42, None, False)

        with self.assertRaises(TypeError):
            self.id_v2i_i_i_Z_(objc.simd.vector_int2(0, 1), -42, -42, None)

    def test_id_v2i_i_i_Z_Class_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v2i_i_i_Z_Class_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v2i_i_i_Z_Class_, 0, b"<2i>")
        self.assertArgHasType(OC_VectorCall.id_v2i_i_i_Z_Class_, 1, b"i")
        self.assertArgHasType(OC_VectorCall.id_v2i_i_i_Z_Class_, 2, b"i")
        self.assertArgHasType(OC_VectorCall.id_v2i_i_i_Z_Class_, 3, b"Z")
        self.assertArgHasType(OC_VectorCall.id_v2i_i_i_Z_Class_, 4, b"#")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v2i_i_i_Z_Class_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v2i_i_i_Z_Class_(objc.simd.vector_int2(0, 1), -42, -42, False)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v2i_i_i_Z_Class_(
                objc.simd.vector_int2(0, 1),
                -42,
                -42,
                False,
                objc.lookUpClass("NSObject"),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_v2i_i_i_Z_Class_(
                None, -42, -42, False, objc.lookUpClass("NSObject")
            )

        with self.assertRaises(TypeError):
            self.id_v2i_i_i_Z_Class_(
                objc.simd.vector_int2(0, 1),
                None,
                -42,
                False,
                objc.lookUpClass("NSObject"),
            )

        with self.assertRaises(TypeError):
            self.id_v2i_i_i_Z_Class_(
                objc.simd.vector_int2(0, 1),
                -42,
                None,
                False,
                objc.lookUpClass("NSObject"),
            )

        with self.assertRaises(TypeError):
            self.id_v2i_i_i_Z_Class_(
                objc.simd.vector_int2(0, 1),
                -42,
                -42,
                None,
                objc.lookUpClass("NSObject"),
            )

        with self.assertRaises(TypeError):
            self.id_v2i_i_i_Z_Class_(objc.simd.vector_int2(0, 1), -42, -42, False, 42)

    def test_id_v3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v3f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v3f_, 0, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v3f_(objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_(objc.simd.vector_float3(0.0, 1.5, 3.0), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_v3f_(None)

    def test_id_v3f_v2I_Z_Z_Z_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v3f_v2I_Z_Z_Z_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_Z_Z_q_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_Z_Z_q_id_, 1, b"<2I>")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_Z_Z_q_id_, 2, b"Z")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_Z_Z_q_id_, 3, b"Z")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_Z_Z_q_id_, 4, b"Z")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_Z_Z_q_id_, 5, b"q")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_Z_Z_q_id_, 6, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v3f_v2I_Z_Z_Z_q_id_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_v2I_Z_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                False,
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_v2I_Z_Z_Z_q_id_(
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
        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_Z_Z_q_id_(
                None,
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                False,
                False,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                None,
                False,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                None,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                None,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                False,
                None,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                False,
                -17592186044416,
                NoObjCValueObject,
            )

    def test_id_v3f_v2I_Z_Z_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v3f_v2I_Z_Z_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_Z_q_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_Z_q_id_, 1, b"<2I>")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_Z_q_id_, 2, b"Z")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_Z_q_id_, 3, b"Z")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_Z_q_id_, 4, b"q")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_Z_q_id_, 5, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v3f_v2I_Z_Z_q_id_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_v2I_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_v2I_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                -17592186044416,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_Z_q_id_(
                None,
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                False,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                None,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                None,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                None,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                False,
                -17592186044416,
                NoObjCValueObject,
            )

    def test_id_v3f_v2I_Z_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v3f_v2I_Z_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_q_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_q_id_, 1, b"<2I>")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_q_id_, 2, b"Z")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_q_id_, 3, b"q")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_Z_q_id_, 4, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v3f_v2I_Z_q_id_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_v2I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_v2I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                -17592186044416,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_q_id_(
                None, objc.simd.vector_uint2(0, 1), False, -17592186044416, "hello"
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                None,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                None,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                False,
                -17592186044416,
                NoObjCValueObject,
            )

    def test_id_v3f_v2I_i_Z_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v3f_v2I_i_Z_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_i_Z_q_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_i_Z_q_id_, 1, b"<2I>")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_i_Z_q_id_, 2, b"i")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_i_Z_q_id_, 3, b"Z")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_i_Z_q_id_, 4, b"q")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_i_Z_q_id_, 5, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v3f_v2I_i_Z_q_id_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_v2I_i_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -42,
                False,
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_v2I_i_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -42,
                False,
                -17592186044416,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_v3f_v2I_i_Z_q_id_(
                None, objc.simd.vector_uint2(0, 1), -42, False, -17592186044416, "hello"
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_i_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                -42,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_i_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                None,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_i_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -42,
                None,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_i_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -42,
                False,
                None,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_i_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -42,
                False,
                -17592186044416,
                NoObjCValueObject,
            )

    def test_id_v3f_v2I_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v3f_v2I_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_q_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_q_id_, 1, b"<2I>")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_q_id_, 2, b"q")
        self.assertArgHasType(OC_VectorCall.id_v3f_v2I_q_id_, 3, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v3f_v2I_q_id_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_v2I_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_v2I_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -17592186044416,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_v3f_v2I_q_id_(
                None, objc.simd.vector_uint2(0, 1), -17592186044416, "hello"
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0), None, -17592186044416, "hello"
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                None,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v2I_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint2(0, 1),
                -17592186044416,
                NoObjCValueObject,
            )

    def test_id_v3f_v3I_Z_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v3f_v3I_Z_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v3f_v3I_Z_q_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.id_v3f_v3I_Z_q_id_, 1, b"<3I>")
        self.assertArgHasType(OC_VectorCall.id_v3f_v3I_Z_q_id_, 2, b"Z")
        self.assertArgHasType(OC_VectorCall.id_v3f_v3I_Z_q_id_, 3, b"q")
        self.assertArgHasType(OC_VectorCall.id_v3f_v3I_Z_q_id_, 4, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v3f_v3I_Z_q_id_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_v3I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                False,
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_v3I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                False,
                -17592186044416,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_v3f_v3I_Z_q_id_(
                None, objc.simd.vector_uint3(0, 1, 2), False, -17592186044416, "hello"
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v3I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                False,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v3I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                None,
                -17592186044416,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v3I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                False,
                None,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v3I_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                False,
                -17592186044416,
                NoObjCValueObject,
            )

    def test_id_v3f_v3I_q_Z_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v3f_v3I_q_Z_id_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v3f_v3I_q_Z_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.id_v3f_v3I_q_Z_id_, 1, b"<3I>")
        self.assertArgHasType(OC_VectorCall.id_v3f_v3I_q_Z_id_, 2, b"q")
        self.assertArgHasType(OC_VectorCall.id_v3f_v3I_q_Z_id_, 3, b"Z")
        self.assertArgHasType(OC_VectorCall.id_v3f_v3I_q_Z_id_, 4, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v3f_v3I_q_Z_id_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_v3I_q_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                -17592186044416,
                False,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_v3I_q_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                -17592186044416,
                False,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_v3f_v3I_q_Z_id_(
                None, objc.simd.vector_uint3(0, 1, 2), -17592186044416, False, "hello"
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v3I_q_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v3I_q_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                None,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v3I_q_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                -17592186044416,
                None,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_v3I_q_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_uint3(0, 1, 2),
                -17592186044416,
                False,
                NoObjCValueObject,
            )

    def test_id_v3f_Q_Q_q_Z_Z_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v3f_Q_Q_q_Z_Z_id_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v3f_Q_Q_q_Z_Z_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.id_v3f_Q_Q_q_Z_Z_id_, 1, b"Q")
        self.assertArgHasType(OC_VectorCall.id_v3f_Q_Q_q_Z_Z_id_, 2, b"Q")
        self.assertArgHasType(OC_VectorCall.id_v3f_Q_Q_q_Z_Z_id_, 3, b"q")
        self.assertArgHasType(OC_VectorCall.id_v3f_Q_Q_q_Z_Z_id_, 4, b"Z")
        self.assertArgHasType(OC_VectorCall.id_v3f_Q_Q_q_Z_Z_id_, 5, b"Z")
        self.assertArgHasType(OC_VectorCall.id_v3f_Q_Q_q_Z_Z_id_, 6, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v3f_Q_Q_q_Z_Z_id_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_Q_Q_q_Z_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                False,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_Q_Q_q_Z_Z_id_(
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
        with self.assertRaises(TypeError):
            self.id_v3f_Q_Q_q_Z_Z_id_(
                None,
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_Q_Q_q_Z_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                35184372088832,
                -17592186044416,
                False,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_Q_Q_q_Z_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                35184372088832,
                None,
                -17592186044416,
                False,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_Q_Q_q_Z_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                35184372088832,
                35184372088832,
                None,
                False,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_Q_Q_q_Z_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                35184372088832,
                35184372088832,
                -17592186044416,
                None,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_Q_Q_q_Z_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                None,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_v3f_Q_Q_q_Z_Z_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                False,
                NoObjCValueObject,
            )

    def test_id_v3f_Z_q_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v3f_Z_q_id_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v3f_Z_q_id_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.id_v3f_Z_q_id_, 1, b"Z")
        self.assertArgHasType(OC_VectorCall.id_v3f_Z_q_id_, 2, b"q")
        self.assertArgHasType(OC_VectorCall.id_v3f_Z_q_id_, 3, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v3f_Z_q_id_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0), False, -17592186044416
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v3f_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                False,
                -17592186044416,
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_v3f_Z_q_id_(None, False, -17592186044416, "hello")

        with self.assertRaises(TypeError):
            self.id_v3f_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0), None, -17592186044416, "hello"
            )

        with self.assertRaises(TypeError):
            self.id_v3f_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0), False, None, "hello"
            )

        with self.assertRaises(TypeError):
            self.id_v3f_Z_q_id_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                False,
                -17592186044416,
                NoObjCValueObject,
            )

    def test_id_v4f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_v4f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_v4f_, 0, b"<4f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_v4f_(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v4f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_v4f_(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_v4f_(None)

    def test_id_id_v2d_v2d_v2i_Z_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_v2d_v2d_v2i_Z_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_v2d_v2d_v2i_Z_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_v2d_v2d_v2i_Z_, 1, b"<2d>")
        self.assertArgHasType(OC_VectorCall.id_id_v2d_v2d_v2i_Z_, 2, b"<2d>")
        self.assertArgHasType(OC_VectorCall.id_id_v2d_v2d_v2i_Z_, 3, b"<2i>")
        self.assertArgHasType(OC_VectorCall.id_id_v2d_v2d_v2i_Z_, 4, b"Z")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_v2d_v2d_v2i_Z_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_v2d_v2d_v2i_Z_(
                "hello",
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_int2(0, 1),
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_v2d_v2d_v2i_Z_(
                "hello",
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_int2(0, 1),
                False,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_v2d_v2d_v2i_Z_(
                NoObjCValueObject,
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_int2(0, 1),
                False,
            )

        with self.assertRaises(TypeError):
            self.id_id_v2d_v2d_v2i_Z_(
                "hello",
                None,
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_int2(0, 1),
                False,
            )

        with self.assertRaises(TypeError):
            self.id_id_v2d_v2d_v2i_Z_(
                "hello",
                objc.simd.vector_double2(0.0, 1.5),
                None,
                objc.simd.vector_int2(0, 1),
                False,
            )

        with self.assertRaises(TypeError):
            self.id_id_v2d_v2d_v2i_Z_(
                "hello",
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_double2(0.0, 1.5),
                None,
                False,
            )

        with self.assertRaises(TypeError):
            self.id_id_v2d_v2d_v2i_Z_(
                "hello",
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_double2(0.0, 1.5),
                objc.simd.vector_int2(0, 1),
                None,
            )

    def test_id_id_v2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_v2f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_v2f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_v2f_, 1, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_v2f_("hello", objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_v2f_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_v2f_("hello", objc.simd.vector_float2(0.0, 1.5), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_v2f_(NoObjCValueObject, objc.simd.vector_float2(0.0, 1.5))

        with self.assertRaises(TypeError):
            self.id_id_v2f_("hello", None)

    def test_id_id_v3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_v3f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_v3f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_v3f_, 1, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_v3f_("hello", objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_v3f_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_v3f_("hello", objc.simd.vector_float3(0.0, 1.5, 3.0), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_v3f_(NoObjCValueObject, objc.simd.vector_float3(0.0, 1.5, 3.0))

        with self.assertRaises(TypeError):
            self.id_id_v3f_("hello", None)

    def test_id_id_v4f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_v4f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_v4f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_v4f_, 1, b"<4f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_v4f_("hello", objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_v4f_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_v4f_(
                "hello", objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5), "hello"
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_v4f_(
                NoObjCValueObject, objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5)
            )

        with self.assertRaises(TypeError):
            self.id_id_v4f_("hello", None)

    def test_id_id_id_v2i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_id_v2i_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_id_v2i_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_id_v2i_, 1, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_id_v2i_, 2, b"<2i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_id_v2i_("hello", "hello", objc.simd.vector_int2(0, 1))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 3)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], "hello")
        self.assertEqual(stored[2], objc.simd.vector_int2(0, 1))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_id_v2i_("hello", "hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_id_v2i_("hello", "hello", objc.simd.vector_int2(0, 1), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_id_v2i_(NoObjCValueObject, "hello", objc.simd.vector_int2(0, 1))

        with self.assertRaises(TypeError):
            self.id_id_id_v2i_("hello", NoObjCValueObject, objc.simd.vector_int2(0, 1))

        with self.assertRaises(TypeError):
            self.id_id_id_v2i_("hello", "hello", None)

    def test_id_id_id_v2i_f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_id_v2i_f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_id_v2i_f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_id_v2i_f_, 1, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_id_v2i_f_, 2, b"<2i>")
        self.assertArgHasType(OC_VectorCall.id_id_id_v2i_f_, 3, b"f")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_id_v2i_f_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_id_v2i_f_("hello", "hello", objc.simd.vector_int2(0, 1))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_id_v2i_f_(
                "hello", "hello", objc.simd.vector_int2(0, 1), 2500000000.0, "hello"
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_id_v2i_f_(
                NoObjCValueObject, "hello", objc.simd.vector_int2(0, 1), 2500000000.0
            )

        with self.assertRaises(TypeError):
            self.id_id_id_v2i_f_(
                "hello", NoObjCValueObject, objc.simd.vector_int2(0, 1), 2500000000.0
            )

        with self.assertRaises(TypeError):
            self.id_id_id_v2i_f_("hello", "hello", None, 2500000000.0)

        with self.assertRaises(TypeError):
            self.id_id_id_v2i_f_("hello", "hello", objc.simd.vector_int2(0, 1), None)

    def test_id_id_Q_v2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_Q_v2f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_Q_v2f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_Q_v2f_, 1, b"Q")
        self.assertArgHasType(OC_VectorCall.id_id_Q_v2f_, 2, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_Q_v2f_("hello", 35184372088832, objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 3)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], 35184372088832)
        self.assertEqual(stored[2], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_Q_v2f_("hello", 35184372088832)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_Q_v2f_(
                "hello", 35184372088832, objc.simd.vector_float2(0.0, 1.5), "hello"
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_Q_v2f_(
                NoObjCValueObject, 35184372088832, objc.simd.vector_float2(0.0, 1.5)
            )

        with self.assertRaises(TypeError):
            self.id_id_Q_v2f_("hello", None, objc.simd.vector_float2(0.0, 1.5))

        with self.assertRaises(TypeError):
            self.id_id_Q_v2f_("hello", 35184372088832, None)

    def test_id_id_Q_v3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_Q_v3f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_Q_v3f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_Q_v3f_, 1, b"Q")
        self.assertArgHasType(OC_VectorCall.id_id_Q_v3f_, 2, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_Q_v3f_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_Q_v3f_("hello", 35184372088832)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_Q_v3f_(
                "hello", 35184372088832, objc.simd.vector_float3(0.0, 1.5, 3.0), "hello"
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_Q_v3f_(
                NoObjCValueObject,
                35184372088832,
                objc.simd.vector_float3(0.0, 1.5, 3.0),
            )

        with self.assertRaises(TypeError):
            self.id_id_Q_v3f_("hello", None, objc.simd.vector_float3(0.0, 1.5, 3.0))

        with self.assertRaises(TypeError):
            self.id_id_Q_v3f_("hello", 35184372088832, None)

    def test_id_id_Q_v4f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_Q_v4f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_Q_v4f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_Q_v4f_, 1, b"Q")
        self.assertArgHasType(OC_VectorCall.id_id_Q_v4f_, 2, b"<4f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_Q_v4f_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_Q_v4f_("hello", 35184372088832)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_Q_v4f_(
                "hello",
                35184372088832,
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_Q_v4f_(
                NoObjCValueObject,
                35184372088832,
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
            )

        with self.assertRaises(TypeError):
            self.id_id_Q_v4f_(
                "hello", None, objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5)
            )

        with self.assertRaises(TypeError):
            self.id_id_Q_v4f_("hello", 35184372088832, None)

    def test_id_id_Q_matrix_float4x4_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_Q_matrix_float4x4_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_Q_matrix_float4x4_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_Q_matrix_float4x4_, 1, b"Q")
        self.assertArgHasType(
            OC_VectorCall.id_id_Q_matrix_float4x4_, 2, b"{_matrix_float4x4=[4<4f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_Q_matrix_float4x4_(
            "hello",
            35184372088832,
            simd.matrix_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
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
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_Q_matrix_float4x4_("hello", 35184372088832)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_Q_matrix_float4x4_(
                "hello",
                35184372088832,
                simd.matrix_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_Q_matrix_float4x4_(
                NoObjCValueObject,
                35184372088832,
                simd.matrix_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
            )

        with self.assertRaises(TypeError):
            self.id_id_Q_matrix_float4x4_(
                "hello",
                None,
                simd.matrix_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
            )

        with self.assertRaises(TypeError):
            self.id_id_Q_matrix_float4x4_("hello", 35184372088832, None)

    def test_id_id_Z_id_v2i_q_Q_q_Z_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_Z_id_v2i_q_Q_q_Z_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_Z_id_v2i_q_Q_q_Z_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_Z_id_v2i_q_Q_q_Z_, 1, b"Z")
        self.assertArgHasType(OC_VectorCall.id_id_Z_id_v2i_q_Q_q_Z_, 2, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_Z_id_v2i_q_Q_q_Z_, 3, b"<2i>")
        self.assertArgHasType(OC_VectorCall.id_id_Z_id_v2i_q_Q_q_Z_, 4, b"q")
        self.assertArgHasType(OC_VectorCall.id_id_Z_id_v2i_q_Q_q_Z_, 5, b"Q")
        self.assertArgHasType(OC_VectorCall.id_id_Z_id_v2i_q_Q_q_Z_, 6, b"q")
        self.assertArgHasType(OC_VectorCall.id_id_Z_id_v2i_q_Q_q_Z_, 7, b"Z")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_Z_id_v2i_q_Q_q_Z_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_Z_id_v2i_q_Q_q_Z_(
                "hello",
                False,
                "hello",
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                35184372088832,
                -17592186044416,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_Z_id_v2i_q_Q_q_Z_(
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
        with self.assertRaises(TypeError):
            self.id_id_Z_id_v2i_q_Q_q_Z_(
                NoObjCValueObject,
                False,
                "hello",
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                35184372088832,
                -17592186044416,
                False,
            )

        with self.assertRaises(TypeError):
            self.id_id_Z_id_v2i_q_Q_q_Z_(
                "hello",
                None,
                "hello",
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                35184372088832,
                -17592186044416,
                False,
            )

        with self.assertRaises(TypeError):
            self.id_id_Z_id_v2i_q_Q_q_Z_(
                "hello",
                False,
                NoObjCValueObject,
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                35184372088832,
                -17592186044416,
                False,
            )

        with self.assertRaises(TypeError):
            self.id_id_Z_id_v2i_q_Q_q_Z_(
                "hello",
                False,
                "hello",
                None,
                -17592186044416,
                35184372088832,
                -17592186044416,
                False,
            )

        with self.assertRaises(TypeError):
            self.id_id_Z_id_v2i_q_Q_q_Z_(
                "hello",
                False,
                "hello",
                objc.simd.vector_int2(0, 1),
                None,
                35184372088832,
                -17592186044416,
                False,
            )

        with self.assertRaises(TypeError):
            self.id_id_Z_id_v2i_q_Q_q_Z_(
                "hello",
                False,
                "hello",
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                None,
                -17592186044416,
                False,
            )

        with self.assertRaises(TypeError):
            self.id_id_Z_id_v2i_q_Q_q_Z_(
                "hello",
                False,
                "hello",
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                35184372088832,
                None,
                False,
            )

        with self.assertRaises(TypeError):
            self.id_id_Z_id_v2i_q_Q_q_Z_(
                "hello",
                False,
                "hello",
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                35184372088832,
                -17592186044416,
                None,
            )

    def test_id_id_q_v2i_f_f_f_f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_, 1, b"q")
        self.assertArgHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_, 2, b"<2i>")
        self.assertArgHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_, 3, b"f")
        self.assertArgHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_, 4, b"f")
        self.assertArgHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_, 5, b"f")
        self.assertArgHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_, 6, b"f")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_q_v2i_f_f_f_f_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_q_v2i_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_q_v2i_f_f_f_f_(
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
        with self.assertRaises(TypeError):
            self.id_id_q_v2i_f_f_f_f_(
                NoObjCValueObject,
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises(TypeError):
            self.id_id_q_v2i_f_f_f_f_(
                "hello",
                None,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises(TypeError):
            self.id_id_q_v2i_f_f_f_f_(
                "hello",
                -17592186044416,
                None,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises(TypeError):
            self.id_id_q_v2i_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                None,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises(TypeError):
            self.id_id_q_v2i_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                None,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises(TypeError):
            self.id_id_q_v2i_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                None,
                2500000000.0,
            )

        with self.assertRaises(TypeError):
            self.id_id_q_v2i_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                None,
            )

    def test_id_id_q_v2i_f_f_f_f_f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_f_, 1, b"q")
        self.assertArgHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_f_, 2, b"<2i>")
        self.assertArgHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_f_, 3, b"f")
        self.assertArgHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_f_, 4, b"f")
        self.assertArgHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_f_, 5, b"f")
        self.assertArgHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_f_, 6, b"f")
        self.assertArgHasType(OC_VectorCall.id_id_q_v2i_f_f_f_f_f_, 7, b"f")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_q_v2i_f_f_f_f_f_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_q_v2i_f_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_q_v2i_f_f_f_f_f_(
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
        with self.assertRaises(TypeError):
            self.id_id_q_v2i_f_f_f_f_f_(
                NoObjCValueObject,
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises(TypeError):
            self.id_id_q_v2i_f_f_f_f_f_(
                "hello",
                None,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises(TypeError):
            self.id_id_q_v2i_f_f_f_f_f_(
                "hello",
                -17592186044416,
                None,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises(TypeError):
            self.id_id_q_v2i_f_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                None,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises(TypeError):
            self.id_id_q_v2i_f_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                None,
                2500000000.0,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises(TypeError):
            self.id_id_q_v2i_f_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                None,
                2500000000.0,
                2500000000.0,
            )

        with self.assertRaises(TypeError):
            self.id_id_q_v2i_f_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                None,
                2500000000.0,
            )

        with self.assertRaises(TypeError):
            self.id_id_q_v2i_f_f_f_f_f_(
                "hello",
                -17592186044416,
                objc.simd.vector_int2(0, 1),
                2500000000.0,
                2500000000.0,
                2500000000.0,
                2500000000.0,
                None,
            )

    def test_id_id_GKBox_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_GKBox_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_GKBox_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_GKBox_, 1, b"{GKBox=<3f><3f>}")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_GKBox_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_GKBox_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_GKBox_(
                "hello",
                (
                    objc.simd.vector_float3(1.0, 2.0, 3.0),
                    objc.simd.vector_float3(4.0, 5.0, 6.0),
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_GKBox_(
                NoObjCValueObject,
                (
                    objc.simd.vector_float3(1.0, 2.0, 3.0),
                    objc.simd.vector_float3(4.0, 5.0, 6.0),
                ),
            )

        with self.assertRaises(TypeError):
            self.id_id_GKBox_("hello", None)

    def test_id_id_GKQuad_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_GKQuad_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_GKQuad_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_GKQuad_, 1, b"{GKQuad=<2f><2f>}")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_GKQuad_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_GKQuad_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_GKQuad_(
                "hello",
                (
                    objc.simd.vector_float2(9.0, 10.0),
                    objc.simd.vector_float2(11.0, 12.0),
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_GKQuad_(
                NoObjCValueObject,
                (
                    objc.simd.vector_float2(9.0, 10.0),
                    objc.simd.vector_float2(11.0, 12.0),
                ),
            )

        with self.assertRaises(TypeError):
            self.id_id_GKQuad_("hello", None)

    def test_id_id_MDLAxisAlignedBoundingBox_f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_MDLAxisAlignedBoundingBox_f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_MDLAxisAlignedBoundingBox_f_, 0, b"@")
        self.assertArgHasType(
            OC_VectorCall.id_id_MDLAxisAlignedBoundingBox_f_,
            1,
            b"{_MDLAxisAlignedBoundingBox=<3f><3f>}",
        )
        self.assertArgHasType(OC_VectorCall.id_id_MDLAxisAlignedBoundingBox_f_, 2, b"f")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_MDLAxisAlignedBoundingBox_f_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_MDLAxisAlignedBoundingBox_f_(
                "hello",
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                ),
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_MDLAxisAlignedBoundingBox_f_(
                "hello",
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                ),
                2500000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_MDLAxisAlignedBoundingBox_f_(
                NoObjCValueObject,
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                ),
                2500000000.0,
            )

        with self.assertRaises(TypeError):
            self.id_id_MDLAxisAlignedBoundingBox_f_("hello", None, 2500000000.0)

        with self.assertRaises(TypeError):
            self.id_id_MDLAxisAlignedBoundingBox_f_(
                "hello",
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                ),
                None,
            )

    def test_id_id_matrix_float2x2_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_matrix_float2x2_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_matrix_float2x2_, 0, b"@")
        self.assertArgHasType(
            OC_VectorCall.id_id_matrix_float2x2_, 1, b"{_matrix_float2x2=[2<2f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_matrix_float2x2_(
            "hello",
            simd.matrix_float2x2(
                [objc.simd.vector_float2(0.0, 1.5), objc.simd.vector_float2(0.0, 1.5)]
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
                [objc.simd.vector_float2(0.0, 1.5), objc.simd.vector_float2(0.0, 1.5)]
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_matrix_float2x2_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_matrix_float2x2_(
                "hello",
                simd.matrix_float2x2(
                    [
                        objc.simd.vector_float2(0.0, 1.5),
                        objc.simd.vector_float2(0.0, 1.5),
                    ]
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_matrix_float2x2_(
                NoObjCValueObject,
                simd.matrix_float2x2(
                    [
                        objc.simd.vector_float2(0.0, 1.5),
                        objc.simd.vector_float2(0.0, 1.5),
                    ]
                ),
            )

        with self.assertRaises(TypeError):
            self.id_id_matrix_float2x2_("hello", None)

    def test_id_id_matrix_float3x3_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_matrix_float3x3_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_matrix_float3x3_, 0, b"@")
        self.assertArgHasType(
            OC_VectorCall.id_id_matrix_float3x3_, 1, b"{_matrix_float3x3=[3<3f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_matrix_float3x3_(
            "hello",
            simd.matrix_float3x3(
                [
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                ]
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
                [
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                ]
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_matrix_float3x3_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_matrix_float3x3_(
                "hello",
                simd.matrix_float3x3(
                    [
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                    ]
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_matrix_float3x3_(
                NoObjCValueObject,
                simd.matrix_float3x3(
                    [
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                    ]
                ),
            )

        with self.assertRaises(TypeError):
            self.id_id_matrix_float3x3_("hello", None)

    def test_id_id_matrix_float4x4_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_id_matrix_float4x4_, b"@")
        self.assertArgHasType(OC_VectorCall.id_id_matrix_float4x4_, 0, b"@")
        self.assertArgHasType(
            OC_VectorCall.id_id_matrix_float4x4_, 1, b"{_matrix_float4x4=[4<4f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_id_matrix_float4x4_(
            "hello",
            simd.matrix_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
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
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_matrix_float4x4_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_id_matrix_float4x4_(
                "hello",
                simd.matrix_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_id_matrix_float4x4_(
                NoObjCValueObject,
                simd.matrix_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
            )

        with self.assertRaises(TypeError):
            self.id_id_matrix_float4x4_("hello", None)

    def test_id_CGColor_CGColor_id_v2i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_CGColor_CGColor_id_v2i_, b"@")
        self.assertArgHasType(
            OC_VectorCall.id_CGColor_CGColor_id_v2i_, 0, b"^{CGColor=}"
        )
        self.assertArgHasType(
            OC_VectorCall.id_CGColor_CGColor_id_v2i_, 1, b"^{CGColor=}"
        )
        self.assertArgHasType(OC_VectorCall.id_CGColor_CGColor_id_v2i_, 2, b"@")
        self.assertArgHasType(OC_VectorCall.id_CGColor_CGColor_id_v2i_, 3, b"<2i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_CGColor_CGColor_id_v2i_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_CGColor_CGColor_id_v2i_("color!", "color!", "hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_CGColor_CGColor_id_v2i_(
                "color!", "color!", "hello", objc.simd.vector_int2(0, 1), "hello"
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_CGColor_CGColor_id_v2i_(
                NoObjCValueObject, "color!", "hello", objc.simd.vector_int2(0, 1)
            )

        with self.assertRaises(TypeError):
            self.id_CGColor_CGColor_id_v2i_(
                "color!", NoObjCValueObject, "hello", objc.simd.vector_int2(0, 1)
            )

        with self.assertRaises(TypeError):
            self.id_CGColor_CGColor_id_v2i_(
                "color!", "color!", NoObjCValueObject, objc.simd.vector_int2(0, 1)
            )

        with self.assertRaises(TypeError):
            self.id_CGColor_CGColor_id_v2i_("color!", "color!", "hello", None)

    def test_id_f_v2f_v2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_f_v2f_v2f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_v2f_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_v2f_, 1, b"<2f>")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_v2f_, 2, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_f_v2f_v2f_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_v2f_v2f_(2500000000.0, objc.simd.vector_float2(0.0, 1.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_v2f_v2f_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_f_v2f_v2f_(
                None,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_v2f_(2500000000.0, None, objc.simd.vector_float2(0.0, 1.5))

        with self.assertRaises(TypeError):
            self.id_f_v2f_v2f_(2500000000.0, objc.simd.vector_float2(0.0, 1.5), None)

    def test_id_f_v2f_v2f_Class_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_f_v2f_v2f_Class_, b"@")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_v2f_Class_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_v2f_Class_, 1, b"<2f>")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_v2f_Class_, 2, b"<2f>")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_v2f_Class_, 3, b"#")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_f_v2f_v2f_Class_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_v2f_v2f_Class_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_v2f_v2f_Class_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                objc.lookUpClass("NSObject"),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_f_v2f_v2f_Class_(
                None,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                objc.lookUpClass("NSObject"),
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_v2f_Class_(
                2500000000.0,
                None,
                objc.simd.vector_float2(0.0, 1.5),
                objc.lookUpClass("NSObject"),
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_v2f_Class_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                None,
                objc.lookUpClass("NSObject"),
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_v2f_Class_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                42,
            )

    def test_id_f_v2f_Q_Q_Q_q_Z_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_f_v2f_Q_Q_Q_q_Z_id_, b"@")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_Q_Q_Q_q_Z_id_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_Q_Q_Q_q_Z_id_, 1, b"<2f>")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_Q_Q_Q_q_Z_id_, 2, b"Q")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_Q_Q_Q_q_Z_id_, 3, b"Q")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_Q_Q_Q_q_Z_id_, 4, b"Q")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_Q_Q_Q_q_Z_id_, 5, b"q")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_Q_Q_Q_q_Z_id_, 6, b"Z")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_Q_Q_Q_q_Z_id_, 7, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_f_v2f_Q_Q_Q_q_Z_id_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_v2f_Q_Q_Q_q_Z_id_(
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
        with self.assertRaises(TypeError):
            self.id_f_v2f_Q_Q_Q_q_Z_id_(
                None,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                None,
                35184372088832,
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                None,
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                None,
                35184372088832,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                None,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                35184372088832,
                None,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                35184372088832,
                -17592186044416,
                None,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_Q_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                NoObjCValueObject,
            )

    def test_id_f_v2f_Q_Q_q_Z_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_f_v2f_Q_Q_q_Z_id_, b"@")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_Q_Q_q_Z_id_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_Q_Q_q_Z_id_, 1, b"<2f>")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_Q_Q_q_Z_id_, 2, b"Q")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_Q_Q_q_Z_id_, 3, b"Q")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_Q_Q_q_Z_id_, 4, b"q")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_Q_Q_q_Z_id_, 5, b"Z")
        self.assertArgHasType(OC_VectorCall.id_f_v2f_Q_Q_q_Z_id_, 6, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_f_v2f_Q_Q_q_Z_id_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_v2f_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_v2f_Q_Q_q_Z_id_(
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
        with self.assertRaises(TypeError):
            self.id_f_v2f_Q_Q_q_Z_id_(
                None,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_Q_Q_q_Z_id_(
                2500000000.0,
                None,
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                None,
                35184372088832,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                None,
                -17592186044416,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                None,
                False,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                -17592186044416,
                None,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.id_f_v2f_Q_Q_q_Z_id_(
                2500000000.0,
                objc.simd.vector_float2(0.0, 1.5),
                35184372088832,
                35184372088832,
                -17592186044416,
                False,
                NoObjCValueObject,
            )

    def test_id_f_id_v2i_i_q_Z_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_f_id_v2i_i_q_Z_, b"@")
        self.assertArgHasType(OC_VectorCall.id_f_id_v2i_i_q_Z_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.id_f_id_v2i_i_q_Z_, 1, b"@")
        self.assertArgHasType(OC_VectorCall.id_f_id_v2i_i_q_Z_, 2, b"<2i>")
        self.assertArgHasType(OC_VectorCall.id_f_id_v2i_i_q_Z_, 3, b"i")
        self.assertArgHasType(OC_VectorCall.id_f_id_v2i_i_q_Z_, 4, b"q")
        self.assertArgHasType(OC_VectorCall.id_f_id_v2i_i_q_Z_, 5, b"Z")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_f_id_v2i_i_q_Z_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_id_v2i_i_q_Z_(
                2500000000.0, "hello", objc.simd.vector_int2(0, 1), -42, -17592186044416
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_id_v2i_i_q_Z_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                False,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_f_id_v2i_i_q_Z_(
                None, "hello", objc.simd.vector_int2(0, 1), -42, -17592186044416, False
            )

        with self.assertRaises(TypeError):
            self.id_f_id_v2i_i_q_Z_(
                2500000000.0,
                NoObjCValueObject,
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                False,
            )

        with self.assertRaises(TypeError):
            self.id_f_id_v2i_i_q_Z_(
                2500000000.0, "hello", None, -42, -17592186044416, False
            )

        with self.assertRaises(TypeError):
            self.id_f_id_v2i_i_q_Z_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                None,
                -17592186044416,
                False,
            )

        with self.assertRaises(TypeError):
            self.id_f_id_v2i_i_q_Z_(
                2500000000.0, "hello", objc.simd.vector_int2(0, 1), -42, None, False
            )

        with self.assertRaises(TypeError):
            self.id_f_id_v2i_i_q_Z_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                None,
            )

    def test_id_f_id_v2i_i_q_CGColor_CGColor_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_f_id_v2i_i_q_CGColor_CGColor_, b"@")
        self.assertArgHasType(OC_VectorCall.id_f_id_v2i_i_q_CGColor_CGColor_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.id_f_id_v2i_i_q_CGColor_CGColor_, 1, b"@")
        self.assertArgHasType(
            OC_VectorCall.id_f_id_v2i_i_q_CGColor_CGColor_, 2, b"<2i>"
        )
        self.assertArgHasType(OC_VectorCall.id_f_id_v2i_i_q_CGColor_CGColor_, 3, b"i")
        self.assertArgHasType(OC_VectorCall.id_f_id_v2i_i_q_CGColor_CGColor_, 4, b"q")
        self.assertArgHasType(
            OC_VectorCall.id_f_id_v2i_i_q_CGColor_CGColor_, 5, b"^{CGColor=}"
        )
        self.assertArgHasType(
            OC_VectorCall.id_f_id_v2i_i_q_CGColor_CGColor_, 6, b"^{CGColor=}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_f_id_v2i_i_q_CGColor_CGColor_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_id_v2i_i_q_CGColor_CGColor_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                "color!",
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_id_v2i_i_q_CGColor_CGColor_(
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
        with self.assertRaises(TypeError):
            self.id_f_id_v2i_i_q_CGColor_CGColor_(
                None,
                "hello",
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                "color!",
                "color!",
            )

        with self.assertRaises(TypeError):
            self.id_f_id_v2i_i_q_CGColor_CGColor_(
                2500000000.0,
                NoObjCValueObject,
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                "color!",
                "color!",
            )

        with self.assertRaises(TypeError):
            self.id_f_id_v2i_i_q_CGColor_CGColor_(
                2500000000.0, "hello", None, -42, -17592186044416, "color!", "color!"
            )

        with self.assertRaises(TypeError):
            self.id_f_id_v2i_i_q_CGColor_CGColor_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                None,
                -17592186044416,
                "color!",
                "color!",
            )

        with self.assertRaises(TypeError):
            self.id_f_id_v2i_i_q_CGColor_CGColor_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                -42,
                None,
                "color!",
                "color!",
            )

        with self.assertRaises(TypeError):
            self.id_f_id_v2i_i_q_CGColor_CGColor_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                NoObjCValueObject,
                "color!",
            )

        with self.assertRaises(TypeError):
            self.id_f_id_v2i_i_q_CGColor_CGColor_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                -42,
                -17592186044416,
                "color!",
                NoObjCValueObject,
            )

    def test_id_f_id_v2i_q_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_f_id_v2i_q_, b"@")
        self.assertArgHasType(OC_VectorCall.id_f_id_v2i_q_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.id_f_id_v2i_q_, 1, b"@")
        self.assertArgHasType(OC_VectorCall.id_f_id_v2i_q_, 2, b"<2i>")
        self.assertArgHasType(OC_VectorCall.id_f_id_v2i_q_, 3, b"q")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_f_id_v2i_q_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_id_v2i_q_(2500000000.0, "hello", objc.simd.vector_int2(0, 1))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_id_v2i_q_(
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_f_id_v2i_q_(
                None, "hello", objc.simd.vector_int2(0, 1), -17592186044416
            )

        with self.assertRaises(TypeError):
            self.id_f_id_v2i_q_(
                2500000000.0,
                NoObjCValueObject,
                objc.simd.vector_int2(0, 1),
                -17592186044416,
            )

        with self.assertRaises(TypeError):
            self.id_f_id_v2i_q_(2500000000.0, "hello", None, -17592186044416)

        with self.assertRaises(TypeError):
            self.id_f_id_v2i_q_(
                2500000000.0, "hello", objc.simd.vector_int2(0, 1), None
            )

    def test_id_f_f_id_v2i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_f_f_id_v2i_, b"@")
        self.assertArgHasType(OC_VectorCall.id_f_f_id_v2i_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.id_f_f_id_v2i_, 1, b"f")
        self.assertArgHasType(OC_VectorCall.id_f_f_id_v2i_, 2, b"@")
        self.assertArgHasType(OC_VectorCall.id_f_f_id_v2i_, 3, b"<2i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_f_f_id_v2i_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_f_id_v2i_(2500000000.0, 2500000000.0, "hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_f_f_id_v2i_(
                2500000000.0,
                2500000000.0,
                "hello",
                objc.simd.vector_int2(0, 1),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_f_f_id_v2i_(
                None, 2500000000.0, "hello", objc.simd.vector_int2(0, 1)
            )

        with self.assertRaises(TypeError):
            self.id_f_f_id_v2i_(
                2500000000.0, None, "hello", objc.simd.vector_int2(0, 1)
            )

        with self.assertRaises(TypeError):
            self.id_f_f_id_v2i_(
                2500000000.0,
                2500000000.0,
                NoObjCValueObject,
                objc.simd.vector_int2(0, 1),
            )

        with self.assertRaises(TypeError):
            self.id_f_f_id_v2i_(2500000000.0, 2500000000.0, "hello", None)

    def test_id_GKBox_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_GKBox_, b"@")
        self.assertArgHasType(OC_VectorCall.id_GKBox_, 0, b"{GKBox=<3f><3f>}")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_GKBox_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_GKBox_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_GKBox_(
                (
                    objc.simd.vector_float3(1.0, 2.0, 3.0),
                    objc.simd.vector_float3(4.0, 5.0, 6.0),
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_GKBox_(None)

    def test_id_GKBox_f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_GKBox_f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_GKBox_f_, 0, b"{GKBox=<3f><3f>}")
        self.assertArgHasType(OC_VectorCall.id_GKBox_f_, 1, b"f")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_GKBox_f_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_GKBox_f_(
                (
                    objc.simd.vector_float3(1.0, 2.0, 3.0),
                    objc.simd.vector_float3(4.0, 5.0, 6.0),
                )
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_GKBox_f_(
                (
                    objc.simd.vector_float3(1.0, 2.0, 3.0),
                    objc.simd.vector_float3(4.0, 5.0, 6.0),
                ),
                2500000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_GKBox_f_(None, 2500000000.0)

        with self.assertRaises(TypeError):
            self.id_GKBox_f_(
                (
                    objc.simd.vector_float3(1.0, 2.0, 3.0),
                    objc.simd.vector_float3(4.0, 5.0, 6.0),
                ),
                None,
            )

    def test_id_GKQuad_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_GKQuad_, b"@")
        self.assertArgHasType(OC_VectorCall.id_GKQuad_, 0, b"{GKQuad=<2f><2f>}")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_GKQuad_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_GKQuad_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_GKQuad_(
                (
                    objc.simd.vector_float2(9.0, 10.0),
                    objc.simd.vector_float2(11.0, 12.0),
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_GKQuad_(None)

    def test_id_GKQuad_f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_GKQuad_f_, b"@")
        self.assertArgHasType(OC_VectorCall.id_GKQuad_f_, 0, b"{GKQuad=<2f><2f>}")
        self.assertArgHasType(OC_VectorCall.id_GKQuad_f_, 1, b"f")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_GKQuad_f_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_GKQuad_f_(
                (
                    objc.simd.vector_float2(9.0, 10.0),
                    objc.simd.vector_float2(11.0, 12.0),
                )
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_GKQuad_f_(
                (
                    objc.simd.vector_float2(9.0, 10.0),
                    objc.simd.vector_float2(11.0, 12.0),
                ),
                2500000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_GKQuad_f_(None, 2500000000.0)

        with self.assertRaises(TypeError):
            self.id_GKQuad_f_(
                (
                    objc.simd.vector_float2(9.0, 10.0),
                    objc.simd.vector_float2(11.0, 12.0),
                ),
                None,
            )

    def test_id_MDLVoxelIndexExtent_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_MDLVoxelIndexExtent_, b"@")
        self.assertArgHasType(
            OC_VectorCall.id_MDLVoxelIndexExtent_, 0, b"{_MDLVoxelIndexExtent=<4i><4i>}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_MDLVoxelIndexExtent_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_MDLVoxelIndexExtent_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_MDLVoxelIndexExtent_(
                (
                    objc.simd.vector_int4(100, 101, 102, 103),
                    objc.simd.vector_int4(-20, -21, -22, -23),
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_MDLVoxelIndexExtent_(None)

    def test_id_matrix_float4x4_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_matrix_float4x4_, b"@")
        self.assertArgHasType(
            OC_VectorCall.id_matrix_float4x4_, 0, b"{_matrix_float4x4=[4<4f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_matrix_float4x4_(
            simd.matrix_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            )
        )
        self.assertEqual(rv, "hello")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            simd.matrix_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_matrix_float4x4_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_matrix_float4x4_(
                simd.matrix_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_matrix_float4x4_(None)

    def test_id_matrix_float4x4_Z_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.id_matrix_float4x4_Z_, b"@")
        self.assertArgHasType(
            OC_VectorCall.id_matrix_float4x4_Z_, 0, b"{_matrix_float4x4=[4<4f>]}"
        )
        self.assertArgHasType(OC_VectorCall.id_matrix_float4x4_Z_, 1, b"Z")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.id_matrix_float4x4_Z_(
            simd.matrix_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
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
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )
        self.assertEqual(stored[1], False)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_matrix_float4x4_Z_(
                simd.matrix_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                )
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.id_matrix_float4x4_Z_(
                simd.matrix_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
                False,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.id_matrix_float4x4_Z_(None, False)

        with self.assertRaises(TypeError):
            self.id_matrix_float4x4_Z_(
                simd.matrix_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
                None,
            )

    def test_Z_v2i_id_id_id_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.Z_v2i_id_id_id_id_, b"Z")
        self.assertArgHasType(OC_VectorCall.Z_v2i_id_id_id_id_, 0, b"<2i>")
        self.assertArgHasType(OC_VectorCall.Z_v2i_id_id_id_id_, 1, b"@")
        self.assertArgHasType(OC_VectorCall.Z_v2i_id_id_id_id_, 2, b"@")
        self.assertArgHasType(OC_VectorCall.Z_v2i_id_id_id_id_, 3, b"@")
        self.assertArgHasType(OC_VectorCall.Z_v2i_id_id_id_id_, 4, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.Z_v2i_id_id_id_id_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.Z_v2i_id_id_id_id_(
                objc.simd.vector_int2(0, 1), "hello", "hello", "hello"
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.Z_v2i_id_id_id_id_(
                objc.simd.vector_int2(0, 1), "hello", "hello", "hello", "hello", "hello"
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.Z_v2i_id_id_id_id_(None, "hello", "hello", "hello", "hello")

        with self.assertRaises(TypeError):
            self.Z_v2i_id_id_id_id_(
                objc.simd.vector_int2(0, 1),
                NoObjCValueObject,
                "hello",
                "hello",
                "hello",
            )

        with self.assertRaises(TypeError):
            self.Z_v2i_id_id_id_id_(
                objc.simd.vector_int2(0, 1),
                "hello",
                NoObjCValueObject,
                "hello",
                "hello",
            )

        with self.assertRaises(TypeError):
            self.Z_v2i_id_id_id_id_(
                objc.simd.vector_int2(0, 1),
                "hello",
                "hello",
                NoObjCValueObject,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.Z_v2i_id_id_id_id_(
                objc.simd.vector_int2(0, 1),
                "hello",
                "hello",
                "hello",
                NoObjCValueObject,
            )

    def test_Z_v2i_q_f_id_id_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.Z_v2i_q_f_id_id_id_, b"Z")
        self.assertArgHasType(OC_VectorCall.Z_v2i_q_f_id_id_id_, 0, b"<2i>")
        self.assertArgHasType(OC_VectorCall.Z_v2i_q_f_id_id_id_, 1, b"q")
        self.assertArgHasType(OC_VectorCall.Z_v2i_q_f_id_id_id_, 2, b"f")
        self.assertArgHasType(OC_VectorCall.Z_v2i_q_f_id_id_id_, 3, b"@")
        self.assertArgHasType(OC_VectorCall.Z_v2i_q_f_id_id_id_, 4, b"@")
        self.assertArgHasType(OC_VectorCall.Z_v2i_q_f_id_id_id_, 5, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.Z_v2i_q_f_id_id_id_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.Z_v2i_q_f_id_id_id_(
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                2500000000.0,
                "hello",
                "hello",
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.Z_v2i_q_f_id_id_id_(
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                2500000000.0,
                "hello",
                "hello",
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.Z_v2i_q_f_id_id_id_(
                None, -17592186044416, 2500000000.0, "hello", "hello", "hello"
            )

        with self.assertRaises(TypeError):
            self.Z_v2i_q_f_id_id_id_(
                objc.simd.vector_int2(0, 1),
                None,
                2500000000.0,
                "hello",
                "hello",
                "hello",
            )

        with self.assertRaises(TypeError):
            self.Z_v2i_q_f_id_id_id_(
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                None,
                "hello",
                "hello",
                "hello",
            )

        with self.assertRaises(TypeError):
            self.Z_v2i_q_f_id_id_id_(
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                2500000000.0,
                NoObjCValueObject,
                "hello",
                "hello",
            )

        with self.assertRaises(TypeError):
            self.Z_v2i_q_f_id_id_id_(
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                2500000000.0,
                "hello",
                NoObjCValueObject,
                "hello",
            )

        with self.assertRaises(TypeError):
            self.Z_v2i_q_f_id_id_id_(
                objc.simd.vector_int2(0, 1),
                -17592186044416,
                2500000000.0,
                "hello",
                "hello",
                NoObjCValueObject,
            )

    def test_Z_v4i_Z_Z_Z_Z_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.Z_v4i_Z_Z_Z_Z_, b"Z")
        self.assertArgHasType(OC_VectorCall.Z_v4i_Z_Z_Z_Z_, 0, b"<4i>")
        self.assertArgHasType(OC_VectorCall.Z_v4i_Z_Z_Z_Z_, 1, b"Z")
        self.assertArgHasType(OC_VectorCall.Z_v4i_Z_Z_Z_Z_, 2, b"Z")
        self.assertArgHasType(OC_VectorCall.Z_v4i_Z_Z_Z_Z_, 3, b"Z")
        self.assertArgHasType(OC_VectorCall.Z_v4i_Z_Z_Z_Z_, 4, b"Z")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.Z_v4i_Z_Z_Z_Z_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.Z_v4i_Z_Z_Z_Z_(objc.simd.vector_int4(0, 1, 2, 3), False, False, False)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.Z_v4i_Z_Z_Z_Z_(
                objc.simd.vector_int4(0, 1, 2, 3), False, False, False, False, "hello"
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.Z_v4i_Z_Z_Z_Z_(None, False, False, False, False)

        with self.assertRaises(TypeError):
            self.Z_v4i_Z_Z_Z_Z_(
                objc.simd.vector_int4(0, 1, 2, 3), None, False, False, False
            )

        with self.assertRaises(TypeError):
            self.Z_v4i_Z_Z_Z_Z_(
                objc.simd.vector_int4(0, 1, 2, 3), False, None, False, False
            )

        with self.assertRaises(TypeError):
            self.Z_v4i_Z_Z_Z_Z_(
                objc.simd.vector_int4(0, 1, 2, 3), False, False, None, False
            )

        with self.assertRaises(TypeError):
            self.Z_v4i_Z_Z_Z_Z_(
                objc.simd.vector_int4(0, 1, 2, 3), False, False, False, None
            )

    def test_CGColor_v3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.CGColor_v3f_, b"^{CGColor=}")
        self.assertArgHasType(OC_VectorCall.CGColor_v3f_, 0, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.CGColor_v3f_(objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(rv, "color!")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.CGColor_v3f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.CGColor_v3f_(objc.simd.vector_float3(0.0, 1.5, 3.0), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.CGColor_v3f_(None)

    def test_CGColor_v3f_CGColorSpace_(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.CGColor_v3f_CGColorSpace_, b"^{CGColor=}"
        )
        self.assertArgHasType(OC_VectorCall.CGColor_v3f_CGColorSpace_, 0, b"<3f>")
        self.assertArgHasType(
            OC_VectorCall.CGColor_v3f_CGColorSpace_, 1, b"^{CGColorSpace=}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.CGColor_v3f_CGColorSpace_(
            objc.simd.vector_float3(0.0, 1.5, 3.0), "colorspace!"
        )
        self.assertEqual(rv, "color!")

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], "colorspace!")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.CGColor_v3f_CGColorSpace_(objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.CGColor_v3f_CGColorSpace_(
                objc.simd.vector_float3(0.0, 1.5, 3.0), "colorspace!", "hello"
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.CGColor_v3f_CGColorSpace_(None, "colorspace!")

        with self.assertRaises(TypeError):
            self.CGColor_v3f_CGColorSpace_(
                objc.simd.vector_float3(0.0, 1.5, 3.0), NoObjCValueObject
            )

    def test_f_v2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.f_v2f_, b"f")
        self.assertArgHasType(OC_VectorCall.f_v2f_, 0, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.f_v2f_(objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(rv, 2500000000.0)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.f_v2f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.f_v2f_(objc.simd.vector_float2(0.0, 1.5), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.f_v2f_(None)

    def test_f_v2i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.f_v2i_, b"f")
        self.assertArgHasType(OC_VectorCall.f_v2i_, 0, b"<2i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.f_v2i_(objc.simd.vector_int2(0, 1))
        self.assertEqual(rv, 2500000000.0)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_int2(0, 1))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.f_v2i_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.f_v2i_(objc.simd.vector_int2(0, 1), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.f_v2i_(None)

    def test_v_v2d_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_v2d_d_, b"v")
        self.assertArgHasType(OC_VectorCall.v_v2d_d_, 0, b"<2d>")
        self.assertArgHasType(OC_VectorCall.v_v2d_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_v2d_d_(objc.simd.vector_double2(0.0, 1.5), -557000000000.0)
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_double2(0.0, 1.5))
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v2d_d_(objc.simd.vector_double2(0.0, 1.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v2d_d_(objc.simd.vector_double2(0.0, 1.5), -557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_v2d_d_(None, -557000000000.0)

        with self.assertRaises(TypeError):
            self.v_v2d_d_(objc.simd.vector_double2(0.0, 1.5), None)

    def test_v_v2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_v2f_, b"v")
        self.assertArgHasType(OC_VectorCall.v_v2f_, 0, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_v2f_(objc.simd.vector_float2(0.0, 1.5))
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v2f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v2f_(objc.simd.vector_float2(0.0, 1.5), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_v2f_(None)

    def test_v_v2f_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_v2f_d_, b"v")
        self.assertArgHasType(OC_VectorCall.v_v2f_d_, 0, b"<2f>")
        self.assertArgHasType(OC_VectorCall.v_v2f_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_v2f_d_(objc.simd.vector_float2(0.0, 1.5), -557000000000.0)
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v2f_d_(objc.simd.vector_float2(0.0, 1.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v2f_d_(objc.simd.vector_float2(0.0, 1.5), -557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_v2f_d_(None, -557000000000.0)

        with self.assertRaises(TypeError):
            self.v_v2f_d_(objc.simd.vector_float2(0.0, 1.5), None)

    def test_v_v3d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_v3d_, b"v")
        self.assertArgHasType(OC_VectorCall.v_v3d_, 0, b"<3d>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_v3d_(objc.simd.vector_double3(0.0, 1.5, 3.0))
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_double3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v3d_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v3d_(objc.simd.vector_double3(0.0, 1.5, 3.0), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_v3d_(None)

    def test_v_v3d_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_v3d_d_, b"v")
        self.assertArgHasType(OC_VectorCall.v_v3d_d_, 0, b"<3d>")
        self.assertArgHasType(OC_VectorCall.v_v3d_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_v3d_d_(objc.simd.vector_double3(0.0, 1.5, 3.0), -557000000000.0)
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_double3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v3d_d_(objc.simd.vector_double3(0.0, 1.5, 3.0))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v3d_d_(
                objc.simd.vector_double3(0.0, 1.5, 3.0), -557000000000.0, "hello"
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_v3d_d_(None, -557000000000.0)

        with self.assertRaises(TypeError):
            self.v_v3d_d_(objc.simd.vector_double3(0.0, 1.5, 3.0), None)

    def test_v_v3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_v3f_, b"v")
        self.assertArgHasType(OC_VectorCall.v_v3f_, 0, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_v3f_(objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v3f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v3f_(objc.simd.vector_float3(0.0, 1.5, 3.0), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_v3f_(None)

    def test_v_v3f_v3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_v3f_v3f_, b"v")
        self.assertArgHasType(OC_VectorCall.v_v3f_v3f_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v_v3f_v3f_, 1, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_v3f_v3f_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v3f_v3f_(objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v3f_v3f_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_v3f_v3f_(None, objc.simd.vector_float3(0.0, 1.5, 3.0))

        with self.assertRaises(TypeError):
            self.v_v3f_v3f_(objc.simd.vector_float3(0.0, 1.5, 3.0), None)

    def test_v_v3f_v3f_v3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_v3f_v3f_v3f_, b"v")
        self.assertArgHasType(OC_VectorCall.v_v3f_v3f_v3f_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v_v3f_v3f_v3f_, 1, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v_v3f_v3f_v3f_, 2, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_v3f_v3f_v3f_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v3f_v3f_v3f_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_float3(0.0, 1.5, 3.0),
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v3f_v3f_v3f_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_v3f_v3f_v3f_(
                None,
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_float3(0.0, 1.5, 3.0),
            )

        with self.assertRaises(TypeError):
            self.v_v3f_v3f_v3f_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
                objc.simd.vector_float3(0.0, 1.5, 3.0),
            )

        with self.assertRaises(TypeError):
            self.v_v3f_v3f_v3f_(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                None,
            )

    def test_v_v3f_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_v3f_d_, b"v")
        self.assertArgHasType(OC_VectorCall.v_v3f_d_, 0, b"<3f>")
        self.assertArgHasType(OC_VectorCall.v_v3f_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_v3f_d_(objc.simd.vector_float3(0.0, 1.5, 3.0), -557000000000.0)
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v3f_d_(objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v3f_d_(
                objc.simd.vector_float3(0.0, 1.5, 3.0), -557000000000.0, "hello"
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_v3f_d_(None, -557000000000.0)

        with self.assertRaises(TypeError):
            self.v_v3f_d_(objc.simd.vector_float3(0.0, 1.5, 3.0), None)

    def test_v_v4d_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_v4d_d_, b"v")
        self.assertArgHasType(OC_VectorCall.v_v4d_d_, 0, b"<4d>")
        self.assertArgHasType(OC_VectorCall.v_v4d_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_v4d_d_(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5), -557000000000.0)
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5))
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v4d_d_(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v4d_d_(
                objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5), -557000000000.0, "hello"
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_v4d_d_(None, -557000000000.0)

        with self.assertRaises(TypeError):
            self.v_v4d_d_(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5), None)

    def test_v_v4f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_v4f_, b"v")
        self.assertArgHasType(OC_VectorCall.v_v4f_, 0, b"<4f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_v4f_(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v4f_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v4f_(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_v4f_(None)

    def test_v_v4f_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_v4f_d_, b"v")
        self.assertArgHasType(OC_VectorCall.v_v4f_d_, 0, b"<4f>")
        self.assertArgHasType(OC_VectorCall.v_v4f_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_v4f_d_(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5), -557000000000.0)
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v4f_d_(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v4f_d_(
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5), -557000000000.0, "hello"
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_v4f_d_(None, -557000000000.0)

        with self.assertRaises(TypeError):
            self.v_v4f_d_(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5), None)

    def test_v_v4i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_v4i_, b"v")
        self.assertArgHasType(OC_VectorCall.v_v4i_, 0, b"<4i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_v4i_(objc.simd.vector_int4(0, 1, 2, 3))
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_int4(0, 1, 2, 3))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v4i_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_v4i_(objc.simd.vector_int4(0, 1, 2, 3), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_v4i_(None)

    def test_v_id_v2f_v2f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_id_v2f_v2f_, b"v")
        self.assertArgHasType(OC_VectorCall.v_id_v2f_v2f_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.v_id_v2f_v2f_, 1, b"<2f>")
        self.assertArgHasType(OC_VectorCall.v_id_v2f_v2f_, 2, b"<2f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_id_v2f_v2f_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_id_v2f_v2f_("hello", objc.simd.vector_float2(0.0, 1.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_id_v2f_v2f_(
                "hello",
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_id_v2f_v2f_(
                NoObjCValueObject,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
            )

        with self.assertRaises(TypeError):
            self.v_id_v2f_v2f_("hello", None, objc.simd.vector_float2(0.0, 1.5))

        with self.assertRaises(TypeError):
            self.v_id_v2f_v2f_("hello", objc.simd.vector_float2(0.0, 1.5), None)

    def test_v_id_v2f_v2f_q_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_id_v2f_v2f_q_, b"v")
        self.assertArgHasType(OC_VectorCall.v_id_v2f_v2f_q_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.v_id_v2f_v2f_q_, 1, b"<2f>")
        self.assertArgHasType(OC_VectorCall.v_id_v2f_v2f_q_, 2, b"<2f>")
        self.assertArgHasType(OC_VectorCall.v_id_v2f_v2f_q_, 3, b"q")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_id_v2f_v2f_q_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_id_v2f_v2f_q_(
                "hello",
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_id_v2f_v2f_q_(
                "hello",
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                -17592186044416,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_id_v2f_v2f_q_(
                NoObjCValueObject,
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                -17592186044416,
            )

        with self.assertRaises(TypeError):
            self.v_id_v2f_v2f_q_(
                "hello", None, objc.simd.vector_float2(0.0, 1.5), -17592186044416
            )

        with self.assertRaises(TypeError):
            self.v_id_v2f_v2f_q_(
                "hello", objc.simd.vector_float2(0.0, 1.5), None, -17592186044416
            )

        with self.assertRaises(TypeError):
            self.v_id_v2f_v2f_q_(
                "hello",
                objc.simd.vector_float2(0.0, 1.5),
                objc.simd.vector_float2(0.0, 1.5),
                None,
            )

    def test_v_f_v2i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_f_v2i_, b"v")
        self.assertArgHasType(OC_VectorCall.v_f_v2i_, 0, b"f")
        self.assertArgHasType(OC_VectorCall.v_f_v2i_, 1, b"<2i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_f_v2i_(2500000000.0, objc.simd.vector_int2(0, 1))
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], 2500000000.0)
        self.assertEqual(stored[1], objc.simd.vector_int2(0, 1))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_f_v2i_(2500000000.0)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_f_v2i_(2500000000.0, objc.simd.vector_int2(0, 1), "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_f_v2i_(None, objc.simd.vector_int2(0, 1))

        with self.assertRaises(TypeError):
            self.v_f_v2i_(2500000000.0, None)

    def test_v_MDLAxisAlignedBoundingBox_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_MDLAxisAlignedBoundingBox_, b"v")
        self.assertArgHasType(
            OC_VectorCall.v_MDLAxisAlignedBoundingBox_,
            0,
            b"{_MDLAxisAlignedBoundingBox=<3f><3f>}",
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_MDLAxisAlignedBoundingBox_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_MDLAxisAlignedBoundingBox_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_MDLAxisAlignedBoundingBox_(
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_MDLAxisAlignedBoundingBox_(None)

    def test_v_MDLAxisAlignedBoundingBox_Z_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_MDLAxisAlignedBoundingBox_Z_, b"v")
        self.assertArgHasType(
            OC_VectorCall.v_MDLAxisAlignedBoundingBox_Z_,
            0,
            b"{_MDLAxisAlignedBoundingBox=<3f><3f>}",
        )
        self.assertArgHasType(OC_VectorCall.v_MDLAxisAlignedBoundingBox_Z_, 1, b"Z")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_MDLAxisAlignedBoundingBox_Z_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_MDLAxisAlignedBoundingBox_Z_(
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                )
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_MDLAxisAlignedBoundingBox_Z_(
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                ),
                False,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_MDLAxisAlignedBoundingBox_Z_(None, False)

        with self.assertRaises(TypeError):
            self.v_MDLAxisAlignedBoundingBox_Z_(
                (
                    objc.simd.vector_float3(-8.0, -9.0, -10.0),
                    objc.simd.vector_float3(-11.0, -12.0, -13.0),
                ),
                None,
            )

    def test_v_matrix_double4x4_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_matrix_double4x4_, b"v")
        self.assertArgHasType(
            OC_VectorCall.v_matrix_double4x4_, 0, b"{_matrix_double4x4=[4<4d>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_matrix_double4x4_(
            simd.matrix_double4x4(
                [
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                ]
            )
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            simd.matrix_double4x4(
                [
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_matrix_double4x4_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_matrix_double4x4_(
                simd.matrix_double4x4(
                    [
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_matrix_double4x4_(None)

    def test_v_matrix_double4x4_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_matrix_double4x4_d_, b"v")
        self.assertArgHasType(
            OC_VectorCall.v_matrix_double4x4_d_, 0, b"{_matrix_double4x4=[4<4d>]}"
        )
        self.assertArgHasType(OC_VectorCall.v_matrix_double4x4_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_matrix_double4x4_d_(
            simd.matrix_double4x4(
                [
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                ]
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
                [
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_matrix_double4x4_d_(
                simd.matrix_double4x4(
                    [
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    ]
                )
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_matrix_double4x4_d_(
                simd.matrix_double4x4(
                    [
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
                -557000000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_matrix_double4x4_d_(None, -557000000000.0)

        with self.assertRaises(TypeError):
            self.v_matrix_double4x4_d_(
                simd.matrix_double4x4(
                    [
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
                None,
            )

    def test_v_matrix_float2x2_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_matrix_float2x2_, b"v")
        self.assertArgHasType(
            OC_VectorCall.v_matrix_float2x2_, 0, b"{_matrix_float2x2=[2<2f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_matrix_float2x2_(
            simd.matrix_float2x2(
                [objc.simd.vector_float2(0.0, 1.5), objc.simd.vector_float2(0.0, 1.5)]
            )
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            simd.matrix_float2x2(
                [objc.simd.vector_float2(0.0, 1.5), objc.simd.vector_float2(0.0, 1.5)]
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_matrix_float2x2_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_matrix_float2x2_(
                simd.matrix_float2x2(
                    [
                        objc.simd.vector_float2(0.0, 1.5),
                        objc.simd.vector_float2(0.0, 1.5),
                    ]
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_matrix_float2x2_(None)

    def test_v_matrix_float3x3_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_matrix_float3x3_, b"v")
        self.assertArgHasType(
            OC_VectorCall.v_matrix_float3x3_, 0, b"{_matrix_float3x3=[3<3f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_matrix_float3x3_(
            simd.matrix_float3x3(
                [
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                ]
            )
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            simd.matrix_float3x3(
                [
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                ]
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_matrix_float3x3_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_matrix_float3x3_(
                simd.matrix_float3x3(
                    [
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                        objc.simd.vector_float3(0.0, 1.5, 3.0),
                    ]
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_matrix_float3x3_(None)

    def test_v_matrix_float4x4_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_matrix_float4x4_, b"v")
        self.assertArgHasType(
            OC_VectorCall.v_matrix_float4x4_, 0, b"{_matrix_float4x4=[4<4f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_matrix_float4x4_(
            simd.matrix_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            )
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            simd.matrix_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_matrix_float4x4_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_matrix_float4x4_(
                simd.matrix_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_matrix_float4x4_(None)

    def test_v_matrix_float4x4_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_matrix_float4x4_d_, b"v")
        self.assertArgHasType(
            OC_VectorCall.v_matrix_float4x4_d_, 0, b"{_matrix_float4x4=[4<4f>]}"
        )
        self.assertArgHasType(OC_VectorCall.v_matrix_float4x4_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_matrix_float4x4_d_(
            simd.matrix_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
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
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_matrix_float4x4_d_(
                simd.matrix_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                )
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_matrix_float4x4_d_(
                simd.matrix_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
                -557000000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_matrix_float4x4_d_(None, -557000000000.0)

        with self.assertRaises(TypeError):
            self.v_matrix_float4x4_d_(
                simd.matrix_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
                None,
            )

    def test_v_simd_float4x4_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_simd_float4x4_, b"v")
        self.assertArgHasType(
            OC_VectorCall.v_simd_float4x4_, 0, b"{_simd_float4x4=[4<4f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_simd_float4x4_(
            simd.simd_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            )
        )
        self.assertIs(rv, None)

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            simd.simd_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_simd_float4x4_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_simd_float4x4_(
                simd.simd_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_simd_float4x4_(None)

    def test_v_simd_quatd_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_simd_quatd_d_, b"v")
        self.assertArgHasType(OC_VectorCall.v_simd_quatd_d_, 0, b"{_simd_quatd=<4d>}")
        self.assertArgHasType(OC_VectorCall.v_simd_quatd_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_simd_quatd_d_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_simd_quatd_d_(
                simd.simd_quatd(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5))
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_simd_quatd_d_(
                simd.simd_quatd(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5)),
                -557000000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_simd_quatd_d_(None, -557000000000.0)

        with self.assertRaises(TypeError):
            self.v_simd_quatd_d_(
                simd.simd_quatd(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5)), None
            )

    def test_v_simd_quatf_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_simd_quatf_, b"v")
        self.assertArgHasType(OC_VectorCall.v_simd_quatf_, 0, b"{_simd_quatf=<4f>}")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_simd_quatf_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_simd_quatf_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_simd_quatf_(
                simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5)), "hello"
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_simd_quatf_(None)

    def test_v_simd_quatf_v3f_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_simd_quatf_v3f_, b"v")
        self.assertArgHasType(OC_VectorCall.v_simd_quatf_v3f_, 0, b"{_simd_quatf=<4f>}")
        self.assertArgHasType(OC_VectorCall.v_simd_quatf_v3f_, 1, b"<3f>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_simd_quatf_v3f_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_simd_quatf_v3f_(
                simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_simd_quatf_v3f_(
                simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5)),
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_simd_quatf_v3f_(None, objc.simd.vector_float3(0.0, 1.5, 3.0))

        with self.assertRaises(TypeError):
            self.v_simd_quatf_v3f_(
                simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5)), None
            )

    def test_v_simd_quatf_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.v_simd_quatf_d_, b"v")
        self.assertArgHasType(OC_VectorCall.v_simd_quatf_d_, 0, b"{_simd_quatf=<4f>}")
        self.assertArgHasType(OC_VectorCall.v_simd_quatf_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.v_simd_quatf_d_(
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_simd_quatf_d_(
                simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.v_simd_quatf_d_(
                simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5)),
                -557000000000.0,
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.v_simd_quatf_d_(None, -557000000000.0)

        with self.assertRaises(TypeError):
            self.v_simd_quatf_d_(
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

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.GKBox()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.GKBox("hello")

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

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.GKQuad()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.GKQuad("hello")

    def test_GKTriangle_Q_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.GKTriangle_Q_, b"{GKTriangle=[3<3f>]}")
        self.assertArgHasType(OC_VectorCall.GKTriangle_Q_, 0, b"Q")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.GKTriangle_Q_(35184372088832)
        self.assertEqual(
            rv,
            [
                objc.simd.vector_float3(-8.5, -9.5, -10.5),
                objc.simd.vector_float3(-11.5, -12.5, -13.5),
                objc.simd.vector_float3(-7.5, 1.5, 22.5),
            ],
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], 35184372088832)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.GKTriangle_Q_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.GKTriangle_Q_(35184372088832, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.GKTriangle_Q_(None)

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

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.MDLAxisAlignedBoundingBox()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.MDLAxisAlignedBoundingBox("hello")

    def test_MDLAxisAlignedBoundingBox_v4i_(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.MDLAxisAlignedBoundingBox_v4i_,
            b"{_MDLAxisAlignedBoundingBox=<3f><3f>}",
        )
        self.assertArgHasType(OC_VectorCall.MDLAxisAlignedBoundingBox_v4i_, 0, b"<4i>")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.MDLAxisAlignedBoundingBox_v4i_(objc.simd.vector_int4(0, 1, 2, 3))
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.MDLAxisAlignedBoundingBox_v4i_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.MDLAxisAlignedBoundingBox_v4i_(
                objc.simd.vector_int4(0, 1, 2, 3), "hello"
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.MDLAxisAlignedBoundingBox_v4i_(None)

    def test_MDLAxisAlignedBoundingBox_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.MDLAxisAlignedBoundingBox_d_,
            b"{_MDLAxisAlignedBoundingBox=<3f><3f>}",
        )
        self.assertArgHasType(OC_VectorCall.MDLAxisAlignedBoundingBox_d_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.MDLAxisAlignedBoundingBox_d_(-557000000000.0)
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
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.MDLAxisAlignedBoundingBox_d_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.MDLAxisAlignedBoundingBox_d_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.MDLAxisAlignedBoundingBox_d_(None)

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

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.MDLVoxelIndexExtent()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.MDLVoxelIndexExtent("hello")

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

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.MPSAxisAlignedBoundingBox()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.MPSAxisAlignedBoundingBox("hello")

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

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.MPSImageHistogramInfo()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.MPSImageHistogramInfo("hello")

    def test_matrix_double4x4(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.matrix_double4x4, b"{_matrix_double4x4=[4<4d>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.matrix_double4x4()
        self.assertEqual(
            rv,
            simd.matrix_double4x4(
                [
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.matrix_double4x4()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.matrix_double4x4("hello")

    def test_matrix_double4x4_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.matrix_double4x4_d_, b"{_matrix_double4x4=[4<4d>]}"
        )
        self.assertArgHasType(OC_VectorCall.matrix_double4x4_d_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.matrix_double4x4_d_(-557000000000.0)
        self.assertEqual(
            rv,
            simd.matrix_double4x4(
                [
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.matrix_double4x4_d_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.matrix_double4x4_d_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.matrix_double4x4_d_(None)

    def test_matrix_float2x2(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.matrix_float2x2, b"{_matrix_float2x2=[2<2f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.matrix_float2x2()
        self.assertEqual(
            rv,
            simd.matrix_float2x2(
                [objc.simd.vector_float2(0.0, 1.5), objc.simd.vector_float2(0.0, 1.5)]
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.matrix_float2x2()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.matrix_float2x2("hello")

    def test_matrix_float3x3(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.matrix_float3x3, b"{_matrix_float3x3=[3<3f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.matrix_float3x3()
        self.assertEqual(
            rv,
            simd.matrix_float3x3(
                [
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                ]
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.matrix_float3x3()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.matrix_float3x3("hello")

    def test_matrix_float4x4(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.matrix_float4x4, b"{_matrix_float4x4=[4<4f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.matrix_float4x4()
        self.assertEqual(
            rv,
            simd.matrix_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.matrix_float4x4()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.matrix_float4x4("hello")

    def test_matrix_float4x4_id_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.matrix_float4x4_id_d_, b"{_matrix_float4x4=[4<4f>]}"
        )
        self.assertArgHasType(OC_VectorCall.matrix_float4x4_id_d_, 0, b"@")
        self.assertArgHasType(OC_VectorCall.matrix_float4x4_id_d_, 1, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.matrix_float4x4_id_d_("hello", -557000000000.0)
        self.assertEqual(
            rv,
            simd.matrix_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.matrix_float4x4_id_d_("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.matrix_float4x4_id_d_("hello", -557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.matrix_float4x4_id_d_(NoObjCValueObject, -557000000000.0)

        with self.assertRaises(TypeError):
            self.matrix_float4x4_id_d_("hello", None)

    def test_matrix_float4x4_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.matrix_float4x4_d_, b"{_matrix_float4x4=[4<4f>]}"
        )
        self.assertArgHasType(OC_VectorCall.matrix_float4x4_d_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.matrix_float4x4_d_(-557000000000.0)
        self.assertEqual(
            rv,
            simd.matrix_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.matrix_float4x4_d_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.matrix_float4x4_d_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.matrix_float4x4_d_(None)

    def test_simd_float4x4(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.simd_float4x4, b"{_simd_float4x4=[4<4f>]}"
        )

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.simd_float4x4()
        self.assertEqual(
            rv,
            simd.simd_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.simd_float4x4()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.simd_float4x4("hello")

    def test_simd_float4x4_simd_float4x4_id_(self):
        # Check that the signature is as expected
        self.assertResultHasType(
            OC_VectorCall.simd_float4x4_simd_float4x4_id_, b"{_simd_float4x4=[4<4f>]}"
        )
        self.assertArgHasType(
            OC_VectorCall.simd_float4x4_simd_float4x4_id_,
            0,
            b"{_simd_float4x4=[4<4f>]}",
        )
        self.assertArgHasType(OC_VectorCall.simd_float4x4_simd_float4x4_id_, 1, b"@")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.simd_float4x4_simd_float4x4_id_(
            simd.simd_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
            "hello",
        )
        self.assertEqual(
            rv,
            simd.simd_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(
            stored[0],
            simd.simd_float4x4(
                [
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                ]
            ),
        )
        self.assertEqual(stored[1], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.simd_float4x4_simd_float4x4_id_(
                simd.simd_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                )
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.simd_float4x4_simd_float4x4_id_(
                simd.simd_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
                "hello",
                "hello",
            )

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.simd_float4x4_simd_float4x4_id_(None, "hello")

        with self.assertRaises(TypeError):
            self.simd_float4x4_simd_float4x4_id_(
                simd.simd_float4x4(
                    [
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    ]
                ),
                NoObjCValueObject,
            )

    def test_simd_quatd_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.simd_quatd_d_, b"{_simd_quatd=<4d>}")
        self.assertArgHasType(OC_VectorCall.simd_quatd_d_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.simd_quatd_d_(-557000000000.0)
        self.assertEqual(
            rv, simd.simd_quatd(objc.simd.vector_double4(0.0, 1.5, 3.0, 4.5))
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.simd_quatd_d_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.simd_quatd_d_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.simd_quatd_d_(None)

    def test_simd_quatf(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.simd_quatf, b"{_simd_quatf=<4f>}")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.simd_quatf()
        self.assertEqual(
            rv, simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.simd_quatf()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.simd_quatf("hello")

    def test_simd_quatf_d_(self):
        # Check that the signature is as expected
        self.assertResultHasType(OC_VectorCall.simd_quatf_d_, b"{_simd_quatf=<4f>}")
        self.assertArgHasType(OC_VectorCall.simd_quatf_d_, 0, b"d")

        # Create test object
        oc = OC_VectorCall.alloc().init()
        self.assertIsNot(oc, None)

        # Valid call
        rv = oc.simd_quatf_d_(-557000000000.0)
        self.assertEqual(
            rv, simd.simd_quatf(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        )

        stored = oc.storedvalue()
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], -557000000000.0)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.simd_quatf_d_()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "execpted.*arguments.*got"):
            self.simd_quatf_d_(-557000000000.0, "hello")

        # Bad value for arguments
        with self.assertRaises(TypeError):
            self.simd_quatf_d_(None)
