#import "pyobjc.h"
#import <Foundation/Foundation.h>

@interface OC_PythonDate : NSDate
{
	PyObject* value;
	NSDate*   oc_value;
}

+ (instancetype)depythonifyObject:(PyObject*)object;
+ (instancetype)dateWithPythonObject:(PyObject*)value;
- (id)initWithPythonObject:(PyObject*)value;
-(void)dealloc;
-(PyObject*)__pyobjc_PythonObject__;

/* Implementation of the NSDate interface */

/* This one is the biggy: this is the once required method, all other
 * NSDate methods build on this.
 */
-(NSTimeInterval)timeIntervalSinceReferenceDate;

/* These two are only present to *disable* coding, not implement it */
- (void)encodeWithCoder:(NSCoder*)coder;
- (id)initWithCoder:(NSCoder*)coder;

@end
