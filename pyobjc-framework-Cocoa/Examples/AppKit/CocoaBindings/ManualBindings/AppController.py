#
#  AppController.py
#  ManualBindings
#
import objc

from Foundation import *
from AppKit import *

from PyObjCTools import NibClassBuilder


NibClassBuilder.extractClasses("MainMenu")

class AppController(NibClassBuilder.AutoBaseClass):

    def awakeFromNib(self):
        self.totalCountField.bind_toObject_withKeyPath_options_(u"value", self.arrayController, u"arrangedObjects.@sum.price", None)
        bindingOptions = {}
        bindingOptions[u'NSNullPlaceholder'] = u"No Name"
        self.selectedNameField.bind_toObject_withKeyPath_options_(u"value", self.arrayController, u"selection.name", bindingOptions)
        # binding for "name" column
        tableColumn = self.tableView.tableColumnWithIdentifier_(u'name')
        tableColumn.bind_toObject_withKeyPath_options_(u"value", self.arrayController, u"arrangedObjects.name", bindingOptions)
        
        # binding options for "price"
        del bindingOptions[u'NSNullPlaceholder']
        bindingOptions[NSValidatesImmediatelyBindingOption] = True
        
        # binding for selected "price" field
        self.selectedPriceField.bind_toObject_withKeyPath_options_(u"value", self.arrayController, u"selection.price", bindingOptions)
        
        #binding for "price" column
        tableColumn = self.tableView.tableColumnWithIdentifier_(u'price')
        tableColumn.bind_toObject_withKeyPath_options_(u"value", self.arrayController, u"arrangedObjects.price", bindingOptions)
        
        # bind array controller to self's itemsArray
        # we use _k_itemsArray because Python does not have a separate
        # namespace for instance variables, and we are using accessors.
        self._k_itemsArray = []
        self.arrayController.bind_toObject_withKeyPath_options_(u"contentArray", self, u"self.itemsArray", None)
        
    def countOfItemsArray(self):
        print "countOfItemsArray"
        return len(self._k_itemsArray)
    countOfItemsArray = objc.accessor(countOfItemsArray)
        
    def objectInItemsArrayAtIndex_(self, index):
        print "objectInItemsArrayAtIndex_", index
        return self._k_itemsArray[index]
    objectInItemsArrayAtIndex_ = objc.accessor(objectInItemsArrayAtIndex_)
        
    def insertObject_inItemsArrayAtIndex_(self, obj, idx):
        print "insertObject_inItemsArrayAtIndex_", idx
        self._k_itemsArray.insert(idx, obj)
    insertObject_inItemsArrayAtIndex_ = objc.accessor(insertObject_inItemsArrayAtIndex_)
        
    def removeObjectFromItemsArrayAtIndex_(self, idx):
        print "removeObjectFromItemsArrayAtIndex_", idx
        del self._k_itemsArray[idx]
    removeObjectFromItemsArrayAtIndex_ = objc.accessor(removeObjectFromItemsArrayAtIndex_)
        
    def replaceObjectInItemsArrayAtIndex_withObject_(self, idx, obj):
        print "!!! replaceObjectInItemsArrayAtIndex_withObject_", idx
        self._k_itemsArray[idx] = obj
    replaceObjectInItemsArrayAtIndex_withObject_ = objc.accessor(replaceObjectInItemsArrayAtIndex_withObject_)
        
ITEM_ERROR_DOMAIN = u'ITEM_ERROR_DOMAIN'
ITEM_NEGATIVE_PRICE = 10001
        
class Item(NSObject):
    def price(self):
        return getattr(self, '_k_price', 0.0)

    def setPrice_(self, aPrice):
        self._k_price = aPrice

    def name(self):
        return getattr(self, '_k_name', None)

    def setName_(self, aName):
        self._k_name = aName
    
    def validatePrice_error_(self, value):
        print ">>>> validatePrice_error_", value #.price
        error = None
        if value >= 0:
            return True, value, error

        errorString = u'Price cannot be negative'
        userInfoDict = {NSLocalizedDescriptionKey: errorString}
        error = NSError.alloc().initWithDomain_code_userInfo_(
            ITEM_ERROR_DOMAIN,
            ITEM_NEGATIVE_PRICE,
            userInfoDict)

        return False, value, error

    validatePrice_error_ = objc.accessor(validatePrice_error_)
