#import "NSURLRequest_IDNSnitch.h"
#import "Python.h"
#import <objc/objc-class.h>
#define GETISA(cls) ((cls)->isa)

@implementation IDNSnitchBase
+(id)checkURL:(NSURL *)anURL
{
    NSLog(@"Base implementation of NSURL! This shouldn't happen!");
    return anURL;
}
+(void)startIDNSnitch:(id)sender
{
    [NSURLRequest_IDNSnitch setIDNSnitchEnabled:YES];
}
@end

static id (*initWithURL_cachePolicy_timeoutInterval_IMP)(id, SEL, id, NSURLRequestCachePolicy, NSTimeInterval) = nil;
static BOOL NSURLRequest_IDNSnitch_enabled = NO;
struct objc_method_list *PyObjCRT_AllocMethodList(int numMethods)
{   
    struct objc_method_list *mlist;

    mlist = malloc(sizeof(struct objc_method_list)
             + ((numMethods+1) * sizeof(struct objc_method)));

    if (mlist == NULL) {
            return NULL;
    }

    mlist->method_count = 0;
    mlist->obsolete = NULL;

    return mlist;
}

@interface NSObject(IDNSnitchSupport)
+(id)checkURL:(NSURL *)anURL;
@end

@implementation NSURLRequest_IDNSnitch
+(BOOL)IDNSnitchEnabled
{
    return NSURLRequest_IDNSnitch_enabled;
}

+(void)setIDNSnitchEnabled:(BOOL)shouldEnable
{
    if (NSURLRequest_IDNSnitch_enabled == shouldEnable) {
        return;
    }
    if (!initWithURL_cachePolicy_timeoutInterval_IMP) {
        initWithURL_cachePolicy_timeoutInterval_IMP = (id (*)(id, SEL, id, NSURLRequestCachePolicy, NSTimeInterval))[NSURLRequest instanceMethodForSelector:@selector(initWithURL:cachePolicy:timeoutInterval:)];
    }
	struct objc_method* objcMethod;
	struct objc_method_list* methodsToAdd;
	methodsToAdd = PyObjCRT_AllocMethodList(1);
	if (methodsToAdd == NULL) {
		return;
	}
	methodsToAdd->method_count = 1;
	objcMethod = methodsToAdd->method_list;
	objcMethod->method_name = @selector(initWithURL:cachePolicy:timeoutInterval:);
	objcMethod->method_types = "@#@id";
    if (shouldEnable) {
        objcMethod->method_imp = [self instanceMethodForSelector:@selector(initWithURL:cachePolicy:timeoutInterval:)];
    } else {
        objcMethod->method_imp = (IMP)initWithURL_cachePolicy_timeoutInterval_IMP;
    }
	class_addMethods([NSURLRequest class], methodsToAdd);
}

-(id)initWithURL:(NSURL *)theURL cachePolicy:(NSURLRequestCachePolicy)cachePolicy timeoutInterval:(NSTimeInterval)timeoutInterval
{
    theURL = [NSClassFromString(@"IDNSnitch") checkURL:theURL];
    return initWithURL_cachePolicy_timeoutInterval_IMP(self, @selector(initWithURL:cachePolicy:timeoutInterval:), theURL, cachePolicy, timeoutInterval);
}


@end

PyMODINIT_FUNC
initNSURLRequest_IDNSnitch(void)
{
    (void)Py_InitModule("NSURLRequest_IDNSnitch", NULL);
}
