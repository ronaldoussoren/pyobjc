import sys

import DataProvidersAndConsumers
import Utilities

import Cocoa
import Quartz

from LaunchServices import * # kUTType* constants


def drawJPEGImage(context, url):
    # Create a Quartz data provider for the supplied URL.
    jpgProvider = Quartz.CGDataProviderCreateWithURL(url)
    if jpgProvider is None:
        print("Couldn't create JPEG Data provider!")
        return

    # Create the CGImageRef for the JPEG image from the data provider.
    jpgImage = Quartz.CGImageCreateWithJPEGDataProvider(jpgProvider, None,
                            True, Quartz.kCGRenderingIntentDefault)

    # CGImageCreateWithJPEGDataProvider retains the data provider.
    # Since this code created the data provider and this code no
    # longer needs it, it must release it.
    del jpgProvider

    if jpgImage is None:
        print("Couldn't create CGImageRef for JPEG data!")
        return

    # Make a rectangle that has its origin at (0,0) and
    # has a width and height that is 1/4 the native width
    # and height of the image.
    jpgRect = Quartz.CGRectMake(0.0, 0.0,
            Quartz.CGImageGetWidth(jpgImage)/4, Quartz.CGImageGetHeight(jpgImage)/4)


    # Draw the image into the rectangle.
    # This is Image 1.
    Quartz.CGContextDrawImage(context, jpgRect, jpgImage)

    Quartz.CGContextSaveGState(context)

    # Translate to the top-right corner of the image just drawn.
    Quartz.CGContextTranslateCTM(context, jpgRect.size.width,
                                        jpgRect.size.height)
    # Rotate by -90 degrees.
    Quartz.CGContextRotateCTM(context, Utilities.DEGREES_TO_RADIANS(-90))
    # Translate in -x by the width of the drawing.
    Quartz.CGContextTranslateCTM(context, -jpgRect.size.width, 0)

    # Draw the image into the same rectangle as before.
    # This is Image 2.
    Quartz.CGContextDrawImage(context, jpgRect, jpgImage)
    Quartz.CGContextRestoreGState(context)

    Quartz.CGContextSaveGState(context)

    # Translate so that the next drawing of the image appears
    # below and to the right of the image just drawn.
    Quartz.CGContextTranslateCTM(context,
        jpgRect.size.width+jpgRect.size.height, jpgRect.size.height)
    # Scale the y axis by a negative value and flip the image.
    Quartz.CGContextScaleCTM(context, 0.75, -1.0)
    # This is Image 3.
    Quartz.CGContextDrawImage(context, jpgRect, jpgImage)
    Quartz.CGContextRestoreGState(context)

    # Adjust the position of the rectangle so that its origin is
    # to the right and above where Image 3 was drawn. Adjust the
    # size of the rectangle so that it is 1/4 the image width
    # and 1/6 the image height.
    jpgRect = Quartz.CGRectMake( 1.75*jpgRect.size.width + jpgRect.size.height,
                            jpgRect.size.height,
                            Quartz.CGImageGetWidth(jpgImage)/4,
                            Quartz.CGImageGetHeight(jpgImage)/6)
    # This is Image 4.
    Quartz.CGContextDrawImage(context, jpgRect, jpgImage)

def drawImageFromURL(context, url, width, height, bitsPerComponent, isRGB):
    # This routine treats color images as RGB
    if isRGB:
        bitsPerPixel = bitsPerComponent * 3
    else:
        bitsPerPixel = bitsPerComponent

    bytesPerRow = (width * bitsPerPixel + 7)/8
    shouldInterpolate = True

    # Create a Quartz data provider from the supplied URL.
    dataProvider = Quartz.CGDataProviderCreateWithURL(url)
    if dataProvider is None:
        print("Couldn't create Image data provider!")
        return

    # Get a Quartz color space object appropriate for the image type.
    if isRGB:
        colorspace = Utilities.getTheCalibratedRGBColorSpace()
    else:
        colorspace = Utilities.getTheCalibratedGrayColorSpace()

    # Create an image of the width, height, and bitsPerComponent with
    # no alpha data, the default decode array, with interpolation,
    # and the default rendering intent for images. This code is
    # intended for Gray images of the format GGGGG... or RGB images
    # of the format RGBRGBRGB... .
    image = Quartz.CGImageCreate(width, height, bitsPerComponent,
                            bitsPerPixel, bytesPerRow, colorspace,
                            Quartz.kCGImageAlphaNone, dataProvider, None,
                            shouldInterpolate, Quartz.kCGRenderingIntentDefault)
    # Quartz retains the data provider with the image and since this
    # code does not create any more images with the data provider, it
    # can release it.
    del dataProvider
    if image is None:
        print("Couldn't create CGImageRef for this data!")
        return

    # Create a rectangle into which the code will draw the image.
    imageRect = Quartz.CGRectMake(0.0, 0.0, width, height)

    # Draw the image into the rectangle.
    Quartz.CGContextDrawImage(context, imageRect, image)

def doColorRampImage(context):
    width = 256
    height = 256
    bitsPerComponent = 8
    bitsPerPixel = 24
    bytesPerRow = width * 3
    shouldInterpolate = True

    imageDataProvider = DataProvidersAndConsumers.createRGBRampDataProvider()
    if imageDataProvider is None:
        print("Couldn't create Image Data provider!")
        return

    colorspace = Utilities.getTheCalibratedRGBColorSpace()
    image = Quartz.CGImageCreate(width, height, bitsPerComponent,
                bitsPerPixel, bytesPerRow, colorspace, Quartz.kCGImageAlphaNone,
                imageDataProvider, None, shouldInterpolate,
                Quartz.kCGRenderingIntentDefault)
    # No longer need the data provider.
    del imageDataProvider
    if image is None:
        print("Couldn't create CGImageRef for this data!")
        return

    imageRect = Quartz.CGRectMake(0.0, 0.0, width, height)
    # Draw the image.
    Quartz.CGContextDrawImage(context, imageRect, image)

def doImageWithCallbacksCreatedFromURL(context, url, width, height,
        bitsPerComponent, isRGB):

    if isRGB:
        bitsPerPixel = bitsPerComponent * 3
    else:
        bitsPerPixel = bitsPerComponent

    bytesPerRow = ((width * bitsPerPixel) + 7)/8
    shouldInterpolate = True

    dataProvider = DataProvidersAndConsumers.createSequentialAccessDPForURL(url)
    if dataProvider is None:
        print("Couldn't create Image Data provider!")
        return

    # Create a Quartz color space object appropriate for the image type.
    # These user written functions create the color space object
    # and that reference must be released by this code.
    if isRGB:
        colorspace = Utilities.getTheCalibratedRGBColorSpace()
    else:
        colorspace = Utilities.getTheCalibratedGrayColorSpace()

    image = Quartz.CGImageCreate(width, height, bitsPerComponent,
                    bitsPerPixel, bytesPerRow, colorspace,
                    Quartz.kCGImageAlphaNone, dataProvider, None, shouldInterpolate,
                    Quartz.kCGRenderingIntentDefault)
    del dataProvider
    if image is None:
        print("Couldn't create CGImageRef for this data!")
        return

    imageRect = Quartz.CGRectMake(0.0, 0.0, width, height)

    # Draw the image into the rectangle.
    Quartz.CGContextDrawImage(context, imageRect, image)

def doGrayRamp(context):
    width = 256
    height = 1
    bitsPerComponent = 8
    bitsPerPixel = 8
    bytesPerRow = width
    shouldInterpolate = True

    dataProvider = DataProvidersAndConsumers.createGrayRampDirectAccessDP()
    if dataProvider is None:
        print("Couldn't create Gray Ramp provider!")
        return

    colorspace = Utilities.getTheCalibratedGrayColorSpace()
    image = Quartz.CGImageCreate(width, height, bitsPerComponent, bitsPerPixel,
                bytesPerRow, colorspace, Quartz.kCGImageAlphaNone, dataProvider,
                None, shouldInterpolate, Quartz.kCGRenderingIntentDefault)
    del dataProvider
    if image is None:
        print("Couldn't create CGImageRef for image data!")
        return

    imageRect = Quartz.CGRectMake(0.0, 0.0, 256, 256)
    # Drawing the image that is 256 samples wide and
    # 1 scanline high into a rectangle that is 256 x 256 units
    # on a side causes Quartz to stretch the image to fill
    # the destination rectangle.
    Quartz.CGContextDrawImage(context, imageRect, image)

# This routine examines the CGImageSource at index 0 to
# determine if the first image is a floating point image and
# if it is, it returns an options dictionary suitable for
# passing to CGImageSourceCreateImageAtIndex in order to create
# a CGImageRef that contains full dynamic range floating point data.
def createFloatingPointImageOptions(imageSource):
    # Allow the image to be a floating point image.
    # Without this, Quartz would return integer pixel data, even for
    # floating point images. Typically you don't need floating point data
    # but in some special cases you might want it.
    options = {
        Quartz.kCGImageSourceShouldAllowFloat: True
    }
    isFloat = False

    # Obtain the properties for the first image
    # in the image source. This is a 'Copy' function
    # so the code owns a reference to the
    # dictionary returned.
    properties = Quartz.CGImageSourceCopyPropertiesAtIndex(imageSource,
                                                        0, options)
    if properties is not None:
    # Get the value for the kCGImagePropertyIsFloat if it exists
    # and if the value is a CFBoolean then get the corresponding
    # Boolean result.
        if Quartz.kCGImagePropertyIsFloat in properties:
            isFloat = bool(properties[Quartz.kCGImagePropertyIsFloat])

    if not isFloat:
        return None

    return options

def myCreateImageUsingImageSource(url):
    # Set to zero, indicating the property was unavailable.
    xdpi = ydpi = 0

    # Create the image source from the URL.
    imageSource = Quartz.CGImageSourceCreateWithURL(url, None)
    if imageSource is None:
        print("Couldn't create image source from URL!")
        return (None, xdpi, ydpi)

    if False:
        options = createFloatingPointImageOptions(imageSource)
        if options is not None:
            print("image IS a floating point image")
        else:
            print("image IS NOT a floating point image")
    else:
        options = None

    # Obtain the properties dictionary for the first image
    # in the image source. This is a copy function so this
    # code owns the reference returned and must
    # must release it.
    properties = Quartz.CGImageSourceCopyPropertiesAtIndex(
                    imageSource, 0, options)
    if properties is not None:
        # Check for the x and y resolution of the image.
        xdpi = properties[Quartz.kCGImagePropertyDPIWidth]
        ydpi = properties[Quartz.kCGImagePropertyDPIHeight]

    # Create a CGImageRef from the first image in the CGImageSource.
    image = Quartz.CGImageSourceCreateImageAtIndex(imageSource, 0, options)
    # Release the CGImageSource object since it is no longer needed
    # and this code created it. This code uses CFRelease since a
    # CGImageSource object is a CoreFoundation object.
    del imageSource
    del options

    if image is None:
        print("Couldn't create image from image source!")
        return None

    return (image, xdpi, ydpi)

def myCreateThumbnailFromImageSource(url):
    maxThumbSize = 160

    # Create the image source from the URL.
    imageSource = Quartz.CGImageSourceCreateWithURL(url, None)
    if imageSource is None:
        print("Couldn't create image source from URL!")
        return None

    options = {
        # Specify 160 pixels as the maximum width and height of
        # the thumbnail for Quartz to create.
        Quartz.kCGImageSourceThumbnailMaxPixelSize: maxThumbSize,

        # Request that Quartz create a thumbnail image if
        # thumbnail data isn't present in the file.
        Quartz.kCGImageSourceCreateThumbnailFromImageIfAbsent: True,
    }

    # Create the thumbnail image for the first image in the
    # image source, that at index 0, using the options
    # dictionary that the code just created.
    thumb = Quartz.CGImageSourceCreateThumbnailAtIndex(imageSource, 0, options)

    # Release the options dictionary.
    del options
    # Release the image source the code created.
    del imageSource

    if thumb is None:
        print("Couldn't create thumbnail from image source!")
        return None

    return thumb

def imageHasFloatingPointSamples(image):
    if hasattr(Quartz, 'CGImageGetBitmapInfo'):
        return (Quartz.kCGBitmapFloatComponents & Quartz.CGImageGetBitmapInfo(image)) != 0
    return False


def drawImageWithCGImageDataSource(context, url):
    # This code would be better if it created the image source
    # once and used the same image source to create the image and its
    # thumbnail, but the point here is to simply test the routines
    # myCreateImageUsingImageSource and myCreateThumbnailFromImageSource.

    image, xdpi, ydpi = myCreateImageUsingImageSource(url)
    if image is None:
        print("myCreateImageFromImageSource didn't create a CGImage!")
        return

    print("xdpi = %2.f, ydpi = %2.f"%(xdpi, ydpi))
    imageRect = Quartz.CGRectMake(0.0, 0.0,
            Quartz.CGImageGetWidth(image)/3, Quartz.CGImageGetHeight(image)/3)
    Quartz.CGContextDrawImage(context, imageRect, image)

    if 0:
        isFloatingImage = imageHasFloatingPointSamples(image)
        if isFloatingImage:
            print("First image IS a floating point image")
        else:
            print("First image IS NOT a floating point image")

    del image

    image = myCreateThumbnailFromImageSource(url)
    if image is None:
        print("myCreateThumbnailFromImageSource didn't create a CGImage!")
        return

    imageRect = Quartz.CGRectMake(400.0, 0.0,
            Quartz.CGImageGetWidth(image), Quartz.CGImageGetHeight(image))
    Quartz.CGContextDrawImage(context, imageRect, image)

    del image


class MyIncrementalData (object):
    data = None
    dataSize = 0
    repCount = 0
    chunkSize = 0

# This is a dummy data accumulation routine used to demonstrate incremental
# loading of an image.
def myCreateAccumulatedDataSoFar(myDataP):
    myDataP.repCount += 1
    sizeToReturn = myDataP.chunkSize*myDataP.repCount

    if sizeToReturn > myDataP.dataSize:
        sizeToReturn = myDataP.dataSize

    done = (sizeToReturn == myDataP.dataSize)
    data = Cocoa.CFDataCreate(None, myDataP.data, sizeToReturn)
    return data, done


def MyDrawIncrementalImage(context, image,  fullHeight):
    # Obtain the width and height of the image that has been
    # accumulated so far.
    print("MyDrawIncrementalImage", context, image, fullHeight)
    width = Quartz.CGImageGetWidth(image)
    height = Quartz.CGImageGetHeight(image)
    # Adjust the location of the imageRect so that the origin is
    # such that the full image would be located at 0,0 and the partial
    # image top-left corner does not move as the image is filled in.
    # This is only needed for views where the y axis points up the
    # drawing canvas.
    imageRect = Quartz.CGRectMake(0, fullHeight-height, width, height)
    Quartz.CGContextDrawImage(context, imageRect, image)


def myDrawFirstImageIncrementally(context, myDataP):
    height = -1
    # Create an incremental image source.
    imageSource = Quartz.CGImageSourceCreateIncremental(None)
    if imageSource is None:
        print("Couldn't create incremental imagesource!")
        return


    # Loop, gathering the necessary data to find the True
    # height of the image.
    while 1:
        # Fetch the data. The CFData object returned by
        # myCreateAccumulatedDataSoFar is used to update the
        # image source. When the data is complete, the code
        # passes True in the 'done' parameter passed to
        # CGImageSourceUpdateData. Once the data is passed
        # to CGImageSourceUpdateData, the code can release
        # its reference to the data.

        # Accumulate the data.
        data, done = myCreateAccumulatedDataSoFar(myDataP)
        Quartz.CGImageSourceUpdateData(imageSource, data, done)

        # Release the data since Quartz retains it and this code
        # no longer needs it.
        del data

        if height < 0:
            print("height < 0", height)
            # Determine the height of the full image. This is needed in order
            # to adjust the location of the drawing of the partial image in
            # a context where the y axis has the default Quartz orientation
            # pointing up the drawing canvas.
            properties = Quartz.CGImageSourceCopyPropertiesAtIndex(
                                            imageSource, 0, None)
            if properties is not None:
                if Quartz.kCGImagePropertyPixelHeight in properties:
                    height = properties[Quartz.kCGImagePropertyPixelHeight]
            del properties

        # Once the height is obtained, go ahead and see if Quartz
        # has enough data to create a CGImage object.
        print("height", height)
        if height > 0:
            # Now create the CGImageRef from the image source for the
            # first image.
            image = Quartz.CGImageSourceCreateImageAtIndex(
                                                imageSource, 0, None)
            if image is not None:
                # Draw the image using the height of the full image
                # to adjust the location where the image is drawn.
                MyDrawIncrementalImage(context, image, height)
                # Release the partial image once you've drawn it.
                del image
                # Potentially you would want to flush the context so
                # that drawing to a window would appear, even inside
                # this loop. Of course this flush should really be
                # done on a timer so that the flush only occurs at
                # most every 60th of a second. See Chapter 17 regarding
                # timing your usage of CGContextFlush.
                Quartz.CGContextFlush(context)

        # Obtain the status for the image source for the first image.
        status = Quartz.CGImageSourceGetStatusAtIndex(imageSource, 0)

        if done: # or status  == Quartz.kCGImageStatusComplete:
            print(done, status, status  == Quartz.kCGImageStatusComplete)
            break

def createMyIncrementalDataFromURL(url, myDataP):
    myDataP.data = None
    myDataP.dataSize = 0
    myDataP.repCount = 0

    success, pathString = CFURLGetFileSystemRepresentation(url, True, None, 1024)
    pathString = pathString.rstrip(b'\0')


    if success and len(pathString):
        fp = open(pathString, 'rb')
        myDataP.data = fp.read()
        fp.close()
        myDataP.dataSize = len(myDataP.data)

    if myDataP.dataSize > 0:
        myDataP.chunkSize = myDataP.dataSize/10  # 10 chunks

def doIncrementalImageWithURL(context, url):
    myData = MyIncrementalData()
    createMyIncrementalDataFromURL(url, myData)
    if myData.data is None:
        print("couldn't read data from URL!")

    myDrawFirstImageIncrementally(context, myData)
    del myData

# This code requires QuickTime.framework.
# from Carbon import Qt
def createCGImageWithQuickTimeFromURL(url):
    """
    Note: this function doesn't actually worked because the APIs used in here
    aren't properly wrapped (yet).
    """
    return None

    imageRef = None

    err = noErr
    result, dataRef, dataRefType = QTNewDataReferenceFromCFURL(url, 0, None, None)
    if dataRef is not None:
        err, gi = GetGraphicsImporterForDataRefWithFlags(dataRef,
                                            dataRefType, None, 0)
        if not err and gi:
            # Tell the graphics importer that it shouldn't perform
            # gamma correction and it should create an image in
            # the original source color space rather than matching it to
            # a generic calibrated color space.
            result = GraphicsImportSetFlags(gi,
                            (kGraphicsImporterDontDoGammaCorrection +
                            kGraphicsImporterDontUseColorMatching)
            )
            if result == 0:
                result, imageRef = GraphicsImportCreateCGImage(gi,None,0)
                if result != 0:
                    print("got a bad result = %d!"%(result,))
            DisposeHandle(dataRef)
            CloseComponent(gi)

    return imageRef

def drawQTImageWithQuartz(context, url):
    image = createCGImageWithQuickTimeFromURL(url)
    if image is None:
        print("createCGImageWithQuickTimeFromURL didn't create a CGImage!")
        return

    imageRect = Quartz.CGRectMake(0.0, 0.0,
            Quartz.CGImageGetWidth(image), Quartz.CGImageGetHeight(image))
    Quartz.CGContextDrawImage(context, imageRect, image)

def drawJPEGDocumentWithMultipleProfiles(context, url):
    isDeviceRGBImage = False

    # Create a Quartz data provider for the supplied URL.
    jpgProvider = Quartz.CGDataProviderCreateWithURL(url)
    if jpgProvider is None:
        print("Couldn't create JPEG Data provider!")
        return

    # Create the Quartz.CGImageRef for the JPEG image from the data provider.
    jpgImage = Quartz.CGImageCreateWithJPEGDataProvider(
            jpgProvider, None, True, Quartz.kCGRenderingIntentDefault)
    del jpgProvider
    if jpgImage is None:
        print("Couldn't create CGImageRef for JPEG data!")
        return

    # Get the color space characterizing the image. This is a
    # function with 'Get' semantics so the code doesn't own a reference
    # to the color space returned and must not release it.
    originalColorSpace = Quartz.CGImageGetColorSpace(jpgImage)
    if originalColorSpace is None:
        print("image is a masking image, not an image with color!")
        return

    if Quartz.CGColorSpaceGetNumberOfComponents(originalColorSpace) != 3:
        print("This example only works with 3 component JPEG images")
        return

    # Determine if the original color space is DeviceRGB. If that is
    # not the case then bail.
    comparisonColorSpace = Quartz.CGColorSpaceCreateDeviceRGB()

    # Note that this comparison of color spaces works only on
    # Jaguar and later where a CGColorSpaceRef is a
    # CoreFoundation object. Otherwise this will crash!
    #
    # NOTE: 20140109: Disabled the color space comparison because that's not valid
    #       on recent enough OSX versions.

    #isDeviceRGBImage = (comparisonColorSpace == originalColorSpace)

    # This code created 'comparisonColorSpace' so it must release it.
    #del comparisonColorSpace

    #if not isDeviceRGBImage:
    #    print("The color space for the JPEG image is not DeviceRGB!", comparisonColorSpace, originalColorSpace)
    #    #return

    # Might need to adjust this based on the size of the original image.
    Quartz.CGContextScaleCTM(context, 0.5, 0.5)

    imageRect = Quartz.CGRectMake(0.0, Quartz.CGImageGetHeight(jpgImage)/2,
                    Quartz.CGImageGetWidth(jpgImage), Quartz.CGImageGetHeight(jpgImage))

    # Draw the original image to the left of the other two.
    Quartz.CGContextDrawImage(context, imageRect, jpgImage)

    # Recharacterize the original image with the generic Calibrated RGB
    # color space.
    updatedImage1 = Quartz.CGImageCreateCopyWithColorSpace(jpgImage,
                                    Utilities.getTheCalibratedRGBColorSpace())
    # Release the original image since this code is done with it.
    del jpgImage
    if updatedImage1 is None:
        print("There is no updated image to draw!")
        return

    # Draw the image characterized by the Generic profile
    # to the right of the other image.
    imageRect = Quartz.CGRectOffset(imageRect, Quartz.CGRectGetWidth(imageRect) + 10, 0)
    Quartz.CGContextDrawImage(context, imageRect, updatedImage1)

    # Recharacterize the image but now with a color space
    # created with the sRGB profile.
    updatedImage2 = Quartz.CGImageCreateCopyWithColorSpace(updatedImage1,
                                            Utilities.getTheSRGBColorSpace())
    # Release updatedImage1 since this code is done with it.
    del updatedImage1
    if updatedImage2 is None:
        print("There is no second updated image to draw!")
        return

    # Draw the image characterized by the sRGB profile to the right of
    # the image characterized by the generic RGB profile.
    imageRect = Quartz.CGRectOffset(imageRect, Quartz.CGRectGetWidth(imageRect) + 10, 0)
    Quartz.CGContextDrawImage(context, imageRect, updatedImage2)

def createRedGreenRampImageData(width, height, size):
    try:
        dataP = objc.allocateBuffer(size)
    except MemoryError:
        return None

    idx = 0
    # Build an image that is RGB 24 bits per sample. This is a ramp
    # where the red component value increases in red from left to
    # right and the green component increases from top to bottom.
    for g in range(height):
        for r in range(width):
            dataP[idx+0] = r
            dataP[idx+1] = g
            dataP[idx+2] = 0
            idx+=3

    return dataP

def createRGBRampSubDataProvider(subRect):
    bytesPerSample = 3
    width = 256
    height = 256
    bytesPerRow = width*bytesPerSample
    startOffsetX = subRect.origin.x
    startOffsetY = subRect.origin.y
    imageDataSize = bytesPerRow*height

    # The first image sample is at
    # (startOffsetY*bytesPerRow + startOffsetX*bytesPerSample)
    # bytes into the RGB ramp data.
    firstByteOffset = startOffsetY*bytesPerRow + startOffsetX*bytesPerSample

    # The actual size of the image data provided is the full image size
    # minus the amount skipped at the beginning. This is more than the
    # total amount of data that is needed for the subimage but it is
    # valid and easy to calculate.
    totalBytesProvided = imageDataSize - firstByteOffset

    # Create the full color ramp.
    dataP = createRedGreenRampImageData(width, height, imageDataSize)
    if dataP is None:
        print("Couldn't create image data!")
        return None

    # Use the pointer to the first byte as the info parameter since
    # that is the pointer to the block to free when done.
    dataProvider = Quartz.CGDataProviderCreateWithData(dataP,
                        buffer(dataP, firstByteOffset),
                        totalBytesProvided, None)

    if dataProvider is None:
        return None

    return dataProvider

def doColorRampSubImage(context):
    # Start 4 scanlines from the top and 16 pixels from the left edge,
    # skip the last 40 scanlines of the image and the right
    # most 64 pixels.
    insetLeft = 16
    insetTop = 4
    insetRight = 64
    insetBottom = 40

    fullImageWidth = 256
    fullImageHeight = 256
    subImageWidth = fullImageWidth-insetLeft-insetRight
    subImageHeight = fullImageHeight-insetTop-insetBottom
    bitsPerComponent = 8
    bitsPerPixel = 24
    bytesPerRow = fullImageWidth * 3
    shouldInterpolate = True

    imageSubRect = Quartz.CGRectMake(
            insetLeft, insetTop, subImageWidth, subImageHeight)
    colorspace = Utilities.getTheCalibratedRGBColorSpace()

    if hasattr(Quartz, 'CGImageCreateWithImageInRect'):
        imageDataProvider = DataProvidersAndConsumers.createRGBRampDataProvider()
        if imageDataProvider is None:
            print("Couldn't create Image Data provider!")
            return

        fullImage = Quartz.CGImageCreate(fullImageWidth, fullImageHeight,
                        bitsPerComponent, bitsPerPixel,
                        bytesPerRow, colorspace, Quartz.kCGImageAlphaNone,
                        imageDataProvider, None, shouldInterpolate,
                        Quartz.kCGRenderingIntentDefault)
        if fullImage is not None:
            image = Quartz.CGImageCreateWithImageInRect(fullImage, imageSubRect)
            # release the full image since it is no longer required.
            del fullImage

    # If the image hasn't been created yet, this code uses the
    # customized data provider to do so.
    if image is None:
        imageDataProvider = createRGBRampSubDataProvider(imageSubRect)
        if imageDataProvider is None:
            print("Couldn't create Image Data provider!")
            return

        # By supplying bytesPerRow, the extra data at the end of
        # each scanline and the beginning of the next is properly skipped.
        image = Quartz.CGImageCreate(subImageWidth, subImageHeight,
                            bitsPerComponent, bitsPerPixel,
                            bytesPerRow, colorspace, Quartz.kCGImageAlphaNone,
                            imageDataProvider, None, shouldInterpolate,
                            Quartz.kCGRenderingIntentDefault)

    # This code no longer needs the data provider.
    del imageDataProvider

    if image is None:
        print("Couldn't create CGImageRef for this data!")
        return

    # Draw the subimage.
    rect = Quartz.CGRectMake(0, 0, subImageWidth, subImageHeight)
    Quartz.CGContextDrawImage(context, rect, image)

def exportCGImageToPNGFileWithDestination(image, url):
    resolution = 144.

    # Create an image destination at the supplied URL that
    # corresponds to the PNG image format.
    imageDestination = Quartz.CGImageDestinationCreateWithURL(url, kUTTypePNG, 1, None)

    if imageDestination is None:
        print("couldn't create image destination!")
        return

    # Set the keys to be the x and y resolution of the image.
    options = {
        Quartz.kCGImagePropertyDPIWidth: resolution,
        Quartz.kCGImagePropertyDPIHeight: resolution,
    }

    # Add the image with the options dictionary to the destination.
    Quartz.CGImageDestinationAddImage(imageDestination, image, options)

    # Release the options dictionary this code created.
    del options

    # When all the images are added to the destination, finalize it.
    Quartz.CGImageDestinationFinalize(imageDestination)

    # Release the destination when done with it.
    del imageDestination


# This code requires QuickTime.framework
#   include <QuickTime/QuickTime.h>
def exportCGImageToJPEGFile(imageRef, url):
    # This doesn't actually work due to lame Python Quicktime bindings...
    return

    result, dataRef, dataRefType = QTNewDataReferenceFromCFURL(
            url, 0, None, None)
    if result == 0:
        result, graphicsExporter = OpenADefaultComponent(GraphicsExporterComponentType,
                            kQTFileTypeJPEG)
        if result == 0:
            result = GraphicsExportSetInputCGImage(graphicsExporter,
                                            imageRef)
            if result == 0:
                result = GraphicsExportSetOutputDataReference(
                            graphicsExporter, dataRef, dataRefType)
            if result == 0:
                result, sizeWritten = GraphicsExportDoExport(
                        graphicsExporter, None)

            CloseComponent(graphicsExporter)

    if dataRef is not None:
        DisposeHandle(dataRef)

    if result != 0:
        print("Exporting QT image got bad result = %d!"%(result,))

def exportColorRampImageWithQT(context):
    width = 256
    height = 256
    bitsPerComponent = 8
    bitsPerPixel = 24
    bytesPerRow = width * 3
    shouldInterpolate = True

    imageDataProvider = DataProvidersAndConsumers.createRGBRampDataProvider()
    if imageDataProvider is None:
        print("Couldn't create Image Data provider!")
        return

    colorspace = Utilities.getTheCalibratedRGBColorSpace()
    image = Quartz.CGImageCreate(width, height, bitsPerComponent,
                            bitsPerPixel, bytesPerRow, colorspace,
                            Quartz.kCGImageAlphaNone, imageDataProvider,
                            None, shouldInterpolate, Quartz.kCGRenderingIntentDefault)
    del imageDataProvider
    if image is None:
        print("Couldn't create CGImageRef for this data!")
        return

    rect = Quartz.CGRectMake(0.0, 0.0, width, height)
    Quartz.CGContextDrawImage(context, rect, image)

    # Of course this is a total hack.
    outPath = b"/tmp/imageout.jpg"
    exportURL = CFURLCreateFromFileSystemRepresentation(None,
                                outPath, len(outPath), False)
    if exportURL:
        exportCGImageToJPEGFile(image, exportURL)
