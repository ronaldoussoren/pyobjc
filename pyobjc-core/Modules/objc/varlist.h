/*
 * PyObjC_VarList - Variable length C arrays
 *
 * The 'objc.varlist' type is used to represent (mutable)
 * C arrays where the bridge does not know the size of
 * the array (arrays of a known size are converted to
 * a python list)
 *
 * Using 'objc.varlist' objects in inherently unsafe, the
 * bridge cannot protect against accessing memory beyond
 * the (unknown) size of the underlying C array, and the
 * C array might be deallocated before the 'objc.varlist'
 * object is garbage collected.
 */
#ifndef PyObjC_VARLIST_H
#define PyObjC_VARLIST_H

NS_ASSUME_NONNULL_BEGIN

extern PyTypeObject PyObjC_VarList_Type;

extern PyObject* _Nullable PyObjC_VarList_New(const char* tp, void* array);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_VARLIST_H */
