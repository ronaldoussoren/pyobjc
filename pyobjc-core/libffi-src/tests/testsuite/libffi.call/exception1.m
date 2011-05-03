/* Area:	ffi_call
   Purpose:	Check raising/catching exceptions
   Limitations:	none.
   PR:		none.
   Originator:	Ronald Oussoren */

/* { dg-do run } */
#include "ffitest.h"
#import <Foundation/Foundation.h>

static void raiseit(void)
{
  [NSException raise:NSInvalidArgumentException format:@"Dummy exception"];
}

int main (void)
{
  ffi_cif cif;
  ffi_type *args[MAX_ARGS];
  void *values[MAX_ARGS];
  int ok;

  NSAutoreleasePool* pool = [[NSAutoreleasePool alloc] init];


  /* Initialize the cif */
  CHECK(ffi_prep_cif(&cif, FFI_DEFAULT_ABI, 0, 
		     &ffi_type_void, args) == FFI_OK);
  
  ok = 0;
  NS_DURING
	ffi_call(&cif, FFI_FN(raiseit), NULL, values);
  NS_HANDLER
 	ok = 1;

  NS_ENDHANDLER
  
  CHECK(ok);

  [pool release];
  exit(0);

}
