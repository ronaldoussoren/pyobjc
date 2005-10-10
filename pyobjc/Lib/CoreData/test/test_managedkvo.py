#! /usr/bin/python

import unittest
import objc

import CoreData

class Test (unittest.TestCase):
    def setUp(self):
	self.entity = CoreData.NSEntityDescription.new()
	self.entity.setName_('TestEntity')

	self.attribute = CoreData.NSAttributeDescription.new()
	self.attribute.setName_('testAttribute')
	self.attribute.setAttributeType_(CoreData.NSStringAttributeType)

	self.entity.setProperties_([self.attribute])

	self.managedObjectModel = CoreData.NSManagedObjectModel.new()
	self.managedObjectModel.setEntities_([self.entity])

	self.persistentStoreCoordinator = CoreData.NSPersistentStoreCoordinator.alloc().initWithManagedObjectModel_(self.managedObjectModel)
	self.persistentStoreCoordinator.addPersistentStoreWithType_configuration_URL_options_error_(CoreData.NSInMemoryStoreType, None, None, None)

	self.managedObjectContext = CoreData.NSManagedObjectContext.new()
	self.managedObjectContext.setPersistentStoreCoordinator_(self.persistentStoreCoordinator)

    def testManagedKVO(self):
	managedObject = CoreData.NSManagedObject.alloc().initWithEntity_insertIntoManagedObjectContext_(self.entity, self.managedObjectContext)

	testValue = u'FooBarBaz'

	managedObject.setValue_forKey_(testValue, u'testAttribute')

	self.assertEquals(testValue, managedObject.valueForKey_(u'testAttribute'))
	self.assertEquals(testValue, managedObject.testAttribute)

	testValue = u'BobFred'
	managedObject.setValue_forKey_(testValue, u'testAttribute')

	self.assertEquals(testValue, managedObject.valueForKey_(u'testAttribute'))
	self.assertEquals(testValue, managedObject.testAttribute)
	

if __name__ == "__main__":
    unittest.main()

