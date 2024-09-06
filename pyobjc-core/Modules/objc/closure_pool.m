/*
 * A simple allocator for closure. This assumes that most closures are kept
 * alive forever and we therefore don't have to return storage to the OS.
 *
 * These functions are only used when deploying to macOS 10.14 or earlier.
 *
 */
#include "pyobjc.h"
#include "closure_pool.h"

#if defined(__x86_64__) && MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_15

#include <sys/mman.h>
#include <sys/sysctl.h>

NS_ASSUME_NONNULL_BEGIN

typedef struct freelist {
    struct freelist* _Nullable next;
} freelist;

#ifdef Py_GIL_DISABLED
/*
 * Mutex protecting *closure_freelist*. There is no need for
 * minimizing the amount of code protected by the lock, allocating
 * of new closures is not anywhere close to being on a fast path.
 */
static PyMutex freelist_mutex = {0};
#endif

static freelist* closure_freelist = NULL;

#ifdef MAP_JIT

/*
 * Checks  if the current system requires MAP_JIT. This
 * flag only needs to be used on macOS 10.14 or later.
 */
static int
use_map_jit(void)
{
    static _Atomic int cached_result = -1;

    if (cached_result == -1) {
        char   buf[256];
        size_t buflen = 256;

        /*
         * In the unlikely event that sysctlbyname fails, or
         * returns a value that is not usable we disable MAP_JIT
         * support
         */

        if (sysctlbyname("kern.osrelease", buf, &buflen, NULL, 0) == -1) {
            cached_result = 0;
        } else {
            long ver      = strtol(buf, NULL, 10);
            cached_result = (ver >= 18);
        }
    }

    return cached_result;
}

#endif

static freelist* _Nullable allocate_block(void)
{

    /* Allocate ffi_closure in groups of 10 VM pages */
#define BLOCKSIZE ((PAGE_SIZE * 10) / sizeof(ffi_closure*))

#ifdef MAP_JIT
    freelist* newblock = mmap(
        NULL, BLOCKSIZE * sizeof(ffi_closure), PROT_READ | PROT_WRITE | PROT_EXEC,
        use_map_jit() ? MAP_PRIVATE | MAP_ANON | MAP_JIT : MAP_PRIVATE | MAP_ANON, -1, 0);

#else  /* !MAP_JIT */
    freelist* newblock =
        mmap(NULL, BLOCKSIZE * sizeof(ffi_closure), PROT_READ | PROT_WRITE | PROT_EXEC,
             MAP_PRIVATE | MAP_ANON, -1, 0);
#endif /* !MAP_JIT */

    size_t i;

    if (newblock == MAP_FAILED) {
        PyErr_NoMemory();
        return NULL;
    }
    for (i = 0; i < BLOCKSIZE - 1; i++) {
        ((freelist*)(((ffi_closure*)newblock) + i))->next =
            (freelist*)(((ffi_closure*)newblock) + (i + 1));
    }

    ((freelist*)(((ffi_closure*)newblock) + (BLOCKSIZE - 1)))->next = NULL;
    return newblock;
}

ffi_closure* _Nullable PyObjC_ffi_closure_alloc(size_t size, void** codeloc)
{
    if (size != sizeof(ffi_closure)) {
        PyErr_SetString(PyObjCExc_Error, "Allocating closure of unexpected size");
        return NULL;
    }
    PyObjC_Assert(codeloc, NULL);
#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&freelist_mutex);
#endif
    if (closure_freelist == NULL) {
        closure_freelist = allocate_block();
        if (closure_freelist == NULL) {
#ifdef Py_GIL_DISABLED
            PyMutex_Unlock(&freelist_mutex);
#endif
            return NULL;
        }
    }
    ffi_closure* result = (ffi_closure*)closure_freelist;
    closure_freelist    = closure_freelist->next;
    *codeloc            = (void*)result;
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&freelist_mutex);
#endif
    return result;
}

int
PyObjC_ffi_closure_free(ffi_closure* cl)
{
#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&freelist_mutex);
#endif
    ((freelist*)cl)->next = closure_freelist;
    closure_freelist      = (freelist*)cl;
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&freelist_mutex);
#endif
    return 0;
}

NS_ASSUME_NONNULL_END

#endif
