#include "pyobjc.h"
#import "OC_PythonArray.h"

@implementation OC_BuiltinPythonArray

+ (BOOL)supportsSecureCoding {
    return YES;
}

-(Class)classForKeyedArchiver
{
    return [OC_BuiltinPythonArray class];
}

+(NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonArray", @"NSArray", nil];
}


@end
