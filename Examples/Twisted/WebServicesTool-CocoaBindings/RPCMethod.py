from Foundation import *
import objc

class RPCMethod(NSObject):
    def initWithDocument_name_(self, aDocument, aName):
        self = super(RPCMethod, self).init()
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

    def setMethodSignature_(self, aSignature):
        self.k_methodSignature = aSignature
    setMethodSignature_ = objc.accessor(setMethodSignature_)

    def methodDescription(self):
        if self.k_methodDescription is None:
            self.setMethodDescription_(u"<description not yet received>")
            self.document.fetchMethodDescription_(self)
        return self.k_methodDescription

    def setMethodDescription_(self, aDescription):
        self.k_methodDescription = aDescription
    setMethodDescription_ = objc.accessor(setMethodDescription_)
