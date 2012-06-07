/* { dg-do run } */
#include "ffitest.h"

static long chars(long a,
		  char b1,
		  char b2,
		  char b3,
		  char b4,
		  char b5,
		  char b6,
		  char b7,
		  char b8,
		  char b9,
		  char b10,
		  char b11,
		  char b12,
		  char b13,
		  char b14,
		  char b15,
		  char b16)

{
  printf("%ld %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d\n",
	a, (int)b1, (int)b2, (int)b3, (int)b4, (int)b5, (int)b6, 
	(int)b7, (int)b8, (int)b9, (int)b10, (int)b11, (int)b12, 
	(int)b13, (int)b14, (int)b15, (int)b16);
  return a+b1+b2+b3+b4+b5+b6+b7+b8+b9+b10+b11+b12+b13+b14+b15+b16;
}

int main (void)
{
  ffi_cif cif;
  ffi_type *args[17];
  void *values[17];
  long a1,r;
  char bytes[16];
  int i;

  args[0] = &ffi_type_slong;
  values[i] = &a1;
  a1 = 0;

  for (i = 1; i < 17; i++)
    {
      args[i] = &ffi_type_sint8;
      values[i] = &bytes[i-1];
      bytes[i-1] = i;
    }

    /* Initialize the cif */
    CHECK(ffi_prep_cif(&cif, FFI_DEFAULT_ABI, 17, 
		       &ffi_type_slong, args) == FFI_OK);

    ffi_call(&cif, FFI_FN(chars), &r, values);
    /* dg-output: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 */

    printf("%ld\n", r);
    /* dg-output: 136 */

    r =  chars(a1, bytes[0], bytes[1], bytes[2], bytes[3],
		    bytes[4], bytes[5], bytes[6], bytes[7],
		    bytes[8], bytes[9], bytes[10], bytes[11],
		    bytes[12], bytes[13], bytes[14], bytes[15]);
    /* dg-output: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 */
    printf("%ld\n", r);
    /* dg-output: 136 */

    return 0;
}
