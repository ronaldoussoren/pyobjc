#
#  FilteringControllerDocument.py
#  FilteringController
#
#  Converted by u.fiedler on 05.02.05.
#
#  The original version was written in Objective-C by Malcolm Crawford
#  at http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

from PyObjCTools import NibClassBuilder, AppHelper
import objc
from Foundation import NSKeyedArchiver, NSKeyedUnarchiver

NibClassBuilder.extractClasses("FilteringControllerDocument")

class FilteringControllerDocument(NibClassBuilder.AutoBaseClass):
    # the actual base class is NSDocument
    # The following outlets are added to the class:
    # peopleController

    def init(self):
        self = super(FilteringControllerDocument, self).init()
        if self is None: return None
        self._k_people = []
        return self

    def windowNibName(self):
        return u"FilteringControllerDocument"

    def windowControllerDidLoadNib_(self, controller):
        super(FilteringControllerDocument, self).windowControllerDidLoadNib_(controller)

    def dataRepresentationOfType_(self, aType):
        return NSKeyedArchiver.archivedDataWithRootObject_(self._k_people)
        
    def loadDataRepresentation_ofType_(self, data, aType):
        self.setPeople_(NSKeyedUnarchiver.unarchiveObjectWithData_(data))
        return True
        
        
    ### indexed accessors

    def people(self):
        return self._k_people

    def setPeople_(self, people):
        self._k_people[:] = people

    def countOfPeople(self):
        return len(self._k_people)
    countOfPeople = objc.accessor(countOfPeople)
        
    def objectInPeopleAtIndex_(self, idx):
        return self._k_people[idx]
    objectInPeopleAtIndex_ = objc.accessor(objectInPeopleAtIndex_)
        
    def insertObject_inPeopleAtIndex_(self, obj, idx):
        self._k_people.insert(idx, obj)
    insertObject_inPeopleAtIndex_ = objc.accessor(insertObject_inPeopleAtIndex_)

    def removeObjectFromPeopleAtIndex_(self, idx):
        del self._k_people[idx]
    removeObjectFromPeopleAtIndex_ = objc.accessor(removeObjectFromPeopleAtIndex_)
        
    def replaceObjectInPeopleAtIndex_withObject_(self, idx, obj):
        self._k_people[idx] = obj
    replaceObjectInPeopleAtIndex_withObject_ = objc.accessor(replaceObjectInPeopleAtIndex_withObject_)


		
