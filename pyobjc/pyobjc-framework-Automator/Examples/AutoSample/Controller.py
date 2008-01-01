from Cocoa import *
from Automator import *

class Controller (NSObject):
    # interface builder variables 
    myWindow = objc.IBOutlet()
    workflowView = objc.IBOutlet()
    workflowTable = objc.IBOutlet()
    workflowController = objc.IBOutlet()
    tableContent = objc.IBOutlet()
    
    # instance variables
    _workflows = objc.ivar()
    _runningWorkflow = objc.ivar.bool()

    def workflows(self):
        return self._workflows

    def setWorkflows_(self, value):
        self._workflows = value

    def runningWorkflow(self):
        return self._runningWorkflow

    def setRunningWorkflow_(self, value):
        self._runningWorkflow = value

    # display the selected workflow.
    def displaySelectedWorkflow(self):
        # get the selected row from the workflow table. 
        theRow = self.workflowTable.selectedRow()

        # if there is a selection and we are not running
        # the selected workflow, then we can display the
        # workflow selected in the list.
        if theRow != -1 and not self._.runningWorkflow:
            # retrieve the first item in the selection
            selectedEntry = self.tableContent.arrangedObjects()[theRow]

            # retrieve the selected application from our list of applications.
            selectedWorkflow = selectedEntry['workflow']

            # ask the AMWorkflowController to display the selected workflow
            self.workflowController.setWorkflow_(selectedWorkflow)

            # set the window title
            self.myWindow.setTitle_(selectedEntry['name'])

            return True

        else:
            return False

    # awakeFromNib is called after our MainMenu.nib file has been loaded
    # and the main window is ready for use.  Here, we finish initializing
    # our content for display in the window. 
    def awakeFromNib(self):
        # we're only using the AMWorkflowView for display
        self.workflowView.setEditable_(False)

        # set up the data for NSTableView.  We'll store a list of
        # NSDictonary records each containing some information about the
        # workflow.  We'll display the name of the workflow's file in the
        # window. 

        # set up an array for storing the table information 
        theWorkflows = NSMutableArray.alloc().initWithCapacity_(20)

        # retrieve a list of all of the workflows stored in the application's
        # resourced folder.
        workflowPaths = NSBundle.mainBundle().pathsForResourcesOfType_inDirectory_(
                "workflow", "workflows")

        # iterate through the paths, adding them to our table information
        # as we go. 
        for nthWorkflowPath in workflowPaths:
            wfError = None

            # convert the path into an URL 
            nthWorkflowURL = NSURL.fileURLWithPath_isDirectory_(nthWorkflowPath, False)

            # allocate and initialize the workflow
            nthWorkflow, wfError = AMWorkflow.alloc().initWithContentsOfURL_error_(nthWorkflowURL, None)

            if nthWorkflow:
                # calculate the file name without path or extension
                nthFileName = nthWorkflowPath.componentsSeparatedByString_("/")[-1]
                nthDisplayName = nthFileName[:-9]

                # add the workflow to the list
                theWorkflows.append(dict(
                        name=nthDisplayName,
                        path=nthWorkflowPath,
                        workflow=nthWorkflow,
                    ))

        # set the workflows
        self._.workflows = theWorkflows

        # if there are any workflows in the list, then select and display the first one */
        if len(self._.workflows):
            self.workflowTable.selectRowIndexes_byExtendingSelection_(
                NSIndexSet.indexSetWithIndex_(0), False)
            self.displaySelectedWorkflow()


    # NSApplication delegate method - for convenience. We have set the
    # File's Owner's delegate to our Controller object in the MainMenu.nib file.
    def applicationShouldTerminateAfterLastWindowClosed_(self, sender):
        return True

    # NSTableView delegate methods.
    # We have set our controller object as the NSTableView's delegate in the MainMenu.nib file. 

    # selectionShouldChangeInTableView: is called when the user has clicked in the
    # table view in a way that will cause the selection to change.  This method allows us
    # to decide if we would like to allow the selection to change and the response
    # we return depends on if we are running a selection - we don't allow the selection
    # to change while a workflow is running.
    def selectionShouldChangeInTableView_(self, tableView):
        # if the current selected workflow is running, don't change the selection.
        if self._.runningWorkflow:
            # display an alert explaining why the selection cannot be changed.

            # get the name of the action that is running now.
            selectedWorkflow = self.tableContent.arrangedObjects()[self.workflowTable.selectedRow()]['name']

            # display a modal sheet explaining why the selection cannot be changed.
            NSBeginInformationalAlertSheet(
                u"The '%s' action is running."%(selectedWorkflow,),
                u"OK", None, None, self.myWindow, None, None, None, None,
                u"You cannot select another action until the '%s' action has finished running."%(
                    selectedWorkflow)
            )

        # return true only if we are not in the middle of running an action.
        return not self._.runningWorkflow;

    # tableViewSelectionIsChanging: is called after the selection has changed.  All there
    # is to do here is update the workflow displayed in the AMWorkflowView to show the newly
    # selected workflow.
    def tableViewSelectionIsChanging_(self, notification):
        self.displaySelectedWorkflow()

    # AMWorkflowController delegate methods.  In these routines we adjust the
    # value of our runningWorkflow property.  Key value bindings to this property
    # defined in our interface file take care of enabling/disabling the run/stop buttons,
    # and displaying the progress bar.
    def workflowControllerWillRun_(self, controller):
        self._.runningWorkflow = True

    def workflowControllerDidRun_(self, controller):
        self._.runningWorkflow = False

    def workflowControllerDidStop_(self, controller):
        self._.runningWorkflow = False

