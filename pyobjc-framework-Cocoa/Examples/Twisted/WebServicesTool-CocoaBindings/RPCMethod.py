import objc
from Foundation import NSObject
from objc import super


class RPCMethod(NSObject):
    def initWithDocument_name_(self, aDocument, aName):
        self = super().init()
        self.document = aDocument
        self.k_methodName = aName
        self.k_methodSignature = None
        self.k_methodDescription = None
        return self

    def methodName(self):
        return self.k_methodName

    def displayName(self):
        if self.k_methodSignature is None:
            return self.k_methodName
        else:
            return self.k_methodSignature

    @objc.accessor
    def setMethodSignature_(self, aSignature):
        self.k_methodSignature = aSignature

    def methodDescription(self):
        if self.k_methodDescription is None:
            self.setMethodDescription_("<description not yet received>")
            self.document.fetchMethodDescription_(self)
        return self.k_methodDescription

    @objc.accessor
    def setMethodDescription_(self, aDescription):
        self.k_methodDescription = aDescription
