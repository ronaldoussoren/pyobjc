#import <Foundation/Foundation.h>

int main(void)
{
	NSLog(@"%llu", [[NSNumber numberWithDouble:-127.6] unsignedLongLongValue]);
}
