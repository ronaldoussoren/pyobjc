#import <Cocoa/Cocoa.h>

@interface NSWorkspace (PyObjCSupport)
@end
@implementation NSWorkspace (PyObjCSupport)
// - (BOOL)getInfoForFile:(NSString *)fullPath application:(NSString **)appName type:(NSString **)type;
- (NSDictionary *) pyobjcGetInfoForFile:(NSString *)fullPath;
{
  NSString *appName, *type;
  if ( [self getInfoForFile: fullPath application: &appName type: &type] ) {
    NSMutableDictionary *returnDict = [NSMutableDictionary dictionary];

    if (appName) [returnDict setObject: appName forKey: @"application"];
    if (type) [returnDict setObject: type forKey: @"type"];

    return returnDict;
  }

  return nil;
}

// - (BOOL)getFileSystemInfoForPath:(NSString *)fullPath isRemovable:(BOOL *)removableFlag isWritable:(BOOL *)writableFlag isUnmountable:(BOOL *)unmountableFlag description:(NSString **)description type:(NSString **)fileSystemType;
- (NSDictionary *) pyobjcGetFileSystemInfoForPath: (NSString *) fullPath;
{
  BOOL removableFlag, writableFlag, unmountableFlag;
  NSString *description, *fileSystemType;

  if ([self getFileSystemInfoForPath: fullPath
	    isRemovable: &removableFlag
	    isWritable: &writableFlag
	    isUnmountable: &unmountableFlag
	    description: &description
	    type: &fileSystemType]) {
    NSMutableDictionary *returnDict = [NSMutableDictionary dictionary];

    [returnDict setObject: [NSNumber numberWithBool: removableFlag] forKey: @"isRemovable"];    
    [returnDict setObject: [NSNumber numberWithBool: writableFlag] forKey: @"isWritable"];    
    [returnDict setObject: [NSNumber numberWithBool: unmountableFlag] forKey: @"isUnmountable"];

    if (description) [returnDict setObject: description forKey: @"description"];
    if (fileSystemType) [returnDict setObject: description forKey: @"description"];
  }

  return nil;
}
@end
