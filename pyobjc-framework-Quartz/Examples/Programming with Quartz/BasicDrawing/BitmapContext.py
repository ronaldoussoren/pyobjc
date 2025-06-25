import AppDrawing
import DrawingBasics
import LaunchServices
import Quartz
import Utilities

# import Carbon.QT


BEST_BYTE_ALIGNMENT = 16


def COMPUTE_BEST_BYTES_PER_ROW(bpr):
    return (int(bpr) + BEST_BYTE_ALIGNMENT - 1) & ~(BEST_BYTE_ALIGNMENT - 1)


# We need to ensure that the raster data stays alive until we clean up
# the context, store it here.
_rasterDataForContext = {}


def createRGBBitmapContext(width, height, wantDisplayColorSpace, needsTransparentBitmap):
    # This routine allocates data for a pixel array that contains width*height
    # pixels where each pixel is 4 bytes. The format is 8-bit ARGB or XRGB, depending on
    # whether needsTransparentBitmap is true. In order to get the recommended
    # pixel alignment, the bytesPerRow is rounded up to the nearest multiple
    # of BEST_BYTE_ALIGNMENT bytes.

    # Minimum bytes per row is 4 bytes per sample * number of samples.
    bytesPerRow = width * 4
    # Round to nearest multiple of BEST_BYTE_ALIGNMENT.
    bytesPerRow = COMPUTE_BEST_BYTES_PER_ROW(bytesPerRow)

    # Allocate the data for the raster. The total amount of data is bytesPerRow
    # times the number of rows. The function 'calloc' is used so that the
    # memory is initialized to 0.
    try:
        rasterData = bytearray(int(bytesPerRow * height))
    except MemoryError:
        return None

    # The wantDisplayColorSpace argument passed to the function determines
    # whether or not to use the display color space or the generic calibrated
    # RGB color space. The needsTransparentBitmap argument determines whether
    # create a context that records alpha or not.
    if wantDisplayColorSpace:
        cs = Utilities.getTheDisplayColorSpace()
    else:
        cs = Utilities.getTheCalibratedRGBColorSpace()

    if needsTransparentBitmap:
        transparency = Quartz.kCGImageAlphaPremultipliedFirst
    else:
        transparency = Quartz.kCGImageAlphaPremultipliedFirst

    context = Quartz.CGBitmapContextCreate(
        rasterData, width, height, 8, bytesPerRow, cs, transparency
    )
    if context is None:
        return None

    _rasterDataForContext[context] = rasterData

    # Either clear the rect or paint with opaque white, depending on
    # the needs of the caller.
    if needsTransparentBitmap:
        # Clear the context bits so they are transparent.
        Quartz.CGContextClearRect(context, Quartz.CGRectMake(0, 0, width, height))

    else:
        # Since the drawing destination is opaque, first paint
        # the context bits to white.
        Quartz.CGContextSaveGState(context)
        Quartz.CGContextSetFillColorWithColor(context, Utilities.getRGBOpaqueWhiteColor())
        Quartz.CGContextFillRect(context, Quartz.CGRectMake(0, 0, width, height))
        Quartz.CGContextRestoreGState(context)

    return context


def myCGContextGetBitmapInfo(c):
    if hasattr(Quartz, "CGBitmapContextGetBitmapInfo"):
        return Quartz.CGBitmapContextGetBitmapInfo(c)
    else:
        return Quartz.CGBitmapContextGetAlphaInfo(c)


# createImageFromBitmapContext creates a CGImageRef
# from a bitmap context. Calling this routine
# transfers 'ownership' of the raster data
# in the bitmap context, to the image. If the
# image can't be created, this routine frees
# the memory associated with the raster.
def createImageFromBitmapContext(c):
    rasterData = _rasterDataForContext[c]
    # We own the data, hence remove from the mapping
    del _rasterDataForContext[c]

    imageDataSize = Quartz.CGBitmapContextGetBytesPerRow(
        c
    ) * Quartz.CGBitmapContextGetHeight(c)

    if rasterData is None:
        print("Context is not a bitmap context!")

    # Create the data provider from the image data
    dataProvider = Quartz.CGDataProviderCreateWithData(
        None, rasterData, imageDataSize, None
    )
    if dataProvider is None:
        print("Couldn't create data provider!")
        return None

    # Now create the image. The parameters for the image closely match
    # the parameters of the bitmap context. This code uses a NULL
    # decode array and shouldInterpolate is true.
    image = Quartz.CGImageCreate(
        Quartz.CGBitmapContextGetWidth(c),
        Quartz.CGBitmapContextGetHeight(c),
        Quartz.CGBitmapContextGetBitsPerComponent(c),
        Quartz.CGBitmapContextGetBitsPerPixel(c),
        Quartz.CGBitmapContextGetBytesPerRow(c),
        Quartz.CGBitmapContextGetColorSpace(c),
        myCGContextGetBitmapInfo(c),
        dataProvider,
        None,
        True,
        Quartz.kCGRenderingIntentDefault,
    )

    if image is None:
        print("Couldn't create image!")
        return None
    return image


def exportCGImageToFileWithQT(image, url, outputFormat, dpi):
    """
    Export an image using QuickTime API's.

    This function can't possibly work, as the relevant APIs aren't available
    through MacPython. The code below is mostly there in case someone fixes
    the MacPython QuickTime bindings.
    """
    # XXX: Finish
    return

    if outputFormat.lower() == LaunchServices.kUTTypeTIFF.lower():
        imageExportType = LaunchServices.kQTFileTypeTIFF

    elif outputFormat.lower() == LaunchServices.kUTTypePNG.lower():
        imageExportType = LaunchServices.kQTFileTypePNG

    elif outputFormat.lower() == LaunchServices.kUTTypeJPEG.lower():
        imageExportType = LaunchServices.kQTFileTypeJPEG

    else:
        print(f"Requested image export format {outputFormat!r} unsupported")
        return

        result, dataRef, dataRefType = Quartz.QTNewDataReferenceFromCFURL(
            url, 0, None, None
        )
        if result == 0:
            result, graphicsExporter = Quartz.OpenADefaultComponent(
                Quartz.GraphicsExporterComponentType,
                imageExportType,
                graphicsExporter,  # noqa: F821
            )
            if result == 0:
                result = Quartz.GraphicsExportSetInputCGImage(graphicsExporter, image)
                if result == 0:
                    result = Quartz.GraphicsExportSetResolution(
                        graphicsExporter,
                        Quartz.FloatToFixed(dpi),
                        Quartz.FloatToFixed(dpi),
                    )
                if result == 0:
                    result = Quartz.GraphicsExportSetOutputDataReference(
                        graphicsExporter, dataRef, dataRefType
                    )
                if result == 0:
                    result, sizeWritten = Quartz.GraphicsExportDoExport(
                        graphicsExporter, None
                    )
                Quartz.CloseComponent(graphicsExporter)

        if dataRef:
            Quartz.DisposeHandle(dataRef)

        if result:
            print("QT export got bad result = %d!" % (result,))


def exportCGImageToFileWithDestination(image, url, outputFormat, dpi):
    # Create an image destination at the supplied URL that
    # corresponds to the output image format. The destination will
    # only contain 1 image.
    imageDestination = Quartz.CGImageDestinationCreateWithURL(url, outputFormat, 1, None)

    if imageDestination is None:
        print("Couldn't create image destination!")
        return

    # Create an options dictionary with the X&Y resolution of the image
    options = {
        Quartz.kCGImagePropertyDPIWidth: dpi,
        Quartz.kCGImagePropertyDPIHeight: dpi,
    }

    # Add the image with the options dictionary to the destination.
    Quartz.CGImageDestinationAddImage(imageDestination, image, options)

    # When all the images are added to the destination, finalize it.
    Quartz.CGImageDestinationFinalize(imageDestination)


def MakeImageDocument(url, imageType, exportInfo):
    # First make a bitmap context for a US Letter size
    # raster at the requested resolution.
    dpi = exportInfo.dpi
    width = int(8.5 * dpi)
    height = int(11 * dpi)

    # For JPEG output type the bitmap should not be transparent. If other types are added that
    # do not support transparency, this code should be updated to check for those types as well.
    needTransparentBitmap = imageType.lower() != LaunchServices.kUTTypeJPEG.lower()

    # Create an RGB Bitmap context using the generic calibrated RGB color space
    # instead of the display color space.
    useDisplayColorSpace = False
    c = createRGBBitmapContext(width, height, useDisplayColorSpace, needTransparentBitmap)

    if c is None:
        print("Couldn't make destination bitmap context")
        return -1

    # Scale the coordinate system based on the resolution in dots per inch.
    Quartz.CGContextScaleCTM(c, dpi / 72, dpi / 72)

    # Set the font smoothing parameter to false since it's better to
    # draw any text without special LCD text rendering when creating
    # rendered data for export.
    if hasattr(Quartz, "CGContextSetShouldSmoothFonts"):
        Quartz.CGContextSetShouldSmoothFonts(c, False)

    # Set the scaling factor for shadows. This is a hack so that
    # drawing code that needs to know the scaling factor can
    # obtain it. Better would be that DispatchDrawing and the code
    # it calls would take this scaling factor as a parameter.
    Utilities.setScalingFactor(dpi / 72)

    # Draw into that raster...
    AppDrawing.DispatchDrawing(c, exportInfo.command)

    # Set the scaling factor back to 1.0.
    Utilities.setScalingFactor(1.0)

    # Create an image from the raster data. Calling
    # createImageFromBitmapContext gives up ownership
    # of the raster data used by the context.
    image = createImageFromBitmapContext(c)

    # Release the context now that the image is created.
    del c

    if image is None:
        # Users of this code should update this to be an error code they find useful.
        return -1

    # Now export the image.
    if exportInfo.useQTForExport:
        exportCGImageToFileWithQT(image, url, imageType, exportInfo.dpi)
    else:
        exportCGImageToFileWithDestination(image, url, imageType, exportInfo.dpi)


def MakeTIFFDocument(url, exportInfo):
    return MakeImageDocument(url, LaunchServices.kUTTypeTIFF, exportInfo)


def MakePNGDocument(url, exportInfo):
    return MakeImageDocument(url, LaunchServices.kUTTypePNG, exportInfo)


def MakeJPEGDocument(url, exportInfo):
    return MakeImageDocument(url, LaunchServices.kUTTypeJPEG, exportInfo)


def createCGLayerForDrawing(c):
    rect = Quartz.CGRectMake(0, 0, 50, 50)

    # Make the layer the size of the rectangle that
    # this code draws into the layer.
    layerSize = rect.size

    # Create the layer to draw into.
    layer = Quartz.CGLayerCreateWithContext(c, layerSize, None)
    if layer is None:
        return None

    # Get the context corresponding to the layer.
    layerContext = Quartz.CGLayerGetContext(layer)
    if layerContext is None:
        return None

    # $ Set the fill color to opaque black.
    Quartz.CGContextSetFillColorWithColor(
        layerContext, Utilities.getRGBOpaqueBlackColor()
    )

    # Draw the content into the layer.
    Quartz.CGContextFillRect(layerContext, rect)

    # Now the layer has the contents needed.
    return layer


def doSimpleCGLayer(context):
    # Create the layer.
    layer = createCGLayerForDrawing(context)

    if layer is None:
        print("Couldn't create layer!")
        return

    # Get the size of the layer created.
    s = Quartz.CGLayerGetSize(layer)

    # Clip to a rect that corresponds to
    # a grid of 8x8 layer objects.
    Quartz.CGContextClipToRect(
        context, Quartz.CGRectMake(0, 0, 8 * s.width, 8 * s.height)
    )

    # Paint 8 rows of layer objects.
    for j in range(8):
        Quartz.CGContextSaveGState(context)
        # Paint 4 columns of layer objects, moving
        # across the drawing canvas by skipping a
        # square on the grid each time across.
        for _ in range(4):
            # Draw the layer at the current origin.
            Quartz.CGContextDrawLayerAtPoint(context, Quartz.CGPointZero, layer)
            # Translate across two layer widths.
            Quartz.CGContextTranslateCTM(context, 2 * s.width, 0)

        Quartz.CGContextRestoreGState(context)
        # Translate to the left one layer width on
        # even loop counts and to the right one
        # layer width on odd loop counts. Each
        # time through the outer loop, translate up
        # one layer height.
        if j % 2:
            Quartz.CGContextTranslateCTM(context, s.width, s.height)
        else:
            Quartz.CGContextTranslateCTM(context, -s.width, s.height)


def createAlphaOnlyContext(width, height):
    # This routine allocates data for a pixel array that contains
    # width*height pixels, each pixel is 1 byte. The format is
    # 8 bits per pixel, where the data is the alpha value of the pixel.

    # Minimum bytes per row is 1 byte per sample * number of samples.
    bytesPerRow = width
    # Round to nearest multiple of BEST_BYTE_ALIGNMENT.
    bytesPerRow = COMPUTE_BEST_BYTES_PER_ROW(bytesPerRow)

    # Allocate the data for the raster. The total amount of data is bytesPerRow
    # // times the number of rows. The function 'calloc' is used so that the
    # // memory is initialized to 0.
    try:
        rasterData = bytearray(bytesPerRow * height)
    except MemoryError:
        return None

    # This type of context is only available in Panther and later, otherwise
    # this fails and returns a NULL context. The color space for an alpha
    # // only context is NULL and the BitmapInfo value is kCGImageAlphaOnly.
    context = Quartz.CGBitmapContextCreate(
        rasterData, width, height, 8, bytesPerRow, None, Quartz.kCGImageAlphaOnly
    )
    if context is None:
        print("Couldn't create the context!")
        return None

    _rasterDataForContext[context] = rasterData

    # Clear the context bits so they are initially transparent.
    Quartz.CGContextClearRect(context, Quartz.CGRectMake(0, 0, width, height))

    return context


# createMaskFromAlphaOnlyContext creates a CGImageRef
# from an alpha-only bitmap context. Calling this routine
# transfers 'ownership' of the raster data in the bitmap
# context, to the image. If the image can't be created, this
# routine frees the memory associated with the raster.


def createMaskFromAlphaOnlyContext(alphaContext):
    rasterData = _rasterDataForContext[alphaContext]
    # We own the data, hence remove from the mapping
    del _rasterDataForContext[alphaContext]

    imageDataSize = Quartz.CGBitmapContextGetBytesPerRow(
        alphaContext
    ) * Quartz.CGBitmapContextGetHeight(alphaContext)
    invertDecode = [1.0, 0.0]

    # Create the data provider from the image data.
    dataProvider = Quartz.CGDataProviderCreateWithData(
        None, rasterData, imageDataSize, None
    )

    if dataProvider is None:
        print("Couldn't create data provider!")
        return None

    mask = Quartz.CGImageMaskCreate(
        Quartz.CGBitmapContextGetWidth(alphaContext),
        Quartz.CGBitmapContextGetHeight(alphaContext),
        Quartz.CGBitmapContextGetBitsPerComponent(alphaContext),
        Quartz.CGBitmapContextGetBitsPerPixel(alphaContext),
        Quartz.CGBitmapContextGetBytesPerRow(alphaContext),
        dataProvider,
        # The decode is an inverted decode since a mask has the opposite
        # sense than alpha, i.e. 0 in a mask paints 100% and 1 in a mask
        # paints nothing.
        invertDecode,
        True,
    )

    if mask is None:
        print("Couldn't create image mask!")
        return None

    return mask


def doAlphaOnlyContext(context):
    # This code is going to capture the alpha coverage
    # of the drawing done by the doAlphaRects routine.
    # The value passed here as the width and height is
    # the size of the bounding rectangle of that drawing.
    width = 520
    height = 400
    alphaContext = createAlphaOnlyContext(width, height)
    if context is None:
        print("Couldn't create the alpha-only context!")
        return

    # Draw the content to the alpha-only context, capturing
    # the alpha coverage. The doAlphaRects routine paints
    # a series of translucent red rectangles.
    DrawingBasics.doAlphaRects(alphaContext)

    # Finished drawing to the context and now the raster contains
    # the alpha data captured from the drawing. Create
    # the mask from the data in the context.
    mask = createMaskFromAlphaOnlyContext(alphaContext)
    # This code is now finished with the context so it can
    # release it.
    del alphaContext

    if mask is None:
        return

    # Set the fill color space.
    Quartz.CGContextSetFillColorSpace(context, Utilities.getTheCalibratedRGBColorSpace())
    opaqueBlue = (0.11, 0.208, 0.451, 1.0)
    # Set the painting color to opaque blue.
    Quartz.CGContextSetFillColor(context, opaqueBlue)
    # Draw the mask, painting the mask with blue. This colorizes
    # the image to blue and it is as if we painted the
    # alpha rects with blue instead of red.
    Quartz.CGContextDrawImage(context, Quartz.CGRectMake(0, 0, width, height), mask)


_pdfDoc = None
_pdfURL = None
_width = 0
_height = 0


def getThePDFDoc(url):
    """
    This function caches a CGPDFDocumentRef for
    the most recently requested PDF document.
    """
    global _pdfDoc, _pdfURL, _width, _height

    if url is None:
        return None, 0, 0

    # See whether to update the cached PDF document.
    if _pdfDoc is None or url != _pdfURL:
        # Release any cached document or URL.
        _pdfDoc = Quartz.CGPDFDocumentCreateWithURL(url)
        if _pdfDoc is not None:
            pdfMediaRect = Quartz.CGPDFDocumentGetMediaBox(_pdfDoc, 1)
            _width = pdfMediaRect.size.width
            _height = pdfMediaRect.size.height
            # Keep the URL of the PDF file being cached.
            _pdfURL = url

        else:
            _pdfURL = None

    if _pdfDoc is not None:
        return _pdfDoc, _width, _height

    else:
        return None, 0, 0


# Defining this scales the content down by 1/3.
DOSCALING = True


def TilePDFNoBuffer(context, url):
    # The amount of area to tile should really be based on the
    # window/document. Here it is hard coded to a US Letter
    # size document. This may draw too many or too few tiles
    # for the area actually being filled.
    fillwidth = 612.0
    fillheight = 792.0
    extraOffset = 6.0
    pdfDoc, tileX, tileY = getThePDFDoc(url)
    if pdfDoc is None:
        print("Couldn't get the PDF document!")
        return

    if DOSCALING:
        # Make the tiles 1/3 the size of the PDF document.
        tileX /= 3
        tileY /= 3
        extraOffset /= 3

    # Space the tiles by the tile width and height
    # plus extraOffset units in each dimension.
    tileOffsetX = extraOffset + tileX
    tileOffsetY = extraOffset + tileY

    # Tile the PDF document.
    for h in range(0, int(fillheight), int(tileOffsetY)):
        for w in range(0, int(fillwidth), int(tileOffsetX)):
            Quartz.CGContextDrawPDFDocument(
                context, Quartz.CGRectMake(w, h, tileX, tileY), pdfDoc, 1
            )


def TilePDFWithOffscreenBitmap(context, url):
    # Again this should really be computed based on
    # the area intended to be tiled.
    fillwidth = 612.0
    fillheight = 792.0
    extraOffset = 6.0

    pdfDoc, tileX, tileY = getThePDFDoc(url)
    if pdfDoc is None:
        print("Couldn't get the PDF document")
        return

    if DOSCALING:
        # Make the tiles 1/3 the size of the PDF document.
        tileX /= 3
        tileY /= 3
        extraOffset /= 3

    # Space the tiles by the tile width and height
    # plus extraOffset units in each dimension.
    tileOffsetX = extraOffset + tileX
    tileOffsetY = extraOffset + tileY

    # Since the bitmap context is for use with the display
    # and should capture alpha, these are the values
    # to pass to createRGBBitmapContext.
    useDisplayColorSpace = True
    needTransparentBitmap = True
    bitmapContext = createRGBBitmapContext(
        tileX, tileY, useDisplayColorSpace, needTransparentBitmap
    )
    if bitmapContext is None:
        print("Couldn't create bitmap context!")
        return

    # Draw the PDF document one time into the bitmap context.
    Quartz.CGContextDrawPDFDocument(
        bitmapContext, Quartz.CGRectMake(0, 0, tileX, tileY), pdfDoc, 1
    )

    # Create an image from the raster data. Calling
    # createImageFromBitmapContext gives up ownership
    # of the raster data used by the context.
    image = createImageFromBitmapContext(bitmapContext)

    # Release the context now that the image is created.
    del bitmapContext

    if image is None:
        return

    # Now tile the image.
    for h in range(0, int(fillheight), int(tileOffsetY)):
        for w in range(0, int(fillwidth), int(tileOffsetX)):
            Quartz.CGContextDrawImage(
                context, Quartz.CGRectMake(w, h, tileX, tileY), image
            )


def createLayerWithImageForContext(c, url):
    layerSize = Quartz.CGSize()
    pdfDoc, layerSize.width, layerSize.height = getThePDFDoc(url)
    if pdfDoc is None:
        return None

    if DOSCALING:
        # Make the layer 1/3 the size of the PDF document.
        layerSize.width /= 3
        layerSize.height /= 3

    # Create the layer to draw into.
    layer = Quartz.CGLayerCreateWithContext(c, layerSize, None)
    if layer is None:
        return None

    # Get the context corresponding to the layer. Note
    # that this is a 'Get' function so the code must
    # not release the context.
    layerContext = Quartz.CGLayerGetContext(layer)
    if layerContext is None:
        return None

    # Draw the PDF document into the layer.
    Quartz.CGContextDrawPDFDocument(
        layerContext,
        Quartz.CGRectMake(0, 0, layerSize.width, layerSize.height),
        pdfDoc,
        1,
    )

    # Now the layer has the contents needed.
    return layer


def TilePDFWithCGLayer(context, url):
    # Again this should really be computed based on
    # the area intended to be tiled.
    fillwidth = 612.0
    fillheight = 792.0
    layer = createLayerWithImageForContext(context, url)
    if layer is None:
        print("Couldn't create the layer!")
        return

    # Compute the tile size and offset.
    s = Quartz.CGLayerGetSize(layer)
    tileX = s.width
    tileY = s.height

    if DOSCALING:
        # Space the tiles by the tile width and height
        # plus an extra 2 units in each dimension.
        tileOffsetX = 2.0 + tileX
        tileOffsetY = 2.0 + tileY
    else:
        # Add 6 units to the offset in each direction
        # if there is no scaling of the source PDF document.
        tileOffsetX = 6.0 + tileX
        tileOffsetY = 6.0 + tileY

    # Now draw the contents of the layer to the context.
    # The layer is drawn at its true size (the size of
    # the tile) with its origin located at the corner
    # of each tile.
    for h in range(0, int(fillheight), int(tileOffsetY)):
        for w in range(0, int(fillwidth), int(tileOffsetX)):
            Quartz.CGContextDrawLayerAtPoint(context, Quartz.CGPointMake(w, h), layer)
