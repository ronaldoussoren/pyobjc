from Cocoa import *
from CGImageUtils import *
import math

class Controller (NSObject):
    imageView = objc.IBOutlet()
    scaleYView = objc.IBOutlet()
    textScaleYView = objc.IBOutlet()

    _rotation = objc.ivar.float()
    _scaleX = objc.ivar.float()
    _scaleY = objc.ivar.float()
    _translateX = objc.ivar.float()
    _translateY = objc.ivar.float()
    _preserveAspectRatio = objc.ivar.bool()

    openImageIOSupportedTypes = objc.ivar()

    def awakeFromNib(self):
        self.openImageIOSupportedTypes = None
        # Ask CFBundle for the location of our demo image
        url = CFBundleCopyResourceURL(CFBundleGetMainBundle(), u"demo", u"png", None)
        if url is not None:
            # And if available, load it
            self.imageView.setImage_(IICreateImage(url))

        self.imageView.window().center()
        self.setRotation_(0.0)
        self.setScaleX_(1.0)
        self.setScaleY_(1.0)
        self.setTranslateX_(0.0)
        self.setTranslateY_(0.0)
        self.setPreserveAspectRatio_(False)

    @objc.IBAction
    def changeScaleX_(self, sender):
        self.setScaleX_(self._scaleX + sender.floatValue())
        sender.setFloatValue_(0.0)

    @objc.IBAction
    def changeScaleY_(self, sender):
        self.setScaleY_(self._scaleY + sender.floatValue())
        sender.setFloatValue_(0.0)

    @objc.IBAction
    def changeTranslateX_(self, sender):
        self.setTranslateX_(self._translateX + sender.floatValue())
        sender.setFloatValue_(0.0)

    @objc.IBAction
    def changeTranslateY_(self, sender):
        self.setTranslateY_(self.translateY + sender.floatValue())
        sender.setFloatValue_(0.0)

    @objc.IBAction
    def reset_(self, sender):
        self.setRotation_(0.0)
        self.setScaleX_(1.0)
        self.setScaleY_(1.0)
        self.setTranslateX_(0.0)
        self.setTranslateY_(0.0)

        self.imageView.setNeedsDisplay_(True)

    # Returns an array with the extensions that match the given Uniform Type Identifier (UTI).
    def extensionsForUTI_(self, uti):
        # If anything goes wrong, we'll return None, otherwise this will be the array of extensions
        # for this image type.
        extensions = None
        # Only get extensions for UTIs that are images (i.e. conforms to public.image aka kUTTypeImage)
        # This excludes PDF support that ImageIO advertises, but won't actually use.
        if UTTypeConformsTo(uti, kUTTypeImage):
            # Copy the decleration for the UTI (if it exists)
            decleration = UTTypeCopyDeclaration(uti)
            if decleration is not None:
                # Grab the tags for this UTI, which includes extensions, OSTypes and MIME types.
                tags = CFDictionaryGetValue(decleration, kUTTypeTagSpecificationKey)
                if tags is not None:
                    # We are interested specifically in the extensions that this UTI uses
                    filenameExtensions = tags.get(kUTTagClassFilenameExtension)
                    if filenameExtensios is not None:
                        # It is valid for a UTI to export either an Array (of Strings) representing
                        # multiple tags, or a String representing a single tag.
                        type = CFGetTypeID(filenameExtensions)
                        if type == CFStringGetTypeID():
                            # If a string was exported, then wrap it up in an array.
                            extensions = NSArray.arrayWithObject_(filenameExtensions)
                        elif type == CFArrayGetTypeID():
                            # If an array was exported, then just return that array.
                            extensions = filenameExtensions.copy()

        return extensions

    # On Tiger NSOpenPanel only understands extensions, not UTIs, so we have to obtain a list of extentions
    # from the UTIs that Image IO tells us it can handle.
    def createOpenTypesArray(self):
        if self.openImageIOSupportedTypes is None:
            imageIOUTIs = CGImageSourceCopyTypeIdentifiers()
            count = len(imageIOUTIs)
            self.openImageIOSupportedTypes = NSMutableArray.alloc().initWithCapacity_(count)
            for i in xrange(count):
                self.openImageIOSupportedTypes.addObjectsFromArray_(
                    self.extensionsForUTI_(imageIOUTIs[i]))

    @objc.IBAction
    def openDocument_(self, sender):
        panel = NSOpenPanel.openPanel()
        panel.setAllowsMultipleSelection_(False)
        panel.setResolvesAliases_(True)
        panel.setTreatsFilePackagesAsDirectories_(True)

        self.createOpenTypesArray()

        panel.beginSheetForDirectory_file_types_modalForWindow_modalDelegate_didEndSelector_contextInfo_(
                None, None, self.openImageIOSupportedTypes, self.imageView.window(), self,
                'openImageDidEnd:returnCode:contextInfo:', None)

    @objc.signature("v@:@i^v")
    def openImageDidEnd_returnCode_contextInfo_(self, panel, returnCode, contextInfo_):
        if returnCode == NSOKButton:
            if len(panel.filenames()) > 0:
                image = IICreateImage(NSURL.fileURLWithPath_(panel.filenames()[0]))
                if images is not None:
                    # Ownership is transferred to the CGImageView.
                    self.imageView.setImage_(image)

    @objc.IBAction
    def saveDocumentAs_(self, sender):
        panel = NSSavePanel.savePanel()
        panel.setCanSelectHiddenExtension_(True)
        panel.setRequiredFileType_("jpeg")
        panel.setAllowsOtherFileTypes_(False)
        panel.setTreatsFilePackagesAsDirectories_(True)

        panel.beginSheetForDirectory_file_modalForWindow_modalDelegate_didEndSelector_contextInfo_(
                None, "untitled image", self.imageView.window(), self,
                'saveImageDidEnd:returnCode:contextInfo:', None)

    @objc.signature("v@:@i^v")
    def saveImageDidEnd_returnCode_contextInfo_(self, panel, returnCode, contextInfo):
        if returnCode == NSOKButton:
            frame = self.imageView.frame()
            IISaveImage(self.imageView.image(), panel.URL(),
                    math.ceil(frame.size.width), math.ceil(frame.size.height))

    def setRotation_(self, r):
        r = r % 360.0
        if r < 0:
            r += 360.0

        self._rotation = r
        self.imageView.image().fRotation = 360.0 - r # XXX
        self.imageView.setNeedsDisplay_(True)

    def setScaleX_(self, x):
        self._scaleX = x;
        self.imageView.image().fScaleX = self._scaleX
        if self._preserveAspectRatio:
            self.imageView.image().fScaleY = self._scaleX

        self.imageView.setNeedsDisplay_(True)

    def setScaleY_(self, y):
        self._scaleY = y
        if not self._preserveAspectRatio:
            self.imageView.image().fScaleY = self._scaleY
            self.imageView.setNeedsDisplay_(True)

    def setPreserveAspectRatio_(self, preserve):
        self._preserveAspectRatio = preserve
        self.imageView.image().fScaleX = self._scaleX
        if self._preserveAspectRatio:
            self.imageView.image().fScaleY = self._scaleX

        else:
            self.imageView.image().fScaleY = self._scaleY

        self.scaleYView.setEnabled_(not self._preserveAspectRatio)
        self.textScaleYView.setEnabled_(not self._preserveAspectRatio)
        self.imageView.setNeedsDisplay_(True)

    def setTranslateX_(self, x):
        self._translateX = x
        self.imageView.image().fTranslateX = self._translateX
        self.imageView.setNeedsDisplay_(True)

    def setTranslateY_(self, y):
        self._translateY = y
        self.imageView.image().fTranslateY = self._translateY
        self.imageView.setNeedsDisplay_(True)

    def rotation(self):
        return self._rotation

    def scaleX(self):
        return self._scaleX

    def scaleY(self):
        return self._scaleY

    def preserveAspectRatio(self):
        return self._preserveAspectRatio

    def translateX(self):
        return self._translateX

    def translateY(self):
        return self._translateY
