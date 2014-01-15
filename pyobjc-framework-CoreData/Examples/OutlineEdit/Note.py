import CoreData

noteCount = 1

class Note (CoreData.NSManagedObject):
    def awakeFromInsert(self):
        global noteCount

        contents = "Note #%d"%(noteCount,)
        noteCount += 1
        self.setValue_forKey_(contents, "contents")
