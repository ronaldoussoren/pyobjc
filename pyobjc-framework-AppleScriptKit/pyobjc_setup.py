"""
Generic setup.py file for PyObjC framework wrappers.

This file should only be changed in pyobjc-core and then copied
to all framework wrappers.
"""

__all__ = ('setup', 'Extension', 'Command')

import sys
from pkg_resources import Distribution

try:
    import setuptools

except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()

from setuptools.command import test
from setuptools.command import build_py

from distutils import log

extra_args=dict(
    use_2to3 = True,
)


class oc_build_py (build_py.build_py):
    def build_packages(self):
        log.info("overriding build_packages to copy PyObjCTest")
        p = self.packages
        self.packages = list(self.packages) + ['PyObjCTest']
        try:
            build_py.build_py.build_packages(self)
        finally:
            self.packages = p



class oc_test (test.test):
    def run_tests(self):
        import sys, os

        rootdir =  os.path.dirname(os.path.abspath(__file__))
        if rootdir in sys.path:
            sys.path.remove(rootdir)

        # Ensure that any installed versions of this package aren't on sys.path
        ei_cmd = self.get_finalized_command('egg_info')
        egg_name = ei_cmd.egg_name.replace('-', '_')

        to_remove = []
        for dirname in sys.path:
            bn = os.path.basename(dirname)
            if bn.startswith(egg_name + "-"):
                to_remove.append(dirname)

        for dirname in to_remove:
            log.info("removing installed %r from sys.path before testing"%(dirname,))
            sys.path.remove(dirname)

        # Actually run the tests
        if sys.version_info[0] == 2:
            sys.path.insert(0, rootdir)
    
        import PyObjCTest
        import unittest
        from pkg_resources import EntryPoint
        loader_ep = EntryPoint.parse("x="+self.test_loader)
        loader_class = loader_ep.load(require=False)

        unittest.main(None, None, [unittest.__file__]+self.test_args, testLoader=loader_class())



from setuptools import setup as _setup, Extension as _Extension, Command
from distutils.errors import DistutilsPlatformError
from distutils.command import build, install
from setuptools.command import develop, test, build_ext, install_lib
import pkg_resources
import shutil
import os
import plistlib
import sys
import __main__

CLASSIFIERS = filter(None,
"""
Development Status :: 5 - Production/Stable
Environment :: Console
Environment :: MacOS X :: Cocoa
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: MacOS :: MacOS X
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.1
Programming Language :: Python :: 3.2
Programming Language :: Objective C
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: User Interfaces
""".splitlines())


def get_os_level():
    pl = plistlib.readPlist('/System/Library/CoreServices/SystemVersion.plist')
    v = pl['ProductVersion']
    return '.'.join(v.split('.')[:2])

class pyobjc_install_lib (install_lib.install_lib):
    def get_exclusions(self):
        result = install_lib.install_lib.get_exclusions(self)
        for fn in install_lib._install_lib.get_outputs(self):
            if 'PyObjCTest' in fn:
                result[fn] = 1

        result['PyObjCTest'] = 1
        result[os.path.join(self.install_dir, 'PyObjCTest')] = 1
        for fn in os.listdir('PyObjCTest'):
            result[os.path.join('PyObjCTest', fn)] = 1
            result[os.path.join(self.install_dir, 'PyObjCTest', fn)] = 1

        return result



class pyobjc_build_ext (build_ext.build_ext):
    def run(self):

        # Ensure that the PyObjC header files are available
        # in 2.3 and later the headers are in the egg,
        # before that we ship a copy.
        dist, = pkg_resources.require('pyobjc-core')

        include_root = os.path.join(self.build_temp, 'pyobjc-include')
        if os.path.exists(include_root):
            shutil.rmtree(include_root)

        os.makedirs(include_root)
        if dist.has_metadata('include'):
            for fn in dist.metadata_listdir('include'):
                data = dist.get_metadata('include/%s'%(fn,))
                open(os.path.join(include_root, fn), 'w').write(data)

        else:
            data = gPyObjCAPI_H
            open(os.path.join(include_root, 'pyobjc-api.h'), 'w').write(data)

        for e in self.extensions:
            if include_root not in e.include_dirs:
                e.include_dirs.append(include_root)

        # Run the actual build
        build_ext.build_ext.run(self)

        # Then tweak the copy_extensions bit to ensure PyObjCTest gets
        # copied to the right place.
        extensions = self.extensions
        self.extensions = [
            e for e in extensions if e.name.startswith('PyObjCTest') ]
        self.copy_extensions_to_source()
        self.extensions = extensions



def Extension(*args, **kwds):
    """
    Simple wrapper about distutils.core.Extension that adds additional PyObjC 
    specific flags.
    """
    os_level = get_os_level()
    cflags =  ["-DPyObjC_BUILD_RELEASE=%02d%02d"%(tuple(map(int, os_level.split('.'))))]
    ldflags = []
    if os_level != '10.4':
        cflags.extend(['-isysroot','/'])
        ldflags.extend(['-isysroot','/'])
    else:
        cflags.append('-DNO_OBJC2_RUNTIME')

    if 'extra_compile_args' in kwds:
        kwds['extra_compile_args'] = kwds['extra_compile_args'] + cflags
    else:
        kwds['extra_compile_args'] = cflags

    if 'extra_link_args' in kwds:
        kwds['extra_link_args'] = kwds['extra_link_args'] + ldflags
    else:
        kwds['extra_link_args'] = ldflags

    return _Extension(*args, **kwds)


def setup(
        min_os_level=None,
        max_os_level=None,
        cmdclass=None,
        **kwds):


    k = kwds.copy()
    k.update(extra_args)

    os_level = get_os_level()
    os_compatible = True
    if sys.platform != 'darwin':
        os_compatible = False

    else:
        if min_os_level is not None:
            if os_level < min_os_level:
                os_compatible = False
        if max_os_level is not None:
            if os_level > max_os_level:
                os_compatible = False

    if cmdclass is None:
        cmdclass = {}
    else:
        cmdclass = cmdclass.copy()

    if not os_compatible:
        def create_command_subclass(base_class):
            if min_os_level != None:
                if max_os_level != None:
                    msg = "This distribution is only supported on MacOSX versions %s upto and including %s"%(
                            min_os_level, max_os_level)
                else:
                    msg = "This distribution is only support on MacOSX >= %s"%(min_os_level,)
            elif max_os_level != None:
                    msg = "This distribution is only support on MacOSX <= %s"%(max_os_level,)
            else:
                    msg = "This distribution is only support on MacOSX"

            class subcommand (base_class):
                def run(self):
                    raise DistutilsPlatformError(msg)

            return subcommand

        cmdclass['build'] = create_command_subclass(build.build)
        cmdclass['test'] = create_command_subclass(oc_test)
        cmdclass['install'] = create_command_subclass(pyobjc_install_lib)
        cmdclass['develop'] = create_command_subclass(develop.develop)
        cmdclass['build_py'] = create_command_subclass(oc_build_py)
    else:
        cmdclass['build_ext'] = pyobjc_build_ext
        cmdclass['install_lib'] = pyobjc_install_lib
        cmdclass['test'] = oc_test
        cmdclass['build_py'] = oc_build_py



    _setup(
        cmdclass=cmdclass, 
        long_description=__main__.__doc__,
        author='Ronald Oussoren',
        author_email='pyobjc-dev@lists.sourceforge.net',
        url='http://pyobjc.sourceforge.net',
        platforms = [ "MacOS X" ],
        package_dir = { '': 'Lib', 'PyObjCTest': 'PyObjCTest' },
        dependency_links = [],
        package_data = { '': ['*.bridgesupport'] },
        test_suite='PyObjCTest',
        zip_safe = False,
        **k
    ) 


gPyObjCAPI_H="""\
#ifndef PyObjC_API_H
#define PyObjC_API_H

/*
 * Use this in helper modules for the objc package, and in wrappers
 * for functions that deal with objective-C objects/classes
 * 
 * This header defines some utility wrappers for importing and using 
 * the core bridge. 
 *
 * This is the *only* header file that should be used to access 
 * functionality in the core bridge.
 *
 * WARNING: this file is not part of the public interface of PyObjC and
 * might change or be removed without warning or regard for backward
 * compatibility.
 */

#include "Python.h"
#include <objc/objc.h>

#import <Foundation/Foundation.h>

#ifndef CGFLOAT_DEFINED

#ifdef __LP64__
# error "Huh? 64-bit but no CFFloat available???"
#endif

typedef float CGFloat;
#define CGFLOAT_MIN FLT_MIN
#define CGFLOAT_MAX FLT_MAX
#define CGFLOAT_IS_DOUBLE 0
#define CGFLOAT_DEFINED

#endif /* CGFLOAT_DEFINED */


#ifndef NSINTEGER_DEFINED

#ifdef __LP64__
# error "Huh? 64-bit but no NSINTEGER available???"
#endif

typedef int NSInteger;
typedef unsigned int NSUInteger;

#define NSIntegerMax    LONG_MAX
#define NSIntegerMin    LONG_MIN
#define NSUIntegerMax   ULONG_MAX

#define NSINTEGER_DEFINED

#endif


#ifndef PyObjC_COMPAT_H
#if (PY_VERSION_HEX < 0x02050000)
typedef int Py_ssize_t;
#define PY_FORMAT_SIZE_T ""
#define Py_ARG_SIZE_T "n"
#define PY_SSIZE_T_MAX INT_MAX

#else

#define Py_ARG_SIZE_T "i"
#endif
#endif

#import <Foundation/NSException.h>

struct PyObjC_WeakLink {
	const char* name;
	void (*func)(void);
};


/* threading support */
#ifdef NO_OBJC2_RUNTIME
#define PyObjC_DURING \
		Py_BEGIN_ALLOW_THREADS \
		NS_DURING

#define PyObjC_HANDLER NS_HANDLER

#define PyObjC_ENDHANDLER \
		NS_ENDHANDLER \
		Py_END_ALLOW_THREADS
#else

#define	PyObjC_DURING \
		Py_BEGIN_ALLOW_THREADS \
		@try {

#define PyObjC_HANDLER } @catch(volatile NSObject* _localException) { \
		NSException* localException __attribute__((__unused__))= (NSException*)_localException;

#define PyObjC_ENDHANDLER \
		} \
		Py_END_ALLOW_THREADS

#endif

#define PyObjC_BEGIN_WITH_GIL \
	{ \
		PyGILState_STATE _GILState; \
		_GILState = PyGILState_Ensure(); 

#define PyObjC_GIL_FORWARD_EXC() \
		do { \
            PyObjCErr_ToObjCWithGILState(&_GILState); \
		} while (0)


#define PyObjC_GIL_RETURN(val) \
		do { \
			PyGILState_Release(_GILState); \
			return (val); \
		} while (0)

#define PyObjC_GIL_RETURNVOID \
		do { \
			PyGILState_Release(_GILState); \
			return; \
		} while (0)


#define PyObjC_END_WITH_GIL \
		PyGILState_Release(_GILState); \
	}



#include <objc/objc-runtime.h>

/* On 10.1 there are no defines for the OS version. */
#ifndef MAC_OS_X_VERSION_10_1
#define MAC_OS_X_VERSION_10_1 1010
#define MAC_OS_X_VERSION_MAX_ALLOWED MAC_OS_X_VERSION_10_1

#error "MAC_OS_X_VERSION_10_1 not defined. You aren't running 10.1 are you?"

#endif

#ifndef MAC_OS_X_VERSION_10_2
#define MAC_OS_X_VERSION_10_2 1020
#endif

#ifndef MAC_OS_X_VERSION_10_3
#define MAC_OS_X_VERSION_10_3 1030
#endif

#ifndef MAC_OS_X_VERSION_10_4
#define MAC_OS_X_VERSION_10_4 1040
#endif

#ifndef MAC_OS_X_VERSION_10_5
#define MAC_OS_X_VERSION_10_5 1050
#endif

/* Current API version, increase whenever:
 * - Semantics of current functions change
 * - Functions are removed
 * Do not increase when adding a new function, the struct_len field
 * can be used for detecting if a function has been added.
 *
 * HISTORY:
 * - Version 2.2 adds PyObjCUnsupportedMethod_IMP 
 *       and PyObjCUnsupportedMethod_Caller 
 * - Version 2.1 adds PyObjCPointerWrapper_Register 
 * - Version 2 adds an argument to PyObjC_InitSuper
 * - Version 3 adds another argument to PyObjC_CallPython
 * - Version 4 adds PyObjCErr_ToObjCGILState
 * - Version 4.1 adds PyObjCRT_AlignOfType and PyObjCRT_SizeOfType
 *         (PyObjC_SizeOfType is now deprecated)
 * - Version 4.2 adds PyObjCRT_SELName
 * - Version 4.3 adds PyObjCRT_SimplifySignature
 * - Version 4.4 adds PyObjC_FreeCArray, PyObjC_PythonToCArray and
 *   		PyObjC_CArrayToPython
 * - Version 5 modifies the signature for PyObjC_RegisterMethodMapping,
 *	PyObjC_RegisterSignatureMapping and PyObjCUnsupportedMethod_IMP,
 *      adds PyObjC_RegisterStructType and removes PyObjC_CallPython
 * - Version 6 adds PyObjCIMP_Type, PyObjCIMP_GetIMP and PyObjCIMP_GetSelector
 * - Version 7 adds PyObjCErr_AsExc, PyGILState_Ensure
 * - Version 8 adds PyObjCObject_IsUninitialized,
        removes PyObjCSelector_IsInitializer
 * - Version 9 (???)
 * - Version 10 changes the signature of PyObjCRT_SimplifySignature
 * - Version 11 adds PyObjCObject_Convert, PyObjCSelector_Convert,
     PyObjCClass_Convert, PyObjC_ConvertBOOL, and PyObjC_ConvertChar
 * - Version 12 adds PyObjCObject_New
 * - Version 13 adds PyObjCCreateOpaquePointerType
 * - Version 14 adds PyObjCObject_NewTransient, PyObjCObject_ReleaseTransient
 * - Version 15 changes the interface of PyObjCObject_New
 * - Version 16 adds PyObjC_PerformWeaklinking
 * - Version 17 introduces Py_ssize_t support
 * - Version 18 introduces several API incompatibilities
 */
#define PYOBJC_API_VERSION 18

#define PYOBJC_API_NAME "__C_API__"

/* 
 * Only add items to the end of this list!
 */
typedef int (RegisterMethodMappingFunctionType)(
			Class, 
			SEL, 
			PyObject *(*)(PyObject*, PyObject*, PyObject*),
			void (*)(void*, void*, void**, void*));

struct pyobjc_api {
	int	      api_version;	/* API version */
	size_t	      struct_len;	/* Length of this struct */
	PyTypeObject* class_type;	/* PyObjCClass_Type    */
	PyTypeObject* object_type;	/* PyObjCObject_Type   */
	PyTypeObject* select_type;	/* PyObjCSelector_Type */

	/* PyObjC_RegisterMethodMapping */
	RegisterMethodMappingFunctionType *register_method_mapping;

	/* PyObjC_RegisterSignatureMapping */
	int (*register_signature_mapping)(
			char*,
			PyObject *(*)(PyObject*, PyObject*, PyObject*),
			void (*)(void*, void*, void**, void*));

	/* PyObjCObject_GetObject */
	id (*obj_get_object)(PyObject*);

	/* PyObjCObject_ClearObject */
	void (*obj_clear_object)(PyObject*);

	/* PyObjCClass_GetClass */
	Class (*cls_get_class)(PyObject*);

	/* PyObjCClass_New */
	PyObject* (*cls_to_python)(Class cls);

	/* PyObjC_PythonToId */
	id (*python_to_id)(PyObject*);

	/* PyObjC_IdToPython */
	PyObject* (*id_to_python)(id);

	/* PyObjCErr_FromObjC */
	void (*err_objc_to_python)(NSException*);

	/* PyObjCErr_ToObjC */
	void (*err_python_to_objc)(void);

	/* PyObjC_PythonToObjC */
	int (*py_to_objc)(const char*, PyObject*, void*);

	/* PyObjC_ObjCToPython */
	PyObject* (*objc_to_py)(const char*, void*);

	/* PyObjC_SizeOfType */
	Py_ssize_t   (*sizeof_type)(const char*);

	/* PyObjCSelector_GetClass */
	Class	   (*sel_get_class)(PyObject* sel);

	/* PyObjCSelector_GetSelector */
	SEL	   (*sel_get_sel)(PyObject* sel);

	/* PyObjC_InitSuper */ 	
	void	(*fill_super)(struct objc_super*, Class, id);

	/* PyObjC_InitSuperCls */
	void	(*fill_super_cls)(struct objc_super*, Class, Class);

	/* PyObjCPointerWrapper_Register */ 
	int  (*register_pointer_wrapper)(
		        const char*, PyObject* (*pythonify)(void*),
			int (*depythonify)(PyObject*, void*)
		);

	void (*unsupported_method_imp)(void*, void*, void**, void*);
	PyObject* (*unsupported_method_caller)(PyObject*, PyObject*, PyObject*);

	/* PyObjCErr_ToObjCWithGILState */
	void (*err_python_to_objc_gil)(PyGILState_STATE* state);

	/* PyObjCRT_AlignOfType */
	Py_ssize_t (*alignof_type)(const char* typestr);

	/* PyObjCRT_SELName */
	const char* (*selname)(SEL sel);

	/* PyObjCRT_SimplifySignature */
	int (*simplify_sig)(char* signature, char* buf, size_t buflen);

	/* PyObjC_FreeCArray */
	void    (*free_c_array)(int,void*);

	/* PyObjC_PythonToCArray */
	int     (*py_to_c_array)(BOOL, BOOL, const char*, PyObject*, void**, Py_ssize_t*, PyObject**);
	
	/* PyObjC_CArrayToPython */
	PyObject* (*c_array_to_py)(const char*, void*, Py_ssize_t);

	/* PyObjC_RegisterStructType */
	PyObject* (*register_struct)(const char*, const char*, const char*, initproc, Py_ssize_t, const char**);

	/* PyObjCIMP_Type */
	PyTypeObject* imp_type;

	/* PyObjCIMP_GetIMP */
	IMP  (*imp_get_imp)(PyObject*);

	/* PyObjCIMP_GetSelector */
	SEL  (*imp_get_sel)(PyObject*);

	/* PyObjCErr_AsExc */
	NSException* (*err_python_to_nsexception)(void);

	/* PyGILState_Ensure */
	PyGILState_STATE (*gilstate_ensure)(void);

	/* PyObjCObject_IsUninitialized */
	int (*obj_is_uninitialized)(PyObject*);

	/* PyObjCObject_Convert */
	int (*pyobjcobject_convert)(PyObject*,void*);

	/* PyObjCSelector_Convert */
	int (*pyobjcselector_convert)(PyObject*,void*);

	/* PyObjCClass_Convert */
	int (*pyobjcclass_convert)(PyObject*,void*);

	/* PyObjC_ConvertBOOL */
	int (*pyobjc_convertbool)(PyObject*,void*);

	/* PyObjC_ConvertChar */
	int (*pyobjc_convertchar)(PyObject*,void*);

	/* PyObjCObject_New */
	PyObject* (*pyobjc_object_new)(id, int , int);

	/* PyObjCCreateOpaquePointerType */
	PyObject* (*pointer_type_new)(const char*, const char*, const char*);

	/* PyObject* PyObjCObject_NewTransient(id objc_object, int* cookie); */
	PyObject* (*newtransient)(id objc_object, int* cookie);

	/* void PyObjCObject_ReleaseTransient(PyObject* proxy, int cookie); */
	void (*releasetransient)(PyObject* proxy, int cookie);

	void (*doweaklink)(PyObject*, struct PyObjC_WeakLink*);

	const char* (*removefields)(char*, const char*);

	PyObject** pyobjc_null;

	int (*dep_c_array_count)(const char* type, Py_ssize_t count, BOOL strict, PyObject* value, void* datum);

	PyObject* (*varlistnew)(const char* tp, void* array);
};

#ifndef PYOBJC_BUILD

#ifndef PYOBJC_METHOD_STUB_IMPL
static struct pyobjc_api*	PyObjC_API;
#endif /* PYOBJC_METHOD_STUB_IMPL */

#define PyObjCObject_Check(obj) PyObject_TypeCheck(obj, PyObjC_API->object_type)
#define PyObjCClass_Check(obj)  PyObject_TypeCheck(obj, PyObjC_API->class_type)
#define PyObjCSelector_Check(obj)  PyObject_TypeCheck(obj, PyObjC_API->select_type)
#define PyObjCIMP_Check(obj)  PyObject_TypeCheck(obj, PyObjC_API->imp_type)
#define PyObjCObject_GetObject (PyObjC_API->obj_get_object)
#define PyObjCObject_ClearObject (PyObjC_API->obj_clear_object)
#define PyObjCClass_GetClass   (PyObjC_API->cls_get_class)
#define PyObjCClass_New 	     (PyObjC_API->cls_to_python)
#define PyObjCSelector_GetClass (PyObjC_API->sel_get_class)
#define PyObjCSelector_GetSelector (PyObjC_API->sel_get_sel)
#define PyObjC_PythonToId      (PyObjC_API->python_to_id)
#define PyObjC_IdToPython      (PyObjC_API->id_to_python)
#define PyObjCErr_FromObjC     (PyObjC_API->err_objc_to_python)
#define PyObjCErr_ToObjC       (PyObjC_API->err_python_to_objc)
#define PyObjCErr_ToObjCWithGILState       (PyObjC_API->err_python_to_objc_gil)
#define PyObjCErr_AsExc        (PyObjC_API->err_python_to_nsexception)
#define PyObjC_PythonToObjC    (PyObjC_API->py_to_objc)
#define PyObjC_ObjCToPython    (PyObjC_API->objc_to_py)
#define PyObjC_RegisterMethodMapping (PyObjC_API->register_method_mapping)
#define PyObjC_RegisterSignatureMapping (PyObjC_API->register_signature_mapping)
#define PyObjC_SizeOfType      (PyObjC_API->sizeof_type)
#define PyObjC_PythonToObjC   (PyObjC_API->py_to_objc)
#define PyObjC_ObjCToPython   (PyObjC_API->objc_to_py)
#define PyObjC_InitSuper	(PyObjC_API->fill_super)
#define PyObjC_InitSuperCls	(PyObjC_API->fill_super_cls)
#define PyObjCPointerWrapper_Register (PyObjC_API->register_pointer_wrapper)
#define PyObjCUnsupportedMethod_IMP (PyObjC_API->unsupported_method_imp)
#define PyObjCUnsupportedMethod_Caller (PyObjC_API->unsupported_method_caller)
#define PyObjCRT_SizeOfType      (PyObjC_API->sizeof_type)
#define PyObjCRT_AlignOfType	(PyObjC_API->alignof_type)
#define PyObjCRT_SELName	(PyObjC_API->selname)
#define PyObjCRT_SimplifySignature	(PyObjC_API->simplify_sig)
#define PyObjC_FreeCArray	(PyObjC_API->free_c_array)
#define PyObjC_PythonToCArray	(PyObjC_API->py_to_c_array)
#define PyObjC_CArrayToPython	(PyObjC_API->c_array_to_py)
#define PyObjC_RegisterStructType   (PyObjC_API->register_struct)
#define PyObjCIMP_GetIMP   (PyObjC_API->imp_get_imp)
#define PyObjCIMP_GetSelector   (PyObjC_API->imp_get_sel)
#define PyObjCObject_IsUninitialized (PyObjC_API->obj_is_uninitialized)
#define PyObjCObject_Convert (PyObjC_API->pyobjcobject_convert)
#define PyObjCSelector_Convert (PyObjC_API->pyobjcselector_convert)
#define PyObjCClass_Convert (PyObjC_API->pyobjcselector_convert)
#define PyObjC_ConvertBOOL (PyObjC_API->pyobjc_convertbool)
#define PyObjC_ConvertChar (PyObjC_API->pyobjc_convertchar)
#define PyObjCObject_New (PyObjC_API->pyobjc_object_new)
#define PyObjCCreateOpaquePointerType (PyObjC_API->pointer_type_new)
#define PyObjCObject_NewTransient (PyObjC_API->newtransient)
#define PyObjCObject_ReleaseTransient (PyObjC_API->releasetransient)
#define PyObjC_PerformWeaklinking (PyObjC_API->doweaklink)
#define PyObjCRT_RemoveFieldNames (PyObjC_API->removefields)
#define PyObjC_NULL		  (*(PyObjC_API->pyobjc_null))
#define PyObjC_DepythonifyCArray  (PyObjC_API->dep_c_array_count)
#define PyObjC_VarList_New  (PyObjC_API->varlistnew)


#ifndef PYOBJC_METHOD_STUB_IMPL

static int
PyObjC_ImportAPI(PyObject* calling_module)
{
	PyObject* m;
	PyObject* d;
	PyObject* api_obj;
	PyObject* name = PyString_FromString("objc");
	
	m = PyImport_Import(name);
	Py_DECREF(name);
	if (m == NULL) {
		return -1;
	}

	d = PyModule_GetDict(m);
	if (d == NULL) {
		PyErr_SetString(PyExc_RuntimeError, 
			"No dict in objc module");
		return -1;
	}

	api_obj = PyDict_GetItemString(d, PYOBJC_API_NAME);
	if (api_obj == NULL) {
		PyErr_SetString(PyExc_RuntimeError, 
			"No C_API in objc module");
		return -1;
	}
	PyObjC_API = PyCObject_AsVoidPtr(api_obj);
	if (PyObjC_API == NULL) {
		return 0;
	}
	if (PyObjC_API->api_version != PYOBJC_API_VERSION) {
		PyErr_SetString(PyExc_RuntimeError,
			"Wrong version of PyObjC C API");
		return -1;
	}
	
	if (PyObjC_API->struct_len < sizeof(struct pyobjc_api)) {
		PyErr_SetString(PyExc_RuntimeError,
			"Wrong struct-size of PyObjC C API");
		return -1;
	}

	Py_INCREF(api_obj);

	/* Current pyobjc implementation doesn't allow deregistering 
	 * information, avoid unloading of users of the C-API.
	 * (Yes this is ugle, patches to fix this situation are apriciated)
	 */
	Py_INCREF(calling_module);

	return 0;
}
#endif /* PYOBJC_METHOD_STUB_IMPL */

#else /* PyObjC_BUILD */

extern struct pyobjc_api	objc_api;

#endif /* !PYOBJC_BUILD */

#endif /*  PyObjC_API_H */
"""
