/*
 * A simple allocator for closure. This assumes that most closures are kept
 * alive forever and we therefore don't have to return storage to the OS.
 */
#include "pyobjc.h"

#include <sys/mman.h>

typedef struct freelist {
	struct freelist* next;
} freelist;

static freelist* closure_freelist = NULL;


static freelist* allocate_block(void)
{

	/* Allocate ffi_closure in groups of 10 VM pages */
#define BLOCKSIZE ((PAGE_SIZE*10)/sizeof(ffi_closure*))

	freelist* newblock = mmap(NULL, BLOCKSIZE * sizeof(ffi_closure),
		PROT_READ|PROT_WRITE|PROT_EXEC,
		MAP_PRIVATE|MAP_ANON, -1, 0);
	size_t i;

	if (newblock == (void*)-1) {
		PyErr_NoMemory();
		return NULL;
	}
	for (i = 0; i < BLOCKSIZE-1; i++) {
		((freelist*)(((ffi_closure*)newblock)+i))->next = 
			(freelist*)(((ffi_closure*)newblock)+(i+1));
	}

	((freelist*)(((ffi_closure*)newblock)+(BLOCKSIZE-1)))->next = NULL;
	return newblock;
}



ffi_closure* 
PyObjC_malloc_closure(void)
{
	if (closure_freelist == NULL) {
		closure_freelist = allocate_block();
		if (closure_freelist == NULL) {
			return NULL;
		}
	}
	ffi_closure* result = (ffi_closure*)closure_freelist;
	closure_freelist = closure_freelist->next;
	return result;
}

int
PyObjC_free_closure(ffi_closure* cl)
{
	((freelist*)cl)->next = closure_freelist;
	closure_freelist = (freelist*)cl;
	return 0;
}
