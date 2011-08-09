/* Area:	ffi_call
   Purpose:	Promotion test.
   Limitations:	none.
   PR:		none.
   Originator:	From the original ffitest.c  */

/* { dg-do run } */
#include "ffitest.h"
static inline unsigned int promotion(short s1, short s2)
{
  unsigned int r = s1 << 16 | s2;

  return r;
}

int main (void)
{
  ffi_cif cif;
  ffi_type *args[MAX_ARGS];
  void *values[MAX_ARGS];
  ffi_arg rint;
  short us;
  short us2;
  unsigned long ul = 0;

  args[0] = &ffi_type_ushort;
  args[1] = &ffi_type_ushort;
  values[0] = &us;
  values[1] = &us2;
  
  /* Initialize the cif */
  CHECK(ffi_prep_cif(&cif, FFI_DEFAULT_ABI, 2, 
		     &ffi_type_uint, args) == FFI_OK);
  
  for (us = 55; us < 30000; us+=1034) {
    for (us2 = 100; us2 < 30000; us2+=1945) {
      ffi_call(&cif, FFI_FN(promotion), &rint, values);
      CHECK((unsigned int)rint == (us << 16 | us2));
    }
  }
  printf("%lu promotion2 tests run\n", ul);
  exit(0); 
}
