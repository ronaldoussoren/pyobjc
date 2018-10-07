#include "pyobjc.h"
#import "OC_PythonNumber.h"

@implementation OC_BuiltinPythonNumber

+ (BOOL)supportsSecureCoding {
    return YES;
}

-(Class)classForKeyedArchiver
{
    return [OC_BuiltinPythonNumber class];
}

+(NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonNumber", @"NSNumber", nil];
}

@end
