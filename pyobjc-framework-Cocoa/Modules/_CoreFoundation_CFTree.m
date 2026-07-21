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
        PyErr_SetString(PyExc_ValueError, "invalid context");
        return NULL;
    }

    context.version = 0;

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFTreeGetContext(tree, &context);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (context.version != 0) {
        PyErr_SetString(PyExc_ValueError, "retrieved context is not valid");
        return NULL;
    }

    if (context.retain != mod_CFTreeRetainCallback) {
        PyErr_SetString(PyExc_ValueError, "retrieved context is not supported");
        return NULL;
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

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

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

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (tree == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

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
            if (children != NULL) {
                CFTreeGetChildren(tree, children);
            }

        } @catch (NSException* localException) {
            count = -1;
            if (children != NULL) {
                free(children);
                children = NULL;
            }
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (children == NULL) {
        if (!PyErr_Occurred()) {
            PyErr_NoMemory();
        }
        return NULL;
    }

    if (PyErr_Occurred()) {
        if (children) {
            free(children);
        }
        return NULL;
    }

    result = PyObjC_CArrayToPython(@encode(CFTreeRef), children, count);
    free(children);
    return result;
}

static int
setup_tree(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFTreeCreate, mod_CFTreeCreate) == -1) {
        return -1;
    }
    if (PyObjCRegister_FunctionCaller(CFTreeGetContext, mod_CFTreeGetContext) == -1) {
        return -1;
    }
    if (PyObjCRegister_FunctionCaller(CFTreeSetContext, mod_CFTreeSetContext) == -1) {
        return -1;
    }
    if (PyObjCRegister_FunctionCaller(CFTreeSetContext, mod_CFTreeSetContext) == -1) {
        return -1;
    }
    if (PyObjCRegister_FunctionCaller(CFTreeGetChildren, mod_CFTreeGetChildren) == -1) {
        return -1;
    }
    return 0;
}

NS_ASSUME_NONNULL_END
