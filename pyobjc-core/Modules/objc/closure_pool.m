/*
 * First a trivial implementation, if this works out I'll write a more memory-efficient one
 */
#include "pyobjc.h"

#include <sys/mman.h>

ffi_closure* 
PyObjC_malloc_closure(void)
{
	ffi_closure* page = mmap(NULL, sizeof(ffi_closure*),
		PROT_READ|PROT_WRITE|PROT_EXEC,
		MAP_PRIVATE|MAP_ANON, -1, 0);
	if (page == (void*)-1) {
		PyErr_NoMemory();
		return NULL;
	}
	return page;
}

int
PyObjC_free_closure(ffi_closure* cl)
{
	int rv = munmap(cl, sizeof(ffi_closure));
	if (rv == -1) {
		PyErr_NoMemory();
		return -1;
	}
}
