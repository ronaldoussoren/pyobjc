#
#  Category.py
#  ToDos
#
#  Converted by u.fiedler on 09.02.05.
#
#  The original version was written in Objective-C by Malcolm Crawford
#  at http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

from Foundation import *
import objc


class Category(NSObject):
    title = objc.ivar('title')
    priority = objc.ivar('priority', 'i')

    def allCategories(cls):
        """Predefined global list of categories"""
        return categories
    allCategories = classmethod(allCategories)
        
    def categoryForPriority_(cls, thePriority):
        for category in categories:
            if thePriority >= category.priority:
                return category
        return None
    categoryForPriority_ = classmethod(categoryForPriority_)
        
    def categoryWithTitle_andPriority_(cls, aTitle, aValue):
        """Convenience constructor"""
        newCategory = Category.alloc().init()
        newCategory.title = aTitle
        newCategory.priority = aValue
        return newCategory
    categoryWithTitle_andPriority_ = classmethod(categoryWithTitle_andPriority_)


    # NSCoding methods
    # To encode, simply save 'priority'; on decode, replace self with
    # the existing instance from 'allCategories' with the same priority

    def encodeWithCoder_(self, encoder):
        if encoder.allowsKeyedCoding():
            encoder.encodeInt_forKey_(self.priority, u"priority")
        else:
            encoder.encodeObject_(self.priority)
        
    def initWithCoder_(self, decoder):
        if decoder.allowsKeyedCoding():
            thePriority = decoder.decodeIntForKey_(u"priority")
        else:
            thePriority = decoder.decodeObject()
        return Category.categoryForPriority_(thePriority)
		

categories = [
	Category.categoryWithTitle_andPriority_(u"Vital", 11),
	Category.categoryWithTitle_andPriority_(u"Very Important", 4),
	Category.categoryWithTitle_andPriority_(u"Important", 3),
	Category.categoryWithTitle_andPriority_(u"Not Important", 2),
	Category.categoryWithTitle_andPriority_(u"Whenever", 0)
]

