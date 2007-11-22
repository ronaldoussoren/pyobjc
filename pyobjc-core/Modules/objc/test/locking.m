/*
 * Helper methods opaque-pointer tests (objc.test.test_opaque)
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

typedef struct _Foo* FooHandle;
typedef struct _Bar* BarHandle;

@interface NSObject (OC_LockingTest)
-(void)setLocked:(NSObject*)value;
-(NSObject*)isLocked;
-(void)appendToList:(NSObject*)value;
@end

@interface OC_LockTest : NSObject
-(void)threadFunc:(NSObject*)object;
@end

@implementation OC_LockTest
-(void)threadFunc:(NSObject*)object
{
	int i;
	for (i = 0; i < 6; i++) {
		usleep(500000);
		@synchronized(object) {
			NSNumber* isLocked = (NSNumber*)[object isLocked];
			if ([isLocked boolValue]) {
				[object appendToList:@"LOCK FOUND"];
			}
			[object setLocked:[NSNumber numberWithBool:YES]];
			[object appendToList:@"threading a"];
			usleep(5000000);
			[object appendToList:@"threading b"];
			[object setLocked:[NSNumber numberWithBool:NO]];
		}
	}
}
@end


static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

void initlocking(void);
void initlocking(void)
{
	PyObject* m;

	m = Py_InitModule4("locking", mod_methods, NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

	PyModule_AddObject(m, "OC_LockTest", 
		PyObjCClass_New([OC_LockTest class]));
}
