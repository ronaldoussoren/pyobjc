#import <Foundation/Foundation.h>

@interface IDNSnitchBase : NSObject
{
}
+(id)checkURL:(NSURL *)anURL;
+(void)startIDNSnitch:(id)sender;
@end;

@interface NSURLRequest_IDNSnitch : NSURLRequest
{
}
+(void)setIDNSnitchEnabled:(BOOL)isEnabled;
+(BOOL)IDNSnitchEnabled;
@end
