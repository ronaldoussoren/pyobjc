#ifndef PYOBJC_PICKLE_CODER_H
#define PYOBJC_PICKLE_CODER_H
/**
 * Two simple classes that help in pickling Objective-C objects
 * that implement the NSCoding protocol.
 */
#include "pyobjc.h"

@interface OC_PickleCoder : NSArchiver
{
	PyObject* serialValues;
	PyObject* keyedValues;
}
-(PyObject*)data;
@end

@interface OC_PickleDecoder : NSUnarchiver
{
	PyObject* serialValues;
	PyObject* keyedValues;
}
-(OC_PickleDecoder*)initWithData:(PyObject*)data;
@end

#endif /* PYOBJC_PICKLE_CODER_H */
