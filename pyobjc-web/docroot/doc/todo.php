<?
    $title = "TODO list";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<h1 class="title">TODO list</h1>
<div class="contents topic" id="contents">
<p class="topic-title first"><a name="contents">Contents</a></p>
<ul class="simple">
<li><a class="reference" href="#introduction" id="id2" name="id2">Introduction</a></li>
<li><a class="reference" href="#important-items" id="id3" name="id3">Important items</a><ul>
<li><a class="reference" href="#better-documentation" id="id4" name="id4">Better documentation</a></li>
<li><a class="reference" href="#test-suite" id="id5" name="id5">Test suite</a></li>
</ul>
</li>
<li><a class="reference" href="#less-important-items" id="id6" name="id6">Less important items</a><ul>
<li><a class="reference" href="#refactor-some-parts-of-the-bridge" id="id7" name="id7">Refactor some parts of the bridge</a></li>
<li><a class="reference" href="#support-for-gnustep" id="id8" name="id8">Support for GNUstep</a></li>
<li><a class="reference" href="#complete-cocoa-wrapping" id="id9" name="id9">Complete Cocoa wrapping</a></li>
<li><a class="reference" href="#pickle-support" id="id10" name="id10">Pickle support</a></li>
<li><a class="reference" href="#nscoder-support" id="id11" name="id11">NSCoder support</a></li>
<li><a class="reference" href="#known-issues" id="id12" name="id12">Known issues</a></li>
<li><a class="reference" href="#code-cleanup" id="id13" name="id13">Code cleanup</a></li>
<li><a class="reference" href="#cleanup-examples" id="id14" name="id14">Cleanup Examples</a></li>
<li><a class="reference" href="#performance-tuning-testing" id="id15" name="id15">Performance tuning/testing</a></li>
<li><a class="reference" href="#add-freelists" id="id16" name="id16">Add freelists</a></li>
<li><a class="reference" href="#links-to-apple-documentation" id="id17" name="id17">Links to Apple documentation</a></li>
<li><a class="reference" href="#implement-more-of-nsmutabledictionary-in-oc-pythondictionary" id="id18" name="id18">Implement more of NSMutableDictionary in OC_PythonDictionary</a></li>
<li><a class="reference" href="#clean-up-oc-pythonobject" id="id19" name="id19">Clean up OC_PythonObject</a></li>
<li><a class="reference" href="#rewrite-scripts-find-raw-pointers-py" id="id20" name="id20">Rewrite scripts/find-raw-pointers.py</a></li>
<li><a class="reference" href="#finish-refactoring-of-the-code-generator-scripts" id="id21" name="id21">Finish refactoring of the code-generator scripts</a></li>
<li><a class="reference" href="#setup-py-cleanup" id="id22" name="id22">setup.py cleanup</a></li>
<li><a class="reference" href="#nsset-vs-set" id="id23" name="id23">NSSet vs set</a></li>
<li><a class="reference" href="#python-2-4" id="id24" name="id24">Python 2.4</a></li>
<li><a class="reference" href="#nslog-stringwithformat" id="id25" name="id25">NSLog, stringWithFormat, ...</a></li>
<li><a class="reference" href="#darwin-x86" id="id26" name="id26">Darwin/x86</a></li>
</ul>
</li>
</ul>
</div>
<div class="section" id="introduction">
<h3><a class="toc-backref" href="#id2" name="introduction">Introduction</a></h3>
<p>This document contains an (incomplete) list of work items.</p>
</div>
<div class="section" id="important-items">
<h3><a class="toc-backref" href="#id3" name="important-items">Important items</a></h3>
<div class="section" id="better-documentation">
<h4><a class="toc-backref" href="#id4" name="better-documentation">Better documentation</a></h4>
<ul class="simple">
<li>There should be more developer and and end-user documentation.</li>
<li>The tutorials should have screenshots for the website.</li>
<li>There should be a document containing references to &quot;third party&quot; tutorials,
articles, and information about PyObjC.</li>
<li>The documentation should be updated to take advantage of reStructuredText
features.  Currently, documentation doesn't refer to itself consistently
(usually without hyperlink), and most documents are missing metadata.</li>
<li>build_html should include a step that performs syntax highlighting for
Python and Objective-C code snippets.</li>
</ul>
</div>
<div class="section" id="test-suite">
<h4><a class="toc-backref" href="#id5" name="test-suite">Test suite</a></h4>
<p>The test suite needs to be enhanced.</p>
<ul class="simple">
<li>Somehow find a way to check code-coverage of the unittests.</li>
<li>Tests in the AppKit and Foundation packages that test functionality in
the objc package should be moved to the objc package.</li>
<li>Enhance KVO/KVC tests</li>
<li>tests for all functions in <tt class="docutils literal"><span class="pre">Modules/*/*Mapping*.m</span></tt>
(including IMPs)</li>
<li>tests for all non-generated function wrappers (and some for the generated
functions as well, just in case the generator script is buggy)</li>
<li>tests where Python implementation of method with output arguments returns
the wrong value (type, number of values)</li>
<li>Add tests for accepting any sequence when depythonifying structs and arrays.</li>
<li>Add more tests for objc_support.m to unittest.c</li>
<li>Tests for <tt class="docutils literal"><span class="pre">objc.createOpaquePointerType</span></tt>.</li>
</ul>
</div>
</div>
<div class="section" id="less-important-items">
<h3><a class="toc-backref" href="#id6" name="less-important-items">Less important items</a></h3>
<div class="section" id="refactor-some-parts-of-the-bridge">
<h4><a class="toc-backref" href="#id7" name="refactor-some-parts-of-the-bridge">Refactor some parts of the bridge</a></h4>
<p>From the top of my head:</p>
<ul class="simple">
<li>Restructure selector.m, this file is too long and complicated. We could
do away with the difference between method implemented in Python and
Objective-C.</li>
<li>Remove the need for <tt class="docutils literal"><span class="pre">pyobjc_classMethods</span></tt>, you should be able to call
class methods in the obvious way.  This would (finally) close <a class="reference" href="http://sourceforge.net/tracker/index.php?func=detail&amp;aid=836247&amp;group_id=14534&amp;atid=114534">836247</a>.</li>
</ul>
<ul>
<li><p class="first">Also restructure class-builder.m, this file is way to large.</p>
</li>
<li><p class="first">Rewrite selectors to work as regular functions with some attributes,
rather than descriptors, so that they can be used more easily with tools
such as PyProtocols dispatch.</p>
<p>XXX(Ronald): that's only possible for methods with a python implementation,
and should result in less code as well. A disadvantage is that this would
probably be a backward-incomptable change, but that should not be a problem.</p>
</li>
</ul>
</div>
<div class="section" id="support-for-gnustep">
<h4><a class="toc-backref" href="#id8" name="support-for-gnustep">Support for GNUstep</a></h4>
<p>The current SVN version contains some support for GNUstep, this needs to
be enhanced.</p>
<p>Unless somebody actually starts working on this GNUstep support will slowly
fade away.</p>
</div>
<div class="section" id="complete-cocoa-wrapping">
<h4><a class="toc-backref" href="#id9" name="complete-cocoa-wrapping">Complete Cocoa wrapping</a></h4>
<p>We do not yet have a 100% coverage of the Cocoa API's. We also need code in
the testsuite that checks if the function wrappers are working as expected.</p>
<p>Not all constants and enums from Cocoa are currently wrapped.  The annotations
for input/output arguments are not all checked and may not be complete or
correct.</p>
<p>We also don't support all &quot;difficult&quot; methods yet, implementing these is
not too hard but it is a lot of work.</p>
<p>Note that even though we do not have 100% coverage of Cocoa, the majority
of useful functions, constants, and &quot;difficult&quot; methods are wrapped.  If you
run across a missing or incorrectly wrapped constant, function, or method
please report it as a bug and/or post to pyobjc-dev about the issue.  This is
one area we intend to improve after the release of 1.3 when our new
wrapper-generators are in a more complete state.</p>
</div>
<div class="section" id="pickle-support">
<h4><a class="toc-backref" href="#id10" name="pickle-support">Pickle support</a></h4>
<p>Objective-C objects don't support pickling.</p>
<p>This is post-1.3 work, in general this is a hard problem because it may 
involve object cycles that cross the Python-ObjC boundary.</p>
</div>
<div class="section" id="nscoder-support">
<h4><a class="toc-backref" href="#id11" name="nscoder-support">NSCoder support</a></h4>
<p>It might be useful to add default implementations of <tt class="docutils literal"><span class="pre">encodeWithCoder:</span></tt> and
<tt class="docutils literal"><span class="pre">initWithCoder:</span></tt> methods to Python subclasses of Objective-C classes that 
implement these.  Note that property list types should already be serializable
(<tt class="docutils literal"><span class="pre">int</span></tt>, <tt class="docutils literal"><span class="pre">long</span></tt>, <tt class="docutils literal"><span class="pre">unicode</span></tt>, <tt class="docutils literal"><span class="pre">list</span></tt>, <tt class="docutils literal"><span class="pre">tuple</span></tt>, <tt class="docutils literal"><span class="pre">dict</span></tt>).</p>
<p>See also <cite>Pickle support</cite>.</p>
</div>
<div class="section" id="known-issues">
<h4><a class="toc-backref" href="#id12" name="known-issues">Known issues</a></h4>
<p>It is impossible to support methods with a variable number of arguments in the
generic code (you have to re-implement almost all of the logic of these 
methods in order to know how many and which types of arguments are expected).
Luckily there are not many varargs methods and most (if no all) of them can
be easily avoided.</p>
<p>All existing varargs methods should be located and documented. Where possible
we should provide custom wrappers, otherwise we should document alternatives.</p>
<p>Limitations such as the above should be clearly documented elsewhere, these
are not necessarily TODO items.</p>
</div>
<div class="section" id="code-cleanup">
<h4><a class="toc-backref" href="#id13" name="code-cleanup">Code cleanup</a></h4>
<ul class="simple">
<li>Check all error/exception messages</li>
<li>Check/cleanup error handling</li>
<li>Finish in-code documentation for the C code</li>
</ul>
</div>
<div class="section" id="cleanup-examples">
<h4><a class="toc-backref" href="#id14" name="cleanup-examples">Cleanup Examples</a></h4>
<p>The CurrencyConverter example should be removed, this should be the same as the
final step of the tutorial. It isn't at the moment because additional cruft in
the example.</p>
<ul class="simple">
<li>dictionary.py and subclassing-objective-c.py
These are doctests and should be moved to the documentation (with a hook
in the unittests for making sure the code keeps working).</li>
<li>pydict-to-objcdict.py
Move to unittests</li>
<li>super-call.py
Move to documentation  (unittest?)</li>
</ul>
<p>Add examples that demonstrate:</p>
<ul class="simple">
<li>how to use a lot of Cocoa features</li>
<li>how to integrate with MacPython</li>
<li>how to use PIL with Cocoa</li>
</ul>
</div>
<div class="section" id="performance-tuning-testing">
<h4><a class="toc-backref" href="#id15" name="performance-tuning-testing">Performance tuning/testing</a></h4>
<p>Design and implement a set of performance tests for the bridge. Use this to 
investigate and fix any possible performance problems.</p>
</div>
<div class="section" id="add-freelists">
<h4><a class="toc-backref" href="#id16" name="add-freelists">Add freelists</a></h4>
<p>PyObjCSelector objects and PyObjCObject objects are created on
a regular basis, we should check if using freelists would speed this up. See
also <cite>Performance tuning/testing</cite>.</p>
<p>NOTE: first add performance tests then experiment with freelists.</p>
</div>
<div class="section" id="links-to-apple-documentation">
<h4><a class="toc-backref" href="#id17" name="links-to-apple-documentation">Links to Apple documentation</a></h4>
<p>Links to Apple documentation are not stable, can we add a layer of indirection
here, e.g. link to the PyObjC website that will redirect to the right
location?</p>
<p>We should also provide links to locally installed documentation,
especially in the documentation that will be installed on the users machine.</p>
</div>
<div class="section" id="implement-more-of-nsmutabledictionary-in-oc-pythondictionary">
<h4><a class="toc-backref" href="#id18" name="implement-more-of-nsmutabledictionary-in-oc-pythondictionary">Implement more of NSMutableDictionary in OC_PythonDictionary</a></h4>
<p>The implementation of OC_PythonDictionary is very minimal, we should add
additional methods in the NSMutableDictionary interface if those can be 
implemented efficiently. The default implementation will take care of the
methods we cannot implement efficiently.</p>
<p>And the same is true of OC_PythonArray</p>
<p>In both cases we shouldn't do this unless we can measure the difference in
performance.</p>
</div>
<div class="section" id="clean-up-oc-pythonobject">
<h4><a class="toc-backref" href="#id19" name="clean-up-oc-pythonobject">Clean up OC_PythonObject</a></h4>
<p>The code is a mess.</p>
</div>
<div class="section" id="rewrite-scripts-find-raw-pointers-py">
<h4><a class="toc-backref" href="#id20" name="rewrite-scripts-find-raw-pointers-py">Rewrite scripts/find-raw-pointers.py</a></h4>
<p>This is a script for finding 'difficult' methods. The script should be 
refactored to make it easier to create readable reports.</p>
</div>
<div class="section" id="finish-refactoring-of-the-code-generator-scripts">
<h4><a class="toc-backref" href="#id21" name="finish-refactoring-of-the-code-generator-scripts">Finish refactoring of the code-generator scripts</a></h4>
<ol class="arabic simple">
<li>Change code-generator scripts to use loadBundleFunctions, etc.</li>
<li>Move the code-generator scripts to <tt class="docutils literal"><span class="pre">PyObjCTools</span></tt>, to make it easier
for others to generate wrappers.</li>
<li>Install <tt class="docutils literal"><span class="pre">pyobjc-api.h</span></tt>.</li>
</ol>
</div>
<div class="section" id="setup-py-cleanup">
<h4><a class="toc-backref" href="#id22" name="setup-py-cleanup">setup.py cleanup</a></h4>
<ul class="simple">
<li>Use 'WrapperGenerator.py', probably need to create a custom build action
for that.</li>
</ul>
</div>
<div class="section" id="nsset-vs-set">
<h4><a class="toc-backref" href="#id23" name="nsset-vs-set">NSSet vs set</a></h4>
<p>Check if it is possible to wrap <tt class="docutils literal"><span class="pre">NSSet</span></tt> using <tt class="docutils literal"><span class="pre">set</span></tt> (and v.v.).</p>
<p>Only implement this when it is possible to convert without loss of information.</p>
<p><strong>Ronald, 20050130</strong>: <em>converting</em> is not an option: PyObjC takes care to
preserve the identity of ObjC objects when passed through python. This is 
necessary for at least some APIs.   Furthermore, both <tt class="docutils literal"><span class="pre">NSSet</span></tt> and 
<tt class="docutils literal"><span class="pre">__builtin__.set</span></tt> are mutable!</p>
</div>
<div class="section" id="python-2-4">
<h4><a class="toc-backref" href="#id24" name="python-2-4">Python 2.4</a></h4>
<p>Python 2.4 introduces a decorator syntax. Add convenience functions that
make it easier to use decorators with PyObjC.</p>
<p>Also add example programs using decorators. Actually, first add the example(s)
and extract useful convenience functions from those.</p>
<p>An example of a convenience function would be:</p>
<pre class="literal-block">
import objc

def method_signature(signature):
        def make_selector(func):
                return objc.selector(func, signature=signature)
        return make_selector
</pre>
<p>Which can be used like this:</p>
<pre class="literal-block">
class FooClass (NSObject):

        &#64;method_signature(&quot;v&#64;:i&quot;)
        def myIntMethod_(self, value):
                pass
</pre>
</div>
<div class="section" id="nslog-stringwithformat">
<h4><a class="toc-backref" href="#id25" name="nslog-stringwithformat">NSLog, stringWithFormat, ...</a></h4>
<p>Functions and methods that use format strings are not properly wrapped. Fix
that.</p>
</div>
<div class="section" id="darwin-x86">
<h4><a class="toc-backref" href="#id26" name="darwin-x86">Darwin/x86</a></h4>
<ul class="simple">
<li>mach_inject needs to be ported to intel.</li>
<li>when that works we need to figure out if and how we can inject code into 
programs running an other instruction set (e.g. cross-platform inject).</li>
<li>drop autoconf/automake for libffi, integrate into the normal build machinery.
This will make it easier to create fat binaries of PyObjC later on.</li>
</ul>
</div>
</div>
</div>
<?
    include "footer.inc";
?>