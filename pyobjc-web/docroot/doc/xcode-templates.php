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
<td><a class="first last reference" href="mailto:bbum&#64;mac.com">bbum&#64;mac.com</a></td></tr>
</tbody>
</table>
<p>To use the project templates, simply copy (or link) them into the Project
Templates directory used by Project Builder.  The project templates are also
included in the PyObjC installer package.</p>
<div class="contents topic" id="contents">
<p class="topic-title first"><a name="contents">Contents</a></p>
<ul class="simple">
<li><a class="reference" href="#notes" id="id1" name="id1">Notes</a></li>
<li><a class="reference" href="#cocoa-python-templates" id="id2" name="id2">Cocoa-Python Templates</a></li>
<li><a class="reference" href="#cocoa-python-application" id="id3" name="id3">Cocoa-Python Application</a></li>
</ul>
</div>
<div class="section" id="notes">
<h3><a class="toc-backref" href="#id1" name="notes">Notes</a></h3>
<ul>
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
<li><p class="first">There is risk that the pyobjc modules compiled for one version of python
will not work with another.  Where this may be a problem is if the a
standalone application is packaged with the pyobjc modules compiled
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
<h3><a class="toc-backref" href="#id2" name="cocoa-python-templates">Cocoa-Python Templates</a></h3>
<p>The Cocoa-Python templates all create various different kinds of Cocoa
application projects.  Be sure and pick the correct project type for your
needs.</p>
</div>
<div class="section" id="cocoa-python-application">
<h3><a class="toc-backref" href="#id3" name="cocoa-python-application">Cocoa-Python Application</a></h3>
<p>A project created from this template is designed to implement standalone,
pure-Python, applications that are compatible with Apple's build of Python as
well as all other builds of python that support PyObjC.</p>
<p>When building the 'install' target, the resulting application wrapper will
included the PyObjC module and can be launched on any stock OS X 10.3 system
without requiring PyObjC to be preinstalled.</p>
</div>
</div>
<?
    include "footer.inc";
?>