<?
    $title = "PyObjC Xcode Templates";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<h1 class="title">PyObjC Xcode Templates</h1>
<table class="docinfo" frame="void" rules="none">
<col class="docinfo-name" />
<col class="docinfo-content" />
<tbody valign="top">
<tr><th class="docinfo-name">Author:</th>
<td>Bob Ippolito</td></tr>
<tr><th class="docinfo-name">Contact:</th>
<td><a class="first last reference" href="mailto:bob&#64;redivi.com">bob&#64;redivi.com</a></td></tr>
</tbody>
</table>
<p>The PyObjC Xcode Templates offer an alternative to developing
applications &quot;by hand&quot; using py2app, as described in the
tutorial.  As of PyObjC 1.3.1, these templates are py2app based,
so there is no longer a technical reason not to use them.</p>
<div class="contents topic" id="contents">
<p class="topic-title first"><a name="contents">Contents</a></p>
<ul class="simple">
<li><a class="reference" href="#installing" id="id3" name="id3">Installing</a></li>
<li><a class="reference" href="#notes" id="id4" name="id4">Notes</a></li>
<li><a class="reference" href="#groups" id="id5" name="id5">Groups</a></li>
<li><a class="reference" href="#targets" id="id6" name="id6">Targets</a></li>
<li><a class="reference" href="#custom-executable" id="id7" name="id7">Custom Executable</a></li>
<li><a class="reference" href="#pyobjc-application" id="id8" name="id8">PyObjC Application</a></li>
<li><a class="reference" href="#pyobjc-document-based-application" id="id9" name="id9">PyObjC Document Based Application</a></li>
<li><a class="reference" href="#pyobjc-mixed-application" id="id10" name="id10">PyObjC Mixed Application</a></li>
</ul>
</div>
<div class="section" id="installing">
<h3><a class="toc-backref" href="#id3" name="installing">Installing</a></h3>
<p>If you have installed PyObjC 1.3.1 or later using the installer, then
the Xcode templates are already installed.</p>
<p>If you have installed any version of PyObjC prior to 1.3.1, then you
may have old Xcode templates installed.  These Xcode templates named
&quot;Cocoa-Python Application&quot; and &quot;Cocoa-Python Document Based Application&quot;
should NOT be used, and it would be wise to remove them.  They can
be found here:</p>
<pre class="literal-block">
/Library/Application Support/Apple/Developer Tools/Project Templates
</pre>
<p>To install the templates manually, simply copy (or link) them into
this Project Templates folder.</p>
</div>
<div class="section" id="notes">
<h3><a class="toc-backref" href="#id4" name="notes">Notes</a></h3>
<ul class="simple">
<li>These templates are brand new in PyObjC 1.3.1 and haven't had much
use yet.  If you think that you have found a bug or would like them to be
changed in some way, please speak up on the <a class="reference" href="http://lists.sourceforge.net/lists/listinfo/pyobjc-dev">pyobjc-dev</a>
mailing list, and/or <a class="reference" href="http://sourceforge.net/tracker/?group_id=14534&amp;atid=114534">report a bug</a>.</li>
</ul>
<ul>
<li><p class="first">The Python interpreter used by the templates is determined by the
first line of the <tt class="docutils literal"><span class="pre">setup.py</span></tt> file.  By default, it points to:</p>
<pre class="literal-block">
#!/usr/bin/env python
</pre>
<p>This means that whichever Python that comes first on the <tt class="docutils literal"><span class="pre">PATH</span></tt>
will be used.  This will normally be the Python 2.3 interpreter
that ships with Mac OS X.  If you would like to use a different
interpreter, you have two choices:</p>
<ol class="arabic">
<li><p class="first">Edit the first line of <tt class="docutils literal"><span class="pre">setup.py</span></tt> to point to the desired
interpreter explicitly, for example:</p>
<pre class="literal-block">
#!/usr/local/bin/python2.4
</pre>
<p>This change must be done to every project that you use the
template from.  Alternatively, you can make this change
to the templates themselves so that this is set for all
new projects.  See the Installing section above for the
location of these templates.  If you choose to do this,
edit the <tt class="docutils literal"><span class="pre">setup.py</span></tt> directly.  Do not open the
<tt class="docutils literal"><span class="pre">.xcode</span></tt> project in the template, as Xcode templates
can be rather fragile.</p>
</li>
<li><p class="first">Change your <tt class="docutils literal"><span class="pre">PATH</span></tt> environment variable so that the location
of your Python interpreter appears before the others.  Since
LaunchServices and thus Xcode is not started by your user shell,
you will need to specify it in a plist.  See <a class="reference" href="http://developer.apple.com/qa/qa2001/qa1067.html">QA1067</a>, 
<a class="reference" href="http://developer.apple.com/documentation/MacOSX/Conceptual/BPRuntimeConfig/Concepts/EnvironmentVars.html">Runtime Configuration: Environment Variables</a>, and the 
<a class="reference" href="file:///Developer/Python/PyObjC/Examples/Plugins/EnvironmentPrefs">EnvironmentPrefs</a> System Preferences plug-in example that
comes with PyObjC for more information about how to do this.</p>
</li>
</ol>
</li>
</ul>
<blockquote>
This change will be specific to your user account, and will
take effect globally, which may or may not be a good thing.</blockquote>
<ul class="simple">
<li>The Clean command currently does not remove everything, if you
want to ensure that the project has actually been completely
cleaned, then you should remove the <tt class="docutils literal"><span class="pre">build</span></tt> folder yourself.</li>
<li>Like Xcode, the built product and temporary files will both end
up in the <tt class="docutils literal"><span class="pre">build</span></tt> folder unless explicitly specified that they
should go elsewhere.  When not using these templates, py2app
would normally put the result in a <tt class="docutils literal"><span class="pre">dist</span></tt> folder.</li>
<li>If you need to include non-system frameworks or dylibs that are not otherwise
referenced by a Python extension, then link to them from an Objective-C
plug-in.  py2app will find them and put them into your application!
See PyObjC Mixed Application below for more information about using
plug-ins to integrate non-Python code into your application.</li>
</ul>
</div>
<div class="section" id="groups">
<h3><a class="toc-backref" href="#id5" name="groups">Groups</a></h3>
<p>The PyObjC Xcode templates use py2app to build applications,
but they parse the <tt class="docutils literal"><span class="pre">.xcode</span></tt> project file to determine
how they should be built, rather than directly in the
<tt class="docutils literal"><span class="pre">setup.py</span></tt>.  The parser, in <tt class="docutils literal"><span class="pre">PyObjCTools.XcodeSupport</span></tt>,
gives special meaning to several groups.  If these groups
are renamed or removed, your project may not build correctly!</p>
<dl class="docutils">
<dt>Main Script:</dt>
<dd><p class="first">This group should contain exactly one file, the main script
of your application.  The default main script in the template
generally does not need to be changed.</p>
<p>If you need to ensure that additional code is imported, simply
place it in the Classes group.  You shouldn't need to modify
your main script.</p>
<p class="last">ONLY the main script should be in this group.</p>
</dd>
<dt>Resources:</dt>
<dd><p class="first">Every file in this group goes into the <tt class="docutils literal"><span class="pre">Resources</span></tt> folder
inside of your application bundle.</p>
<p>Any <tt class="docutils literal"><span class="pre">.nib</span></tt> files that are in this folder will
be parsed with <tt class="docutils literal"><span class="pre">PyObjCTools.NibClassBuilder.extractClasses</span></tt>
by  the main script before any modules in the Classes group
are imported, and before the run loop is started.  You should
not need to call <tt class="docutils literal"><span class="pre">extractClasses</span></tt> manually in your code.</p>
<p class="last">Source code should not go in here.</p>
</dd>
<dt>Classes:</dt>
<dd><p class="first">Modules in the classes group will be imported by the main
script in the order that they appear in the Xcode project,
after all classes are extracted from the nibs.</p>
<p class="last">Every Python module in this group is guaranteed to be scanned
by py2app for dependencies.</p>
</dd>
<dt>Other Sources:</dt>
<dd><p class="first">This group is not actually special.  You may put anything you
want in this group.  It is used by the templates to store
files and source code that do not fit into any of the above
categories, such as the <tt class="docutils literal"><span class="pre">Info.plist</span></tt> and the <tt class="docutils literal"><span class="pre">setup.py</span></tt>.</p>
<dl class="last docutils">
<dt>setup.py:</dt>
<dd><p class="first">This is the script that is actually used to build your
project.  It may also be used from the command line
either directly or via <tt class="docutils literal"><span class="pre">xcodebuild</span></tt>.  Read the file
for more instructions.  This script must not be renamed
or removed.</p>
<p class="last">If you need to customize the py2app or distutils
build process, you should modify the <tt class="docutils literal"><span class="pre">setup_options</span></tt>
dict before the <tt class="docutils literal"><span class="pre">setup(...)</span></tt> function is called.</p>
</dd>
<dt>Info.plist:</dt>
<dd>When present, this file is used as a template for your
application's <tt class="docutils literal"><span class="pre">Info.plist</span></tt>.  If you rename or delete
it, then it will not be used and plist will be
generated by py2app.  For information about what
can go in this plist, see
<a class="reference" href="http://developer.apple.com/documentation/MacOSX/Conceptual/BPRuntimeConfig/Concepts/PListKeys.html">Runtime Configuration: Property List Key Reference</a>.</dd>
</dl>
</dd>
</dl>
</div>
<div class="section" id="targets">
<h3><a class="toc-backref" href="#id6" name="targets">Targets</a></h3>
<dl class="docutils">
<dt>Development:</dt>
<dd>This target will use py2app <tt class="docutils literal"><span class="pre">--alias</span></tt> build mode.  Executables
built with this mechanism are produced very quickly, and use the
sources in-place via symlinks and <tt class="docutils literal"><span class="pre">sys.path</span></tt> manipulations.
These executables are not redistributable, much like development
executables produced by Xcode when using Zero-Link.</dd>
<dt>Deployment:</dt>
<dd><p class="first">This target will use py2app's default build mode, <tt class="docutils literal"><span class="pre">--standalone</span></tt>.
This will create a standalone bundle out of your application that is
redistributable.  Everything that py2app determines to be
needed by your application will be included in the executable,
including Python itself, extensions you use, and dynamic
libraries or frameworks that are linked to by these extensions.</p>
<p>If you are using a Python distributed by
Apple, then it will be built in <tt class="docutils literal"><span class="pre">--semi-standalone</span></tt> mode.
This means that Python and its standard library <em>will not</em>
be included in the application.</p>
<p class="last">Using the Deployment <em>target</em> does not automatically
imply that you are using the Deployment <em>build style</em>.  This is
only relevant when using the PyObjC Mixed Application template,
or are otherwise using the same project to compile non-Python
source code.  To change the current build style, Get Info on the
project.  The build style has no effect on Python code.</p>
</dd>
</dl>
</div>
<div class="section" id="custom-executable">
<h3><a class="toc-backref" href="#id7" name="custom-executable">Custom Executable</a></h3>
<p>The custom executable enables for your built application to be run from Xcode.</p>
<p>If you rename your main script or fiddle around with your <tt class="docutils literal"><span class="pre">Info.plist</span></tt>,
the path to your application may change and this will no longer work.
If that is the case, use Get Info on the custom executable and change
the Arguments to point to the correct path.</p>
<p>By default, executables are launched with the <tt class="docutils literal"><span class="pre">USE_PDB</span></tt> environment variable
set for both Development and Deployment targets.  This turns on verbose stack
traces whenever an exception crosses the PyObjC bridge, and will drop you at
a pdb prompt in the console when an uncaught exception occurs.</p>
<p>Other useful environment variables that you can set, such as <tt class="docutils literal"><span class="pre">NSZombieEnabled</span></tt>,
as well as all kinds of other debugging tricks you should know are covered
in <a class="reference" href="http://developer.apple.com/technotes/tn2004/tn2124.html">TN2124: Mac OS X Debugging Magic</a>.</p>
<p>If Xcode screwed up and didn't create a Custom Executable, which is not
beyond the realm of possibility, then you can create one as follows:</p>
<ol class="arabic simple">
<li>Create a Custom Executable for <tt class="docutils literal"><span class="pre">/usr/bin/env</span></tt> (yes, Xcode is dumb)</li>
<li>Set that it runs from the Built Product directory</li>
<li>Use <tt class="docutils literal"><span class="pre">YourProject.app/Contents/MacOS/YourProject</span></tt> as the first (and only) argument</li>
<li>Optionally set the <tt class="docutils literal"><span class="pre">USE_PDB</span></tt> (or any other) environment variables</li>
</ol>
<p>Note that when debugging using gdb, you'll get a trap signal because
<tt class="docutils literal"><span class="pre">/usr/bin/env</span></tt> will be <tt class="docutils literal"><span class="pre">execve</span></tt>'ing your application.  Unfortunately,
there's nothing we can do from the template, because Xcode can only create
Custom Executables to absolute paths.  However, you can probably modify
yours such that it points directly to your built application after it
has been built once.</p>
<p>Custom executables are specific to a particular user in Xcode, so anything
you do to this part of the template won't be seen by anyone else unless
they happen to have the same short user name as you.</p>
</div>
<div class="section" id="pyobjc-application">
<h3><a class="toc-backref" href="#id8" name="pyobjc-application">PyObjC Application</a></h3>
<p>This is a simple template that has a window and an application delegate.</p>
</div>
<div class="section" id="pyobjc-document-based-application">
<h3><a class="toc-backref" href="#id9" name="pyobjc-document-based-application">PyObjC Document Based Application</a></h3>
<p>This is template demonstrates a Document-based application written in Python.
It is a simple text editor (like the TinyTinyEdit example).</p>
</div>
<div class="section" id="pyobjc-mixed-application">
<h3><a class="toc-backref" href="#id10" name="pyobjc-mixed-application">PyObjC Mixed Application</a></h3>
<p>This template contains both Objective-C and Python code.  The Objective-C code
is built as a &quot;ProjectNamePlugIn.bundle&quot; plug-in in a separate target.  The plug-in
is placed in the <tt class="docutils literal"><span class="pre">Resources</span></tt> directory of your application.  A wrapper script
in the Classes group, &quot;ProjectNamePlugIn.py&quot; can be imported from Python and will
contain all of the Objective-C classes referenced in the plug-in (even if there
is more than just the example <tt class="docutils literal"><span class="pre">ProjectNamePlugIn</span></tt> class).</p>
<p>The example class implements a simple method, <tt class="docutils literal"><span class="pre">-(BOOL)plugInLoaded</span></tt> which will
always return <tt class="docutils literal"><span class="pre">YES</span></tt>.  The Python application delegate creates an instances of
this class, and will beep when the application has finished launching if the
plug-in loaded correctly.  If it didn't load correctly, you would get an exception,
but that shouldn't happen :)</p>
<p>Note that this template doesn't have any special machinery behind it.  If you find
that you later need to add Objective-C code to a project that you started with
one of the other templates, you can do the following:</p>
<ol class="arabic simple">
<li>Create a new Objective-C loadable bundle target</li>
<li>Make the Development and Deployment targets depend on this target</li>
<li>Drag the product loadable bundle into the Resources group</li>
<li>Create a wrapper module, that uses <tt class="docutils literal"><span class="pre">objc.loadBundle(...)</span></tt> in the
Classes group (see the example in the template).</li>
</ol>
<p>Note that switching between Development and Deployment targets does
not imply that you are switching to the build style of the same name.
See the Targets section for more information.</p>
</div>
</div>
<?
    include "footer.inc";
?>