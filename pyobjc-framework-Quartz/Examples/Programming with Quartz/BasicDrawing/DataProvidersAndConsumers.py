import os
import sys

import Cocoa
import Quartz


def createDataProviderFromPathName(path):
    # Create a CFURL for the supplied file system path.
    url = Cocoa.CFURLCreateWithFileSystemPath(
        None, path, Cocoa.kCFURLPOSIXPathStyle, False
    )
    if url is None:
        print("Couldn't create url!")
        return None

    # Create a Quartz data provider for the URL.
    dataProvider = Quartz.CGDataProviderCreateWithURL(url)
    if dataProvider is None:
        print("Couldn't create data provider!")
        return None

    return dataProvider


def createRGBRampDataProvider():
    width = 256
    height = 256
    imageDataSize = width * height * 3

    dataP = bytearray(imageDataSize)

    #    Build an image that is RGB 24 bits per sample. This is a ramp
    #    where the red component value increases in red from left to
    #    right and the green component increases from top to bottom.
    #
    idx = 0
    for g in range(height):
        for r in range(width):
            dataP[idx] = chr(r) if sys.version_info[0] == 2 else r
            dataP[idx + 1] = chr(g) if sys.version_info[0] == 2 else g
            dataP[idx + 2] = "\0" if sys.version_info[0] == 2 else 0
            idx += 3

    # Once this data provider is created, the data associated
    # with dataP MUST be available until Quartz calls the data
    # releaser function 'rgbReleaseRampData'.
    dataProvider = Quartz.CGDataProviderCreateWithData(None, dataP, imageDataSize, None)
    return dataProvider


class MyImageDataInfo:
    fp = None
    totalBytesRead = 0
    skippedBytes = 0
    numRewinds = 0


def getBytesSequentialAccessDP(data, buffer, count):
    buf = data.fp.read(count)
    buffer[: len(buf)] = buf
    data.totalBytesRead += len(buf)
    return len(buf), buffer


def skipBytesSequentialAccessDP(data, count):
    try:
        data.fp.seek(count, os.SEEK_CUR)
        data.skippedBytes += count

    except OSError as msg:
        print("Couldn't seek %d bytes because of %s" % (count, msg))


def rewindSequentialAccessDP(data):
    # Rewind the beginning of the data.
    data.fp.seek(0, 0)
    data.numRewinds += 1


def releaseSequentialAccessDP(data):
    if data is not None:
        print(
            "read %d bytes, skipped %d bytes, rewind called %d times"
            % (data.totalBytesRead, data.skippedBytes, data.numRewinds)
        )
        data.fp.close()


def createSequentialAccessDPForURL(url):
    success, pathString = Cocoa.CFURLGetFileSystemRepresentation(url, True, None, 1024)
    pathString = pathString.rstrip(b"\0")
    if not success:
        print("Couldn't get the path name C string!")
        return None

    fp = open(pathString, "rb")
    if fp is None:
        print(f"Couldn't open path to file {pathString}!")
        return None

    imageDataInfoP = MyImageDataInfo()
    imageDataInfoP.fp = fp

    provider = Quartz.CGDataProviderCreate(
        imageDataInfoP,
        (
            getBytesSequentialAccessDP,
            skipBytesSequentialAccessDP,
            rewindSequentialAccessDP,
            releaseSequentialAccessDP,
        ),
    )
    if provider is None:
        print("Couldn't create data provider!")
        # Release the info data and cleanup.
        releaseSequentialAccessDP(imageDataInfoP)
        return None

    return provider


def getBytesGrayRampDirectAccess(info, buffer, offset, count):
    # This computes a linear gray ramp that is 256 samples wide and
    # 1 sample high. The ith byte in the image is the sample
    # value i. This produces a gray ramp that goes from 0 (black) to
    # FF (white).
    idx = 0

    # This data provider provides 256 bytes total. If Quartz
    # requests more data than is available, only return
    # the available data.
    if (offset + count) > 256:
        count = 256 - offset

    for i in range(offset, offset + count):
        buffer[idx] = chr(i) if sys.version_info[0] == 2 else i
        idx += 1

    return count, buffer


def createGrayRampDirectAccessDP():
    provider = Quartz.CGDataProviderCreateDirectAccess(
        None, 256, (None, None, getBytesGrayRampDirectAccess, None)
    )
    if provider is None:
        print("Couldn't create data provider!")
        return None

    return provider


# This only builds on Tiger and later.
def myCGDataProviderCreateWithCFData(data):
    # If the CFData object passed in is None, this code returns
    # a None data provider.
    if data is None:
        return None

    # Test to see if the Quartz version is available and if so, use it.

    # XXX: force the replacement code to be used
    # if hasattr(Quartz, 'CGDataProviderCreateWithCFData'):
    #    return CGDataProviderCreateWithCFData(data)

    dataSize = Cocoa.CFDataGetLength(data)
    provider = Quartz.CGDataProviderCreateWithData(data, data, dataSize, None)
    return provider


def createDataConsumerFromPathName(path):
    # Create a CFURL for the supplied file system path.
    url = Cocoa.CFURLCreateWithFileSystemPath(
        None, path, Cocoa.kCFURLPOSIXPathStyle, False
    )
    if url is None:
        print("Couldn't create url!")
        return None
    # Create a Quartz data provider for the URL.
    dataConsumer = Quartz.CGDataConsumerCreateWithURL(url)
    if dataConsumer is None:
        print("Couldn't create data consumer!")
        return None

    return dataConsumer


def myCFDataConsumerPutBytes(data, buffer, count):
    # Append 'count' bytes from 'buffer' to the CFData
    # object 'data'.
    Cocoa.CFDataAppendBytes(data, buffer, count)
    return count


# This only builds on Tiger and later.
def myCGDataConsumerCreateWithCFData(data):
    # If the CFData object passed in is None, this code returns
    # a None data consumer.
    if data is None:
        return None

    # Test to see if the Quartz version is available.

    # XXX: force the replacement code to be used:
    # if hasattr(Quartz, 'CGDataConsumerCreateWithCFData'):
    #    return CGDataConsumerCreateWithCFData(data)

    consumer = Quartz.CGDataConsumerCreate(data, (myCFDataConsumerPutBytes, None))
    return consumer
