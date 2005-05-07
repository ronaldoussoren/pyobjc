"""
Automator doesn't add 'interesting' behaviour, just check that the
module loaded correctly.
"""

import unittest
import objc

class Test (unittest.TestCase):

    def testClasses(self):
        import Quartz

        self.assert_(hasattr(Quartz, 'PDFAnnotation'))
        self.assert_(isinstance(Quartz.PDFAnnotation, objc.objc_class))

        self.assert_(hasattr(Quartz, 'QCRenderer'))
        self.assert_(isinstance(Quartz.QCRenderer, objc.objc_class))

    def testConstants(self):
        import Quartz

        self.assert_(hasattr(Quartz, 'kPDFWidgetUnknownControl'))
        self.assert_(isinstance(Quartz.kPDFWidgetUnknownControl, (int,long)))
        self.assert_(hasattr(Quartz, 'kPDFMarkupTypeHighlight'))
        self.assert_(isinstance(Quartz.kPDFMarkupTypeHighlight, (int,long)))
        self.assert_(hasattr(Quartz, 'PDFDocumentDidUnlockNotification'))

        self.assert_(hasattr(Quartz, 'QCRendererEventKey'))
        self.assert_(isinstance(Quartz.QCRendererEventKey, unicode))

if __name__ == "__main__":
    unittest.main()
