#! /usr/bin/python

from PyObjCTools.TestSupport import *
import objc

import Foundation
import CoreData

class CoreDataTestObject (CoreData.NSManagedObject):
    def __getattr__(self, k):
        raise AttributeError(k)

    def __setattr__(self, k, v):
        super(CoreDataTestObject, self).__setattr__(k, v)

    pass

class Test (TestCase):
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
        self.persistentStoreCoordinator.addPersistentStoreWithType_configuration_URL_options_error_(CoreData.NSInMemoryStoreType, None, None, None, None)

        self.managedObjectContext = CoreData.NSManagedObjectContext.new()
        self.managedObjectContext.setPersistentStoreCoordinator_(self.persistentStoreCoordinator)

    def testModeledAttribute(self):
        managedObject = CoreData.NSManagedObject.alloc().initWithEntity_insertIntoManagedObjectContext_(self.entity, self.managedObjectContext)

        testValue = b'FooBarBaz'.decode('ascii')

        managedObject.setValue_forKey_(testValue, b'testAttribute'.decode('ascii'))

        self.assertEquals(testValue, managedObject.valueForKey_(b'testAttribute'.decode('ascii')))
        self.assertEquals(testValue, managedObject._.testAttribute)

        testValue = b'BobFred'.decode('ascii')
        managedObject.setValue_forKey_(testValue, b'testAttribute'.decode('ascii'))

        self.assertEquals(testValue, managedObject.valueForKey_(b'testAttribute'.decode('ascii')))
        self.assertEquals(testValue, managedObject._.testAttribute)

        testValue = b'Zebras have long legs.'.decode('ascii')
        managedObject.testAttribute = testValue

        self.assertEquals(testValue, managedObject.valueForKey_(b'testAttribute'.decode('ascii')))
        self.assertEquals(testValue, managedObject._.testAttribute)

    def testPythonicAttribute(self):
        managedObject = CoreData.NSManagedObject.alloc().initWithEntity_insertIntoManagedObjectContext_(self.entity, self.managedObjectContext)

        testValue = b'Ducks have webbed feet'.decode('ascii')
        self.assertRaises(AttributeError, setattr, managedObject, 'attributeWithoutModel', testValue)
        return

        # XXX: this test is invalid, you cannot add arbitrary attributes
        # to an object that is fully implemented in ObjC.
        managedObject.attributeWithoutModel = testValue

        self.assertEquals(testValue, managedObject.attributeWithoutModel)

        self.assertRaises(Foundation.NSUnknownKeyException, managedObject.valueForKey_(b'attributeWithoutModel'.decode('ascii')))

class TestSubclass (TestCase):
    def setUp(self):
        self.entity = CoreData.NSEntityDescription.new()
        self.entity.setName_('TestObject')
        self.entity.setManagedObjectClassName_('CoreDataTestObject')

        self.attribute = CoreData.NSAttributeDescription.new()
        self.attribute.setName_('testAttribute')
        self.attribute.setAttributeType_(CoreData.NSStringAttributeType)

        self.entity.setProperties_([self.attribute])

        self.managedObjectModel = CoreData.NSManagedObjectModel.new()
        self.managedObjectModel.setEntities_([self.entity])

        self.persistentStoreCoordinator = CoreData.NSPersistentStoreCoordinator.alloc().initWithManagedObjectModel_(self.managedObjectModel)
        self.persistentStoreCoordinator.addPersistentStoreWithType_configuration_URL_options_error_(CoreData.NSInMemoryStoreType, None, None, None, None)

        self.managedObjectContext = CoreData.NSManagedObjectContext.new()
        self.managedObjectContext.setPersistentStoreCoordinator_(self.persistentStoreCoordinator)

    def testModeledAttribute(self):
        managedObject = CoreDataTestObject.alloc().initWithEntity_insertIntoManagedObjectContext_(self.entity, self.managedObjectContext)
        self.assert_(isinstance(managedObject, CoreDataTestObject))

        testValue = b'FooBarBaz'.decode('ascii')

        managedObject.setValue_forKey_(testValue, b'testAttribute'.decode('ascii'))

        self.assertEquals(testValue, managedObject.valueForKey_(b'testAttribute'.decode('ascii')))
        self.assertEquals(testValue, managedObject._.testAttribute)

        testValue = b'BobFred'.decode('ascii')
        managedObject.setValue_forKey_(testValue, b'testAttribute'.decode('ascii'))

        self.assertEquals(testValue, managedObject.valueForKey_(b'testAttribute'.decode('ascii')))
        self.assertEquals(testValue, managedObject._.testAttribute)

        self.assert_('testAttribute' not in managedObject.__dict__)

        testValue = b'Zebras have long legs.'.decode('ascii')
        managedObject._.testAttribute = testValue

        self.assertEquals(testValue, managedObject.valueForKey_(b'testAttribute'.decode('ascii')))
        self.assertEquals(testValue, managedObject._.testAttribute)

    def testPythonicAttribute(self):
        #self.fail("research recursion problem")
        managedObject = CoreDataTestObject.alloc().initWithEntity_insertIntoManagedObjectContext_(self.entity, self.managedObjectContext)
        self.assert_(isinstance(managedObject, CoreDataTestObject))

        testValue = b'Ducks have webbed feet'.decode('ascii')
        managedObject.attributeWithoutModel = testValue

        self.assertEquals(testValue, managedObject.attributeWithoutModel)
        self.assert_('attributeWithoutModel' in managedObject.__dict__)


if __name__ == "__main__":
    main()
