/* { dg-do run } */

#include "ffitest.h"

static int
base_func(void* self, void* args, void* kwds)
{
  printf("%ld %ld %ld\n", (long)self, (long)args, (long)kwds);
  return -42;
}


static void
closure_test_fn7(ffi_cif* cif,void* resp,void** args, void* userdata)
{
   *(int*)resp = base_func(*(void**)args[0], *(void**)args[1], *(void**)args[2]);
}

typedef int (*closure_test_type7)(void*, void*, void*);

int main (void)
{
  ffi_cif cif;
#ifndef USING_MMAP
  static ffi_closure cl;
#endif
  ffi_closure *pcl;
  ffi_type * cl_arg_types[3];
  int i, res;
#ifdef USING_MMAP
  pcl = allocate_mmap (sizeof(ffi_closure));
#else
  //pcl = &cl;
  pcl = malloc(sizeof(*pcl));

#endif

  cl_arg_types[0] = &ffi_type_pointer;
  cl_arg_types[1] = &ffi_type_pointer;
  cl_arg_types[2] = &ffi_type_pointer;

  /* Initialize the cif */
  CHECK(ffi_prep_cif(&cif, FFI_DEFAULT_ABI, 3,
		     &ffi_type_sint, cl_arg_types) == FFI_OK);

  CHECK(ffi_prep_closure(pcl, &cif, closure_test_fn7,
			 (void *) 99 /* userdata */) == FFI_OK);

  base_func(4, 5, 6);
  /* { dg-output "4 5 6\n" } */

  (*((closure_test_type7)pcl))((void*)1, (void*)2, (void*)3);
  /* { dg-output "1 2 3\n" } */

  exit(0);
}
