/* Area:	ffi_call
   Purpose:	Check strlen function call.
   Limitations:	none.
   PR:		none.
   Originator:	From the original ffitest.c  */

/* { dg-do run } */
#include "ffitest.h"

static int array_reverse(float *s, int len)
{
	int i;

	for (i = 0; i < len/2;i++) {
		float tmp = s[i];
		s[i] = s[len-1-i];
		s[len-1-i] = tmp;
	}
	return 1;
}

int main (void)
{
  ffi_cif cif;
  ffi_type *args[MAX_ARGS];
  void *values[MAX_ARGS];

  int rint;
  float value[] = { 1.0, 2.0, 3.0, 4.0, 5.0 };

  struct X {
	  int rint;
	  float* input;
	  int count;
  } valbuf;

  valbuf.input = value;
  valbuf.count = 5;

  args[0] = &ffi_type_pointer;
  args[1] = &ffi_type_sint;
  values[0] = (void*) &valbuf.input;
  values[1] = (void*) &valbuf.count;

  /* Initialize the cif */
  CHECK(ffi_prep_cif(&cif, FFI_DEFAULT_ABI, 2, 
		     &ffi_type_sint, args) == FFI_OK);

  printf("%f\n", valbuf.input[0]);
  
  ffi_call(&cif, FFI_FN(array_reverse), &valbuf.rint, values);

  printf("%f\n", valbuf.input[0]);
  CHECK(valbuf.rint == 1);
  CHECK(valbuf.count == 5);
  CHECK(valbuf.input[0] == 5.0);
  CHECK(valbuf.input[1] == 4.0);
  CHECK(valbuf.input[2] == 3.0);
  CHECK(valbuf.input[3] == 2.0);
  CHECK(valbuf.input[4] == 1.0);

  return 0;
}
  
