/* Area:	ffi_call
   Purpose:	Check structures.
   Limitations:	none.
   PR:		none.
   Originator:	From the original ffitest.c  */

/* { dg-do run } */
#include "ffitest.h"

typedef struct
{
  double f;
  double i;
} test_structure_11;

static test_structure_11 struct9 (test_structure_11 ts)
{
  ts.f += 1;
  ts.i += 1;

  return ts;
}

int main (void)
{
  ffi_cif cif;
  ffi_type *args[MAX_ARGS];
  void *values[MAX_ARGS];
  ffi_type ts11_type;
  ffi_type *ts11_type_elements[3];
  ts11_type.size = 0;
  ts11_type.alignment = 0;
  ts11_type.type = FFI_TYPE_STRUCT;
  ts11_type.elements = ts11_type_elements;
  ts11_type_elements[0] = &ffi_type_double;
  ts11_type_elements[1] = &ffi_type_double;
  ts11_type_elements[2] = NULL;

  test_structure_11 ts11_arg;
  
  /* This is a hack to get a properly aligned result buffer */
  test_structure_11 *ts11_result = 
    (test_structure_11 *) malloc (sizeof(test_structure_11));
  
  args[0] = &ts11_type;
  values[0] = &ts11_arg;
  
  /* Initialize the cif */
  CHECK(ffi_prep_cif(&cif, FFI_DEFAULT_ABI, 1, &ts11_type, args) == FFI_OK);
  
  ts11_arg.f = 5.55;
  ts11_arg.i = 5.99;
  
  printf ("%g\n", ts11_arg.f);
  printf ("%g\n", ts11_arg.i);
  
  ffi_call(&cif, FFI_FN(struct9), ts11_result, values);

  printf ("%g\n", ts11_result->f);
  printf ("%g\n", ts11_result->i);
  
  CHECK(ts11_result->f == 5.55 + 1);
  CHECK(ts11_result->i == 5.99 + 1);

  free (ts11_result);
  exit(0);
}
