/*
 * Special wrappers for NSArray methods with 'difficult' arguments.
 *
 * TODO:
 *
 * -apply:context:
 * -arrayByAddingObjects:count:
 * -arrayWithObjects:count:
 * -getObjects:
 * -getObjects:range:
 * -initWithObjects:count:
 * -sortedArrayUsingFunction:context:
 * -sortedArrayUsingFunction:context:hint:
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"


static int 
_pyobjc_install_NSArray(void)
{
	Class classNSDictionary = objc_lookUpClass("NSArray");

	return 0;
}
