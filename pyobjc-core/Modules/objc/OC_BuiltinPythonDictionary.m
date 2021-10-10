#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_BuiltinPythonDictionary

+ (BOOL)supportsSecureCoding
{
    return YES;
}

- (Class _Nullable)classForKeyedArchiver
{
    return [OC_BuiltinPythonDictionary class];
}

+ (NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonDictionary", @"NSDictionary", nil];
}

@end

NS_ASSUME_NONNULL_END
