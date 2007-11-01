from Cocoa import *
from Quartz import *

# APPLICATION DATA STORAGE NOTES:
# - This application uses a simple data storage as an array of entries, 
#   each containing two attributes: a label and a value
# - The array is represented as a NSMutableArray, the entries as 
#   NSMutableDictionaries, the label as a NSString with the "label" key and 
#   the value as a NSNumber with the "value" key
#
#
# QUARTZ COMPOSER COMPOSITION NOTES:
# - The enclosed Quartz Composer composition renders a 3D bars chart and is 
#   loaded on the QCView in the application's window
# - This composition has three input parameters:
#   * "Data": the data to display by the chart which must be formatted as a 
#     NSArray of NSDictionaries, each NSDictionary containing "label" / NSString
#     and "value" / NSNumber value-key pairs
#   * "Scale": a NSNumber used to scale the chart bars
#   * "Spacing": a NSNumber indicating the extra spacing between the chart bars
# - The "Data" and "Scale" input parameters are set programmatically while the 
#   "Spacing" is set directly from the UI through Cocoa bindings
# - Note that this composition is quite simple and has the following 
#   limitations:
#   * it may have rendering artifacts when looking at the chart from some angles
#   * it does not support negative values
#   * labels are not truncated if too long
# - Basically, the composition performs the following:
#   * renders a background gradient
#   * draws three planes on the X, Y and Z axes
#   * uses an Iterator patch to loop on the chart data, which is available as 
#     a Structure, and for each member, retrieves the label and value, then 
#     draws them
#   * the chart rendering is enclosed into a Camera macro patch used to center 
#     it in the view
#   * the Camera macro patch is itself enclosed into a TrackBall macro patch 
#     so that the user can rotate the chart with the mouse
#   * the TrackBall macro patch is itself enclosed into a Lighting macro patch 
#     so that the chart is lighted
# - This composition makes uses of transparency for a nicer effect, but 
#   neither OpenGL nor Quartz Composer handle automatically proper rendering 
#   of mixed opaque and transparent 3D objects
# - A simple, but not fail-proof, algorithm to render opaque and transparent 
#   3D objects is to: 
#   * render opaque objects first with depth testing set to "Read / Write"
#   * render transparent objects with depth testing set to "Read-Only"
#
#
#  NIB FILES NOTES:
# - The QCView is configured to start rendering automatically and forward user 
#   events (mouse events are required to rotate the chart)
# - An AppController instance is connected as the data source for the 
#   NSTableView
# - The NSTableView is set up so that the identifiers of table columns match 
#   the keys used in the data storage
# - The "Value" column of the NSTableView has a NSNumberFormatter which 
#   guarantees only positive or null numbers can be entered here
# - The "Label" column of the NSTableView simply contains text
#

# Keys for the entries in the data storage 
kDataKey_Label = "label" # NSString
kDataKey_Value = "value" # NSNumber

# Keys for the composition input parameters
kParameterKey_Data      = "Data"    # NSArray of NSDictionaries
kParameterKey_Scale	= "Scale"   # NSNumber
kParameterKey_Spacing	= "Spacing" # NSNumber
	
class AppController (NSObject):
    tableView = objc.IBOutlet()
    view = objc.IBOutlet()
	
    _data = objc.ivar()

    def init(self):
        # Allocate our data storage
        self = super(AppController, self).init()
        if self is None:
            return None

        self._data = []
        
        return self

    def awakeFromNib(self):
        # Load the composition file into the QCView (because this 
        # QCView is bound to a QCPatchController in the nib file, this 
        # will actually update the QCPatchController along with all the 
        # bindings)
        if not self.view.loadCompositionFromFile_(NSBundle.mainBundle().pathForResource_ofType_("Chart", "qtz")):
            NSLog("Composition loading failed")
            NSApp.terminate_(None)
            
        # Populate data storage
        self._data.extend([
            {
                kDataKey_Label:"Palo Alto",
                kDataKey_Value: 2,
            },
            {
                kDataKey_Label: "Cupertino",
                kDataKey_Value: 1,
            },
            {
                kDataKey_Label: "Menlo Park",
                kDataKey_Value: 4,
            },
            {
                kDataKey_Label: "Mountain View",
                kDataKey_Value: 8,
            },
            {
                kDataKey_Label: "San Francisco",
                kDataKey_Value: 7,
            },
            {
                kDataKey_Label: "Los Altos",
                kDataKey_Value: 3,
            },
        ])
        
        #Initialize the views
        self.tableView.reloadData()
        self.updateChart()

    def updateChart(self):
        #Update the data displayed by the chart - it will be converted to a 
        # Structure of Structures by Quartz Composer
        self.view.setValue_forInputKey_(self._data, kParameterKey_Data)
            
        #Compute the maximum value and set the chart scale accordingly
        max = 0.0
        for obj in self._data:
            value = obj[kDataKey_Value]
            if value > max:
                max = value

        if max == 0.0:
            scale = 1.0
        else:
            scale = 1/max
        self.view.setValue_forInputKey_(scale, kParameterKey_Scale)

    @objc.IBAction
    def addEntry_(self, sender):
        #Add a new entry to the data storage
        self._data.append({
            kDataKey_Label: "Untitled",
            kDAtaKey_Value: 0,
        })
            
        #Notify the NSTableView and update the chart
        self.tableView.reloadData()
        self.updateChart()
        
        #Automatically select and edit the new entry
        self.tableView.selectRow_byExtendingSelection(len(self._data)-1, False)
        self.tableView.editColumn_row_withEvent_select_(
                self.tableView.columnWithIdentifier_(kDataKey_Label),
                len(self._data)-1, None, True)

    @objc.IBAction
    def removeEntry_(self, sender):
        #Make sure we have a valid selected row
        selectedRow = self.tableView.selectedRow()
        if selectedRow < 0 or tableView.editedRow() == selectedRow:
            return
            
        #Remove the currently selected entry from the data storage
        del self._data[selectedRow]
            
        #Notify the NSTableView and update the chart
        self.tableView.reloadData()
        self.updateChart()

     
    def numberOfRowsInTableView_(self, aTableView):
        # Return the number of entries in the data storage
        return len(self._data)

    def tableView_objectValueForTableColumn_row_(self, aTableView, aTableColumn, rowIndex):
        # Get the "label" or "value" attribute of the entry from the data 
        # storage at index "rowIndex"
        return self._data[rowIndex][aTableColumn.identifier()]

    def tableView_setObjectValue_forTableColumn_row_(
            self, aTableView, anObject, aTableColumn, rowIndex):

        # Set the "label" or "value" attribute of the entry from the data 
        # storage at index "rowIndex"
        self._data[rowIndex][aTableColumn.identifier()] = anObject

        # Update the chart
        self.updateChart()
