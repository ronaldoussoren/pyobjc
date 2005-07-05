<?
    $title = "PyObjC Examples";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<h1 class="title">PyObjC Examples</h1>
<div class="section" id="simple-scripts-that-demo-the-core-modules">
<h3><a name="simple-scripts-that-demo-the-core-modules">Simple scripts that demo the core modules</a></h3>
<p>The directory <a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Scripts">Scripts</a> contains a number of simple command-line scripts
that make use of Cocoa features.</p>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Scripts/autoreadme.py">autoreadme.py</a></p>
<p>This script is a daemon that will open the ReadMe file in the root of any
(removable) volume that is inserted while this script is running.</p>
<p>The script is part of <a class="reference" href="http://macdevcenter.com/pub/a/mac/2003/01/31/pyobjc_one.html">Introduction to PyObjC</a>, an article at O'Reilly
<a class="reference" href="http://macdevcenter.com/">MacDevCenter.com</a>.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Scripts/debugging.py">debugging.py</a></p>
<p>This script shows how to use <tt class="docutils literal"><span class="pre">PyObjCTools.Debugging</span></tt> to show tracebacks
of all (Cocoa) exceptions (handled and unhandled).</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Scripts/dictionary.py">dictionary.py</a></p>
<p>Demonstrate the usage of an <tt class="docutils literal"><span class="pre">NSMutableDictionary</span></tt> object with both
Objective-C and Python dictionary syntax.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Scripts/exportBook.py">exportBook.py</a></p>
<p>An example of using the <tt class="docutils literal"><span class="pre">AddressBook</span></tt> framework, this script exports some
of the information about people in your addressbook to a CSV file.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Scripts/findPython.py">findPython.py</a></p>
<p>Demonstrate the usage of <tt class="docutils literal"><span class="pre">objc.loadBundleFunctions</span></tt> to access
functionality from the standard C library on Mac OS X (<tt class="docutils literal"><span class="pre">libSystem</span></tt>,
which is also available as the <tt class="docutils literal"><span class="pre">System.framework</span></tt> bundle).  This
example uses the dyld runtime to determine which dylib the Python
runtime came from.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Scripts/HelloWorld.py">HelloWorld.py</a></p>
<p>Demonstrates a nib-less Cocoa GUI (purely for informational purposes, you
probably shouldn't make a habit of this)</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Scripts/kvo-debugging.py">kvo-debugging.py</a></p>
<p>XXX
An example script that demonstrates how PyObjC interacts with Key-Value
Observing (KVO) at the lowest level.  This script was used to debug
the PyObjC runtime and should not be used as a guideline for writing
new KVO code.  It may be interesting to some until we ensure that we
have proper unit tests for KVO and remove this example!</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Scripts/pydict-to-objcdict.py">pydict-to-objcdict.py</a></p>
<p>Shows how <tt class="docutils literal"><span class="pre">PyObjCTools.Conversion</span></tt> can be used to convert a Python
collection into an Objective-C property list.  These functions should
not typically be necessary as the proxies for Python objects are
compatible with Objective-C plists.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Scripts/rendezvous.py">rendezvous.py</a></p>
<p>Use an NSNetService class to look for servers using rendezvous.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Scripts/signal-demo.py">signal-demo.py</a></p>
<p>Demonstrates how to get a backtrace when handling a fatal signal using
<tt class="docutils literal"><span class="pre">PyObjCTools.Signals</span></tt>.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Scripts/stdinreader.py">stdinreader.py</a></p>
<p>Demonstrates how to write a console runloop based application that uses
<tt class="docutils literal"><span class="pre">NSFileHandle</span></tt> to read stdin asynchronously.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Scripts/subclassing-objective-c.py">subclassing-objective-c.py</a></p>
<p>A doctest that demonstrates the subclassing of an Objective-C class from
Python.  Note that it is typically discouraged to define a <tt class="docutils literal"><span class="pre">__del__</span></tt>
method.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Scripts/super-call.py">super-call.py</a></p>
<p>Demonstrates how create a subclass of an Objective-C class that overrides
a selector, but calls the super implementation using Python syntax
equivalent to <tt class="docutils literal"><span class="pre">[super</span> <span class="pre">init]</span></tt>.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Scripts/wmEnable.py">wmEnable.py</a></p>
<p>Another <tt class="docutils literal"><span class="pre">objc.loadBundleFunctions</span></tt> demonstration that shows how to
call into a private CoreGraphics SPI and enable full WindowManager
access from a process that would not otherwise have it due to a
quirk in the implementation of WindowManager (the reason why <tt class="docutils literal"><span class="pre">pythonw</span></tt>
should be used instead of <tt class="docutils literal"><span class="pre">python</span></tt>).  Use at your own risk!</p>
</li>
</ul>
</div>
<div class="section" id="cocoa-applications">
<h3><a name="cocoa-applications">Cocoa Applications</a></h3>
<p>The directory <a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit">AppKit</a> contains example applications using the Cocoa
Application Framework (aka &quot;AppKit&quot;).</p>
<p>Most of the following examples contain a <tt class="docutils literal"><span class="pre">setup.py</span></tt> script that can
build an application. See <a class="reference" href="../Doc/intro.html#building-applications">Building applications</a> for details how to invoke
these scripts. Some examples contain an <tt class="docutils literal"><span class="pre">Xcode</span></tt> or <tt class="docutils literal"><span class="pre">Project</span> <span class="pre">Builder</span></tt>
project file; simply double-click it and choose <tt class="docutils literal"><span class="pre">Build</span> <span class="pre">and</span> <span class="pre">Run</span></tt>, or invoke
<tt class="docutils literal"><span class="pre">xcodebuild</span></tt> or <tt class="docutils literal"><span class="pre">pbxbuild</span></tt> from the command line depending on which you
have installed.</p>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/ClassBrowser">ClassBrowser</a></p>
<p>A simple class browser, demonstrating the use of <tt class="docutils literal"><span class="pre">NSBrowser</span></tt>
(a &quot;column view&quot; hierarchical widget) and <tt class="docutils literal"><span class="pre">NSTableView</span></tt>.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/CurrencyConverter">CurrencyConverter</a></p>
<p>A simple NIB based application. Start with this one. Also see the 
<a class="reference" href="../Doc/tutorial/tutorial.html">PyObjC tutorial</a>.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/DotView">DotView</a></p>
<p>A simple one-window demo showing how to custom drawing in a custom
<tt class="docutils literal"><span class="pre">NSView</span></tt>. Additionally shows how easy it is to embed a view in an
<tt class="docutils literal"><span class="pre">NSScrollView</span></tt>, as well as how to use an <tt class="docutils literal"><span class="pre">NSColorWell</span></tt>.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/FieldGraph">FieldGraph</a></p>
<p>This shows an simple example of an MVC based application, that also
makes use of <tt class="docutils literal"><span class="pre">NSBezierPaths</span></tt>.  Contains a <tt class="docutils literal"><span class="pre">Project</span> <span class="pre">Builder</span></tt> project,
as well as a <tt class="docutils literal"><span class="pre">setup.py</span></tt> script.</p>
<p>The application calculates the field pattern and RMS field of an antenna 
array with up to three elements.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/HotKeyPYthon">HotKeyPython</a></p>
<p>Demonstrates how to use Carbon global hot keys from a PyObjC application.
Also demonstrates how to use a <tt class="docutils literal"><span class="pre">NSApplication</span></tt> subclass.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/iClass">iClass</a></p>
<p>A more elaborate class browser; demonstrates <tt class="docutils literal"><span class="pre">NSOutlineView</span></tt> and
<tt class="docutils literal"><span class="pre">NSTableView</span></tt>.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/PackageManager">PackageManager</a></p>
<p>An implementation of the MacPython PackageManager application using
Cocoa.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/PyInterpreter">PyInterpreter</a></p>
<p>A full featured embedded Python interpreter.  This demonstrates
more complicated uses of <tt class="docutils literal"><span class="pre">NSTextView</span></tt>, manual event dispatching,
and the new text completion feature of OS X 10.3.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/PyObjCLauncher">PyObjCLauncher</a></p>
<p>A reimplementation of the Python script launcher helper application
in PyObjC.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/PythonBrowser">PythonBrowser</a></p>
<p>A reusable Python object browser, demonstrating the use of <tt class="docutils literal"><span class="pre">NSOutlineView</span></tt>
as well as how to use an <tt class="docutils literal"><span class="pre">NSWindowController</span></tt> subclass to create a window
from a menu action.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/SimpleService">SimpleService</a></p>
<p>Shows how to implement entries for the Services menu.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/TableModel">TableModel</a></p>
<p>Basic demo that shows how to use a <tt class="docutils literal"><span class="pre">NSTableView</span></tt>.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/TinyTinyEdit">TinyTinyEdit</a></p>
<p>A minimal Document-based text editor application.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/TinyURLService">TinyURLService</a></p>
<p>Another simple service, this one converts URL or strings from the
pasteboard to tinyurl.com equivalents.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/ToDo">Todo</a></p>
<p>A more complex NIB based applications. This is a document-based application.
The code is a translation into Python of an example project in 
<a class="reference" href="http://www.oreilly.com/catalog/learncocoa2/">Learning Cocoa</a> from O'Reilly</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/WebServicesTool">WebServicesTool</a></p>
<p>Queries an XML-RPC enabled web server for the methods that it implements.
Demonstrates a more advanced use of an <tt class="docutils literal"><span class="pre">NSTableView</span></tt>, how to make a
toolbar as well as how to use multi-threading.  Contains a
<tt class="docutils literal"><span class="pre">Project</span> <span class="pre">Builder</span></tt> project as well as a <tt class="docutils literal"><span class="pre">setup.py</span></tt> script.</p>
</li>
</ul>
</div>
<div class="section" id="cocoa-bindings">
<h3><a name="cocoa-bindings">Cocoa Bindings</a></h3>
<p>The <a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/CocoaBindings">CocoaBindings</a> directory contains a number of examples that make use of
Key-Value Coding and Cocoa Bindings. These scripts require Mac OS X 10.3 or
later.</p>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/CocoaBindings/Bookmarks">Bookmarks</a></p>
<p>Shows custom array controller that implements table view data
source methods to support drag and drop, including copying
objects from one window to another, drop of URLs, and 
re-ordering of the content array.</p>
<p>Originally from <a class="reference" href="http://homepage.mac.com/mmalc/CocoaExamples/controllers.html">Cocoa Bindings Examples and Hints</a>,
converted to PyObjC by u.fiedler.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/CocoaBindings/ControlledPreferences">ControlledPreferences</a></p>
<p>Demonstrates how to use Cocoa Bindings to simplify storing and
retrieving user preferences.  Also demonstrates how to use an
<tt class="docutils literal"><span class="pre">NSValueTransformer</span></tt> to archive/unarchive a non-property-list
type automatically (<tt class="docutils literal"><span class="pre">NSColor</span></tt>, in this case).</p>
<p>Originally from <a class="reference" href="http://homepage.mac.com/mmalc/CocoaExamples/controllers.html">Cocoa Bindings Examples and Hints</a>,
converted to PyObjC by u.fiedler.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/CocoaBindings/CurrencyConvBinding">CurrencyConvBinding</a></p>
<p>A rewrite of <a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/AppKit/CurrencyConverter">CurrencyConverter</a> using Cocoa Bindings.</p>
<p>Originally from
<a class="reference" href="http://developer.apple.com/documentation/Cocoa/Conceptual/CurrencyConverterBindings/index.html">Introduction to Developing Cocoa Applications Using Bindings</a>,
converted to PyObjC by u.fiedler.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/CocoaBindings/FilteringController">FilteringController</a></p>
<p>Demonstrates how to subclass <tt class="docutils literal"><span class="pre">NSArrayController</span></tt> to implement filtering
of a <tt class="docutils literal"><span class="pre">NSTableView</span></tt>.  Also demonstrates the use of indexed accessors.</p>
<p>Originally from <a class="reference" href="http://homepage.mac.com/mmalc/CocoaExamples/controllers.html">Cocoa Bindings Examples and Hints</a>,
converted to PyObjC by u.fiedler.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/CocoaBindings/GraphicsBindings">GraphicsBindings</a></p>
<blockquote>
<p>Shows the use of a custom controller, a value transformer, and two custom
bindings-enabled views. One view is a control that allows you to set the
angle and offset of a shadow; the other view observes and displays a
collection of graphic objects.</p>
</blockquote>
<p>Originally from <a class="reference" href="http://homepage.mac.com/mmalc/CocoaExamples/controllers.html">Cocoa Bindings Examples and Hints</a>,
converted to PyObjC by u.fiedler.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/CocoaBindings/ManualBindings">ManualBindings</a></p>
<p>A simple example that illustrates establishing bindings
programmatically, including a number of options such as validation
and an array operator, and indexed accessor methods. A custom model
object implements custom validation method.</p>
<p>Originally from <a class="reference" href="http://homepage.mac.com/mmalc/CocoaExamples/controllers.html">Cocoa Bindings Examples and Hints</a>,
converted to PyObjC by u.fiedler.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/CocoaBindings/TableModel">TableModel</a></p>
<p>Shows how to fill an <tt class="docutils literal"><span class="pre">NSTableView</span></tt> using Key-Value Coding.  Contains
contains an <tt class="docutils literal"><span class="pre">Xcode</span></tt> project as well as a <tt class="docutils literal"><span class="pre">setup.py</span></tt> script.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/CocoaBindings/TableModelWithSearch">TableModelWithSearch</a></p>
<p>A more advanced example of Key-Value Coding. This uses a custom 
<tt class="docutils literal"><span class="pre">NSArrayController</span></tt>.  Contains contains an <tt class="docutils literal"><span class="pre">Xcode</span></tt> project
as well as a <tt class="docutils literal"><span class="pre">setup.py</span></tt> script.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/CocoaBindings/TemperatureTransformer">TemperatureTransformer</a></p>
<p>An example that uses <tt class="docutils literal"><span class="pre">NSValueTransformer</span></tt> to convert between Celsius
and Fahrenheit.</p>
<p>Based on Apple's <a class="reference" href="http://developer.apple.com/documentation/Cocoa/Conceptual/ValueTransformers/index.html">Value Transformers</a> documentation,
converted to PyObjC by u.fiedler.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/CocoaBindings/ToDos">ToDos</a></p>
<p>Shows two array controllers, one to manage the contents of a table
view, the other to manage a pop-up menu in a table column. Also 
shows two value transformers to alter the color of text.</p>
<p>Originally from <a class="reference" href="http://homepage.mac.com/mmalc/CocoaExamples/controllers.html">Cocoa Bindings Examples and Hints</a>,
converted to PyObjC by u.fiedler.</p>
</li>
</ul>
</div>
<div class="section" id="coredata">
<h3><a name="coredata">CoreData</a></h3>
<p>The directory <a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/CoreData">CoreData</a> contains a number of examples
that use the CoreData framework. This framework is available
in MacOS X 10.4 and later.</p>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/CoreData/OutlineEdit">OutlineEdit</a></p>
<p>A python version of the OutlineEdit example that's included with
Xcode 2.0.</p>
</li>
</ul>
</div>
<div class="section" id="foundation">
<h3><a name="foundation">Foundation</a></h3>
<p>The directory <a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/#foundation">Foundation</a> contains a number of examples
that use only Foundation facilities.</p>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Foundation/simple-kvo.py">simple-kvo.py</a></p>
<p>Demonstrates the use of Key-Value Observing from a simple
script, without a runloop.  Requires Mac OS X 10.3 or later.</p>
</li>
</ul>
</div>
<div class="section" id="inject">
<h3><a name="inject">Inject</a></h3>
<p>The directory <a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Inject">Inject</a> contains a number of examples that use the
<tt class="docutils literal"><span class="pre">objc.inject</span></tt> facility to inject code into another process.  These
examples require Mac OS X 10.3 or later.</p>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Inject/IDNSnitch">IDNSnitch</a></p>
<p>A proof of concept <a class="reference" href="http://bob.pythonmac.org/archives/2005/02/07/idn-spoofing-defense-for-safari/">IDN spoofing defense</a> for Safari (tested with
v1.2.4 on Mac OS X 10.3.8).  Demonstrates how to write an application
that detects the launch of another application by bundle identifier,
how to use <tt class="docutils literal"><span class="pre">objc.inject</span></tt> to load code into another application,
how to override the implementation of an existing class but still
call back into the original implementation, and how to reduce the
size of such an application/plugin combination by using symlinks
to share object files (the PyObjC extensions in this case).</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Inject/InjectInterpreter">InjectInterpreter</a>:</p>
<p>Shows how to inject an in-process Python interpreter into another
process.  Based on the AppKit PyInterpreter example.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Inject/ClassBrowser">InjectBrowser</a>:</p>
<p>Shows how to inject an in-process Python class browser into another
process.  Based on the AppKit ClassBrowser example.</p>
</li>
</ul>
</div>
<div class="section" id="opengl">
<h3><a name="opengl">OpenGL</a></h3>
<p>The directory <a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/OpenGL">OpenGL</a> contains a number of examples that use OpenGL with
a Cocoa UI.  These examples also require <a class="reference" href="http://pyopengl.sourceforge.net/">PyOpenGL</a>.</p>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/OpenGL/OpenGLDemo">OpenGLDemo</a></p>
<p>A simple program that shows how to use OpenGL in a Cocoa program.  It is a 
port of Apple's &quot;CocoaGL&quot; example.</p>
</li>
</ul>
</div>
<div class="section" id="plugins">
<h3><a name="plugins">Plugins</a></h3>
<p>The directory <a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Plugins">Plugins</a> contains a number of examples that embed a Python
plugin into another application.  Note that due to an implementation detail
of the py2app bundle template, these plugins are only compatible with
Mac OS X 10.3 and later.</p>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Plugins/EnvironmentPrefs">EnvironmentPrefs</a></p>
<p>This <tt class="docutils literal"><span class="pre">NSPreferencePane</span></tt> can be used to edit the default environment
for the current user. It also is a simple example of a localized application.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Plugins/ProgressViewPalette">ProgressViewPalette</a></p>
<p>A simple InterfaceBuilder palette written in Python.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Plugins/SillyBallsSaver">SillyBallsSaver</a></p>
<p>A simple screensaver written in Python.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Plugins/WebKitInterpreter">WebKitInterpreter</a></p>
<p>Uses the new WebKit Cocoa plugin API available in Safari 1.3
and later to embed a PyInterpreter in the browser.</p>
</li>
</ul>
</div>
<div class="section" id="twisted-integration">
<h3><a name="twisted-integration">Twisted Integration</a></h3>
<p>The directory <a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Twisted">Twisted</a> contains a number of examples that use
<a class="reference" href="http://www.twistedmatrix.com">Twisted (2.0 or later)</a> with Cocoa.</p>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Twisted/WebServicesTool">WebServicesTool</a></p>
<p>This is a refactor of the WebServicesTool example that is made much simpler
and faster by using Twisted.</p>
</li>
</ul>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/Twisted/WebServicesTool-ControllerLayer">WebServicesTool-ControllerLayer</a></p>
<p>This is an even simpler refactor of the Twisted WebServicesTool example that
uses Cocoa Bindings to remove a lot of the UI related code.</p>
</li>
</ul>
</div>
<div class="section" id="webkit">
<h3><a name="webkit">WebKit</a></h3>
<p>The directory <a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/WebKit">WebKit</a> contains a number of examples that use the <tt class="docutils literal"><span class="pre">WebKit</span></tt>
framework, the HTML rendering engine from Safari.</p>
<ul>
<li><p class="first"><a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/WebKit/PyDocURLProtocol">PyDocURLProtocol</a></p>
<p>This example implements a subclass of <tt class="docutils literal"><span class="pre">NSURLProtocol</span></tt> that can be used
to load the <tt class="docutils literal"><span class="pre">pydoc</span></tt> documentation of a module.</p>
<p>It also includes a simple documentation browser using <tt class="docutils literal"><span class="pre">WebKit</span></tt> and the 
<tt class="docutils literal"><span class="pre">PyDocURLProtocol</span></tt> class.</p>
</li>
</ul>
</div>
<div class="section" id="some-work-in-progress-examples">
<h3><a name="some-work-in-progress-examples">Some work-in-progress examples</a></h3>
<p>The directory <a class="reference" href="http://svn.red-bean.com/pyobjc/trunk/pyobjc/Examples/NonFunctional">NonFunctional</a> may contain a number of examples that are not working
for one reason or another. The most likely reason is that example relies on features
that have not yet been implemented.</p>
</div>
</div>
<?
    include "footer.inc";
?>