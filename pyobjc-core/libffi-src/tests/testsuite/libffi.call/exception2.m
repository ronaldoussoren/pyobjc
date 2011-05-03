/* Area:	ffi_call
   Purpose:	Check raising/catching exceptions
   Limitations:	none.
   PR:		none.
   Originator:	Ronald Oussoren */

/* { dg-do run } */
#include "ffitest.h"
#import <Foundation/Foundation.h>

static void
closure_raise(ffi_cif* cif,void* resp,void** args, void* userdata)
{
  [NSException raise:NSInvalidArgumentException format:@"Dummy exception"];
}


typedef void (*testfunc)(void);

int main (void)
{
  ffi_cif cif;
  ffi_type *args[MAX_ARGS];
  void *values[MAX_ARGS];
  int ok;

#ifndef USING_MMAP
  static ffi_closure cl;
#endif
  ffi_closure *pcl;

#ifdef USING_MMAP
  pcl = allocate_mmap (sizeof(ffi_closure));
#else
  pcl = &cl;
#endif

 NSAutoreleasePool* pool = [[NSAutoreleasePool alloc] init];





  /* Initialize the cif */
  CHECK(ffi_prep_cif(&cif, FFI_DEFAULT_ABI, 0, 
		     &ffi_type_void, args) == FFI_OK);
  
  CHECK(ffi_prep_closure(pcl, &cif, closure_raise,
                         (void *) 3 /* userdata */) == FFI_OK);
  ok = 0;
  NS_DURING
	((testfunc)pcl)();
  NS_HANDLER
 	ok = 1;

  NS_ENDHANDLER
  
  CHECK(ok);

  [pool release];
  exit(0);
}
