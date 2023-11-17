#! /usr/bin/python

import CoreData
import Foundation
from objc import super  # noqa: A004
from PyObjCTools.TestSupport import TestCase


class CoreDataTestObject(CoreData.NSManagedObject):
    def __getattr__(self, k):
        raise AttributeError(k)

    def __setattr__(self, k, v):
        super().__setattr__(k, v)

    pass


class Test(TestCase):
    def setUp(self):
        self.entity = CoreData.NSEntityDescription.new()
        self.entity.setName_("TestEntity")

        self.attribute = CoreData.NSAttributeDescription.new()
        self.attribute.setName_("testAttribute")
        self.attribute.setAttributeType_(CoreData.NSStringAttributeType)

        self.entity.setProperties_([self.attribute])

        self.managedObjectModel = CoreData.NSManagedObjectModel.new()
        self.managedObjectModel.setEntities_([self.entity])

        self.persistentStoreCoordinator = (
            CoreData.NSPersistentStoreCoordinator.alloc().initWithManagedObjectModel_(
                self.managedObjectModel
            )
        )
        self.persistentStoreCoordinator.addPersistentStoreWithType_configuration_URL_options_error_(
            CoreData.NSInMemoryStoreType, None, None, None, None
        )

        self.managedObjectContext = CoreData.NSManagedObjectContext.new()
        self.managedObjectContext.setPersistentStoreCoordinator_(
            self.persistentStoreCoordinator
        )

    def testModeledAttribute(self):
        managedObject = CoreData.NSManagedObject.alloc().initWithEntity_insertIntoManagedObjectContext_(
            self.entity, self.managedObjectContext
        )

        testValue = "FooBarBaz"

        managedObject.setValue_forKey_(testValue, "testAttribute")

        self.assertEqual(testValue, managedObject.valueForKey_("testAttribute"))
        self.assertEqual(testValue, managedObject._.testAttribute)

        testValue = "BobFred"
        managedObject.setValue_forKey_(testValue, "testAttribute")

        self.assertEqual(testValue, managedObject.valueForKey_("testAttribute"))
        self.assertEqual(testValue, managedObject._.testAttribute)

        testValue = "Zebras have long legs."
        managedObject._.testAttribute = testValue

        self.assertEqual(testValue, managedObject.valueForKey_("testAttribute"))
        self.assertEqual(testValue, managedObject._.testAttribute)

    def testPythonicAttribute(self):
        managedObject = CoreData.NSManagedObject.alloc().initWithEntity_insertIntoManagedObjectContext_(
            self.entity, self.managedObjectContext
        )

        testValue = "Ducks have webbed feet"
        self.assertRaises(
            AttributeError, setattr, managedObject, "attributeWithoutModel", testValue
        )
        return

        # XXX: this test is invalid, you cannot add arbitrary attributes
        # to an object that is fully implemented in ObjC.
        managedObject.attributeWithoutModel = testValue

        self.assertEqual(testValue, managedObject.attributeWithoutModel)

        self.assertRaises(
            Foundation.NSUnknownKeyException,
            managedObject.valueForKey_("attributeWithoutModel"),
        )


class TestSubclass(TestCase):
    def setUp(self):
        self.entity = CoreData.NSEntityDescription.new()
        self.entity.setName_("TestObject")
        self.entity.setManagedObjectClassName_("CoreDataTestObject")

        self.attribute = CoreData.NSAttributeDescription.new()
        self.attribute.setName_("testAttribute")
        self.attribute.setAttributeType_(CoreData.NSStringAttributeType)

        self.entity.setProperties_([self.attribute])

        self.managedObjectModel = CoreData.NSManagedObjectModel.new()
        self.managedObjectModel.setEntities_([self.entity])

        self.persistentStoreCoordinator = (
            CoreData.NSPersistentStoreCoordinator.alloc().initWithManagedObjectModel_(
                self.managedObjectModel
            )
        )
        self.persistentStoreCoordinator.addPersistentStoreWithType_configuration_URL_options_error_(
            CoreData.NSInMemoryStoreType, None, None, None, None
        )

        self.managedObjectContext = CoreData.NSManagedObjectContext.new()
        self.managedObjectContext.setPersistentStoreCoordinator_(
            self.persistentStoreCoordinator
        )

    def testModeledAttribute(self):
        managedObject = (
            CoreDataTestObject.alloc().initWithEntity_insertIntoManagedObjectContext_(
                self.entity, self.managedObjectContext
            )
        )
        self.assertIsInstance(managedObject, CoreDataTestObject)

        testValue = "FooBarBaz"

        managedObject.setValue_forKey_(testValue, "testAttribute")

        self.assertEqual(testValue, managedObject.valueForKey_("testAttribute"))
        self.assertEqual(testValue, managedObject._.testAttribute)

        testValue = "BobFred"
        managedObject.setValue_forKey_(testValue, "testAttribute")

        self.assertEqual(testValue, managedObject.valueForKey_("testAttribute"))
        self.assertEqual(testValue, managedObject._.testAttribute)

        self.assertTrue("testAttribute" not in managedObject.__dict__)

        testValue = "Zebras have long legs."
        managedObject._.testAttribute = testValue

        self.assertEqual(testValue, managedObject.valueForKey_("testAttribute"))
        self.assertEqual(testValue, managedObject._.testAttribute)

    def testPythonicAttribute(self):
        # self.fail("research recursion problem")
        managedObject = (
            CoreDataTestObject.alloc().initWithEntity_insertIntoManagedObjectContext_(
                self.entity, self.managedObjectContext
            )
        )
        self.assertIsInstance(managedObject, CoreDataTestObject)

        testValue = "Ducks have webbed feet"
        managedObject.attributeWithoutModel = testValue

        self.assertEqual(testValue, managedObject.attributeWithoutModel)
        self.assertTrue("attributeWithoutModel" in managedObject.__dict__)
