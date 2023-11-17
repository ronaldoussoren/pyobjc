#
#  FilteringControllerDocument.py
#  FilteringController
#
#  Converted by u.fiedler on 05.02.05.
#
#  The original version was written in Objective-C by Malcolm Crawford
#  at http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

import objc
from Cocoa import NSDocument, NSKeyedArchiver, NSKeyedUnarchiver
from objc import super  # noqa: A004


class FilteringControllerDocument(NSDocument):
    peopleController = objc.IBOutlet()

    def init(self):
        self = super().init()
        if self is None:
            return None
        self._k_people = []
        return self

    def windowNibName(self):
        return "FilteringControllerDocument"

    def windowControllerDidLoadNib_(self, controller):
        super().windowControllerDidLoadNib_(controller)

    def dataRepresentationOfType_(self, aType):
        return NSKeyedArchiver.archivedDataWithRootObject_(self._k_people)

    def loadDataRepresentation_ofType_(self, data, aType):
        self.setPeople_(NSKeyedUnarchiver.unarchiveObjectWithData_(data))
        return True

    # indexed accessors

    def people(self):
        return self._k_people

    def setPeople_(self, people):
        self._k_people[:] = people

    @objc.accessor
    def countOfPeople(self):
        return len(self._k_people)

    @objc.accessor
    def objectInPeopleAtIndex_(self, idx):
        return self._k_people[idx]

    @objc.accessor
    def insertObject_inPeopleAtIndex_(self, obj, idx):
        self._k_people.insert(idx, obj)

    @objc.accessor
    def removeObjectFromPeopleAtIndex_(self, idx):
        del self._k_people[idx]

    @objc.accessor
    def replaceObjectInPeopleAtIndex_withObject_(self, idx, obj):
        self._k_people[idx] = obj
