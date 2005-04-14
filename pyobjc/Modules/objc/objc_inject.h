#ifndef PyObjC_OBJC_INJECT_H
#define PyObjC_OBJC_INJECT_H
#ifdef __APPLE__
#include <AvailabilityMacros.h>
#ifdef MAC_OS_X_VERSION_10_3
#if MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_3

#include <sys/types.h>
int
objc_inject(pid_t pid, int use_main_thread, char *bundlePath, char *systemPath, char *carbonPath);

#endif /* MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_3 */
#endif /* MAC_OS_X_VERSION_10_3 */
#endif /* __APPLE__ */
#endif /* PyObjC_OBJC_INJECT_H */
