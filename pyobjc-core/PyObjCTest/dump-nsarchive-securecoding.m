/*
 * Helper tool for converting an NSArchive or NSKeyedArchive
 * to a plist on stdout.
 *
 * This variant uses NSSecureCoding
 */
#import <Foundation/Foundation.h>
#include <stdio.h>

#if PyObjC_BUILD_RELEASE < 1014
@interface
NSKeyedUnarchiver (PyObjCCompat)
+ (id)unarchivedObjectOfClasses:(NSSet*)classes
                       fromData:(NSData*)data
                          error:(NSError**)error;
@end
#endif

int
main(int argc, char** argv)
{
    NSAutoreleasePool* pool = [[NSAutoreleasePool alloc] init];

    if (argc != 2) {
        printf("Usage: dump-nsarchive-securecoding FILE\n");
        return 1;
    }

    NSString* path = [[NSString alloc] initWithUTF8String:argv[1]];
    NSObject* value;

    @try {
        NSData* data = [NSData dataWithContentsOfFile:path];

        if (!data) {
            fprintf(stderr, "Cannot read data from %s\n", argv[1]);
            return 1;
        }

        NSError* error = nil;

        value = [NSKeyedUnarchiver
            unarchivedObjectOfClasses:[NSSet
                                          setWithObjects:[NSArray class],
                                                         [NSDictionary class],
                                                         [NSString class], [NSData class],
                                                         [NSNumber class], [NSDate class],
                                                         [NSSet class], nil]
                             fromData:data
                                error:&error];
        if (value == nil) {
            NSLog(@"Cannot decode archive: %@", error);
            return 2;
        }

    } @catch (NSException* localException) {
        printf("Exception during unarchiving: %s\n",
               [[localException description] UTF8String]);
        return 2;
    }

    [path release];

    NSError* error = nil;
    NSData*  data  = [NSPropertyListSerialization
        dataWithPropertyList:value
                      format:NSPropertyListXMLFormat_v1_0
                     options:NSPropertyListMutableContainersAndLeaves
                       error:&error];

    if (data == nil) {
        /* Some types we test cannot be represented as a plist */
        printf("%s\n", [[value description] UTF8String]);
        return 0;
    }

    fwrite([data bytes], 1, [data length], stdout);
    return 0;
}
