#ifndef PyObjC_CLASS_LIST_H
#define PyObjC_CLASS_LIST_H

NS_ASSUME_NONNULL_BEGIN

/*!
 * PYOBJC_EXPECTED_CLASS_COUNT: Hint about the number of classes to expect
 *
 * Loading Quartz results close to 5K classes on OSX 10.8
 */
#define PYOBJC_EXPECTED_CLASS_COUNT 10000

/*!
 * @function PyObjC_GetClassList
 * @result Returns a list of Objective-C classes
 * @discussion
 *     This function returns a list containing the wrappers for all classes
 *     in the Objective-C runtime.
 */
PyObject* _Nullable PyObjC_GetClassList(bool ignore_invalid_identifiers);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_CLASS_LIST_H */
