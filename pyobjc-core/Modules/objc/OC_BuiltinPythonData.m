#include "pyobjc.h"
#import "OC_PythonData.h"

@implementation OC_BuiltinPythonData

+ (BOOL)supportsSecureCoding {
    return YES;
}

-(Class)classForKeyedArchiver
{
    return [OC_BuiltinPythonData class];
}

+(NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonData", @"NSData", nil];
}

@end
