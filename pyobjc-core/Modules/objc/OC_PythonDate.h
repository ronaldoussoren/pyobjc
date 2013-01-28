#import "pyobjc.h"

@interface OC_PythonDate : NSDate
{
    PyObject* value;
    NSDate*   oc_value;
}

+(instancetype)depythonifyObject:(PyObject*)object;
+(instancetype)dateWithPythonObject:(PyObject*)value;
-(instancetype)initWithPythonObject:(PyObject*)value;
-(void)dealloc;
-(PyObject*)__pyobjc_PythonObject__;

/* Implementation of the NSDate interface */
-(NSTimeInterval)timeIntervalSinceReferenceDate;

/* NSCoding support */
-(void)encodeWithCoder:(NSCoder*)coder;
-(id)initWithCoder:(NSCoder*)coder;

@end
