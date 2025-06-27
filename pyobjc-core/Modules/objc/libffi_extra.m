#include "libffi_extra.h"
#include "closure_pool.h"
#include <ffi/ffi.h>

int
alloc_prepped_closure(ffi_closure** cl, ffi_cif* cif, void** codeloc, void* func,
                      void* userdata)
{
    int rv;
    *cl      = NULL;
    *codeloc = NULL;

    /* And finally create the actual closure */
#ifdef HAVE_CLOSURE_POOL

#if PyObjC_BUILD_RELEASE >= 1015
    if (@available(macOS 10.15, *)) { // LCOV_BR_EXCL_LINE
        (*cl) = ffi_closure_alloc(sizeof(**cl), codeloc);
    } else
#endif
    {
        (*cl) = PyObjC_ffi_closure_alloc(sizeof(**cl), codeloc);
    }
#else
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability-new"
    (*cl) = ffi_closure_alloc(sizeof(**cl), codeloc);
#pragma clang diagnostic pop
#endif
    if (*cl == NULL) { // LCOV_BR_EXCL_LINE
        return -1;     // LCOV_EXCL_LINE
    }

#ifdef __arm64__

    /* This pragma is needed because we compile with deployment
     * target 10.9 even for arm64.
     */
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability-new"

    rv = ffi_prep_closure_loc(*cl, cif, (void (*)(ffi_cif*, void*, void**, void*))func,
                              userdata, *codeloc);

#pragma clang diagnostic pop

#else /* x86_64 */

#if PyObjC_BUILD_RELEASE >= 1015

    if (@available(macOS 10.15, *)) { // LCOV_BR_EXCL_LINE
        rv = ffi_prep_closure_loc(
            *cl, cif, (void (*)(ffi_cif*, void*, void**, void*))func, userdata, *codeloc);
    } else {
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

        rv = ffi_prep_closure(*cl, cif, (void (*)(ffi_cif*, void*, void**, void*))func,
                              userdata);

#pragma clang diagnostic pop
    }

#else  /* PyObjC_BUILD_RELEASE < 1015 */
    rv = ffi_prep_closure(*cl, cif, func, userdata);
#endif /* PyObjC_BUILD_RELEASE < 1015 */

#endif /* !__arm64__ */

    return rv == FFI_OK ? 0 : -1;
}

extern void
free_closure_from_codeloc(void* codeloc, ffi_cif** cif, void** userdata)
{
    ffi_closure* cl;

#ifdef HAVE_CLOSURE_POOL

#if PyObjC_BUILD_RELEASE >= 1015
    if (@available(macOS 10.15, *)) { // LCOV_BR_EXCL_LINE
        cl        = ffi_find_closure_for_code_np(codeloc);
        *cif      = cl->cif;
        *userdata = cl->user_data;
        ffi_closure_free(cl);
    } else
#endif
    {
        cl        = (ffi_closure*)codeloc;
        *cif      = cl->cif;
        *userdata = cl->user_data;
        PyObjC_ffi_closure_free(cl);
    }
#else
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability-new"
    cl        = ffi_find_closure_for_code_np(codeloc);
    *cif      = cl->cif;
    *userdata = cl->user_data;
    ffi_closure_free(cl);
#pragma clang diagnostic pop
#endif
}
