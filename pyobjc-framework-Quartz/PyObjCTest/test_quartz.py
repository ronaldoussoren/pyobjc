from PyObjCTools.TestSupport import TestCase

import Quartz


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            Quartz,
            exclude_attrs={
                "NSColor",
                ("NSColor", "scn_C3DColorIgnoringColorSpace_success_"),
                "IOGPUMetalIOHandleRaw",
                "IOGPUMetalDevice",
                "IOGPUMetalIOHandleCompressed",
                "IOGPUMetalDebugCommandEncoder",
                "IOGPUMetalCommandBuffer",
                "AGXG13GFamilyDevice",
                "AGXG13GDevice",
                "AGXG13GFamilyDebugContext",
                "AGXG13GFamilyBinaryArchive",
                "AGXG13GFamilyCommandBuffer",
                "_MTLDevice",
            },
        )

    def test_framework_identifiers(self):
        from Quartz import (
            CoreGraphics,
            ImageIO,
            ImageKit,
            CoreVideo,
            QuartzCore,
            PDFKit,
            QuartzFilters,
            QuickLookUI,
            QuartzComposer,
        )

        for fwk in (
            CoreGraphics,
            ImageIO,
            ImageKit,
            CoreVideo,
            QuartzCore,
            PDFKit,
            QuartzFilters,
            QuickLookUI,
            QuartzComposer,
        ):
            with self.subTest(framework=fwk.__name__):
                self.assertEqual(
                    fwk.__bundle__.bundleIdentifier(), fwk.__framework_identifier__
                )
