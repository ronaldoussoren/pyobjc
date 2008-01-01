#ifndef PyObjC_ALLOC_HACK_H
#define PyObjC_ALLOC_HACK_H
/*!
 * @header   alloc_hack.h
 * @abstract Special wrappers for the +alloc method
 * @discussion
 *      This module defines custom wrappers for the +alloc method. These
 *      are needed for some classes on MacOS X 10.2 because those classes
 *      cause crashes when alloc is called using NSInvocation.
 *
 *      The issue seems to be fixed in MacOS X 10.3. We keep using these
 *      wrapers just in case the problem returns.
 */

/*!
 * @function PyObjC_InstallAllocHack
 * @abstract Register the custom wrappers with the bridge
 * @result Returns 0 on success, -1 on error
 * @discussion
 *    This function installs the custom wrappers with the super-call.h module.
 */
int PyObjC_InstallAllocHack(void);

#endif /* PyObjC_ALLOC_HACK_H */
