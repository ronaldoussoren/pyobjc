import sys

import DataProvidersAndConsumers
import Utilities

from Quartz import *
import Quartz

from LaunchServices import * # kUTType* constants


def drawJPEGImage(context, url):
	# Create a Quartz data provider for the supplied URL.
	jpgProvider = CGDataProviderCreateWithURL(url)
        if jpgProvider is None: 
            print >>sys.stderr, "Couldn't create JPEG Data provider!"
            return
	
	# Create the CGImageRef for the JPEG image from the data provider.
	jpgImage = CGImageCreateWithJPEGDataProvider(jpgProvider, None, 
                                True, kCGRenderingIntentDefault)
    
	# CGImageCreateWithJPEGDataProvider retains the data provider.
	# Since this code created the data provider and this code no
	# longer needs it, it must release it.
	del jpgProvider

        if jpgImage is None:
            print >>sys.stderr, "Couldn't create CGImageRef for JPEG data!"
            return
		
	# Make a rectangle that has its origin at (0,0) and 
	# has a width and height that is 1/4 the native width 
	# and height of the image.
	jpgRect = CGRectMake(0.0, 0.0, 
                CGImageGetWidth(jpgImage)/4, CGImageGetHeight(jpgImage)/4)
    
    
	# Draw the image into the rectangle.
	# This is Image 1.
	CGContextDrawImage(context, jpgRect, jpgImage)
	
	CGContextSaveGState(context)

        # Translate to the top-right corner of the image just drawn.
        CGContextTranslateCTM(context, jpgRect.size.width,
                                            jpgRect.size.height)
        # Rotate by -90 degrees.
        CGContextRotateCTM(context, Utilities.DEGREES_TO_RADIANS(-90))
        # Translate in -x by the width of the drawing.
        CGContextTranslateCTM(context, -jpgRect.size.width, 0)
		
        # Draw the image into the same rectangle as before.
        # This is Image 2.
        CGContextDrawImage(context, jpgRect, jpgImage)
	CGContextRestoreGState(context)
	
        CGContextSaveGState(context)

        # Translate so that the next drawing of the image appears
        # below and to the right of the image just drawn.
        CGContextTranslateCTM(context, 
            jpgRect.size.width+jpgRect.size.height, jpgRect.size.height)
        # Scale the y axis by a negative value and flip the image.
        CGContextScaleCTM(context, 0.75, -1.0)
        # This is Image 3.
        CGContextDrawImage(context, jpgRect, jpgImage)
	CGContextRestoreGState(context)

	# Adjust the position of the rectangle so that its origin is
	# to the right and above where Image 3 was drawn. Adjust the
	# size of the rectangle so that it is 1/4 the image width 
	# and 1/6 the image height.
	jpgRect = CGRectMake( 1.75*jpgRect.size.width + jpgRect.size.height, 
				jpgRect.size.height,
				CGImageGetWidth(jpgImage)/4, 
				CGImageGetHeight(jpgImage)/6)
	# This is Image 4.
	CGContextDrawImage(context, jpgRect, jpgImage)

def drawImageFromURL(context, url, width, height, bitsPerComponent, isRGB):
	# This routine treats color images as RGB
        if isRGB:
            bitsPerPixel = bitsPerComponent * 3
        else:
            bitsPerPixel = bitsPerComponent

	bytesPerRow = (width * bitsPerPixel + 7)/8
	shouldInterpolate = True

	# Create a Quartz data provider from the supplied URL.	 
	dataProvider = CGDataProviderCreateWithURL(url)
        if dataProvider is None:
            print >>sys.stderr, "Couldn't create Image data provider!"
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
	image = CGImageCreate(width, height, bitsPerComponent, 
                                bitsPerPixel, bytesPerRow, colorspace,
                                kCGImageAlphaNone, dataProvider, None,
                                shouldInterpolate, kCGRenderingIntentDefault)
	# Quartz retains the data provider with the image and since this
	# code does not create any more images with the data provider, it
	# can release it.
	del dataProvider
        if image is None:
            print >>sys.stderr,  "Couldn't create CGImageRef for this data!"
            return

	# Create a rectangle into which the code will draw the image.
	imageRect = CGRectMake(0.0, 0.0, width, height)
	
	# Draw the image into the rectangle.
	CGContextDrawImage(context, imageRect, image)

def doColorRampImage(context):
	width = 256
        height = 256
	bitsPerComponent = 8
        bitsPerPixel = 24
	bytesPerRow = width * 3
	shouldInterpolate = True
	
	imageDataProvider = DataProvidersAndConsumers.createRGBRampDataProvider()
        if imageDataProvider is None:
            print >>sys.stderr, "Couldn't create Image Data provider!"
            return
	
	colorspace = Utilities.getTheCalibratedRGBColorSpace()
	image = CGImageCreate(width, height, bitsPerComponent,
                    bitsPerPixel, bytesPerRow, colorspace, kCGImageAlphaNone,
                    imageDataProvider, None, shouldInterpolate, 
                    kCGRenderingIntentDefault)
	# No longer need the data provider.
	del imageDataProvider
        if image is None:
            print >>sys.stderr, "Couldn't create CGImageRef for this data!"
            return

	imageRect = CGRectMake(0.0, 0.0, width, height)
	# Draw the image.
	CGContextDrawImage(context, imageRect, image)

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
        print >>sys.stderr, "Couldn't create Image Data provider!"
        return
	
    # Create a Quartz color space object appropriate for the image type.
    # These user written functions create the color space object
    # and that reference must be released by this code.
    if isRGB:
        colorspace = Utilities.getTheCalibratedRGBColorSpace()
    else:
        colorspace = Utilities.getTheCalibratedGrayColorSpace()

    image = CGImageCreate(width, height, bitsPerComponent, 
                    bitsPerPixel, bytesPerRow, colorspace, 
                    kCGImageAlphaNone, dataProvider, None, shouldInterpolate, 
                    kCGRenderingIntentDefault)
    del dataProvider
    if image is None:
        print >>sys.stder, "Couldn't create CGImageRef for this data!"
        return
	
    imageRect = CGRectMake(0.0, 0.0, width, height)
	
    # Draw the image into the rectangle.
    CGContextDrawImage(context, imageRect, image)

def doGrayRamp(context):
	width = 256
        height = 1
	bitsPerComponent = 8
        bitsPerPixel = 8
	bytesPerRow = width
	shouldInterpolate = True

	dataProvider = DataProvidersAndConsumers.createGrayRampDirectAccessDP()
        if dataProvider is None:
            print >>sys.stderr, "Couldn't create Gray Ramp provider!"
            return
	
	colorspace = Utilities.getTheCalibratedGrayColorSpace()
	image = CGImageCreate(width, height, bitsPerComponent, bitsPerPixel, 
                    bytesPerRow, colorspace, kCGImageAlphaNone, dataProvider, 
                    None, shouldInterpolate, kCGRenderingIntentDefault)
	del dataProvider
        if image is None:
            print >>sys.stderr, "Couldn't create CGImageRef for image data!"
            return

	imageRect = CGRectMake(0.0, 0.0, 256, 256)
	# Drawing the image that is 256 samples wide and
	# 1 scanline high into a rectangle that is 256 x 256 units
	# on a side causes Quartz to stretch the image to fill
	# the destination rectangle.
	CGContextDrawImage(context, imageRect, image)

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
        kCGImageSourceShouldAllowFloat: True
    }
    isFloat = False

    # Obtain the properties for the first image
    # in the image source. This is a 'Copy' function
    # so the code owns a reference to the
    # dictionary returned.
    properties = CGImageSourceCopyPropertiesAtIndex(imageSource, 
                                                        0, options)
    if properties is not None:
        # Get the value for the kCGImagePropertyIsFloat if it exists
        # and if the value is a CFBoolean then get the corresponding 
        # Boolean result.
        if kCGImagePropertyIsFloat in properties:
            isFloat = bool(properties[kCGImagePropertyIsFloat])

    if not isFloat:
        return None

    return options

def myCreateImageUsingImageSource(url):
    # Set to zero, indicating the property was unavailable.
    xdpi = ydpi = 0

    # Create the image source from the URL.
    imageSource = CGImageSourceCreateWithURL(url, None)
    if imageSource is None:
        print >>sys.stderr,  "Couldn't create image source from URL!"
        return (None, xdpi, ydpi)

    if False:
        options = createFloatingPointImageOptions(imageSource)
        if options is not None:
            print >>sys.stderr, "image IS a floating point image"
        else:
            print >>sys.stderr, "image IS NOT a floating point image"
    else:
        options = None
    
    # Obtain the properties dictionary for the first image
    # in the image source. This is a copy function so this
    # code owns the reference returned and must
    # must release it.
    properties = CGImageSourceCopyPropertiesAtIndex(
                    imageSource, 0, options)
    if properties is not None:
        # Check for the x and y resolution of the image.
        xdpi = properties[kCGImagePropertyDPIWidth]
        ydpi = properties[kCGImagePropertyDPIHeight]
	
    # Create a CGImageRef from the first image in the CGImageSource.
    image = CGImageSourceCreateImageAtIndex(imageSource, 0, options)
    # Release the CGImageSource object since it is no longer needed
    # and this code created it. This code uses CFRelease since a
    # CGImageSource object is a CoreFoundation object.
    del imageSource
    del options
    
    if image is None:
        print >>sys.stderr, "Couldn't create image from image source!"
        return None
	
    return (image, xdpi, ydpi)

def myCreateThumbnailFromImageSource(url):
    maxThumbSize = 160
	
    # Create the image source from the URL.
    imageSource = CGImageSourceCreateWithURL(url, None)
    if imageSource is None:
        print >>sys.stderr, "Couldn't create image source from URL!"
        return None

    options = {
        # Specify 160 pixels as the maximum width and height of 
        # the thumbnail for Quartz to create. 
        kCGImageSourceThumbnailMaxPixelSize: maxThumbSize,
    
        # Request that Quartz create a thumbnail image if
        # thumbnail data isn't present in the file.
        kCGImageSourceCreateThumbnailFromImageIfAbsent: True,
    }

    # Create the thumbnail image for the first image in the
    # image source, that at index 0, using the options
    # dictionary that the code just created.
    thumb = CGImageSourceCreateThumbnailAtIndex(imageSource, 0, options)
    
    # Release the options dictionary.
    del options
    # Release the image source the code created.
    del imageSource

    if thumb is None:
        print >>sys.stderr, "Couldn't create thumbnail from image source!"
        return None
    
    return thumb

def imageHasFloatingPointSamples(image):
    if hasattr(Quartz, CGImageGetBitmapInfo):
        return (kCGBitmapFloatComponents & CGImageGetBitmapInfo(image)) != 0
    return False

 
def drawImageWithCGImageDataSource(context, url):
    # This code would be better if it created the image source
    # once and used the same image source to create the image and its 
    # thumbnail, but the point here is to simply test the routines 
    # myCreateImageUsingImageSource and myCreateThumbnailFromImageSource.
    
    image, xdpi, ydpi = myCreateImageUsingImageSource(url)
    if image is None:
        print >>sys.stderr,  "myCreateImageFromImageSource didn't create a CGImage!"
        return
    
    print "xdpi = %2.f, ydpi = %2.f"%(xdpi, ydpi)
    imageRect = CGRectMake(0.0, 0.0, 
            CGImageGetWidth(image)/3, CGImageGetHeight(image)/3)
    CGContextDrawImage(context, imageRect, image)

    if 0:
        isFloatingImage = imageHasFloatingPointSamples(image)
        if isFloatingImage:
            print "First image IS a floating point image"
        else:
            print "First image IS NOT a floating point image"

    del image
    
    image = myCreateThumbnailFromImageSource(url)
    if image is None:
        print >>sys.stderr, "myCreateThumbnailFromImageSource didn't create a CGImage!"
        return

    imageRect = CGRectMake(400.0, 0.0, 
            CGImageGetWidth(image), CGImageGetHeight(image))
    CGContextDrawImage(context, imageRect, image)

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
    data = CFDataCreate(None, myDataP.data, sizeToReturn)
    return data, done


def MyDrawIncrementalImage(context, image,  fullHeight):
    # Obtain the width and height of the image that has been 
    # accumulated so far.
    width = CGImageGetWidth(image)
    height = CGImageGetHeight(image)
    # Adjust the location of the imageRect so that the origin is 
    # such that the full image would be located at 0,0 and the partial 
    # image top-left corner does not move as the image is filled in. 
    # This is only needed for views where the y axis points up the
    # drawing canvas.
    imageRect = CGRectMake(0, fullHeight-height, width, height)
    CGContextDrawImage(context, imageRect, image)


def myDrawFirstImageIncrementally(context, myDataP):
    height = -1
    # Create an incremental image source.
    imageSource = CGImageSourceCreateIncremental(None)
    if imageSource is None:
        print >>sys.stderr, "Couldn't create incremental imagesource!"
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
        CGImageSourceUpdateData(imageSource, data, done)

        # Release the data since Quartz retains it and this code
        # no longer needs it.
        del data

        if height < 0:
            # Determine the height of the full image. This is needed in order
            # to adjust the location of the drawing of the partial image in
            # a context where the y axis has the default Quartz orientation
            # pointing up the drawing canvas.
            properties = CGImageSourceCopyPropertiesAtIndex(
                                            imageSource, 0, None)
            if properties is not None:
                if kCGImagePropertyPixelHeight in properties:
                    height = properties[kCGImagePropertyPixelHeight]
            del properties

        # Once the height is obtained, go ahead and see if Quartz
        # has enough data to create a CGImage object.
        if height > 0:
            # Now create the CGImageRef from the image source for the
            # first image.
            image = CGImageSourceCreateImageAtIndex(
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
                CGContextFlush(context)

        # Obtain the status for the image source for the first image.
        status = CGImageSourceGetStatusAtIndex(imageSource, 0)

        if done or status  == kCGImageStatusComplete:
            break

def createMyIncrementalDataFromURL(url, myDataP):
    myDataP.data = None
    myDataP.dataSize = 0
    myDataP.repCount = 0
    
    success, pathString = CFURLGetFileSystemRepresentation(url, True, None, 1024)
    pathString = pathString.rstrip('\0')


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
        print >>sys.stderr,  "couldn't read data from URL!"
    
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
                    print >>sys.stderr, "got a bad result = %d!"%(result,)
            DisposeHandle(dataRef)
            CloseComponent(gi)

    return imageRef

def drawQTImageWithQuartz(context, url):
    image = createCGImageWithQuickTimeFromURL(url)
    if image is None:
        print >>sys.stderr, "createCGImageWithQuickTimeFromURL didn't create a CGImage!"
        return
    
    imageRect = CGRectMake(0.0, 0.0, 
            CGImageGetWidth(image), CGImageGetHeight(image))
    CGContextDrawImage(context, imageRect, image)

def drawJPEGDocumentWithMultipleProfiles(context, url):
    isDeviceRGBImage = False

    # Create a Quartz data provider for the supplied URL.
    jpgProvider = CGDataProviderCreateWithURL(url)
    if jpgProvider is None:
        print >>sys.stderr, "Couldn't create JPEG Data provider!"
        return
    
    # Create the CGImageRef for the JPEG image from the data provider.
    jpgImage = CGImageCreateWithJPEGDataProvider(
            jpgProvider, None, True, kCGRenderingIntentDefault)
    del jpgProvider
    if jpgImage is None:
        print >>sys.stderr, "Couldn't create CGImageRef for JPEG data!"
        return
    
    # Get the color space characterizing the image. This is a 
    # function with 'Get' semantics so the code doesn't own a reference
    # to the color space returned and must not release it.
    originalColorSpace = CGImageGetColorSpace(jpgImage)
    if originalColorSpace is None:
        print >>sys.stderr, "image is a masking image, not an image with color!"
        return
    
    if CGColorSpaceGetNumberOfComponents(originalColorSpace) != 3:
        print >>sys.stderr, "This example only works with 3 component JPEG images"
        return

    # Determine if the original color space is DeviceRGB. If that is
    # not the case then bail.
    comparisonColorSpace = CGColorSpaceCreateDeviceRGB()
    
    # Note that this comparison of color spaces works only on 
    # Jaguar and later where a CGColorSpaceRef is a 
    # CoreFoundation object. Otherwise this will crash!
    isDeviceRGBImage = (comparisonColorSpace == originalColorSpace)

    # This code created 'comparisonColorSpace' so it must release it.
    del comparisonColorSpace

    if not isDeviceRGBImage:
        print >>sys.stderr, "The color space for the JPEG image is not DeviceRGB!"
        return

    # Might need to adjust this based on the size of the original image.
    CGContextScaleCTM(context, 0.5, 0.5)
    
    imageRect = CGRectMake(0.0, CGImageGetHeight(jpgImage)/2, 
                    CGImageGetWidth(jpgImage), CGImageGetHeight(jpgImage))

    # Draw the original image to the left of the other two.
    CGContextDrawImage(context, imageRect, jpgImage)

    # Recharacterize the original image with the generic Calibrated RGB
    # color space.
    updatedImage1 = CGImageCreateCopyWithColorSpace(jpgImage, 
                                    Utilities.getTheCalibratedRGBColorSpace())
    # Release the original image since this code is done with it.
    del jpgImage
    if updatedImage1 is None:
        print >>sys.stderr, "There is no updated image to draw!"
        return

    # Draw the image characterized by the Generic profile
    # to the right of the other image.
    imageRect = CGRectOffset(imageRect, CGRectGetWidth(imageRect) + 10, 0)
    CGContextDrawImage(context, imageRect, updatedImage1)
    
    # Recharacterize the image but now with a color space
    # created with the sRGB profile. 
    updatedImage2 = CGImageCreateCopyWithColorSpace(updatedImage1, 
                                            Utilities.getTheSRGBColorSpace())
    # Release updatedImage1 since this code is done with it.
    del updatedImage1
    if updatedImage2 is None:
        print >>sys.stderr, "There is no second updated image to draw!"
        return

    # Draw the image characterized by the sRGB profile to the right of
    # the image characterized by the generic RGB profile.
    imageRect = CGRectOffset(imageRect, CGRectGetWidth(imageRect) + 10, 0)
    CGContextDrawImage(context, imageRect, updatedImage2)

def createRedGreenRampImageData(width, height, size):
    try:
        dataP = objc.allocateBuffer(size)
    except MemoryError:
        return None

    idx = 0
    # Build an image that is RGB 24 bits per sample. This is a ramp
    # where the red component value increases in red from left to 
    # right and the green component increases from top to bottom.
    for g in xrange(height):
        for r in xrange(width):
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
        print >>sys.stderr, "Couldn't create image data!"
        return None
    
    # Use the pointer to the first byte as the info parameter since
    # that is the pointer to the block to free when done.
    dataProvider = CGDataProviderCreateWithData(dataP, 
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

    imageSubRect = CGRectMake(
            insetLeft, insetTop, subImageWidth, subImageHeight)
    colorspace = Utilities.getTheCalibratedRGBColorSpace()

    if hasattr(Quartz, 'CGImageCreateWithImageInRect'):
        imageDataProvider = DataProvidersAndConsumers.createRGBRampDataProvider()
        if imageDataProvider is None:
            print >>sys.stderr, "Couldn't create Image Data provider!"
            return

        fullImage = CGImageCreate(fullImageWidth, fullImageHeight,
                        bitsPerComponent, bitsPerPixel, 
                        bytesPerRow, colorspace, kCGImageAlphaNone, 
                        imageDataProvider, None, shouldInterpolate, 
                        kCGRenderingIntentDefault)
        if fullImage is not None:
            image = CGImageCreateWithImageInRect(fullImage, imageSubRect)
            # release the full image since it is no longer required.
            del fullImage

    # If the image hasn't been created yet, this code uses the
    # customized data provider to do so.
    if image is None:
        imageDataProvider = createRGBRampSubDataProvider(imageSubRect)
        if imageDataProvider is None:
            print >>sys.stderr, "Couldn't create Image Data provider!"
            return
    
        # By supplying bytesPerRow, the extra data at the end of 
        # each scanline and the beginning of the next is properly skipped.
        image = CGImageCreate(subImageWidth, subImageHeight,
                            bitsPerComponent, bitsPerPixel,
                            bytesPerRow, colorspace, kCGImageAlphaNone,
                            imageDataProvider, None, shouldInterpolate,
                            kCGRenderingIntentDefault)

    # This code no longer needs the data provider.
    del imageDataProvider

    if image is None:
        print >>sys.stderr, "Couldn't create CGImageRef for this data!"
        return

    # Draw the subimage.
    rect = CGRectMake(0, 0, subImageWidth, subImageHeight)
    CGContextDrawImage(context, rect, image)

def exportCGImageToPNGFileWithDestination(image, url):
    resolution = 144.

    # Create an image destination at the supplied URL that
    # corresponds to the PNG image format.
    imageDestination = CGImageDestinationCreateWithURL(url, kUTTypePNG, 1, None)
		
    if imageDestination is None:
        print >>sys.stderr, "couldn't create image destination!"
        return

    # Set the keys to be the x and y resolution of the image.
    options = {
        kCGImagePropertyDPIWidth: resolution,
        kCGImagePropertyDPIHeight: resolution,
    }

    # Add the image with the options dictionary to the destination.
    CGImageDestinationAddImage(imageDestination, image, options)

    # Release the options dictionary this code created.
    del options

    # When all the images are added to the destination, finalize it. 
    CGImageDestinationFinalize(imageDestination)
    
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
        print >>sys.stderr, "Exporting QT image got bad result = %d!"%(result,)

def exportColorRampImageWithQT(context):
    width = 256
    height = 256
    bitsPerComponent = 8
    bitsPerPixel = 24
    bytesPerRow = width * 3
    shouldInterpolate = True

    imageDataProvider = DataProvidersAndConsumers.createRGBRampDataProvider()
    if imageDataProvider is None:
        print >>sys.stderr, "Couldn't create Image Data provider!"
        return

    colorspace = Utilities.getTheCalibratedRGBColorSpace()
    image = CGImageCreate(width, height, bitsPerComponent, 
                            bitsPerPixel, bytesPerRow, colorspace,
                            kCGImageAlphaNone, imageDataProvider, 
                            None, shouldInterpolate, kCGRenderingIntentDefault)
    del imageDataProvider
    if image is None:
        print >>sys.stderr, "Couldn't create CGImageRef for this data!"
        return
    
    rect = CGRectMake(0.0, 0.0, width, height)
    CGContextDrawImage(context, rect, image)
    
    # Of course this is a total hack.
    outPath = "/tmp/imageout.jpg"
    exportURL = CFURLCreateFromFileSystemRepresentation(None,
                                outPath, len(outPath), False)
    if exportURL:
        exportCGImageToJPEGFile(image, exportURL)
