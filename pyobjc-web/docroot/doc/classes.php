<?
    $title = "Python classes and Objective-C code";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:46 $';

    include "header.inc";
?>
<div class="document" id="python-classes-and-objective-c-code">
<h1 class="title">Python classes and Objective-C code</h1>
<!-- This file is formatted using the rules for StructuredText -->
<!-- Version 0.1 -->
<div class="section" id="introduction">
<h1><a name="introduction">Introduction</a></h1>
<p>PyObjC is a proxy between Objective-C and Python and allows access to Python
classes from Objective-C and vice versa. PyObjC also allows you to subclass
Objective-C classes from Python.</p>
</div>
<div class="section" id="accessing-python-objects-from-objective-c">
<h1><a name="accessing-python-objects-from-objective-c">Accessing Python objects from Objective-C</a></h1>
<p>All Python objects can be accessed from Objective-C through proxy objects. 
Whenever a Python object crosses the line from Python to Objective-C a proxy
object is created (of class OC_PythonObject, a subclass of NSProxy). This
proxy object will forward all method calls from Objective-C to python, and
will return the results back to Objective-C.</p>
<p>See the section 'Method protocol' for a description of how PyObjC translates 
between Python and Objective-C method calls.</p>
<p>A number of Python types/classes are treated specially:</p>
<ul class="simple">
<li>Python numbers are translated into NSNumber instances</li>
<li>Python strings and unicode objects are translated into NSString instances</li>
<li>Python dictionaries are proxied using OC_PythonDictionary, a subclass of NSMutableDictionary. This allows you to use a Python dictionary everywhere where an NSDictionary is expected.</li>
<li>Python lists or tuples are proxied using OC_PythonArray, a subclas of NSMutableArray. This allows you to use a Python list or tuple everywhere where an NSArray is expected.</li>
</ul>
<p>The special cases allow for more transparent bridging between Python and
Objective-C.</p>
</div>
<div class="section" id="accessing-objective-c-objects-from-python">
<h1><a name="accessing-objective-c-objects-from-python">Accessing Objective-C objects from Python</a></h1>
<p>Objective-C objects are accessed through proxy objects that forward method
calls from Python to Objective-C. All proxy objects are instances of 
objc.objc_object, or a subclass of this class.</p>
<p>See the section 'Method protocol' for a description of how PyObjC translates 
between Python and Objective-C method calls.</p>
<p>The only Objective-C class that is not proxied is NSString, instances of this
class are translated to Python strings or unicode objects (depending on the
value of the string).</p>
</div>
<div class="section" id="accessing-objective-c-classes-from-python">
<h1><a name="accessing-objective-c-classes-from-python">Accessing Objective-C classes from Python</a></h1>
<p>Objective-C classes are also accessed through proxy objects, but those are
subclasses of objc.objc_class. The proxies for Objective-C classes are 
classes in Python.</p>
<p>Instances are created by calling allocator class methods (like 'alloc' or
factory methods). Objective-C instances cannot be created by using the class
as a factory function.</p>
<p>It is possible to create subclasses from Objective-C classes using the normal
mechanism. There are some limitations though:</p>
<ol class="arabic simple">
<li>The Objective-C class must be the first base class</li>
<li>There can be only 1 Objective-C base class.
It is not possible to multiple-inherit from two Objective-C classes, this
limitation is inherited from Objective-C.</li>
<li>It is not possible to overide or extend an Objective-C method using a mixin.
This is limitation will be lifted in future versions of PyObjC.</li>
<li>It is not possible to overide or extend an Objective-C method by adding a new method to the class after creating it.</li>
</ol>
<p>PyObjC provides limited support for Objective-C protocols. The type 
obc.informal_protocol can be used to shadow protocol definitions in Objective-C.
Instances of this type can be used as a superclass when defining a subclass of
an existing Objective-C class. The information in an 'informal_protocol' object
will be used to check if the new class does implement the protocol, and to
provide information to the bridge that is needed to correctly forward methods.</p>
<p>A subclass of an Objective-C (proxy) class is not only a Python class, but also
an Objective-C class. This means that it is possible to create instances of 
these classes from Objective-C using normal Objective-C syntax, although you
must locate the class using the function 'objc_lookUpClass' (e.g. defining
&#64;class MyPythonClass will not work). One of the results of this feature is that
these classes can be used to implement classes that are defined in Interface
Builder NIB files.</p>
<p>Like Python classes Objective-C classes can have instance variables. If you
define new instance variables in the Python subclass they will only be visible
in Python, and not in Objective-C. This means that normal Python instance
variables cannot be used as 'outlets' in interface builder. Those can be 
defined using special properties: objc.instance_variable or objc.IBOutlet.</p>
<p>The Objective-C class:</p>
<pre class="literal-block">
&#64;interface MyClass : NSObject
{
  IBOutlet id my_outlet1;
  IBOutlet id my_outlet2;
}

// ...
&#64;end // MyClass
</pre>
<p>can be defined in Python like this:</p>
<pre class="literal-block">
class MyClass (NSObject):
  my_outlet1 = objc.IBOutlet('my_outlet1')
  my_outlet2 = objc.IBOutlet('my_outlet2')

# ...
</pre>
</div>
<div class="section" id="method-protocol">
<h1><a name="method-protocol">Method protocol</a></h1>
<p>There is a straightforward translation from Objective-C method names to
Python method names: Concatenate all parts of the Objective-C method name
(without any whitespace) and then replace all colons by underscores.</p>
<p>Examples:</p>
<pre class="literal-block">
(void)myAction:(id)sender     &lt;-&gt;     def `myAction_`(self, sender)
method:(int)x andY:y          &lt;-&gt;     def `method_andY_`(self, x, y)
</pre>
<p>As can be seen in the examples above, Objective-C allows you to specify
the types of arguments and the return value, while this is not possible in
Python. This is not a problem when calling existing Objective-C methods, 
because PyObjC will automaticly read the needed information from the 
Objective-C runtime, but it can be a problem when defining new Objective-C
methods in Python.</p>
<p>PyObjC therefore provides a function to define the signature of a python method
in subclasses of Objective-C classes. This function, objc.selector, should be
used whenever you define a method that does not extend or override an existing
Objective-C method in the superclass.</p>
<p>The following Objective-C class:</p>
<blockquote>
<p>&#64;interface MyClass : NSObject
{
}</p>
<p>-(int)methodWithX:(int)x andY:(float)y;
-(void)myAction:(id)sender;</p>
</blockquote>
<p>can be defined in Python like this:</p>
<pre class="literal-block">
class MyClass (NSObject):

        def `methodWithX_andY_`(self, x, y):
                pass

        `methodWithX_and_Y_` = selector(`methodWithX_andY_`,
                signature='i&#64;:if')

        def `myAction_`(self, sender):
                pass

        myAction_ = selector(`myAction_`,
                signature='v&#64;:')
</pre>
<p>The explicit selectors don't really help to increase readability, especially
given the cryptic signature strings. It is therefore advisable to use other
methods to define the signature if possible, the most likely way to do this
is by using existing objc.informal_protocol definitions (like 
AppKit.NSOutlineViewDataSource).</p>
<p>There is one instance where you don't have to define the signature: The default
signature is for a method that returns and object and where all arguments are
also objects.</p>
</div>
</div>
<?
    include "footer.inc";
?>