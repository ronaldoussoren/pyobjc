#include <Python.h>
#include "pyobjc-api.h"

#import <CoreServices/CoreServices.h>

static const void* 
mod_retain(const void* info) 
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_INCREF((PyObject*)info);
	PyGILState_Release(state);
	return info;
}

static void
mod_release(const void* info)
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_DECREF((PyObject*)info);
	PyGILState_Release(state);
}


static CFStreamClientContext mod_CFStreamClientContext = {
	0,		
	NULL,
	(void*(*)(void*))mod_retain,
	(void(*)(void*))mod_release,
	NULL
};

static CFHostClientContext mod_CFHostClientContext = {
	0,
	NULL,
	mod_retain,
	mod_release,
	0
};

#if PyObjC_BUILD_RELEASE >= 1005
static void
m_CFProxyAutoConfigurationResultCallback(void* _context, CFArrayRef proxyList, CFErrorRef error)
{
	PyObject* context = (PyObject*)_context;

	PyGILState_STATE state = PyGILState_Ensure();

	PyObject* py_func = PyTuple_GET_ITEM(context, 0);
	PyObject* py_ctx = PyTuple_GET_ITEM(context, 1);

	PyObject* py_list = PyObjC_IdToPython((NSObject*)proxyList);
	if (py_list == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}
	PyObject* py_error = PyObjC_IdToPython((NSObject*)error);
	if (py_error == NULL) {
		Py_DECREF(py_list);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	PyObject* rv = PyObject_CallFunction(py_func, "ONN",
			py_ctx, py_list, py_error);

	if (rv == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}
	Py_DECREF(rv);

	PyGILState_Release(state);
}
#endif

static void
m_CFHostClientCallBack(CFHostRef host, CFHostInfoType typeInfo, const CFStreamError* error, void* _context)
{
	PyObject* context = (PyObject*)_context;

	PyGILState_STATE state = PyGILState_Ensure();

	PyObject* py_func = PyTuple_GET_ITEM(context, 0);
	PyObject* py_ctx = PyTuple_GET_ITEM(context, 1);

	PyObject* py_host = PyObjC_IdToPython((NSObject*)host);
	if (py_host == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}
	PyObject* py_info = PyObjC_ObjCToPython(@encode(CFHostInfoType), &typeInfo);
	if (py_info == NULL) {
		Py_DECREF(py_host);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

#ifdef __LP64__
	PyObject* py_error = PyObjC_ObjCToPython("{_CFStreamError=qi}", (void*)error);
#else
	PyObject* py_error = PyObjC_ObjCToPython("{_CFStreamError=ii}", (void*)error);
#endif
	if (py_error == NULL) {
		Py_DECREF(py_host);
		Py_DECREF(py_info);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	PyObject* rv = PyObject_CallFunction(py_func, "NNNO",
			py_host, py_info, py_error, py_ctx);

	if (rv == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}
	Py_DECREF(rv);

	PyGILState_Release(state);
}


#if PyObjC_BUILD_RELEASE >= 1006
  /* This function is available on 10.5 or later, but the prototype isn't in the headers on 10.5 */
static PyObject*
m_CFNetworkExecuteProxyAutoConfigurationScript(PyObject* mod __attribute__((__unused__)),
		PyObject* args)
{
	CFStringRef script;
	CFURLRef    url;
	PyObject*   callback;
	PyObject*   ctx;
	PyObject*   py_script;
	PyObject*   py_url;

	if (!PyArg_ParseTuple(args, "OOOO", &py_script, &py_url,
				&callback, &ctx)) {
		return NULL;
	}

	script = (CFStringRef)PyObjC_PythonToId(py_script);
	if (PyErr_Occurred()) {
		return NULL;
	}

	url = (CFURLRef)PyObjC_PythonToId(py_url);
	if (PyErr_Occurred()) {
		return NULL;
	}

	PyObject* py_context = Py_BuildValue("OO", callback, ctx);
	if (py_context == NULL) {
		return NULL;
	}

	CFStreamClientContext context = mod_CFStreamClientContext;
	context.info = py_context;

	CFRunLoopSourceRef ref = NULL;

	PyObjC_DURING
		ref = CFNetworkExecuteProxyAutoConfigurationScript(
				script, url, 
				m_CFProxyAutoConfigurationResultCallback,
				&context);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		ref = NULL;

	PyObjC_ENDHANDLER

	Py_DECREF(py_context);

	if (PyErr_Occurred()) {
		return NULL;
	}

	PyObject* rv = PyObjC_IdToPython((NSObject*)ref);

	return rv;
}
#endif

#if PyObjC_BUILD_RELEASE >= 1005
static PyObject*
m_CFNetworkExecuteProxyAutoConfigurationURL(PyObject* mod __attribute__((__unused__)),
		PyObject* args)
{
	CFURLRef    script;
	CFURLRef    url;
	PyObject*   callback;
	PyObject*   ctx;
	PyObject*   py_script;
	PyObject*   py_url;

	if (!PyArg_ParseTuple(args, "OOOO", &py_script, &py_url,
				&callback, &ctx)) {
		return NULL;
	}

	script = (CFURLRef)PyObjC_PythonToId(py_script);
	if (PyErr_Occurred()) {
		return NULL;
	}

	url = (CFURLRef)PyObjC_PythonToId(py_url);
	if (PyErr_Occurred()) {
		return NULL;
	}

	PyObject* py_context = Py_BuildValue("OO", callback, ctx);
	if (py_context == NULL) {
		return NULL;
	}

	CFStreamClientContext context = mod_CFStreamClientContext;
	context.info = py_context;

	CFRunLoopSourceRef ref = NULL;

	PyObjC_DURING
		ref = CFNetworkExecuteProxyAutoConfigurationURL(
				script, url, 
				m_CFProxyAutoConfigurationResultCallback,
				&context);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		ref = NULL;

	PyObjC_ENDHANDLER

	Py_DECREF(py_context);

	if (PyErr_Occurred()) {
		return NULL;
	}

	PyObject* rv = PyObjC_IdToPython((NSObject*)ref);

	return rv;
}
#endif  /* OSX 10.5 */

static PyObject*
m_CFHostSetClient(PyObject* mod __attribute__((__unused__)),
		PyObject* args)
{
	CFHostRef   host;
	PyObject*   callback;
	PyObject*   ctx;
	PyObject*   py_host;
	Boolean ok = 0;

	if (!PyArg_ParseTuple(args, "OOO", &py_host, 
				&callback, &ctx)) {
		return NULL;
	}

	host = (CFHostRef)PyObjC_PythonToId(py_host);
	if (PyErr_Occurred()) {
		return NULL;
	}

	if (callback == Py_None) {
		PyObjC_DURING
			ok = CFHostSetClient(host, NULL, NULL);
		PyObjC_HANDLER
			PyObjCErr_FromObjC(localException);

		PyObjC_ENDHANDLER

		if (PyErr_Occurred()) {
			return NULL;
		}

		return PyBool_FromLong(!!ok);
	}

	PyObject* py_context = Py_BuildValue("OO", callback, ctx);
	if (py_context == NULL) {
		return NULL;
	}

	CFHostClientContext context = mod_CFHostClientContext;
	context.info = py_context;


	PyObjC_DURING
		ok = CFHostSetClient(
				host,
				m_CFHostClientCallBack,
				&context);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF(py_context);

	if (PyErr_Occurred()) {
		return NULL;
	}

	return PyBool_FromLong(!!ok);
}



static PyMethodDef mod_methods[] = {
#if PyObjC_BUILD_RELEASE >= 1006
	{
		"CFNetworkExecuteProxyAutoConfigurationScript",
		(PyCFunction)m_CFNetworkExecuteProxyAutoConfigurationScript,
		METH_VARARGS,
		NULL
	},
#endif /* OSX >= 10.5 */
#if PyObjC_BUILD_RELEASE >= 1005
	{
		"CFNetworkExecuteProxyAutoConfigurationURL",
		(PyCFunction)m_CFNetworkExecuteProxyAutoConfigurationURL,
		METH_VARARGS,
		NULL
	},
#endif /* OSX >= 10.5 */

	{
		"CFHostSetClient",
		(PyCFunction)m_CFHostSetClient,
		METH_VARARGS,
		NULL
	},

	{ 0, 0, 0, }
};

PyObjC_MODULE_INIT(_manual)
{
	PyObject* m;

	m = PyObjC_MODULE_CREATE(_manual)
	if (!m) {
		PyObjC_INITERROR();
	}

        if (PyObjC_ImportAPI(m) < 0) { 
		PyObjC_INITERROR();
	}

#if PyObjC_BUILD_RELEASE >= 1006
	if (CFNetworkExecuteProxyAutoConfigurationScript == NULL) {
		if (PyDict_DelItemString(m, "CFNetworkExecuteProxyAutoConfigurationScript") < 0) {
			PyObjC_INITERROR();
		}
	}
#endif
#if PyObjC_BUILD_RELEASE >= 1005
	if (CFNetworkExecuteProxyAutoConfigurationURL == NULL) {
		if (PyDict_DelItemString(m, "CFNetworkExecuteProxyAutoConfigurationURL") < 0) {
			PyObjC_INITERROR();
		}
	}
#endif

	PyObjC_INITDONE();
}
