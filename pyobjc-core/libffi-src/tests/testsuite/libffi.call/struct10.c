/* Area:	ffi_call
   Purpose:	Check structures.
   Limitations:	none.
   PR:		none.
   Originator:	RonaldOussoren@mac.com */

/* { dg-do run } */
#include "ffitest.h"

typedef struct {
	float x;
	float y;
} point;

typedef struct
{
  point l;
  point r;
} test_structure_10;

static test_structure_10 struct10 (test_structure_10 ts)
{
  ts.r.x += 1.0;
  ts.r.y += 1.5;
  ts.l.x += 2.0;
  ts.l.y += 2.5;

  return ts;
}

static test_structure_10 struct10b (test_structure_10 ts)
{
	return struct10(ts);
}

int main (void)
{
  ffi_cif cif;
  ffi_type *args[MAX_ARGS];
  void *values[MAX_ARGS];
  ffi_type ts10_type;
  ffi_type *ts10_type_elements[3];
  ffi_type ts10p_type;
  ffi_type *ts10p_type_elements[3];

  ts10p_type.size = 0;
  ts10p_type.alignment = 0;
  ts10p_type.type = FFI_TYPE_STRUCT;
  ts10p_type.elements = ts10p_type_elements;
  ts10p_type_elements[0] = &ffi_type_float;
  ts10p_type_elements[1] = &ffi_type_float;
  ts10p_type_elements[2] = NULL;

  ts10_type.size = 0;
  ts10_type.alignment = 0;
  ts10_type.type = FFI_TYPE_STRUCT;
  ts10_type.elements = ts10_type_elements;
  ts10_type_elements[0] = &ts10p_type;
  ts10_type_elements[1] = &ts10p_type;
  ts10_type_elements[2] = NULL;

  test_structure_10 ts10_arg;
  
  /* This is a hack to get a properly aligned result buffer */
  test_structure_10 *ts10_result = 
    (test_structure_10 *) malloc (sizeof(test_structure_10));
  
  args[0] = &ts10_type;
  values[0] = &ts10_arg;
  
  /* Initialize the cif */
  CHECK(ffi_prep_cif(&cif, FFI_DEFAULT_ABI, 1, &ts10_type, args) == FFI_OK);
  
  ts10_arg.r.x = 1.44;
  ts10_arg.r.y = 2.44;
  ts10_arg.l.x = 3.44;
  ts10_arg.l.y = 4.44;
  
  printf ("%g\n", ts10_arg.r.x);
  printf ("%g\n", ts10_arg.r.y);
  printf ("%g\n", ts10_arg.l.x);
  printf ("%g\n", ts10_arg.l.y);
  
  ffi_call(&cif, FFI_FN(struct10b), ts10_result, values);

  printf ("%g\n", ts10_result->r.x);
  printf ("%g\n", ts10_result->r.y);
  printf ("%g\n", ts10_result->l.x);
  printf ("%g\n", ts10_result->l.y);

  CHECK(ts10_result->r.x == 1.44f + 1.0);
  CHECK(ts10_result->r.y == 2.44f + 1.5);
  CHECK(ts10_result->l.x == 3.44f + 2.0);
  CHECK(ts10_result->l.y == 4.44f + 2.5);

  free (ts10_result);
  exit(0);
}
