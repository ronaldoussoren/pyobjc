#import "OC_NSBundleHack.h"

static id (*bundleForClassIMP)(id, SEL, Class);

@implementation OC_NSBundleHackCheck
+(NSBundle*)bundleForClass
{
	return [NSBundle bundleForClass:[NSObject class]];
}
@end

static void
nsmaptable_objc_retain(NSMapTable *table __attribute__((__unused__)), const void *datum) {
	[(id)datum retain];
}

static void
nsmaptable_objc_release(NSMapTable *table __attribute__((__unused__)), void *datum) {
	[(id)datum release];
}

static
NSMapTableKeyCallBacks PyObjC_ClassToNSBundleTable_KeyCallBacks = {
	NULL, // use pointer value for hash
	NULL, // use pointer value for equality
	NULL, // no need to retain classes
	NULL, // no need to release classes
	NULL, // generic description
	NULL // not a key
};

static
NSMapTableValueCallBacks PyObjC_ClassToNSBundle_ValueCallBacks = {
	&nsmaptable_objc_retain,
	&nsmaptable_objc_release,
	NULL  // generic description
};

@implementation OC_NSBundleHack
+(NSBundle*)bundleForClass:(Class)aClass
{
	static NSBundle* mainBundle = nil;
	static NSMapTable* bundleCache = nil;
	if (!mainBundle) mainBundle = [[NSBundle mainBundle] retain];
	if (!bundleCache) bundleCache = NSCreateMapTable(PyObjC_ClassToNSBundleTable_KeyCallBacks, PyObjC_ClassToNSBundle_ValueCallBacks, PYOBJC_EXPECTED_CLASS_COUNT);
	id rval = (id)NSMapGet(bundleCache, (const void *)aClass);
	if (rval) {
		return rval;
	}
	rval = bundleForClassIMP([NSBundle class], @selector(bundleForClass:), aClass);
	if (rval == mainBundle) {
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
				rval = [(id)aClass performSelector:@selector(bundleForClass)];
			}
		}
	}
	NSMapInsert(bundleCache, (const void *)aClass, (const void *)rval);
	return rval;
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
