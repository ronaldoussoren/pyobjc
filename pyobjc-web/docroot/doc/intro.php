<?
    $title = "An introduction to PyObjC";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/05/04 12:56:38 $';

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
<li><a class="reference" href="#work-in-progress" id="id1" name="id1">WORK IN PROGRESS</a></li>
<li><a class="reference" href="#preface" id="id2" name="id2">Preface</a></li>
<li><a class="reference" href="#objective-c-for-pyobjc-users" id="id3" name="id3">Objective-C for PyObjC users</a></li>
<li><a class="reference" href="#overview-of-the-bridge" id="id4" name="id4">Overview of the bridge</a></li>
<li><a class="reference" href="#cocoa-for-python-programmers" id="id5" name="id5">Cocoa for Python programmers</a></li>
<li><a class="reference" href="#building-applications" id="id6" name="id6">Building applications</a><ul>
<li><a class="reference" href="#pure-python-buildapp-py" id="id7" name="id7">&quot;Pure python&quot; :  buildapp.py</a></li>
<li><a class="reference" href="#ide-approach-project-builder" id="id8" name="id8">&quot;IDE approach&quot; : Project builder</a></li>
</ul>
</li>
</ul>
</div>
<div class="section" id="work-in-progress">
<h1><a class="toc-backref" href="#id1" name="work-in-progress">WORK IN PROGRESS</a></h1>
<p>This document is work in progress and thin on details.</p>
</div>
<div class="section" id="preface">
<h1><a class="toc-backref" href="#id2" name="preface">Preface</a></h1>
<p>PyObjC is a bridge between Python and Objective-C. It allows you to write 
Python scripts that reuse and extend existing Objective-C class libraries, 
most importantly the <a class="reference" href="http://developer.apple.com/techpubs/macosx/Cocoa/CocoaTopics.html">Cocoa library</a> by <a class="reference" href="http://www.apple.com/">Apple</a>.</p>
<p>This document describes how to use Objective-C class libraries from Python
scripts and how to interpret the documentation of those libraries, from the 
point of view of a Python programmer.</p>
</div>
<div class="section" id="objective-c-for-pyobjc-users">
<h1><a class="toc-backref" href="#id3" name="objective-c-for-pyobjc-users">Objective-C for PyObjC users</a></h1>
<p>Objective-C is an object-oriented programming language that is an extention 
of C and borrows heavily from Smalltalk. It features single inheritance with
(in theory) multiple root classes and dynamic dispatch of methods. This is
basicly the same as python with single inheritance.</p>
<p>An important difference between Python and Objective-C is that the latter is
not a pure object-oriented language. Some values are not objects, but values
of plain C types, such as <tt class="literal"><span class="pre">int</span></tt> and <tt class="literal"><span class="pre">double</span></tt>. These basic C types can also
be used as the types of arguments and the return value of methods.</p>
<p>Object allocation and initialization are explicit and seperate actions in 
Objective-C. The former is done by the class-method <tt class="literal"><span class="pre">alloc</span></tt>, while the
latter is done by instance-methods whose name customarily starts with <tt class="literal"><span class="pre">init</span></tt>.</p>
<p>For more information about Objective-C see:</p>
<ul class="simple">
<li><a class="reference" href="http://developer.apple.com/techpubs/macosx/Cocoa/ObjectiveC/index.html">The Objective-C Programming Language</a> at <a class="reference" href="http://www.apple.com/">Apple</a>.</li>
</ul>
</div>
<div class="section" id="overview-of-the-bridge">
<h1><a class="toc-backref" href="#id4" name="overview-of-the-bridge">Overview of the bridge</a></h1>
<p>Objective-C classes are visible as Python classes and can be subclassed just
like normal Python classes. The major differences between normal Python classes
and Objective-C classes are the way you create instances and the fact that 
Objective-C classes have <em>odd</em> names.</p>
<p>As described in <a class="reference" href="#objective-c-for-pyobjc-users">Objective-C for PyObjC users</a> the creation of Objective-C 
objects is a two-stage process. You first call the class method <tt class="literal"><span class="pre">alloc</span></tt>, and
then call some variation of <tt class="literal"><span class="pre">init</span></tt> to initialize the objects. The newly
created object is the result of the call to <tt class="literal"><span class="pre">init</span></tt>. Most classes have 
convienence class methods that combine the calls to <tt class="literal"><span class="pre">alloc</span></tt> and <tt class="literal"><span class="pre">init</span></tt>.</p>
<p>Objective-C methods are bridged to python callables. Because Objective-C method 
names can contain colons it is necessary to translate methods names. The rules
for translation are:</p>
<ul class="simple">
<li>Concatenate all elements of the method name: <tt class="literal"><span class="pre">someMethod:withFoo:andBar:</span></tt></li>
<li>Then convert all colons to underscores: <tt class="literal"><span class="pre">someMethod_withFoo_andBar_</span></tt></li>
</ul>
<p>The bridged method usually has the same number of arguments as the orginal 
method and also returns the same as the original method. In special 
circumstances the method interface may be different from the Objective-C 
interface, those methods are document in 'some other document'. Furthermore,
some methods have pass-by-reference arguments (that is a pointer to a single
value that is used to transfer data to (in), from (out) or to-and-from (inout)
the method. The arguments that are passed to methods is present as normal 
arguments in the bridged method (e.g. if the method has an <tt class="literal"><span class="pre">int*</span></tt> argument
the bridged method has has an integer argument).  Data that is passed from the
function results in additional return values from the function.</p>
<p>When the bridge cannot automaticly deduce the right signature for a method, or
if you want to add a method whose name cannot be transformed into python (
for example a methodname containing <tt class="literal"><span class="pre">$</span></tt>), you'll have to add explicit hints
to your code. You do this by calling the function <tt class="literal"><span class="pre">objc.selector</span></tt> and using
the result instead of your method definition:</p>
<pre class="literal-block">
class MyObject (NSObject):
        def someMethod_(self, arg):
                pass

        someMethod_ = objc.selector(someMethod_, ...)
</pre>
<p>The other arguments of <tt class="literal"><span class="pre">objc.selector</span></tt> (not shown in the example) provide
additional information about the method to the bridge, see the online 
documentation for more information about this function. It is almost never
necessary to use this technique.</p>
<p>The need for additional hints to the bridge often arises from implementing an
(informal) protocol in Python. Because the methods compromising the protocol
are probably not implemented in the superclass the bridge often cannot deduce 
the correct method signatures for the methods you implemented. To avoid the
need for using <tt class="literal"><span class="pre">objc.selector</span></tt> and to make it explicit that your implementing
an (informal) protocol the bridge has explicit support for these (informal)
protocols.</p>
<p>To tell the bridge that your implementing an informal protocol you use an
<tt class="literal"><span class="pre">informal_protocol</span></tt> object as a mixin:</p>
<pre class="literal-block">
class MyModel (NSObject, anInformalProtocol):
        pass
</pre>
<p>The <tt class="literal"><span class="pre">AppKit</span></tt> and <tt class="literal"><span class="pre">Foundation</span></tt> modules define <tt class="literal"><span class="pre">informal_protocol</span></tt> objects 
for most (informal) protocols and defined by these frameworks (both the 
explicitly documented protocols and the protocols used to communicate between
an object and its delegate).</p>
</div>
<div class="section" id="cocoa-for-python-programmers">
<h1><a class="toc-backref" href="#id5" name="cocoa-for-python-programmers">Cocoa for Python programmers</a></h1>
<p>Cocoa frameworks are mapped onto Python packages with the same name, that is
the classes, constants and functioins from the AppKit framework are available
after you import <tt class="literal"><span class="pre">AppKit</span></tt> in your Python script.</p>
<p>The module <tt class="literal"><span class="pre">PyObjCTools.NibClassBuilder</span></tt> can be used to make working with 
NIB files more convenient. This module can be used to extract information 
about classes from NIB files, both as a standalone tool generating source code 
and during runtime. See the online documentation for this module for more
information.</p>
<p><strong>TODO</strong>:</p>
<ul class="simple">
<li>Links to example PyObjC scripts.</li>
</ul>
<p>More information on Cocoa programming can be found at:</p>
<ul class="simple">
<li><a class="reference" href="http://developer.apple.com/techpubs/macosx/Cocoa/CocoaTopics.html">Cocoa documentation at the Apple developer website</a></li>
<li><a class="reference" href="http://developer.apple.com/samplecode/Sample_Code/Cocoa.htm">Cocoa examples at the Apple developer website</a></li>
<li><a class="reference" href="http://www.stepwise.com/">stepwise.com</a></li>
<li>Your local bookstore or library</li>
</ul>
</div>
<div class="section" id="building-applications">
<h1><a class="toc-backref" href="#id6" name="building-applications">Building applications</a></h1>
<p>There are two different ways to build applications with PyObjC. There are no
major advantages to using either one of them, use the one that is most 
convenient to you.</p>
<div class="section" id="pure-python-buildapp-py">
<h2><a class="toc-backref" href="#id7" name="pure-python-buildapp-py">&quot;Pure python&quot; :  buildapp.py</a></h2>
<p>PyObjC includes a copy of the <tt class="literal"><span class="pre">bundlebuilder</span></tt> module. This module will be part
of the Python 2.3 MacPython release and is a to build distutil-style scripts 
for building (standalone) applications.</p>
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
<p>The online documentation for <tt class="literal"><span class="pre">bundlebuilder</span></tt> contains more information on 
building <tt class="literal"><span class="pre">buildapp.py</span></tt> scripts.</p>
</div>
<div class="section" id="ide-approach-project-builder">
<h2><a class="toc-backref" href="#id8" name="ide-approach-project-builder">&quot;IDE approach&quot; : Project builder</a></h2>
<p>PyObjC includes a number of Project Builder templates that can be used to 
build (standalone) applications.</p>
<p><strong>TODO</strong>:</p>
<ul class="simple">
<li>Expand this section, input needed as I don't use Project Builder</li>
<li>Add link to documentation about our templates</li>
<li>Add link to documentation for Project Builder</li>
</ul>
</div>
</div>
</div>
<?
    include "footer.inc";
?>