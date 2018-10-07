#include "pyobjc.h"
#import "OC_PythonUnicode.h"

@implementation OC_BuiltinPythonUnicode

+ (BOOL)supportsSecureCoding {
    return YES;
}

-(Class)classForKeyedArchiver
{
    return [OC_BuiltinPythonUnicode class];
}

+(NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonString", @"NSString", nil];
}

@end
