#ifndef PyObjC_BUNDLE_VARIABLES_H
#define PyObjC_BUNDLE_VARIABLES_H

extern PyObject* PyObjC_loadSpecialVar(PyObject*, PyObject*, PyObject*) __attribute__((__nonnull__)) __attribute__((__warn_unused_result__));
extern PyObject* PyObjC_loadBundleVariables(PyObject*, PyObject*, PyObject*) __attribute__((__nonnull__)) __attribute__((__warn_unused_result__));
extern PyObject* PyObjC_loadBundleFunctions(PyObject*, PyObject*, PyObject*) __attribute__((__nonnull__)) __attribute__((__warn_unused_result__));
extern PyObject* PyObjC_loadFunctionList(PyObject*, PyObject*, PyObject*) __attribute__((__nonnull__)) __attribute__((__warn_unused_result__));

#endif /* PyObjC_BUNDLE_VARIABLES_H */
