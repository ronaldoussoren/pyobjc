#include <Python.h>
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

#ifndef NSINTEGER_DEFINED

typedef unsigned int NSUInteger;

#endif


@interface OC_TestSet : NSObject {}
@end

@implementation OC_TestSet

+(Class)classOf:(NSObject*)value
{
	return [value class];
}

/* copying */
+(id)set:(NSSet*)set copyWithZone:(NSZone*)zone
{
	return [set copyWithZone:zone];
}

+(id)set:(NSSet*)set mutableCopyWithZone:(NSZone*)zone
{
	return [set mutableCopyWithZone:zone];
}


/* Base set */

+(NSArray*)allObjectsOfSet:(NSSet*)set
{
	return [set allObjects];
}

+(id)anyObjectOfSet:(NSSet*)set
{
	return [set anyObject];
}

+(BOOL)set:(NSSet*)set containsObject:(id)anObject
{
	return [set containsObject:anObject];
}

+(NSUInteger)countOfSet:(NSSet*)set
{
	return [set count];
}

+(NSString*)descriptionOfSet:(NSSet*)set
{
	return [set description];
}

+(NSString*)set:(NSSet*)set descriptionWithLocale:(id)locale
{
	return [set descriptionWithLocale:locale];
}


+(NSSet*)set:(NSSet*)set filteredSetUsingPredicate:(NSPredicate*)predicate
{
	return [set filteredSetUsingPredicate:predicate];
}

+(BOOL)set:(NSMutableSet*)set intersectsSet:(NSSet *)otherSet
{
	return [set intersectsSet:otherSet];
}

+(BOOL)set:(NSSet*)set isEqualToSet:(NSSet*)otherSet
{
	return [set isEqualToSet:otherSet];
}

+(BOOL)set:(NSSet*)set isSubsetOfSet:(NSSet*)otherSet
{
	return [set isSubsetOfSet:otherSet];
}

+(void)set:(NSSet*)set makeObjectsPerformSelector:(SEL)aSelector
{
	return [set makeObjectsPerformSelector:aSelector];
}

+(void)set:(NSSet*)set makeObjectsPerformSelector:(SEL)aSelector withObject:(id)anObject
{
	return [set makeObjectsPerformSelector:aSelector withObject:anObject];
}

+(id)set:(NSSet*)set member:(id)anObject
{
	return [set member:anObject];
}

+(NSEnumerator*)objectEnumeratorOfSet:(NSSet*)set
{
	return [set objectEnumerator];
}

+(NSSet*)set:(NSSet*)set setByAddingObject:(id)anObject
{
	return [set setByAddingObject:anObject];
}

+(NSSet*)set:(NSSet*)set setByAddingObjectsFromArray:(NSArray*)anObject
{
	return [set setByAddingObjectsFromArray:anObject];
}

+(NSSet*)set:(NSSet*)set setByAddingObjectsFromSet:(NSSet*)anObject
{
	return [set setByAddingObjectsFromSet:anObject];
}

+(void)set:(NSSet*)set setValue:(id)value forKey:(id)key
{
	[set setValue:value forKey:key];
}

+(id)set:(NSSet*)set valueForKey:(id)key
{
	return [set valueForKey:key];
}

/* Mutable set */

+(void)set:(NSMutableSet*)set addObject:(id)anObject
{
	[set addObject:anObject];
}

+(void)set:(NSMutableSet*)set addObjectsFromArray:(NSArray *)anArray
{
	[set addObjectsFromArray:anArray];
}

+(void)set:(NSMutableSet*)set filterUsingPredicate:(NSPredicate *)predicate
{
	[set filterUsingPredicate:predicate];
}

+(void)set:(NSMutableSet*)set intersectSet:(NSSet *)otherSet
{
	[set intersectSet:otherSet];
}

+(void)set:(NSMutableSet*)set minusSet:(NSSet *)otherSet
{
	[set minusSet:otherSet];
}

+(void)removeAllObjecsFromSet:(NSMutableSet*)set
{
	[set removeAllObjects];
}

+(void)set:(NSMutableSet*)set removeObject:(id)anObject
{
	[set removeObject:anObject];
}

+(void)set:(NSMutableSet*)set setSet:(NSSet *)otherSet
{
	[set setSet:otherSet];
}

+(void)set:(NSMutableSet*)set unionSet:(NSSet *)otherSet
{
	[set unionSet:otherSet];
}



@end


static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"pythonset",
	NULL,
	0,
	mod_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit_pythonset(void);

PyObject*
PyInit_pythonset(void)

#else

#define INITERROR() return
#define INITDONE() return

void initpythonset(void);

void
initpythonset(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("pythonset", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "OC_TestSet",
	    PyObjCClass_New([OC_TestSet class])) < 0) {
		INITERROR();
	}

	INITDONE();
}
