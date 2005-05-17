<?
    $title = "Python classes and Objective-C code";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<h1 class="title">Python classes and Objective-C code</h1>
<!-- This file is formatted using the rules for reStructuredText -->
<!-- Version 0.2 -->
<div class="section" id="introduction">
<h3><a name="introduction">Introduction</a></h3>
<p>PyObjC is a proxy between Objective-C and Python and allows access to Python
classes from Objective-C and vice versa.  PyObjC also allows Python to subclass
Objective-C classes, and these subclasses will be natively visible to both runtimes.</p>
</div>
<div class="section" id="accessing-python-objects-from-objective-c">
<h3><a name="accessing-python-objects-from-objective-c">Accessing Python objects from Objective-C</a></h3>
<p>All Python objects can be accessed from Objective-C through proxy objects. 
Whenever a Python object crosses the line from Python to Objective-C a proxy
object is created (of class <tt class="docutils literal"><span class="pre">OC_PythonObject</span></tt>, a subclass of <tt class="docutils literal"><span class="pre">NSProxy</span></tt>).
This proxy object will forward all method calls from Objective-C to Python, and
will return the results back to Objective-C.</p>
<p>See the section 'Method protocol' for a description of how PyObjC translates 
between Python and Objective-C method calls.</p>
<p>A number of Python types/classes are treated specially:</p>
<ul class="simple">
<li>Python numbers (<tt class="docutils literal"><span class="pre">int</span></tt>, <tt class="docutils literal"><span class="pre">float</span></tt>, <tt class="docutils literal"><span class="pre">long</span></tt>) are translated into
<tt class="docutils literal"><span class="pre">NSNumber</span></tt> instances.  Their identity is not preserved across the bridge.</li>
<li>Python <tt class="docutils literal"><span class="pre">str</span></tt> is proxied using <tt class="docutils literal"><span class="pre">OC_PythonString</span></tt>, a subclass of
<tt class="docutils literal"><span class="pre">NSString</span></tt>.  A Python <tt class="docutils literal"><span class="pre">str</span></tt> may be used anywhere a <tt class="docutils literal"><span class="pre">NSString</span></tt> is
expected, but <tt class="docutils literal"><span class="pre">unicode</span></tt> should be used whenever possible.
<tt class="docutils literal"><span class="pre">OC_PythonString</span></tt> will use the default encoding of <tt class="docutils literal"><span class="pre">NSString</span></tt>, which is
normally MacRoman but could be something else.</li>
<li>Python <tt class="docutils literal"><span class="pre">unicode</span></tt> is proxied using <tt class="docutils literal"><span class="pre">OC_PythonUnicode</span></tt>, a subclass of
<tt class="docutils literal"><span class="pre">NSString</span></tt>.  A Python <tt class="docutils literal"><span class="pre">unicode</span></tt> may be used anywhere a <tt class="docutils literal"><span class="pre">NSString</span></tt>
is expected.</li>
<li>Python <tt class="docutils literal"><span class="pre">dict</span></tt> is proxied using <tt class="docutils literal"><span class="pre">OC_PythonDictionary</span></tt>, a subclass of
<tt class="docutils literal"><span class="pre">NSMutableDictionary</span></tt>.  A Python <tt class="docutils literal"><span class="pre">dict</span></tt> may be used anywhere 
an <tt class="docutils literal"><span class="pre">NSDictionary</span></tt> is expected.</li>
<li>Python <tt class="docutils literal"><span class="pre">list</span></tt> and <tt class="docutils literal"><span class="pre">tuple</span></tt> are proxied using <tt class="docutils literal"><span class="pre">OC_PythonArray</span></tt>, a
subclass of <tt class="docutils literal"><span class="pre">NSMutableArray</span></tt>.  Python <tt class="docutils literal"><span class="pre">list</span></tt> or <tt class="docutils literal"><span class="pre">tuple</span></tt> objects
may be used anywhere an <tt class="docutils literal"><span class="pre">NSArray</span></tt> is expected.</li>
<li>Python objects that implement the Python buffer API, except for <tt class="docutils literal"><span class="pre">str</span></tt>
and <tt class="docutils literal"><span class="pre">unicode</span></tt>, are proxied using <tt class="docutils literal"><span class="pre">OC_PythonData</span></tt>, a <tt class="docutils literal"><span class="pre">NSData</span></tt> subclass.
Objects that implement the Python buffer API such as <tt class="docutils literal"><span class="pre">buffer</span></tt>,
<tt class="docutils literal"><span class="pre">array.array</span></tt>, <tt class="docutils literal"><span class="pre">mmap.mmap</span></tt>, etc. may be used anywhere a <tt class="docutils literal"><span class="pre">NSData</span></tt> is
expected.</li>
</ul>
<p>These special cases allow for more transparent bridging between Python and
Objective-C.</p>
</div>
<div class="section" id="accessing-objective-c-objects-from-python">
<h3><a name="accessing-objective-c-objects-from-python">Accessing Objective-C objects from Python</a></h3>
<p>Objective-C objects are accessed through proxy objects that forward method
calls from Python to Objective-C.  All proxy objects are instances of 
<tt class="docutils literal"><span class="pre">objc.objc_object</span></tt>, or a subclass of this class.</p>
<p>See the section 'Method protocol' for a description of how PyObjC translates 
between Python and Objective-C method calls.</p>
</div>
<div class="section" id="accessing-objective-c-classes-from-python">
<h3><a name="accessing-objective-c-classes-from-python">Accessing Objective-C classes from Python</a></h3>
<p>Objective-C classes are also accessed through proxy objects, but those are
subclasses of <tt class="docutils literal"><span class="pre">objc.objc_class</span></tt>.  The proxies for Objective-C classes are 
classes in Python.</p>
<p>Instances are created by calling allocator class methods (like <tt class="docutils literal"><span class="pre">+alloc</span></tt> or
factory methods).  Objective-C instances can not be created by using the class
as a factory function.</p>
<p>It is possible to create subclasses from Objective-C classes using the normal
mechanism.  There are some limitations though:</p>
<ol class="arabic simple">
<li>The Objective-C class must be the first base class</li>
<li>There can be only 1 Objective-C base class.
It is not possible to multiple-inherit from two Objective-C classes, this
limitation is inherited from Objective-C.</li>
<li>It is not possible to override or extend an Objective-C method using a mixin.
This is limitation will be lifted in future versions of PyObjC.</li>
<li>It is not possible to override or extend an Objective-C method by adding a
new method to the class after creating it.</li>
</ol>
<p>Limitations 3 and 4 can be worked around by creating a category using
<tt class="docutils literal"><span class="pre">objc.Category</span></tt>.</p>
<p>PyObjC provides support for Objective-C protocols.  The type 
<tt class="docutils literal"><span class="pre">obc.informal_protocol</span></tt> can be used to shadow protocol definitions in
Objective-C.  Instances of this type can be used as a superclass when defining
a subclass of an existing Objective-C class.  The information in an
'informal_protocol' object will be used to check if the new class does
implement the protocol, and to provide information to the bridge that is needed
to correctly forward methods.</p>
<p>Formal protocols are wrapped by the type <tt class="docutils literal"><span class="pre">objc.formal_protocol</span></tt> and can be
accessed using the function <tt class="docutils literal"><span class="pre">objc.protocolNamed(...)</span></tt>.  Instances of this
type can be used as a superclass when defining a subclass of an existing
Objective-C class.  The class will not be checked to see if it actually
does conform to the protocol.  Formal protocols can be created by using
<tt class="docutils literal"><span class="pre">objc.formal_protocol</span></tt>'s constructor.</p>
<p>A subclass of an Objective-C (proxy) class is not only a Python class, but also
an Objective-C class.  This means that it is possible to create instances of 
these classes from Objective-C using normal Objective-C syntax, although the
class must be located using the function <tt class="docutils literal"><span class="pre">NSClassFromString</span></tt> or equivalent
(e.g. <a class="reference" href="mailto:defining``&#64;class">defining``&#64;class</a> MyPythonClass`` will not work).  One of the results of
this feature is that these classes can be used to implement classes that are
defined in Interface Builder NIB files.</p>
<p>Like Python classes, Objective-C classes can have instance variables.  Normal
Python instance variables in a Python subclass will only be visible from Python,
and not Objective-C (except when using Key-Value Coding).  This means that
normal Python instance variables can not be used as outlets in Interface Builder.
Objective-C visible instance variables can be defined using special properties:
<tt class="docutils literal"><span class="pre">objc.ivar</span></tt> and <tt class="docutils literal"><span class="pre">objc.IBOutlet</span></tt>.</p>
<p>The Objective-C class:</p>
<pre class="literal-block">
&#64;interface MyClass : NSObject
{
  IBOutlet id my_outlet1;
  IBOutlet id my_outlet2;
  id my_ivar;
  int my_int;
}

// ...
&#64;end // MyClass
</pre>
<p>The Python equivalent:</p>
<pre class="literal-block">
class MyClass(NSObject):
  my_outlet1 = objc.IBOutlet('my_outlet1')
  my_outlet2 = objc.IBOutlet('my_outlet2')
  my_ivar = objc.ivar('my_ivar')
  my_int = objc.ivar('my_int', 'i')

# ...
</pre>
</div>
<div class="section" id="method-protocol">
<h3><a name="method-protocol">Method protocol</a></h3>
<p>There is a straightforward translation from Objective-C method names to
Python method names: Concatenate all parts of the Objective-C method name
(without any whitespace) and then replace all colons by underscores.</p>
<p>Examples:</p>
<pre class="literal-block">
(void)myAction:(id)sender     &lt;-&gt;     def myAction_(self, sender)
method:(int)x andY:y          &lt;-&gt;     def method_andY_(self, x, y)
</pre>
<p>As can be seen in the examples above, Objective-C allows explicit specification
of the types of arguments and the return value, while this is not possible in
Python.  This is not a problem when calling existing Objective-C methods, 
because PyObjC will automatically read the needed information from the 
Objective-C runtime, but it can be a problem when defining new Objective-C
methods in Python.</p>
<p>PyObjC therefore provides a function to define the signature of a python method
in subclasses of Objective-C classes.  This function, objc.selector, should be
used whenever defining a method that does not extend or override an existing
Objective-C method in the superclass.</p>
<p>The following Objective-C class:</p>
<pre class="literal-block">
&#64;interface MyClass : NSObject
{
}

-(int)methodWithX:(int)x andY:(float)y;
-(void)myAction:(id)sender;
</pre>
<p>can be defined in Python like this:</p>
<pre class="literal-block">
class MyClass(NSObject):

        def methodWithX_andY_(self, x, y):
                return 0

        methodWithX_andY_ = objc.selector(methodWithX_andY_,
                signature='i&#64;:if')

        def myAction_(self, sender):
                pass

        myAction_ = objc.selector(myAction_,
                signature='v&#64;:')
</pre>
<p>In Python 2.4, it is also possible to write this example as such:</p>
<pre class="literal-block">
class MyClass(NSObject):

        &#64;objc.signature('i&#64;:if')
        def methodWithX_andY_(self, x, y):
                return 0

        &#64;objc.signature('v&#64;:')
        def myAction_(self, sender):
                pass
</pre>
<p>The explicit selectors don't really help to increase readability, especially
given the cryptic type signature strings.  It is therefore advisable to use other
methods to define the signature if possible, the most likely way to do this
is by using existing <tt class="docutils literal"><span class="pre">objc.informal_protocol</span></tt> definitions (like 
<tt class="docutils literal"><span class="pre">AppKit.NSOutlineViewDataSource</span></tt>).</p>
<p>Unless explicitly specified as above, or defined by a superclass or protocol,
PyObjC creates a default signature with an object return value, and object
arguments.  If no return statement is in the function, then the return value
is <tt class="docutils literal"><span class="pre">void</span></tt>, such as the above <tt class="docutils literal"><span class="pre">myAction_</span></tt>.  Fortunately, these cases cover
most usage of PyObjC, so it is not often necessary to explicitly define selectors
as above.</p>
</div>
</div>
<?
    include "footer.inc";
?>