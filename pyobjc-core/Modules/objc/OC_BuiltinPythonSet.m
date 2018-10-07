#include "pyobjc.h"
#import "OC_PythonSet.h"

@implementation OC_BuiltinPythonSet

+ (BOOL)supportsSecureCoding {
    return YES;
}

-(Class)classForKeyedArchiver
{
    return [OC_BuiltinPythonSet class];
}

+(NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonSet", @"NSSet", nil];
}

@end
