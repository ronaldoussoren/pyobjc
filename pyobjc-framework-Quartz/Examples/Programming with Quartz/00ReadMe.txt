The samples in this directory are transcriptions of the 
examples in the book "Programming with Quartz" (ISBN: 978-0-12-369473-7), except for code
that relies on Carbon APIs like HIToolbox.

The APIs in the folder "python" use the pre-Leopard bindings to CoreGraphics, which are deprecated at best.

The original Readme file:

These directories contain the sample source code for the Quartz Book. Note that the source files are formatted
so that the tab indentation looks best in Xcode or BBEdit with 4 spaces per tab. 

CocoaDrawingShell:
Contains source for building the sample application created in Chapter 3.

CarbonDrawingShell:
Contains source for building the sample application created in Chapter 4.

BasicDrawing:
An application that contains the bulk of the sample code presented in the book. The directory BasicDrawing.cocoa contains an Xcode project and Cocoa specific source code for building a Cocoa version of the application. The directory BasicDrawing.carbon contains an Xcode project and Carbon specific source code for building a Carbon version of the application. The directory CommonCode contains the C code that is common to both the Cocoa and Carbon versions of the application.

PDFDraw:
This is a basic application that contains the code from Chapters 13 and 16 for opening and displaying PDF, PostScript, and EPS documents. This example is a Carbon application that uses the QDBeginCGContext/QDEndCGContext routines discussed in Chapter 4 as an alternate to using HIView. The user interface here is rudimentary; the focus of this sample is on the drawing of PDF documents and conversion of PostScript and EPS files into a PDF document that can be displayed like any other PDF file.

CreatePDFDocument:
This contains the sample code from Chapter 14 for creating new PDF documents, including those that contain links. This sample also demonstrates use of the new to Tiger API for creating encrypted PDF documents that have restricted permissions.

ConfidentialStamper:
Contains the source code for a tool that takes an input PDF document and "stamps" a second PDF document onto each page of the input file, creating a new PDF document.

ParsePageContents:
Contains the source code for a tool that takes an input PDF document and "stamps" a second PDF document onto each page of the input file, creating a new PDF document.

PSConverterTool:
Contains source code to a command line tool that uses the CGPSConverter API for converting a PostScript or EPS file into a PDF output file.

python:
Contains the sample Python scripts from Chapter 18. These are:

alpharects.py, which creates a PDF document containing the alpha rectangle drawing from Chapter 2.
pdftojpg.py, which takes an input PDF document and creates a JPEG output file for each page of the input document.
Stamp PDF with "Confidential".py, which is a PDF workflow script that can be installed in the 
	~/Library/PDF Services or /Library/PDF Services directory, adding a workflow item to the 
	workflow menu in the Print dialog. Choosing this workflow item stamps the word 
	"Confidential" onto each page of the PDF document being printed.


