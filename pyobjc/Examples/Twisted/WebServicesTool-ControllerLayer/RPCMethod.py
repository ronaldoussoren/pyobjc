from Foundation import NSObject
from objc import selector

class RPCMethod(NSObject):
    def init(self, aDocument, aName):
        super(RPCMethod, self).init()
        self.document = aDocument
        self._methodName = aName
        self._methodSignature = None
        self._methodDescription = None
        return self

    def methodName(self):
        return self._methodName

    def displayName(self):
        if self._methodSignature:
            return self._methodSignature
        else:
            return self._methodName

    def methodDescription(self):
        if not self._methodDescription:
            self._methodDescription = "<description not yet received>"
            self.document.fetchMethodDescription_(self)
        return self._methodDescription
        
    def setMethodDescription_(self, aDescription):
        NSObject.willChangeValueForKey_(self, "methodDescription")
        self._methodDescription = aDescription
        NSObject.didChangeValueForKey_(self, "methodDescription")
    setMethodDescription_ = selector(setMethodDescription_, signature="v@:@")