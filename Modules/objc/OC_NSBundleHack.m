#import "OC_NSBundleHack.h"

static id (*bundleForClassIMP)(id, SEL, Class);

@implementation OC_NSBundleHackCheck
+(NSBundle*)bundleForClass
{
	return [NSBundle bundleForClass:[NSObject class]];
}
@end

@implementation OC_NSBundleHack
+(NSBundle*)bundleForClass:(Class)aClass
{
	Class base_isa = aClass;
	Class nsobject_isa = GETISA([NSObject class]);
	while (base_isa != nsobject_isa) {
		Class next_isa = GETISA(base_isa);
		if (!next_isa || next_isa == base_isa) {
			break;
		}
		base_isa = next_isa;
	}
	if (base_isa == nsobject_isa) {
		if ([(id)aClass respondsToSelector:@selector(bundleForClass)]) {
			static NSMutableDictionary *bundleCache = NULL;
			if (!bundleCache) {
				bundleCache = [[NSMutableDictionary alloc] initWithCapacity:128];
			}
			id rval = [bundleCache objectForKey:(id)aClass];
			if (!rval) {
				rval = [(id)aClass performSelector:@selector(bundleForClass)];
				[bundleCache setObject:rval forKey:(id)aClass];
			}
			return rval;
		}
	}
	return bundleForClassIMP([NSBundle class], @selector(bundleForClass:), aClass);
}

+(void)installBundleHack
{
	if ([[NSBundle bundleForClass:[NSObject class]] isEqual:[NSBundle bundleForClass:[OC_NSBundleHackCheck class]]]) {
		// implementation is already fine
		return;
	}
	bundleForClassIMP = (id (*)(id, SEL, Class))[NSBundle methodForSelector:@selector(bundleForClass:)];
	
	struct objc_method* objcMethod;
	struct objc_method_list* methodsToAdd;
	methodsToAdd = PyObjCRT_AllocMethodList(1);
	if (methodsToAdd == NULL) {
		return;
	}
	methodsToAdd->method_count = 1;
	objcMethod = methodsToAdd->method_list;
	objcMethod->method_name = @selector(bundleForClass:);
	objcMethod->method_types = "@@:#";
	objcMethod->method_imp = [self methodForSelector:@selector(bundleForClass:)];
	PyObjCRT_ClassAddMethodList(GETISA([NSBundle class]), methodsToAdd);
}
@end
