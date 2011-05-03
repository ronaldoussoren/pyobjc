#import <Foundation/Foundation.h>
#import "JVAutoEmotionDisplay.h"
#import "JVChatRoom.h"
#import "JVDirectChat.h"

@implementation JVAutoEmotionDisplay
- (id) initWithManager:(MVChatPluginManager *) manager {
	self = [super init];
	_manager = manager; // Don't retain, to prevent a circular retain.
	_emotions = [[NSMutableDictionary dictionary] retain];
	return self;
}

- (void) dealloc {
	[_emotions release];
	_emotions = nil;
	_manager = nil;
	[super dealloc];	
}

- (BOOL) processUserCommand:(NSString *) command withArguments:(NSAttributedString *) arguments toRoom:(JVChatRoom *) room {
	if( [command isEqualToString:@"aed"] ) {
		if( arguments ) [_emotions setObject:[[arguments copy] autorelease] forKey:[room target]];
		else [_emotions removeObjectForKey:[room target]];
		return YES;
	}
	return NO;
}

- (BOOL) processUserCommand:(NSString *) command withArguments:(NSAttributedString *) arguments toChat:(JVDirectChat *) chat {
	if( [command isEqualToString:@"aed"] ) {
		if( arguments ) [_emotions setObject:[[arguments copy] autorelease] forKey:[chat target]];
		else [_emotions removeObjectForKey:[chat target]];
		return YES;
	}
	return NO;
}

- (void) processMessage:(NSMutableAttributedString *) message asAction:(BOOL) action toRoom:(JVChatRoom *) room {
	if( [_emotions objectForKey:[room target]] ) {
		NSMutableAttributedString *appd = [[[NSMutableAttributedString alloc] initWithString:@" "] autorelease];
		[appd appendAttributedString:[_emotions objectForKey:[room target]]];
		[message appendAttributedString:appd];
	}
}

- (void) processMessage:(NSMutableAttributedString *) message asAction:(BOOL) action toChat:(JVDirectChat *) chat {
	if( [_emotions objectForKey:[chat target]] ) {
		NSMutableAttributedString *appd = [[[NSMutableAttributedString alloc] initWithString:@" "] autorelease];
		[appd appendAttributedString:[_emotions objectForKey:[chat target]]];
		[message appendAttributedString:appd];
	}
}
@end