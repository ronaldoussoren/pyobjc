NS_ASSUME_NONNULL_BEGIN

static const void* _Nullable mod_CFTreeRetainCallback(const void* _Nullable info)
{
    return [(NSObject*)info retain];
}

static void
mod_CFTreeReleaseCallback(const void* info)
{
    [(NSObject*)info release];
}

static CFStringRef _Nullable mod_CFTreeCopyDescriptionCallback(const void* _Nullable info)
{
    NSString* result = [(NSObject*)info description];
    [result retain];
    return (CFStringRef)result;
}

static CFTreeContext mod_CFTreeContext = {0, NULL, mod_CFTreeRetainCallback,
                                          mod_CFTreeReleaseCallback,
                                          mod_CFTreeCopyDescriptionCallback};

static PyObject* _Nullable mod_CFTreeGetContext(PyObject* meth,
                                                PyObject* _Nonnull const* _Nonnull args,
                                                size_t nargs)
{
    CFTreeRef     tree;
    CFTreeContext context;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFTreeRef), args[0], &tree) < 0) {
        return NULL;
    }

    if (args[1] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "'context' must be None");
        return NULL;
    }

    context.version = 0;

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFTreeGetContext(tree, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    if (context.version != 0) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_ValueError, "retrieved context is not valid");
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (context.retain != mod_CFTreeRetainCallback) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_ValueError, "retrieved context is not supported");
        return NULL;
        // LCOV_EXCL_STOP
    }

    return PyObjC_ObjCToPython(@encode(id), &context.info);
}

static PyObject* _Nullable mod_CFTreeSetContext(PyObject* meth,
                                                PyObject* _Nonnull const* _Nonnull args,
                                                size_t nargs)
{
    CFTreeRef     tree;
    CFTreeContext context;
    NSObject*     info;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFTreeRef), args[0], &tree) < 0) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(id), args[1], &info) < 0) {
        return NULL;
    }

    context      = mod_CFTreeContext;
    context.info = info;

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFTreeSetContext(tree, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject* _Nullable mod_CFTreeCreate(PyObject* meth,
                                            PyObject* _Nonnull const* _Nonnull args,
                                            size_t nargs)
{
    CFTreeRef      tree;
    CFTreeContext  context;
    CFAllocatorRef allocator;
    NSObject*      info;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(id), args[1], &info) < 0) {
        return NULL;
    }

    context      = mod_CFTreeContext;
    context.info = info;

    tree = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            tree = CFTreeCreate(allocator, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    PyObject* py_tree = PyObjC_ObjCToPython(@encode(CFTreeRef), &tree);
    CFRelease(tree); /* we're donated a reference */

    return py_tree;
}

static PyObject* _Nullable mod_CFTreeGetChildren(PyObject* meth,
                                                 PyObject* _Nonnull const* _Nonnull args,
                                                 size_t nargs)
{
    CFTreeRef  tree;
    CFIndex    count;
    CFTreeRef* children = NULL;
    PyObject*  result;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFTreeRef), args[0], &tree) < 0) {
        return NULL;
    }

    if (args[1] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "buffer must be None");
        return NULL;
    }

    children = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            count    = CFTreeGetChildCount(tree);
            children = malloc(count * sizeof(CFTreeRef));
            if (children != NULL) { // LCOV_BR_EXCL_LINE
                CFTreeGetChildren(tree, children);
            }

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            count = -1;                          // LCOV_EXCL_LINE
            if (children != NULL) {              // LCOV_EXCL_LINE
                free(children);                  // LCOV_EXCL_LINE
                children = NULL;                 // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (children == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        if (!PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
            PyErr_NoMemory();    // LCOV_EXCL_LINE
        }
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        if (children) {
            free(children);
        }
        return NULL;
        // LCOV_EXCL_STOP
    }

    result = PyObjC_CArrayToPython(@encode(CFTreeRef), children, count);
    free(children);
    return result;
}

static int
setup_tree(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFTreeCreate, mod_CFTreeCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFTreeGetContext, mod_CFTreeGetContext)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFTreeSetContext, mod_CFTreeSetContext)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFTreeSetContext, mod_CFTreeSetContext)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFTreeGetChildren, mod_CFTreeGetChildren)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

NS_ASSUME_NONNULL_END
