<?
    $title = "An introduction to PyObjC";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/10/08 17:30:40 $';

    include "header.inc";
?>
<div class="document" id="an-introduction-to-pyobjc">
<h1 class="title">An introduction to PyObjC</h1>
<!-- :authors: Ronald Oussoren
:contact: pyobjc-dev@lists.sourceforge.net
:URL: http://pyobjc.sourceforge.net/
:copyright: 2003 The PyObjC Project -->
<div class="contents topic" id="contents">
<p class="topic-title"><a name="contents">Contents</a></p>
<ul class="simple">
<li><a class="reference" href="#preface" id="id3" name="id3">Preface</a></li>
<li><a class="reference" href="#objective-c-for-pyobjc-users" id="id4" name="id4">Objective-C for PyObjC users</a></li>
<li><a class="reference" href="#overview-of-the-bridge" id="id5" name="id5">Overview of the bridge</a><ul>
<li><a class="reference" href="#classes" id="id6" name="id6">Classes</a></li>
<li><a class="reference" href="#methods-and-functions" id="id7" name="id7">Methods and functions</a></li>
<li><a class="reference" href="#reference-counting" id="id8" name="id8">Reference counting</a></li>
<li><a class="reference" href="#informal-protocols" id="id9" name="id9">(Informal) protocols</a></li>
</ul>
</li>
<li><a class="reference" href="#cocoa-for-python-programmers" id="id10" name="id10">Cocoa for Python programmers</a></li>
<li><a class="reference" href="#notes-on-specific-tasks" id="id11" name="id11">Notes on specific tasks</a><ul>
<li><a class="reference" href="#working-with-threads" id="id12" name="id12">Working with threads</a></li>
</ul>
</li>
<li><a class="reference" href="#building-applications" id="id13" name="id13">Building applications</a><ul>
<li><a class="reference" href="#pure-python-buildapp-py" id="id14" name="id14">&quot;Pure Python&quot; :  buildapp.py</a></li>
<li><a class="reference" href="#ide-approach-project-builder" id="id15" name="id15">&quot;IDE approach&quot; : Project builder</a></li>
</ul>
</li>
</ul>
</div>
<div class="section" id="preface">
<h1><a class="toc-backref" href="#id3" name="preface">Preface</a></h1>
<p>PyObjC is a bridge between Python and Objective-C. It allows you to write 
Python scripts that use and extend existing Objective-C class libraries, 
most importantly the <a class="reference" href="http://developer.apple.com/techpubs/macosx/Cocoa/CocoaTopics.html">Cocoa libraries</a> by <a class="reference" href="http://www.apple.com/">Apple</a>.</p>
<p>This document describes how to use Objective-C class libraries from Python
scripts and how to interpret the documentation of those libraries, from the 
point of view of a Python programmer.</p>
</div>
<div class="section" id="objective-c-for-pyobjc-users">
<h1><a class="toc-backref" href="#id4" name="objective-c-for-pyobjc-users">Objective-C for PyObjC users</a></h1>
<p>It is necessary to understand a little bit of Objective-C to use PyObjC,
this helps you to better understand the class libraries and makes it easier
to read (and translate) example code.</p>
<p>Objective-C is an object-oriented programming language that is an extension 
of C and borrows heavily from Smalltalk. It features single inheritance with
(in theory) multiple root classes and dynamic dispatch of methods. This is
basicly the same as Python with single inheritance.</p>
<p>An important difference between Python and Objective-C is that the latter is
not a pure object-oriented language. Some values are not objects, but values
of plain C types, such as <tt class="literal"><span class="pre">int</span></tt> and <tt class="literal"><span class="pre">double</span></tt>. These basic C types can also
be used as the types of arguments and the return value of methods.</p>
<p>Object allocation and initialization are explicit and seperate actions in 
Objective-C. The former is done by the class-method <tt class="literal"><span class="pre">alloc</span></tt>, while the
latter is done by instance-methods whose name customarily starts with <tt class="literal"><span class="pre">init</span></tt>.</p>
<p>Objective-C code looks just like plain C code, with some easily recognizable
extensions for the Object-Oriented parts of the language. And example class
declaration (usually found in <tt class="literal"><span class="pre">.h</span></tt> files) and implementation (usually found
in <tt class="literal"><span class="pre">.m</span></tt> files) are listed below). Class declarations are easily recognized as 
blocks of code between <tt class="literal"><span class="pre">&#64;interface</span></tt> and <tt class="literal"><span class="pre">&#64;end</span></tt>, and simularly the 
implementation is between <tt class="literal"><span class="pre">&#64;implementation</span></tt> and <tt class="literal"><span class="pre">&#64;end</span></tt>. Calling methods
is done using expressions enclosed with brackets (name?), e.g. 
<tt class="literal"><span class="pre">[foo</span> <span class="pre">method]</span></tt>.  This is the same as <tt class="literal"><span class="pre">foo.method()</span></tt> in Python.</p>
<p>A class declaration:</p>
<pre class="literal-block">
&#64;interface MYClass : MySuperClass
{
   id  anInstanceVariable;
   int anotherInstanceVariable;
}

+aClassMethod;

-(int)anInstanceMethodWithArg1:arg1 andArg2:(BOOL)arg2;
&#64;end
</pre>
<p>A class implemenation:</p>
<pre class="literal-block">
&#64;implementation MYClass

+aClassMethod
{
     id res = [[MYClass alloc] init];
     return res;
}

-(int)anInstanceMethodWithArg1:arg1 andArg2:(BOOL)arg2
{
     int res;

     if (arg2) {
             res = [self fooWith:arg1];
     } else {
             res = [arg1 bar];
     }
}

&#64;end
</pre>
<p>Objective-C also features exceptions, but as those are mostly used for disaster
recovery and not for normal error handling you won't see them very often
in example code. The <a class="reference" href="http://developer.apple.com/techpubs/macosx/Cocoa/ObjectiveC/index.html">The Objective-C Programming Language</a> if you want to
know more about exceptions in Objective-C.</p>
<p>One thing to keep in mind when translating Objective-C snippets to python is
that it is valid to call methods on <tt class="literal"><span class="pre">nil</span></tt> (that is the NULL pointer). Those
method calls are ignored by the runtime. The value <tt class="literal"><span class="pre">nil</span></tt> is represented in
Python by the <tt class="literal"><span class="pre">None</span></tt>, this means that calls to non-existing methods are
not ignored but will raise <tt class="literal"><span class="pre">AttributeError</span></tt>.</p>
<p>For more information about Objective-C see:</p>
<ul class="simple">
<li><a class="reference" href="http://developer.apple.com/techpubs/macosx/Cocoa/ObjectiveC/index.html">The Objective-C Programming Language</a> at <a class="reference" href="http://www.apple.com/">Apple</a>.</li>
</ul>
</div>
<div class="section" id="overview-of-the-bridge">
<h1><a class="toc-backref" href="#id5" name="overview-of-the-bridge">Overview of the bridge</a></h1>
<div class="section" id="classes">
<h2><a class="toc-backref" href="#id6" name="classes">Classes</a></h2>
<p>Objective-C classes are visible as (new-style) Python classes and can be 
subclassed just like normal Python classes. All the usual introspection
mechanism work as well, as do __slots__ and descriptors. The major 
differences between normal Python classes and Objective-C classes are the way 
you create instances and the fact that Objective-C methods have odd names.</p>
<p>You can use multiple inheritance with Objective-C classes, as long as the
Objetive-C is the first base-class and there is only one Objective-C 
base-class. E.g. it is not possible to subclass from the Objective-C classes
at the same time. Multiple inheritance should also not be used to mix-in
different implementations for Objective-C methods, that will not work and
you won't get errors about this.</p>
<p>Another thing to keep in mind is that the names of Objective-C classes must
be unique, without taking modules into account. That is, it is <em>not</em> possible
to have two modules that define a class with the same name. If you write classes
that will be used outside of a single project it is customary to pick a 
(short) prefix and stick that in front of all class names, e.g. Apple <tt class="literal"><span class="pre">NS</span></tt> 
as the prefix in the <a class="reference" href="http://developer.apple.com/techpubs/macosx/Cocoa/CocoaTopics.html">Cocoa libraries</a>.</p>
<p>As described in <a class="reference" href="#objective-c-for-pyobjc-users">Objective-C for PyObjC users</a> the creation of Objective-C 
objects is a two-stage process. You first call the class method <tt class="literal"><span class="pre">alloc</span></tt>, and
then call some variation of <tt class="literal"><span class="pre">init</span></tt> to initialize the objects. The newly
created object is the result of the call to <tt class="literal"><span class="pre">init</span></tt>. Most classes have 
convienence class methods that combine the calls to <tt class="literal"><span class="pre">alloc</span></tt> and <tt class="literal"><span class="pre">init</span></tt>.</p>
</div>
<div class="section" id="methods-and-functions">
<h2><a class="toc-backref" href="#id7" name="methods-and-functions">Methods and functions</a></h2>
<p>Objective-C methods are bridged to Python callables. Because Objective-C method 
names can contain colons it is necessary to translate methods names. The rules
for translation are:</p>
<ul class="simple">
<li>Concatenate all elements of the method name: <tt class="literal"><span class="pre">someMethod:withFoo:andBar:</span></tt></li>
<li>Then convert all colons to underscores: <tt class="literal"><span class="pre">someMethod_withFoo_andBar_</span></tt></li>
</ul>
<p>Wrapped/bridged methods (and functions) have the same number of arguments
as the corresponding Objective-C method or function, unless otherwise noted
in the documentation (<a class="reference" href="api-notes-macosx.html">Notes on supported APIs and classes on MacOS X</a> for
Cocoa on MacOS X).</p>
<p>One group of exceptions to this rule can be described in a global way. Some
methods and functions have pointers as arguments, specifically pointers to
a single value that is passed in and/or out of the function. These arguments
are sometimes called <em>pass by reference</em> arguments, and can be subdived into
three types of arguments: <tt class="literal"><span class="pre">in</span></tt> arguments are used to pass data to the 
function, <tt class="literal"><span class="pre">out</span></tt> arguments are used to pass data from the function (e.g. and
additional return value) and <tt class="literal"><span class="pre">inout</span></tt> arguments are a combination of the two.</p>
<p>The <tt class="literal"><span class="pre">in</span></tt> and <tt class="literal"><span class="pre">inout</span></tt> arguments for a method are also present in the Python
interface for that method (or function). In python the value passed to the
function is a &quot;normal&quot; argument. <tt class="literal"><span class="pre">Out</span></tt> arguments are not present in the 
argument list of the Python function.</p>
<p>If a function (or method) has one or more output arguments (<tt class="literal"><span class="pre">out</span></tt> or 
<tt class="literal"><span class="pre">inout</span></tt>) the output values are returned as part of the return value of the
method. That is, the return value of the function is a tuple containing
the return value of the C function (or method), followed by the values of
the <tt class="literal"><span class="pre">out</span></tt> in <tt class="literal"><span class="pre">inout</span></tt> arguments in the order the are present in the argument
list. If the C function (or method) has return type <tt class="literal"><span class="pre">void</span></tt>, the tuple contains
only the output arguments. As a final complication, methods with a single output
argument and return type <tt class="literal"><span class="pre">void</span></tt>, have the value of the output argument as
the return value (e.g. not a tuple containing the return value).</p>
<p>The rules for pass by reference arguments may look quite complicated, but
it turns out this is very straightforward when working with them.</p>
<p>As an example of a method with two output arguments, NSMatrix has a method
named <tt class="literal"><span class="pre">getNumberOfRows_columns_</span></tt> with the following signature:</p>
<pre class="literal-block">
(void)getNumberOfRows:(int *)rowCount columns:(int *)columnCount
</pre>
<p>You use this method in python like this:</p>
<pre class="literal-block">
rowCount, columnCount = matrix.getNumberOfRows_columns_()
</pre>
<p>When you define methods in a subclass of an Objective-C class, the bridge has
to tell the Objective-C runtime what the signature of those methods is. The
basic rule is that all arguments as well as the return value are objects (just
like with normal Python methods). The bridge will automaticly pick a better 
signature when it has more information available. Specifically, if you 
overide an existing method the bridge will assume you want to use the same
method signature. And furthermore, if you implement a method in an (informal)
protocol known to the bridge it will use the signature from the corresponding
method in that signature.</p>
<p>The end result is that you almost never have to add information about the
signature of methods. The only known case where you have to tell the bridge
about the signature of a method is the call-back method for sheets. You can
use the function <tt class="literal"><span class="pre">PyObjCTools.AppHelper.endSheetMethod</span></tt> to create an object
that contains the right information. This function is used like 
<tt class="literal"><span class="pre">staticmethod</span></tt> and <tt class="literal"><span class="pre">classmethod</span></tt> (as introduced in Python 2.2).</p>
<p>For complete control of the mapping to Objective-C you can use the function
<tt class="literal"><span class="pre">objc.selector</span></tt>. See the documentation of the <tt class="literal"><span class="pre">objc</span></tt> module for the
arguments you can use with this function. It is normally used like this:</p>
<pre class="literal-block">
class MyObject (NSObject):
        def someMethod_(self, arg):
                pass

        someMethod_ = objc.selector(someMethod_, ...)
</pre>
</div>
<div class="section" id="reference-counting">
<h2><a class="toc-backref" href="#id8" name="reference-counting">Reference counting</a></h2>
<p>The <a class="reference" href="http://developer.apple.com/techpubs/macosx/Cocoa/CocoaTopics.html">Cocoa libraries</a>, and most (if not all) other class libraries for 
Objective-C use explicit reference counting to manage memory. The methods
<tt class="literal"><span class="pre">retain</span></tt>, <tt class="literal"><span class="pre">release</span></tt> and <tt class="literal"><span class="pre">autorelease</span></tt> are used to manage these 
reference counts. You won't have to manage reference counts in Python, the
bridge does all that work for you.</p>
<p>The only reasons reference counts are mentioned at all are to tell you about
ignoring them, and more importantly to introduce you to some issues w.r.t. 
reference counting.</p>
<p>It turns out that Cocoa uses a primitive form of <a class="reference" href="http://www.python.org/doc/current/lib/module-weakref.html">weak references</a>. Those 
are not true <a class="reference" href="http://www.python.org/doc/current/lib/module-weakref.html">weak references</a> as in Python, but use-cases where an object 
stores a reference to another object without increasing the reference count
for that other object. The bridge cannot solve the issues this introduces
for you, which means that you get hard crashes when you're not carefull when
dealing with those <a class="reference" href="http://www.python.org/doc/current/lib/module-weakref.html">weak references</a>.</p>
<p>The basic rule to deal with weak references is: make sure objects stays
alive as long as someone might have a weak reference to them. Due to the way
the bridge works, this means that you must make sure that you don't create
weak references from Objective-C to a plain Python object. The Python
object stays alive, but the proxy object as seen by the Objective-C code is
actually an autoreleased object that will be cleaned up unless the Objective-C
code increases its reference count.</p>
<p>The document <a class="reference" href="api-notes-macosx.html">Notes on supported APIs and classes on MacOS X</a> contains 
information about classes that work with weak references. The most important
are notification centers and <tt class="literal"><span class="pre">NSOutlineView</span></tt>, to be exact: the outline view
stores weak references to the objects return by the method 
<tt class="literal"><span class="pre">outlineView:child:ofItem:</span></tt> of its data source. The easiest way to avoid
crashes with outline views is to make sure that you model for the view uses
subclasses of <tt class="literal"><span class="pre">NSObject</span></tt> to represent the nodes in the outline view.</p>
<p>Another gotcha is when you're manually allocating and assigning delegate(-like)
objects: most of the time <tt class="literal"><span class="pre">obj.setDelegate_()</span></tt> will <em>not</em> retain the 
delegate, so you must keep a reference manually.</p>
</div>
<div class="section" id="informal-protocols">
<h2><a class="toc-backref" href="#id9" name="informal-protocols">(Informal) protocols</a></h2>
<p>Cocoa defines a number of formal and informal protocols that specify methods
that should be implemented by a class if it is to be used in a specific role,
such as the data source for an NSTableView.</p>
<p>Those protocols are represented by instances of <tt class="literal"><span class="pre">objc.informal_protocol</span></tt>. The
only ones that have to care about these objects are the maintainers of 
wrappers around Objective-C frameworks: they have to keep these protocol
wrappers up-to-date.</p>
<p>PyObjC will automaticly use the information in the <tt class="literal"><span class="pre">informal_protocol</span></tt> 
objects to add the right method signatures to methods, and to warn about
classes that partially implement a protocol.</p>
</div>
</div>
<div class="section" id="cocoa-for-python-programmers">
<h1><a class="toc-backref" href="#id10" name="cocoa-for-python-programmers">Cocoa for Python programmers</a></h1>
<p>Cocoa frameworks are mapped onto Python packages with the same name, that is
the classes, constants and functioins from the AppKit framework are available
after you import <tt class="literal"><span class="pre">AppKit</span></tt> in your Python script.</p>
<p>These helper modules contain <em>only</em> functions, constants and classes that 
wrap items in the corresponding framework. All utility functions and classes 
are located in the <tt class="literal"><span class="pre">PyObjCTools</span></tt> package and <tt class="literal"><span class="pre">objc</span></tt> module. Note that it
is possible to use <tt class="literal"><span class="pre">pydoc</span></tt> (or the <tt class="literal"><span class="pre">help()</span></tt>) function with the framework
wrappers, but that this is not very usefull for the entire module due to the
size of these modules.</p>
<p>This makes it easier to find documentation for an item: if you import it 
from the wrapper module for an Objective-C framework the documentation for
that item can be found in the documentation for the framework, otherwise the
item is documented in the PyObjC documentation.</p>
<p>The module <tt class="literal"><span class="pre">PyObjCTools.NibClassBuilder</span></tt> can be used to make working with 
NIB files more convenient. This module can be used to extract information 
about classes from NIB files, both as a standalone tool generating source code 
and during runtime. See the online documentation for this module for more
information.</p>
<p>PyObjC includes a number of examples that show how to use Cocoa from
Python. The <a class="reference" href="../Examples/00ReadMe.html">PyObjC Example index</a> contains an overview of those examples.</p>
<p>More information on Cocoa programming can be found at:</p>
<ul class="simple">
<li><a class="reference" href="http://developer.apple.com/techpubs/macosx/Cocoa/CocoaTopics.html">Cocoa documentation at the Apple developer website</a></li>
<li><a class="reference" href="http://developer.apple.com/samplecode/Sample_Code/Cocoa.htm">Cocoa examples at the Apple developer website</a></li>
<li><a class="reference" href="http://www.stepwise.com/">stepwise.com</a></li>
<li>Your local bookstore or library</li>
</ul>
</div>
<div class="section" id="notes-on-specific-tasks">
<h1><a class="toc-backref" href="#id11" name="notes-on-specific-tasks">Notes on specific tasks</a></h1>
<div class="section" id="working-with-threads">
<h2><a class="toc-backref" href="#id12" name="working-with-threads">Working with threads</a></h2>
<p>When you create a thread and want to use PyObjC from that thread you will
have to create an <tt class="literal"><span class="pre">NSAutoreleasePool</span></tt> in that thread and clean it up when
you're done. The easiest way to that is to create an instance of that class
bound to a local variable. If the thread is long-lived you may want to arrange
for recycling the pool once in a while.</p>
<p>There are some limitiation w.r.t. threading. You cannot use <tt class="literal"><span class="pre">NSThread</span></tt> to 
create new threads, but must use the python primitives instead.</p>
<p>You must also make sure that Objective-C only makes calls to Python from a 
thread that owns the Python GIL (that's also the reason for not being able 
to use <tt class="literal"><span class="pre">NSThread</span></tt> to create new threads).  This restriction will be lifted
in a future version of PyObjC (at least when using Python 2.3).</p>
</div>
</div>
<div class="section" id="building-applications">
<h1><a class="toc-backref" href="#id13" name="building-applications">Building applications</a></h1>
<p>There are two different ways to build applications with PyObjC. There are no
major advantages to using either one of them, use the one that is most 
convenient to you.</p>
<div class="section" id="pure-python-buildapp-py">
<h2><a class="toc-backref" href="#id14" name="pure-python-buildapp-py">&quot;Pure Python&quot; :  buildapp.py</a></h2>
<p>PyObjC includes a copy of the <tt class="literal"><span class="pre">bundlebuilder</span></tt> module. This module will be
part of the Python 2.3 MacPython release and offers a way to build
distutils-style scripts  for building (standalone) applications.</p>
<p>An example <tt class="literal"><span class="pre">buildapp.py</span></tt> script:</p>
<pre class="literal-block">
from bundlebuilder import buildapp
buildapp(
        name = 'iClass',
        mainprogram = &quot;main.py&quot;,
        resources = [&quot;English.lproj&quot;, &quot;datasource.py&quot; ],
        nibname = &quot;MainMenu&quot;,
)   
</pre>
<p>During development you typically invoke it from the command line like this:</p>
<pre class="literal-block">
python buildapp.py --link build
</pre>
<p>This will build an application bundle in a folder named <tt class="literal"><span class="pre">build</span></tt> in the
current folder. The <tt class="literal"><span class="pre">--link</span></tt> option tells <tt class="literal"><span class="pre">bundlebuilder</span></tt> to add symbolic
links to the application bundle instead of copies of your source and resource
files, allowing you to edit them without having to rebuild the application. To
build a standalone application, either use <tt class="literal"><span class="pre">--standalone</span></tt> or
<tt class="literal"><span class="pre">--semi-standalone</span></tt>. The latter will put all used modules that are not in
Python's standard library into the application bundle. The result will still
depend on an installed Python, but yields a relatively compact application.
<tt class="literal"><span class="pre">--standalone</span></tt> will cause <tt class="literal"><span class="pre">bundlebuilder</span></tt> to include <em>everything</em> needed
into the app bundle, including the entire Python runtime. This is useful if
you're using a different version of Python that the one that comes with MacOSX
10.2, or if you fear that a future version of OSX may come with an
incompatible Python version.</p>
<p>The online documentation for <tt class="literal"><span class="pre">bundlebuilder</span></tt> contains more information on 
building <tt class="literal"><span class="pre">buildapp.py</span></tt> scripts and how to invoke them. There are plenty of
example <tt class="literal"><span class="pre">buildapp.py</span></tt> scripts in the various <a class="reference" href="../Examples/00ReadMe.txt">Examples</a> subfolders.</p>
</div>
<div class="section" id="ide-approach-project-builder">
<h2><a class="toc-backref" href="#id15" name="ide-approach-project-builder">&quot;IDE approach&quot; : Project builder</a></h2>
<p>PyObjC includes a number of Project Builder templates that can be used to 
build (standalone) applications. Those templates are used like any other
Project Builder template. The only non-obvious detail is that you have to
add your sources as resources, but Project Builder usually does the right
thing when you add a new file.</p>
<p>The templates will build an application that makes use of the installed copy
<tt class="literal"><span class="pre">/usr/bin/python</span></tt> (e.g. the one shipped by Apple in MacOS X 10.2) and will 
copy the PyObjC modules into the application bundle. This means that this 
application bundle should be useable on any MacOS X 10.2 system.</p>
<p>See <a class="reference" href="ProjectBuilder-Templates.html">the documentation for the templates</a> for more details.</p>
<p>MacOS X 10.3 seems to ship with Python 2.3 as /usr/bin/python. This means that
standalone applications build using the Project Builder templates will start
to complain about Python ABI versions in the <tt class="literal"><span class="pre">Console</span></tt> when you run them
on MacOS X 10.3. These are harmless messages caused by the extension modules
in PyObjC.</p>
</div>
</div>
</div>
<?
    include "footer.inc";
?>