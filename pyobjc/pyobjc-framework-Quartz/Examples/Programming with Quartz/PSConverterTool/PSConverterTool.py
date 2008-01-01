from CoreFoundation import *
from Quartz import *

import sys
import objc

DEBUG=0

class MyConverterData (object):
    def __init__(self):
        self.doProgress = False
        self.abortConverter = False
        self.outStatusFile = sys.stdout
        self.converter = None

# Converter callbacks

def begin_document_callback(info):
    print >>info.outStatusFile, "\nBegin Document\n"

def end_document_callback(info, success):
    if success:
        success = "success"
    else:
        success = "failed"

    print >>info.outStatusFile, "\nEnd Document: %s\n"%(success,)

def begin_page_callback(info, pageno,  page_info):
    print >>info.outStatusFile, "\nBeginning page %d\n"%(pageno,)
    if DEBUG:
        if page_info is not None:
            CFShow(page_info)


def end_page_callback(info, pageno, page_info):
    print >>info.outStatusFile, "\nEnd page %d\n"%(pageno,)
    if DEBUG:
        if page_info is not None:
            CFShow(page_info)

def progress_callback(info):
    if info.doProgress:
        print >>info.outStatusFile.write(".")
        info.outStatusFile.flush()
    
    # Here would be a callout to code that
    # would conceivably return whether to abort
    # the conversion process.

    #UpdateStatus(converterDataP);
    
    if info.abortConverter:
	CGPSConverterAbort(info.converter);
        print >>info.outStatusFile, "ABORTED!"


def message_callback(info, cfmessage):
    # Extract an ASCII version of the message. Typically
    # these messages are similar to those obtained from
    # any PostScript interpreter. Messages of the form
    # "%%[ Error: undefined; OffendingCommand: bummer ]%%"
    # are PostScript error messages and are the typical
    # reason a conversion job fails.

    print >>info.outStatusFile, "\nMessage: %s"%(
            message)

#  Given an input URL and a destination output URL, convert
#    an input PS or EPS file to an output PDF file. This conversion
#    can be time intensive and perhaps should be performed on
#    a secondary thread or by another process. */
def convertPStoPDF(inputPSURL, outPDFURL):
    provider = CGDataProviderCreateWithURL(inputPSURL);
    consumer = CGDataConsumerCreateWithURL(outPDFURL);

    if provider is None or consumer is None:
        if provider is None:
            print >>sys.stderr, "Couldn't create provider"
	    
        if consumer is None:
            print >>sys.stderr, "Couldn't create consumer"
	    
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
    myConverterData.converter = CGPSConverterCreate(myConverterData, (
        begin_document_callback,
        end_document_callback,
        begin_page_callback,
        end_page_callback,
        progress_callback,
        message_callback,
        None,   # no release_info_callback 
        ), None)

    if myConverterData.converter is None:
	print >>sys.stderr, "Couldn't create converter object!"
	return False

    # There are no conversion options so the options
    # dictionary for the conversion is None.
    success = CGPSConverterConvert(myConverterData.converter, 
		    provider, consumer, None)
    if not success:
        print >>sys.stderr, "Conversion failed!"

    # There is no CGPSConverterRelease function. Since
    # a CGPSConverter object is a CF object, use CFRelease
    # instead.
    return success;

def main(args = None):
    if args is None:
        args = sys.argv

    if len(args) != 3:
	print >>sys.stderr, "Usage: %s inputfile outputfile."%(args[0],)
	return 0

    # Create the data provider and data consumer.
    inputURL = CFURLCreateFromFileSystemRepresentation(None, 
			args[1], len(args[1]), False)

    outputURL = CFURLCreateFromFileSystemRepresentation(None, 
			args[2], len(args[2]), False)

    if inputURL is not None and outputURL is not None:
	convertPStoPDF(inputURL, outputURL)

    return 0


if __name__ == "__main__":
    sys.exit(main())
