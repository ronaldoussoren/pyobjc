<?
    $title = "Python Project Templates";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<h1 class="title">Python Project Templates</h1>
<table class="docinfo" frame="void" rules="none">
<col class="docinfo-name" />
<col class="docinfo-content" />
<tbody valign="top">
<tr><th class="docinfo-name">Author:</th>
<td>Bill Bumgarner</td></tr>
<tr><th class="docinfo-name">Contact:</th>
<td><a class="first last reference" href="mailto:bbum&#64;codefab.com">bbum&#64;codefab.com</a></td></tr>
</tbody>
</table>
<p>To use the project templates, simply copy (or link) them into the Project
Templates directory used by Project Builder.  The project templates are also
included in the PyObjC installer package.</p>
<div class="contents topic" id="contents">
<p class="topic-title first"><a name="contents">Contents</a></p>
<ul class="simple">
<li><a class="reference" href="#notes" id="id2" name="id2">Notes</a></li>
<li><a class="reference" href="#cocoa-python-templates" id="id3" name="id3">Cocoa-Python Templates</a></li>
<li><a class="reference" href="#cocoa-python-application" id="id4" name="id4">Cocoa-Python Application</a></li>
<li><a class="reference" href="#cocoa-python-objc-application" id="id5" name="id5">Cocoa-Python-ObjC Application</a></li>
<li><a class="reference" href="#cocoa-python-document-based-application" id="id6" name="id6">Cocoa-Python Document-based Application</a></li>
<li><a class="reference" href="#cocoa-python-objc-document-based-application" id="id7" name="id7">Cocoa-Python-ObjC Document-based Application</a></li>
</ul>
</div>
<div class="section" id="notes">
<h3><a class="toc-backref" href="#id2" name="notes">Notes</a></h3>
<ul>
<li><p class="first">PyObjC's Project Builder support is unmaintained and its use for new projects
is not recommended.</p>
</li>
<li><p class="first">In all cases that involve loading frameworks or bundles, all of the classes
in that framework or bundle can be made available by using the
<tt class="docutils literal"><span class="pre">loadBundle()</span></tt> function in the <tt class="docutils literal"><span class="pre">objc</span></tt> module:</p>
<pre class="literal-block">
objc.loadBundle(&quot;MyFramework&quot;, globals(), bundle_path=&quot;/path/to/MyFramework.framework&quot;)
</pre>
<p>This has the effect of importing all of the classes in the bundle or
framework into the current python scope's globals.  For all intents and
purposes, it is similar to:</p>
<pre class="literal-block">
from Foundation import *
</pre>
</li>
<li><p class="first">There is risk that the PyObjC modules compiled for one version of python
will not work with another.  Where this may be a problem is if the a
standalone application is packaged with the PyObjC modules compiled
against, say, the Fink or Framework builds of Python, but is then executed
using the Apple supplied python binary.</p>
</li>
</ul>
<blockquote>
<ul class="simple">
<li>The <em>Project Templates</em> directory includes a <strong>clean.py</strong> script that
removes noise files from the project templates.   When working on project
templates, it is recommended that this script be invoked before creating a
test project from one of the templates.   For example, the presence of
user specific project builder settings will cause any projects created
from a template to be incorrect.</li>
</ul>
</blockquote>
</div>
<div class="section" id="cocoa-python-templates">
<h3><a class="toc-backref" href="#id3" name="cocoa-python-templates">Cocoa-Python Templates</a></h3>
<p>The Cocoa-Python templates all create various different kinds of Cocoa
application projects.   Some of the resulting projects are incompatible with
Apple's build of Python[#].  Be sure and pick the correct project type for your
needs.</p>
</div>
<div class="section" id="cocoa-python-application">
<h3><a class="toc-backref" href="#id4" name="cocoa-python-application">Cocoa-Python Application</a></h3>
<p>A project created from this template is designed to implement standalone,
pure-Python, applications that are compatible with Apple's build of Python as
well as all other builds of python that support PyObjC.</p>
<p>When building the 'install' target, the resulting application wrapper will
included the PyObjC module and can be launched on any stock OS X 10.2 system
without requiring PyObjC to be preinstalled.</p>
</div>
<div class="section" id="cocoa-python-objc-application">
<h3><a class="toc-backref" href="#id5" name="cocoa-python-objc-application">Cocoa-Python-ObjC Application</a></h3>
<p>A project created from this template includes an embedded framework project
into which all compiled code can be placed.  Upon launch, the application
automatically dynamically loads the embedded framework containing the
compiled code.</p>
<p>Each Framework's Resources directory is automatically added to sys.path.</p>
<!-- Cocoa-Python Application (Embedded Interpreter)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
<!-- This project template uses an embedded Python interpreter.  As such,
Objective-C classes can be freely mixed into the project along with Python
classes.   However, because it uses an embedded interpreter, this project
must be built and run after some version of Python is installed that can
support an embedded interpreter.  Alternatively, an application based on this
template must include a build of Python within its app wrapper. -->
<!-- This type of project is not compatible with Apple's build of Python. -->
</div>
<div class="section" id="cocoa-python-document-based-application">
<h3><a class="toc-backref" href="#id6" name="cocoa-python-document-based-application">Cocoa-Python Document-based Application</a></h3>
<p>This template works like the <a class="reference" href="#cocoa-python-application">Cocoa-Python Application</a> template in that it
is compatible with the Apple build of Python.   It creates an application
that uses Cocoa's Multiple Document Architecture in the same fashion as the
default Cocoa Document-based Application supplied with Project Builder.</p>
</div>
<div class="section" id="cocoa-python-objc-document-based-application">
<h3><a class="toc-backref" href="#id7" name="cocoa-python-objc-document-based-application">Cocoa-Python-ObjC Document-based Application</a></h3>
<p>A project created from this template includes an embedded framework project
into which all compiled code can be placed.  Upon launch, the application
automatically dynamically loads the embedded framework containing the
compiled code. It is based on the <a class="reference" href="#cocoa-python-document-based-application">Cocoa-Python Document-based Application</a>
template.  It creates an application that uses Cocoa's Multiple Document 
Architecture in the same fashion as the default Cocoa Document-based 
Application supplied with Project Builder.</p>
<p>Each Framework's Resources directory is automatically added to sys.path.</p>
<!-- Cocoa-Python Document-based Application (Embedded Interpreter)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
<!-- This template works like the `Cocoa-Python Application (Embedded
Interpreter)`_ template in that it is incompatible with the Apple build of
Python.   It creates an application that uses Cocoa's Multiple Document
Architecture in the same fashion as the default Cocoa Document-based
Application supplied with Project Builder. -->
<table class="docutils footnote" frame="void" id="id1" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a name="id1">[1]</a></td><td>Apple's build of python lacks a shared or static library to which an
application can be linked.  As such, it is impossible to embed the
Python interpreter into an application.  Because of this, it is
impossible to directly link compiled objective-c directly into an
application project.  Hence, the &quot;Apple Python compatible&quot; projects are
labeled as 100% pure Python.  Since bundles and frameworks can be
loaded into such applications, it is still possible to use compiled
classes.</td></tr>
</tbody>
</table>
</div>
</div>
<?
    include "footer.inc";
?>