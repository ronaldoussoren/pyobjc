<?
    $title = "Documentation for the PyObjC C-API (Preliminary)";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2004/02/02 15:23:01 $';

    include "header.inc";
?>
<div class="document" id="documentation-for-the-pyobjc-c-api-preliminary">
<h1 class="title">Documentation for the PyObjC C-API (Preliminary)</h1>
<div class="section" id="introduction">
<h1><a name="introduction">Introduction</a></h1>
<p><em>WARNING: This API is unstable and might change in the future. Please let
us know if you want to use the C-API in your own code</em></p>
<p>The PyObjC package can be extended in C (or more likely Objective-C) using
the C API described in this document. This API should be used to write
custom wrappers for &quot;hard&quot; methods and to create/access Objective-C proxy
objects from the wrappers for C functions.</p>
<p>IMHO this API shouldn't be used to write modules that &quot;just happen&quot; to
work with Objective-C objects, using (static) methods in a class is much
more convenient.</p>
<p>The C API is defined in <tt class="literal"><span class="pre">pyobjc-api.h</span></tt>. This file is currently not installed
because the API is not entirely stable. This is the only file that can
be included from outside of the 'Modules/objc' directory, future versions of
the bridge may use additional linker flags to make sure that the module doesn't
export symbols other than the module init function.</p>
<p>The easiest way to wrap global functions and constants is by using the scripts
in Scripts/CodeGenerators. This script is unsupported and might not work on
anything but the Apple headers, but if it works it will save you a lot of work.</p>
</div>
<div class="section" id="limititations">
<h1><a name="limititations">Limititations</a></h1>
<p>An important limitation of the current C API is that you can only use the API
from one C file in the implementation of an extension module. This limitation
will probably not be removed in future versions of the API.</p>
</div>
<div class="section" id="initialization">
<h1><a name="initialization">Initialization</a></h1>
<p>The initialiazation function (below) should be called before using the
rest of the API:</p>
<pre class="literal-block">
static int PyObjC_ImportAPI(PyObject* calling_module)
</pre>
<p>This module will return 0 if loading the module was successfull, and -1
otherwise. Reasons for failure include: not being able to locate the module
and API version conflicts.</p>
<p>Loading the API will make it impossible to unload the <tt class="literal"><span class="pre">calling_module</span></tt>.</p>
<p>NOTE: Using the API other than by the mechanism described in this document 
is unsupported.</p>
</div>
<div class="section" id="compatibility-macros">
<h1><a name="compatibility-macros">Compatibility Macros</a></h1>
<p>On MacOS X, the version guard macro <tt class="literal"><span class="pre">MAC_OS_X_VERSION_MAX_ALLOWED</span></tt> will 
always be available.</p>
<p>The macros <tt class="literal"><span class="pre">PyDoc_STR</span></tt>, <tt class="literal"><span class="pre">PyDoc_VAR</span></tt> and <tt class="literal"><span class="pre">PyDoc_STRVAR</span></tt> are defined 
when they are not defined in <tt class="literal"><span class="pre">Python.h</span></tt>.</p>
</div>
<div class="section" id="types">
<h1><a name="types">Types</a></h1>
<pre class="literal-block">
PyObjCObject_Type

int PyObjCObject_Check(value);
</pre>
<p><tt class="literal"><span class="pre">PyObjCObject_Type</span></tt> is the type of Objective-C objects, both pure Objective-C
objects and hybrid Python/Objective-C objects are instances of this type. Use
<tt class="literal"><span class="pre">PyObjCObject_Check</span></tt> to check if a value is an instance of this type.</p>
<p>There is at most 1 proxy for an Objective-C instance. That is, you can use
the <tt class="literal"><span class="pre">is</span></tt> operator in Python to check if two variables refer to the same
Objective-C object.</p>
<pre class="literal-block">
PyObjCClass_Type

int PyObjCClass_Check(value);
</pre>
<p><tt class="literal"><span class="pre">PyObjCClass_Type</span></tt> is the type of Objective-C classes, both pure Objective-C
objects and hybrid Python/Objective-C classes are instances of this type. Use
<tt class="literal"><span class="pre">PyObjCClass_Check</span></tt> to check if a value is an instance of this type.</p>
<p>There is at most 1 class proxy for an Objective-C class. That is, you can use
the <tt class="literal"><span class="pre">is</span></tt> operator in Python to compare two classes for equality.</p>
<pre class="literal-block">
PyObjCSelector_Type

int PyObjCSelector_Check(value);
</pre>
<p><tt class="literal"><span class="pre">PyObjCSelector_Type</span></tt> is the type of Objective-C methods (including the
methods defined in Python).  Use <tt class="literal"><span class="pre">PyObjCSelector_Check</span></tt> to check if a value 
is an instance of this type.</p>
</div>
<div class="section" id="api-functions">
<h1><a name="api-functions">API functions</a></h1>
<pre class="literal-block">
int PyObjC_RegisterMethodMapping(
                     Class cls, 
                     SEL sel, 
                     PyObject *(callObjC)(PyObject*, PyObject*, PyObject*),
                     IMP callPython);
</pre>
<p>Register a custom wrapper for a specific method. Returns -1 on failure.</p>
<pre class="literal-block">
int PyObjC_RegisterSignatureMapping(
                     char* typespec,
                     PyObject *(*callObjC)(PyObject*, PyObject*, PyObject*),
                     IMP callPython);
</pre>
<p>Register a custom wrapper for methods with a specific signature. Returns -1
on failure.</p>
<pre class="literal-block">
id PyObjCObject_GetObject(PyObject* obj);
</pre>
<p>Return the Objective-C object that is proxied by a <tt class="literal"><span class="pre">PyObjCObject_Type</span></tt> 
instance.</p>
<pre class="literal-block">
void PyObjCObject_ClearObject(PyObject* obj);
</pre>
<p>Clear the proxied object. That is, the <tt class="literal"><span class="pre">PyObjCObject_Type</span></tt> instance will
no longer be a proxy.</p>
<pre class="literal-block">
Class PyObjCClass_GetClass(PyObject* cls);
</pre>
<p>Extract the Class from a proxied Objective-C class.</p>
<pre class="literal-block">
PyObject* PyObjCClass_New(Class cls);
</pre>
<p>Create or find a proxy object for the class.</p>
<pre class="literal-block">
id PyObjC_PythonToId(PyObject* value);
</pre>
<p>Create a proxy for the Python object. This will unwrap proxied Objective-C 
objects, and will create the appropriate proxy for Python objects.</p>
<pre class="literal-block">
PyObject* IdToPython(id value);
</pre>
<p>Create a proxy for the Objective-C object. This will unwrap proxied Python
objects and will create a proxy object for Objective-C objects.</p>
<pre class="literal-block">
void PyObjCErr_FromObjC(NSException* localException);
</pre>
<p>Convert an Objective-C exception to Python. Use 
<tt class="literal"><span class="pre">PyObjCErr_FromObjC(localException)</span></tt> to convert the exception in an 
<tt class="literal"><span class="pre">NS_HANDLER</span></tt> block.</p>
<p>Note that PyObjC supports roundtripping for exceptions, if the current 
Objective-C exception is an converted Python exception, the original Python
exception will be rethrown.</p>
<pre class="literal-block">
void PyObjCErr_ToObjC(void);
</pre>
<p>Convert a Python exception to Objective-C. This function does not return.</p>
<p>Note that PyObjC supports roundtripping for exceptions, if the current Python
exception is an converted Objective-C exception, the original Objective-C
exception will be rethrown.</p>
<pre class="literal-block">
int PyObjC_PythonToObjC(const char* typespec, PyObject* value, void* buffer);
</pre>
<p>Convert the value to an Objective-C value of type <tt class="literal"><span class="pre">typespec</span></tt>. The buffer must
be at least <tt class="literal"><span class="pre">PyObjCRT_SizeOfType(typespec)</span></tt> bytes long.</p>
<p>NOTE: The <tt class="literal"><span class="pre">typespec</span></tt> is a type specifier as described in the runtime 
reference of the Objective-C manual from Apple. Use <tt class="literal"><span class="pre">&#64;encode(mytype)</span></tt> if to
get code that is portable to a different Objective-C runtime.</p>
<pre class="literal-block">
PyObject* PyObjC_ObjCToPython(const char* typespec, void* value);
</pre>
<p>Convert an Objective-C value of type <tt class="literal"><span class="pre">typespec</span></tt> to python.</p>
<pre class="literal-block">
PyObject* PyObjC_CallPython(id self, SEL sel, PyObject* arglist, int* isAlloc);
</pre>
<p>Call the Python implementation of method <tt class="literal"><span class="pre">sel</span></tt> of <tt class="literal"><span class="pre">self</span></tt>. The <tt class="literal"><span class="pre">arglist</span></tt>
must contain the complete argument list, including self. If <tt class="literal"><span class="pre">isAlloc</span></tt> is not
<tt class="literal"><span class="pre">NULL</span></tt> it is used to output whether this method should return a new reference
(TRUE) or a borrowed reference (FALSE).</p>
<pre class="literal-block">
int PyObjCRT_SizeOfType(const char* typespec);
</pre>
<p>Return the size of variables of the specified type.</p>
<pre class="literal-block">
int PyObjCRT_AlignOfType(const char* typespec);
</pre>
<p>Return the alignment of variables of the specified type.</p>
<pre class="literal-block">
Class PyObjCSelector_GetClass(PyObject* sel);
</pre>
<p>Return the class containing the definition of <tt class="literal"><span class="pre">sel</span></tt>.</p>
<pre class="literal-block">
SEL PyObjCSelector_GetSelector(PyObject* sel);
</pre>
<p>Return the Objective-C method name for <tt class="literal"><span class="pre">sel</span></tt>.</p>
<pre class="literal-block">
int PyObjCBool_Check(PyObject* obj);
</pre>
<p>Check if <tt class="literal"><span class="pre">obj</span></tt> is a boolean object (either the python bool type in Python
2.3 or the PyObjC bool type in Python 2.2)</p>
<pre class="literal-block">
PyObject* PyObjCBool_FromLong(long i);
</pre>
<p>Create a new bool object. This will return a Python bool object in Python 2.3
(and later) and the PyObjC bool type in Python 2.2.</p>
<pre class="literal-block">
void PyObjC_InitSuper(struct objc_super*, Class, id);
</pre>
<p>Initialize the <tt class="literal"><span class="pre">struct</span> <span class="pre">objc_super</span></tt> for use with <tt class="literal"><span class="pre">objc_sendMsgSuper</span></tt>. Use 
this if the <tt class="literal"><span class="pre">self</span></tt> argument is a normal object.</p>
<pre class="literal-block">
void PyObjC_InitSuperCls(struct objc_super*, Class, Class);
</pre>
<p>Initialize the <tt class="literal"><span class="pre">struct</span> <span class="pre">objc_super</span></tt> for use with <tt class="literal"><span class="pre">objc_sendMsgSuper</span></tt>. Use 
this if the <tt class="literal"><span class="pre">self</span></tt> argument is a Class.</p>
<pre class="literal-block">
int  PyObjCPointerWrapper_Register(
              const char* typespec, PyObject* (*pythonify)(void*),
              int (*depythonify)(PyObject*, void*)
      );
</pre>
<p>Use <tt class="literal"><span class="pre">pythonify</span></tt> to convert pointers of type <tt class="literal"><span class="pre">typespec</span></tt> to python and
<tt class="literal"><span class="pre">depythonify</span></tt> to extract them from Python. Use this to register helper 
function for the conversion of opaque pointers.</p>
<pre class="literal-block">
id  PyObjCUnsupportedMethod_IMP(id, SEL);
</pre>
<p>Use this as an argument for <tt class="literal"><span class="pre">PyObjC_RegisterMethodMapping</span></tt> or 
<tt class="literal"><span class="pre">PyObjC_RegisterSignatureMapping</span></tt> if the method is not callable from 
Objective-C.</p>
<pre class="literal-block">
PyObject* PyObjCUnsupportedMethod_Caller(PyObject*, PyObject*, PyObject*);
</pre>
<p>Use this as an argument for <tt class="literal"><span class="pre">PyObjC_RegisterMethodMapping</span></tt> or 
<tt class="literal"><span class="pre">PyObjC_RegisterSignatureMapping</span></tt> if the method is not callable from Python.</p>
<pre class="literal-block">
int PyObjCObject_Convert(PyObject* object, void* pvar);
</pre>
<p>This is a variation on <tt class="literal"><span class="pre">PyObjC_PythonToId</span></tt> than can be used with 
<tt class="literal"><span class="pre">PyArg_Parse</span></tt>.</p>
<pre class="literal-block">
int PyObjCClass_Convert(PyObject* object, void* pvar);
</pre>
<p>This is a variation on <tt class="literal"><span class="pre">PyObjCClass_GetClass</span></tt> than can be used with 
<tt class="literal"><span class="pre">PyArg_Parse</span></tt>.</p>
<pre class="literal-block">
int PyObjCSelector_Convert(PyObject* object, void* pvar);
</pre>
<p>Write the <tt class="literal"><span class="pre">SEL</span></tt> for a selector object into <tt class="literal"><span class="pre">*pvar</span></tt>. 
For use with <tt class="literal"><span class="pre">PyArg_Parse</span></tt>.</p>
<pre class="literal-block">
int PyObjC_ConvertBOOL(PyObject* object, void* pvar);
</pre>
<p>Write <tt class="literal"><span class="pre">YES</span></tt> into <tt class="literal"><span class="pre">*pvar</span></tt> if <tt class="literal"><span class="pre">object</span></tt> is true, write <tt class="literal"><span class="pre">NO</span></tt> otherwise.
<tt class="literal"><span class="pre">*pvar</span></tt> should be of type BOOL.  For use with <tt class="literal"><span class="pre">PyArg_Parse</span></tt>.</p>
<pre class="literal-block">
int PyObjC_ConvertChar(PyObject* object, void* pvar);
</pre>
<p>Write the value of a string of length 1 into the character (type char)
at <tt class="literal"><span class="pre">*pvar</span></tt>. For use with <tt class="literal"><span class="pre">PyArg_Parse</span></tt>.</p>
</div>
</div>
<?
    include "footer.inc";
?>