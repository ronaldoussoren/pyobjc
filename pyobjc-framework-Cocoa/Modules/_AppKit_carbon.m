/*
 * Support code for dealing with Carbon types (at least those
 * used in AppKit and wrapped in the python core).
 */

#if PY_MAJOR_VERSION == 2 && defined(USE_TOOLBOX_OBJECT_GLUE)

/* As of OSX 10.12 pymactoolbox includes a file that
 * is not longer present, therefore inline the
 * declarations we use instead of using the pymactoolbox.h
 * header file.
 */
extern PyObject *WinObj_New(WindowPtr);
extern int WinObj_Convert(PyObject *, WindowPtr *);
extern PyObject *WinObj_WhichWindow(WindowPtr);


static int
py2window(PyObject* obj, void* output)
{
    return WinObj_Convert(obj, (WindowPtr*)output);
}

static PyObject*
window2py(void* value)
{
    return WinObj_New((WindowPtr)value);
}

#endif /* PY_MAJOR_VERSION == 2 */

static int setup_carbon(PyObject* m __attribute__((__unused__)))
{
#if PY_MAJOR_VERSION == 2 && defined(USE_TOOLBOX_OBJECT_GLUE)
    if (PyObjCPointerWrapper_Register("WindowRef", @encode(WindowRef),
                    &window2py, &py2window) < 0) {
        return -1;
    }
#endif

    return 0;
}
