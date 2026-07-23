/*
 * Manual wrappers for CFBinaryHeap
 */
NS_ASSUME_NONNULL_BEGIN

@interface NSObject (OC_Comparison)
- (NSComparisonResult)compare:(NSObject*)other;
@end

static const void*
mod_binheap_retain(CFAllocatorRef allocator __attribute__((__unused__)), const void* ptr)
{
    if (ptr) {
        CFRetain(ptr);
    }
    return ptr;
}

static void
mod_binheap_release(CFAllocatorRef allocator __attribute__((__unused__)), const void* ptr)
{
    if (ptr) {
        CFRelease(ptr);
    }
}

// LCOV_EXCL_START
// This function cannot be triggered during testing.
static CFStringRef
mod_binheap_copydescription(const void* ptr)
{
    CFStringRef r = CFCopyDescription(ptr);
    return r;
}
// LCOV_EXCL_STOP

CFComparisonResult
mod_binheap_compare(const void* ptr1, const void* ptr2,
                    void* info __attribute__((__unused__)))
{
    NSObject* o1 = (NSObject*)ptr1;
    NSObject* o2 = (NSObject*)ptr2;

    NSComparisonResult result = [o1 compare:o2];
    return (CFComparisonResult)result;
}

static CFBinaryHeapCallBacks mod_NSObjectBinaryHeapCallbacks = {
    0, mod_binheap_retain, mod_binheap_release, mod_binheap_copydescription,
    mod_binheap_compare};

static PyObject* _Nullable mod_CFBinaryHeapCreate(PyObject* meth,
                                                  PyObject* _Nonnull const* _Nonnull args,
                                                  size_t nargs)
{
    Py_ssize_t      count = -1;
    CFAllocatorRef  allocator;
    CFBinaryHeapRef heap;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[1], &count) < 0) {
        return NULL;
    }

    heap = CFBinaryHeapCreate(allocator, count, &mod_NSObjectBinaryHeapCallbacks, NULL);

    PyObject* result = PyObjC_ObjCToPython(@encode(CFBinaryHeapRef), &heap);
    if (heap) {
        CFRelease(heap);
    }
    return result;
}

static PyObject* _Nullable mod_CFBinaryHeapGetValues(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFBinaryHeapRef heap;

    if (PyObjC_CheckArgCount(meth, 1, 1, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFBinaryHeapRef), args[0], &heap) < 0) {
        return NULL;
    }

    CFIndex    count   = CFBinaryHeapGetCount(heap);
    NSObject** members = malloc(sizeof(NSObject*) * count);
    if (members == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }
    memset(members, 0, sizeof(NSObject*) * count);

    CFBinaryHeapGetValues(heap, (const void**)members);
    PyObject* result =
        PyObjC_CArrayToPython(@encode(NSObject*), members, (Py_ssize_t)count);
    free(members);
    return result;
}

static int
setup_cfbinaryheap(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFBinaryHeapCreate, mod_CFBinaryHeapCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFBinaryHeapGetValues, mod_CFBinaryHeapGetValues)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

NS_ASSUME_NONNULL_END
