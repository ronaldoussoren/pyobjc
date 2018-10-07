#include "pyobjc.h"
#import "OC_PythonNumber.h"

@implementation OC_BuiltinPythonNumber

+ (BOOL)supportsSecureCoding {
    return YES;
}

+(NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonNumber", @"NSNumber", nil];
}

@end
