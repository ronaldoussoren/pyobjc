#include "pyobjc.h"
#import "OC_PythonDictionary.h"

@implementation OC_BuiltinPythonDictionary

+ (BOOL)supportsSecureCoding {
    return YES;
}

-(Class)classForKeyedArchiver
{
    return [OC_BuiltinPythonDictionary class];
}

+(NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonDictionary", @"NSDictionary", nil];
}

@end
