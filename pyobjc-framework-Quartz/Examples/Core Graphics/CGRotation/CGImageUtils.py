import math

import Cocoa
import LaunchServices
import objc
import Quartz


class ImageInfo:
    __slots__ = (
        "fRotation",
        "fScaleX",
        "fScaleY",
        "fTranslateX",
        "fTranslateY",
        "fImageRef",
        "fProperties",
        "fOrientation",
    )

    def __init__(self):
        self.fRotation = 0.0  # The rotation about the center of the image (degrees)
        self.fScaleX = 0.0  # The scaling of the image along it's X-axis
        self.fScaleY = 0.0  # The scaling of the image along it's Y-axis
        self.fTranslateX = 0.0  # Move the image along the X-axis
        self.fTranslateY = 0.0  # Move the image along the Y-axis
        self.fImageRef = None  # The image itself
        self.fProperties = None  # Image properties
        self.fOrientation = (
            None  # Affine transform that ensures the image displays correctly
        )


# Create a new image from a file at the given url
# Returns None if unsuccessful.
def IICreateImage(url):
    ii = None
    # Try to create an image source to the image passed to us
    imageSrc = Quartz.CGImageSourceCreateWithURL(url, None)
    if imageSrc is not None:
        # And if we can, try to obtain the first image available
        image = Quartz.CGImageSourceCreateImageAtIndex(imageSrc, 0, None)
        if image is not None:
            # and if we could, create the ImageInfo struct with default values
            ii = ImageInfo()
            ii.fRotation = 0.0
            ii.fScaleX = 1.0
            ii.fScaleY = 1.0
            ii.fTranslateX = 0.0
            ii.fTranslateY = 0.0
            # the ImageInfo struct owns this CGImageRef now, so no need for a retain.
            ii.fImageRef = image
            # the ImageInfo struct owns this CFDictionaryRef, so no need for a retain.
            ii.fProperties = Quartz.CGImageSourceCopyPropertiesAtIndex(imageSrc, 0, None)
            # Setup the orientation transformation matrix so that the image will
            # display with the proper orientation
            IIGetOrientationTransform(ii)

    return ii


# Transforms the context based on the orientation of the image.
# This ensures the image always appears correctly when drawn.
def IIGetOrientationTransform(image):
    w = Quartz.CGImageGetWidth(image.fImageRef)
    h = Quartz.CGImageGetHeight(image.fImageRef)
    if image.fProperties is not None:
        # The Orientations listed here are mirrored from CGImageProperties.h,
        # listed under the kCGImagePropertyOrientation key.
        orientation = IIGetImageOrientation(image)
        if orientation == 1:
            # 1 = 0th row is at the top, and 0th column is on the left.
            # Orientation Normal
            image.fOrientation = Quartz.CGAffineTransformMake(
                1.0, 0.0, 0.0, 1.0, 0.0, 0.0
            )

        elif orientation == 2:
            # 2 = 0th row is at the top, and 0th column is on the right.
            # Flip Horizontal
            image.fOrientation = Quartz.CGAffineTransformMake(-1.0, 0.0, 0.0, 1.0, w, 0.0)

        elif orientation == 3:
            # 3 = 0th row is at the bottom, and 0th column is on the right.
            # Rotate 180 degrees
            image.fOrientation = Quartz.CGAffineTransformMake(-1.0, 0.0, 0.0, -1.0, w, h)

        elif orientation == 4:
            # 4 = 0th row is at the bottom, and 0th column is on the left.
            # Flip Vertical
            image.fOrientation = Quartz.CGAffineTransformMake(1.0, 0.0, 0, -1.0, 0.0, h)

        elif orientation == 5:
            # 5 = 0th row is on the left, and 0th column is the top.
            # Rotate -90 degrees and Flip Vertical
            image.fOrientation = Quartz.CGAffineTransformMake(0.0, -1.0, -1.0, 0.0, h, w)

        elif orientation == 6:
            # 6 = 0th row is on the right, and 0th column is the top.
            # Rotate 90 degrees
            image.fOrientation = Quartz.CGAffineTransformMake(0.0, -1.0, 1.0, 0.0, 0.0, w)

        elif orientation == 7:
            # 7 = 0th row is on the right, and 0th column is the bottom.
            # Rotate 90 degrees and Flip Vertical
            image.fOrientation = Quartz.CGAffineTransformMake(
                0.0, 1.0, 1.0, 0.0, 0.0, 0.0
            )

        elif orientation == 8:
            # 8 = 0th row is on the left, and 0th column is the bottom.
            # Rotate -90 degrees
            image.fOrientation = Quartz.CGAffineTransformMake(0.0, 1.0, -1.0, 0.0, h, 0.0)


# Gets the orientation of the image from the properties dictionary if available
# If the kCGImagePropertyOrientation is not available or invalid,
# then 1, the default orientation, is returned.
def IIGetImageOrientation(image):
    result = 1
    if image.fProperties is not None:
        orientation = image.fProperties.get(Quartz.kCGImagePropertyOrientation)
        if orientation is not None:
            result = orientation

    return result


# Save the given image to a file at the given url.
# Returns true if successful, false otherwise.
def IISaveImage(image, url, width, height):
    result = False

    # If there is no image, no destination, or the width/height is 0, then fail early.
    assert (
        (image is not None) and (url is not None) and (width != 0.0) and (height != 0.0)
    )

    # Try to create a jpeg image destination at the url given to us
    imageDest = Quartz.CGImageDestinationCreateWithURL(
        url, LaunchServices.kUTTypeJPEG, 1, None
    )
    if imageDest is not None:
        # And if we can, then we can start building our final image.
        # We begin by creating a CGBitmapContext to host our destination image.

        # Allocate enough space to hold our pixels
        imageData = objc.allocateBuffer(int(4 * width * height))

        # Create the bitmap context
        bitmapContext = Quartz.CGBitmapContextCreate(
            imageData,  # image data we just allocated...
            width,  # width
            height,  # height
            8,  # 8 bits per component
            4 * width,  # bytes per pixel times number of pixels wide
            Quartz.CGImageGetColorSpace(
                image.fImageRef
            ),  # use the same colorspace as the original image
            Quartz.kCGImageAlphaPremultipliedFirst,
        )  # use premultiplied alpha

        # Check that all that went well
        if bitmapContext is not None:
            # Now, we draw the image to the bitmap context
            IIDrawImageTransformed(
                image, bitmapContext, Quartz.CGRectMake(0.0, 0.0, width, height)
            )

            # We have now gotten our image data to the bitmap context, and correspondingly
            # into imageData. If we wanted to, we could look at any of the pixels of the image
            # and manipulate them in any way that we desire, but for this case, we're just
            # going to ask ImageIO to write this out to disk.

            # Obtain a CGImageRef from the bitmap context for ImageIO
            imageIOImage = Quartz.CGBitmapContextCreateImage(bitmapContext)

            # Check if we have additional properties from the original image
            if image.fProperties is not None:
                # If we do, then we want to inspect the orientation property.
                # If it exists and is not the default orientation, then we
                # want to replace that orientation in the destination file
                orientation = IIGetImageOrientation(image)
                if orientation != 1:
                    # If the orientation in the original image was not the default,
                    # then we need to replace that key in a duplicate of that dictionary
                    # and then pass that dictionary to ImageIO when adding the image.
                    prop = Cocoa.CFDictionaryCreateMutableCopy(None, 0, image.fProperties)
                    orientation = 1
                    prop[Quartz.kCGImagePropertyOrientation] = orientation

                    # And add the image with the new properties
                    Quartz.CGImageDestinationAddImage(imageDest, imageIOImage, prop)

                else:
                    # Otherwise, the image was already in the default orientation and we can
                    # just save it with the original properties.
                    Quartz.CGImageDestinationAddImage(
                        imageDest, imageIOImage, image.fProperties
                    )

            else:
                # If we don't, then just add the image without properties
                Quartz.CGImageDestinationAddImage(imageDest, imageIOImage, None)

            del bitmapContext

        # Finalize the image destination
        result = Quartz.CGImageDestinationFinalize(imageDest)
        del imageDest

    return result


# Applies the transformations specified in the ImageInfo struct without drawing the actual image
def IIApplyTransformation(image, context, bounds):
    if image is not None:
        # Whenever you do multiple CTM changes, you have to be very careful with
        # order.  Changing the order of your CTM changes changes the outcome of
        # the drawing operation. For example, if you scale a context by 2.0 along
        # the x-axis, and then translate the context by 10.0 along the x-axis,
        # then you will see your drawing will be in a different position than if
        # you had done the operations in the opposite order.
        #
        # Our intent with this operation is that we want to change the location
        # from which we start drawing (translation), then rotate our axies so
        # that our image appears at an angle (rotation), and finally
        # scale our axies so that our image has a different size (scale).
        # Changing the order of operations will markedly change the results.
        IITranslateContext(image, context)
        IIRotateContext(image, context, bounds)
        IIScaleContext(image, context, bounds)


# Draw the image to the given context centered inside the given bounds
def IIDrawImage(image, context, bounds):
    imageRect = Cocoa.NSRect()
    if image is not None and context is not None:
        # Setup the image rect so that the image fills it's natural boundaries
        # in the base coordinate system.
        imageRect.origin.x = 0.0
        imageRect.origin.y = 0.0
        imageRect.size.width = Quartz.CGImageGetWidth(image.fImageRef)
        imageRect.size.height = Quartz.CGImageGetHeight(image.fImageRef)

        # Obtain the orientation matrix for this image
        ctm = image.fOrientation

        # Before we can apply the orientation matrix, we need to translate the
        # coordinate system so the center of the rectangle matces the center of
        # the image.
        if image.fProperties is None or IIGetImageOrientation(image) < 5:
            # For orientations 1-4, the images are unrotated, so the width and
            # height of the base image can be used as the width and height of
            # the coordinate translation calculation.
            Quartz.CGContextTranslateCTM(
                context,
                math.floor((bounds.size.width - imageRect.size.width) / 2.0),
                math.floor((bounds.size.height - imageRect.size.height) / 2.0),
            )

        else:
            # For orientations 5-8, the images are rotated 90 or -90 degrees,
            # so we need to use the image width in place of the height and
            # vice versa.
            Quartz.CGContextTranslateCTM(
                context,
                math.floor((bounds.size.width - imageRect.size.height) / 2.0),
                math.floor((bounds.size.height - imageRect.size.width) / 2.0),
            )

        # Finally, orient the context so that the image draws naturally.
        Quartz.CGContextConcatCTM(context, ctm)

        # And draw the image.
        Quartz.CGContextDrawImage(context, imageRect, image.fImageRef)


# Rotates the context around the center point of the given bounds
def IIRotateContext(image, context, bounds):
    # First we translate the context such that the 0,0 location is at the center of the bounds
    Quartz.CGContextTranslateCTM(
        context, bounds.size.width / 2.0, bounds.size.height / 2.0
    )

    # Then we rotate the context, converting our angle from degrees to radians
    Quartz.CGContextRotateCTM(context, image.fRotation * math.pi / 180.0)

    # Finally we have to restore the center position
    Quartz.CGContextTranslateCTM(
        context, -bounds.size.width / 2.0, -bounds.size.height / 2.0
    )


# Scale the context around the center point of the given bounds
def IIScaleContext(image, context, bounds):
    # First we translate the context such that the 0,0 location is at the center of the bounds
    Quartz.CGContextTranslateCTM(
        context, bounds.size.width / 2.0, bounds.size.height / 2.0
    )

    # Next we scale the context to the size that we want
    Quartz.CGContextScaleCTM(context, image.fScaleX, image.fScaleY)

    # Finally we have to restore the center position
    Quartz.CGContextTranslateCTM(
        context, -bounds.size.width / 2.0, -bounds.size.height / 2.0
    )


# Translate the context
def IITranslateContext(image, context):
    # Translation is easy, just translate.
    Quartz.CGContextTranslateCTM(context, image.fTranslateX, image.fTranslateY)


# Draw the image to the given context centered inside the given bounds with
# the transformation info. The CTM of the context is unchanged after this call
def IIDrawImageTransformed(image, context, bounds):
    # We save the current graphics state so as to not disrupt it for the caller.
    Quartz.CGContextSaveGState(context)

    # Apply the transformation
    IIApplyTransformation(image, context, bounds)

    # Draw the image centered in the context
    IIDrawImage(image, context, bounds)

    # Restore our original graphics state.
    Quartz.CGContextRestoreGState(context)


# Release the ImageInfo struct and other associated data
# you should not refer to the reference after this call
# This function is None safe.
def IIRelease(image):
    pass
