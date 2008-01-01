from Cocoa import *
from SearchKit import *

import os

class AppController (NSObject):

    myWindow = objc.IBOutlet()

    selectDirectoryButton = objc.IBOutlet()
    directoryTextField = objc.IBOutlet()

    numberOfDocumentsTextField = objc.IBOutlet()
    numberOfTermsTextField = objc.IBOutlet()

    buildIndexButton = objc.IBOutlet()

    searchField = objc.IBOutlet()
    searchResultsTextView = objc.IBOutlet()
        
    directoryToIndex = objc.ivar()
    myIndex = objc.ivar()


    def awakeFromNib(self):
        # set our default directory to index to be our home directory
        self.directoryToIndex = NSHomeDirectory()
        # go ahead and put that value into the UI right on wake-up
        self.directoryTextField.setStringValue_(self.directoryToIndex)
        
        # tell the search field cell that we only want to send
        # search requests (the associated action) on pressing return
        searchCell = self.searchField.cell()
        searchCell.setSendsWholeSearchString_(True)
        # the alternative (False) would be to get a search initiated
        # with every keystroke - which may be what is desired in a 
        # prefix style search (like iTunes).


    @objc.IBAction
    def chooseDirectory_(self, sender):
        # we are setting up an NSOpenPanel to select only a directory and then
        # we will use that directory to choose where to place our index file and
        # which files we'll read in to make searchable.
        op = NSOpenPanel.openPanel()
        op.setCanChooseDirectories_(True)
        op.setCanChooseFiles_(False)
        op.setResolvesAliases_(True)
        op.setAllowsMultipleSelection_(False)
        result = op.runModalForDirectory_file_types_(None, None, None)
        if result == NSOKButton:
            self.directoryToIndex = op.filename()
            self.directoryTextField.setStringValue_(self.directoryToIndex)

    @objc.IBAction
    def buildIndex_(self, sender):
        # we will need an NSFileManager object to do various checking of files.
        fm = NSFileManager.defaultManager()
        
        # you don't have to provide the index with a name, but we will...
        indexName = "My Arbitrary Index Name"
        # when you build an index on disk, you need to give it a file:# URL
        # So we pick the directory that's been chosen and append "/myindex" 
        # onto it
        indexFile = os.path.join(self.directoryToIndex, "myindex")
        # and build an NSURL from that
        fileUrlToIndex = NSURL.fileURLWithPath_(indexFile)
        
        # When indexing documents, there's a number of index specific 
        # considerations that can be applied with search kit. To set any of 
        # them manually, we first need to create a Dictionary in which to hold 
        # them.
        analysisDict = {}
        # Then we can set things like the language to expect
        # note that the constants associated with these attributes are 
        # CFStringRef's so we cast them to NSString to make it easy to insert 
        # into the dictionary.
        # We could also do this all in procedural C with the native 
        # CoreFoundation components, but I find this is significantly easier
        # - both to write and  to understand.
        analysisDict[kSKLanguageTypes] = u"en"
        # another example of setting an attribute, in this case the minimum term
        # length
        analysisDict[kSKMinTermLength] = 2
        # when we hand this dictionary into the function to create the index, we
        # simply cast it back to a CFDictionaryRef and everything just nicely 
        # moves with it. This toll-free bridging concept is so handy!
        
        if fm.fileExistsAtPath_(indexFile):
            # our index file already exists... if we try to create one anyone, 
            # the function will silently fail. So let's just be sure and 
            # delete it. in a proper function, we would recognize it already 
            # exists and attmept to open it for editing rather than recreate 
            # the whole thing.
            fm.removeFileAtPath_handler_(indexFile, None)

        # the function to create the on-disk index
        self.myIndex = SKIndexCreateWithURL( 
                                        # the file:# URL of where to place the
                                        # index file
                                        fileUrlToIndex,
                                        # a name for the index (this may be None)
                                        indexName,
                                        # the type of index
                                        kSKIndexInverted,
                                        # and our index attributes dictionary
                                        analysisDict)
        # note that the above function call will silently fail if you give it a
        # directory and not a file... or if the index file already exists
        
        if self.myIndex is None:
            # we shouldn't get here...
            NSLog("TROUBLE: index is None")
            return
        
        # display information about our newly created and completely blank index
        self.displayIndexInformation()

        # before we get into the meat of reading in these files, we need to tell
        # the Search Kit to load the default extractor plugins so that the 
        # SearchKit can find the bits it needs to from the files. In 
        # MacOS 10.3, the only plugins supported are the default plugins, 
        # which include processing for plaintext, PDF, HTML, RTF, and 
        # Microsoft Word documents.
        SKLoadDefaultExtractorPlugIns()

        # we're just going to get a "short list". You could alternately use the
        # NSDirectoryEnumerator class to recursively descend through all the 
        # files under a directory, and you would probably want to do it in 
        # some other thread, updating a progress bar or such to indicate 
        # something was happening. It can take a while (for example) to 
        # process every file in your home directory and beneath.

        listOfFiles = fm.directoryContentsAtPath_(self.directoryToIndex)
        for aFile in listOfFiles:
            # the particular function we'll use like to get an NSURL
            # object, so we'll create one and pass it over.
            
            # create the URL with the filename
            fileURL = NSURL.fileURLWithPath_(
                    os.path.join(self.directoryToIndex, aFile))
            
            # invoke a helper method to add this file into our index
            self.addDocumentToIndex_(fileURL)
        
        # once all the files have been added to the index, it's very important 
        # to flush the data down to disk. Without this step, the data resides 
        # in memory but isn't useful for searching and won't respond with the 
        # correct information about the index (number of documents, number of 
        # terms, etc).
        if not SKIndexFlush(self.myIndex):
            NSLog("A problem was encountered flushing the index to disk.")

        NSLog("flushed index to disk")

        # update the index information
        self.displayIndexInformation()

    @objc.IBAction
    def search_(self, sender):
        # do some sanity checking to make sure we're not going to run into some
        # memory exception because we never initialized our SearchKit index 
        # properly
        if self.myIndex is None:
            msg = "No index has been created to against which to search."
            NSLog(msg)
            self.searchResultsTextView.setString_(msg)
            return
        
        # Since this is just an example, I am going to be lazy and just report
        # the results of our search into a text field. I'm creating an
        # NSMutableString to build up what will appear there.
        textOfResults = ''
        
        searchQuery = sender.stringValue()
        textOfResults += "Searching for:"
        textOfResults += searchQuery
        textOfResults += "\n"
        
        # to do a search, we need a SearchGroup
        # so we start by creating an array of 1 item (our search index)
        searchArray = [self.myIndex]
        
        # and then we immediately turn around and use that to create 
        # a Search Kit Search Group reference.
        searchgroup = SKSearchGroupCreate(searchArray)
        
        # now that we have a searchgroup, we can request a result set
        # from it with our search terms.
        searchResults = SKSearchCreate(self.myIndex, searchQuery, kSKSearchRanked)

        if searchResults is None:
            msg = "Search function failed"
            NSLog(msg)
            self.searchResultsTextView.setString_(msg)
            return

        # now to go through the results, we can create an array for each 
        # SearchKit document and another for the scores, and then populate 
        # them from the SearchResults
        busy, outDocumentIDsArray, scoresArray, resultCount=  SKSearchFindMatches(searchResults, # the search result set
                                          10,               
                                          None,      # an array of SKDocumentID
                                          None,      # an array of scores
                                          1.0,       # max 1 sec
                                          None       # outFoundcount
                                          )
        if busy:
            textOfResults += "%d Results Found (still busy)\n"%(resultCount,)
        else:
            textOfResults += "%d Results Found\n"%(resultCount,)

        assert resultCount == len(scoresArray)

        # iterate over the results and tell the NSTextView what we found
        for score, hitID in zip(scoresArray, outDocumentIDsArray):
            hit = SKIndexCopyDocumentForDocumentID(self.myIndex, hitID)
            if hit is None:
                continue

            documentName = SKDocumentGetName(hit)

            textOfResults += "Score: %f ==> %s\n"%(score, documentName)

        self.searchResultsTextView.setString_(textOfResults)

    def addDocumentToIndex_(self, fileURL):
        # do some sanity checking to make sure we're not going to run into some
        # memory exception because we never initialized our SearchKit index 
        # properly
        if self.myIndex is None:
            NSLog("myIndex is None - not processing %@",
                    fileURL)
            return
 
        NSLog("Processing %@", fileURL.absoluteString())
        # create the Search Kit document object
        # note that this method only accepts file:# style URL's
        aDocument = SKDocumentCreateWithURL(fileURL)
        
        # if you wanted to watch them process in, just uncomment the following
        # 2 lines.
        #NSLog("Name: %@", SKDocumentGetName(aDocument))
        #NSLog("Scheme: %@", SKDocumentGetSchemeName(aDocument))
            
        # add the document to the index
        if not SKIndexAddDocument(self.myIndex, # a reference ot the index added to 
                                 aDocument, # the document we want to add
                                 None, # this could be a mime type hint in the form
                                      # of a CFStringRef
                                  1):   # a boolean value indicating the document
                                      # can be overwritten
            NSLog("There was a problem adding %@", fileURL)


    def displayIndexInformation(self):
        if self.myIndex is not None:
            # get the number of documents in the index
            numberOfDocuments = SKIndexGetDocumentCount(self.myIndex)
            # place it into the text field
            self.numberOfDocumentsTextField.setIntValue_(numberOfDocuments)
        
            # get the number of terms in the index
            maxTerm = SKIndexGetMaximumTermID(self.myIndex)
            # place it into the text field
            self.numberOfTermsTextField.setIntValue_(maxTerm)

        else:
            self.numberOfDocumentsTextField.setStringValue_('N/A')
            self.numberOfTermsTextField.setStringValue_('N/A')
