/*
 * Objective-C version of addressbook.py.
 *
 * This is not necessarily an example of good Objective-C programing, but
 * should help to compare two equivalent programs.
 */
#import <AddressBook/AddressBook.h>
#import <Foundation/Foundation.h>
#include <objc/objc-runtime.h>


int main(void)
{
	NSAutoreleasePool* pl = [[NSAutoreleasePool alloc] init];
	ABAddressBook* book = [objc_lookUpClass("ABAddressBook") sharedAddressBook];
	ABPerson* me = [book me];

	if (!me) {
		printf("You don't have a 'my card'\n");
		return 1;
	}

	NSArray* propNames = [ABPerson properties];
	NSMutableDictionary* d = [NSMutableDictionary dictionary];

	NSEnumerator* e = [propNames objectEnumerator];
	id k;
	while (k = [e nextObject]) {
		id v = [me valueForProperty:k];
		if (v) {
			[d setObject:v forKey:k];
		}
	}

	NSMutableArray* keys = [NSMutableArray arrayWithArray:[d allKeys]];
	[keys sortUsingSelector:@selector(compare:)];

	NSLog(@"Information about me");
	NSLog(@"--------------------");

	e = [keys objectEnumerator];
	while (k = [e nextObject]) {
	    NSLog(@"%@: %@", k, [d objectForKey:k]);
        }

	return 0;
}
