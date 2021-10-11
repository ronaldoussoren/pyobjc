#ifndef PyObjC_BUNDLE_VARIABLES_H
#define PyObjC_BUNDLE_VARIABLES_H

NS_ASSUME_NONNULL_BEGIN

extern PyObject* _Nullable PyObjC_loadSpecialVar(PyObject*, PyObject* _Nullable,
                                                 PyObject* _Nullable)
    __attribute__((__warn_unused_result__));
extern PyObject* _Nullable PyObjC_loadBundleVariables(PyObject*, PyObject* _Nullable,
                                                      PyObject* _Nullable)
    __attribute__((__warn_unused_result__));
extern PyObject* _Nullable PyObjC_loadBundleFunctions(PyObject*, PyObject* _Nullable,
                                                      PyObject* _Nullable)
    __attribute__((__warn_unused_result__));
extern PyObject* _Nullable PyObjC_loadFunctionList(PyObject*, PyObject* _Nullable,
                                                   PyObject* _Nullable)
    __attribute__((__warn_unused_result__));

NS_ASSUME_NONNULL_END

#endif /* PyObjC_BUNDLE_VARIABLES_H */
