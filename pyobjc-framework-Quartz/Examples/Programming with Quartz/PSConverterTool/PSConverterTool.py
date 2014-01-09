from __future__ import print_function
import Cocoa
import Quartz

import sys
import objc

DEBUG=1

class MyConverterData (object):
    def __init__(self):
        self.doProgress = False
        self.abortConverter = False
        self.outStatusFile = sys.stdout
        self.converter = None

# Converter callbacks

def begin_document_callback(info):
    print("\nBegin Document\n", file=info.outStatusFile)

def end_document_callback(info, success):
    if success:
        success = "success"
    else:
        success = "failed"

    print("\nEnd Document: %s\n"%(success,), file=info.outStatusFile)

def begin_page_callback(info, pageno,  page_info):
    print("\nBeginning page %d\n"%(pageno,), file=info.outStatusFile)
    if DEBUG:
        if page_info is not None:
            Cocoa.CFShow(page_info)


def end_page_callback(info, pageno, page_info):
    print("\nEnd page %d\n"%(pageno,), file=info.outStatusFile)
    if DEBUG:
        if page_info is not None:
            Cocoa.CFShow(page_info)

def progress_callback(info):
    if info.doProgress:
        info.outStatusFile.write(".")
        info.outStatusFile.flush()

    # Here would be a callout to code that
    # would conceivably return whether to abort
    # the conversion process.

    #UpdateStatus(converterDataP);

    if info.abortConverter:
        Quartz.CGPSConverterAbort(info.converter);
        print("ABORTED!", file=info.outStatusFile)


def message_callback(info, cfmessage):
    # Extract an ASCII version of the message. Typically
    # these messages are similar to those obtained from
    # any PostScript interpreter. Messages of the form
    # "%%[ Error: undefined; OffendingCommand: bummer ]%%"
    # are PostScript error messages and are the typical
    # reason a conversion job fails.

    print("\nMessage: %s"%(
            cfmessage), file=info.outStatusFile)

#  Given an input URL and a destination output URL, convert
#    an input PS or EPS file to an output PDF file. This conversion
#    can be time intensive and perhaps should be performed on
#    a secondary thread or by another process. */
def convertPStoPDF(inputPSURL, outPDFURL):
    provider = Quartz.CGDataProviderCreateWithURL(inputPSURL);
    consumer = Quartz.CGDataConsumerCreateWithURL(outPDFURL);

    if provider is None or consumer is None:
        if provider is None:
            print("Couldn't create provider")

        if consumer is None:
            print("Couldn't create consumer")

        return False

    # Setup the info data for the callbacks to
    # do progress reporting, set the initial state
    # of the abort flag to false and use stdout
    # as the file to write status and other information.
    myConverterData = MyConverterData()
    myConverterData.doProgress = True
    myConverterData.abortConverter = False
    myConverterData.outStatusFile = sys.stdout

    # Create a converter object with myConverterData as the
    # info parameter and our callbacks as the set of callbacks
    # to use for the conversion. There are no converter options
    # defined as of Tiger so the options dictionary passed is None.
    myConverterData.converter = Quartz.CGPSConverterCreate(myConverterData, (
        begin_document_callback,
        end_document_callback,
        begin_page_callback,
        end_page_callback,
        progress_callback,
        message_callback,
        None,   # no release_info_callback
        ), None)

    if myConverterData.converter is None:
        print("Couldn't create converter object!")
        return False

    # There are no conversion options so the options
    # dictionary for the conversion is None.
    success = Quartz.CGPSConverterConvert(myConverterData.converter,
                    provider, consumer, None)
    if not success:
        print("Conversion failed!")

    # There is no CGPSConverterRelease function. Since
    # a CGPSConverter object is a CF object, use CFRelease
    # instead.
    return success;

def main(args = None):
    if args is None:
        args = sys.argv

    if len(args) != 3:
        print("Usage: %s inputfile outputfile."%(args[0],))
        return 0

    infile = args[1]
    outfile = args[2]

    if not isinstance(infile, bytes):
        infile = infile.encode('utf-8')

    if not isinstance(outfile, bytes):
        outfile = outfile.encode('utf-8')

    # Create the data provider and data consumer.
    inputURL = Cocoa.CFURLCreateFromFileSystemRepresentation(None,
                        infile, len(infile), False)

    outputURL = Cocoa.CFURLCreateFromFileSystemRepresentation(None,
                        outfile, len(outfile), False)

    if inputURL is not None and outputURL is not None:
        convertPStoPDF(inputURL, outputURL)

    return 0


if __name__ == "__main__":
    sys.exit(main())
