<?
    $title = "Installation Instructions";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<h1 class="title">Installation Instructions</h1>
<!-- :authors: Bill Bumgarner, Ronald Oussoren, Bob Ippolito -->
<div class="section" id="building-the-package">
<h3><a name="building-the-package">Building the package</a></h3>
<p>PyObjC is built and installed using the distutils package included with Python
2.0 and beyond.  distutils provides a single interface for building and
packaging the PyObjC via a <tt class="docutils literal"><span class="pre">setup.py</span></tt> script. To see usage documentation
for <tt class="docutils literal"><span class="pre">setup.py</span></tt>, issue the <tt class="docutils literal"><span class="pre">--help</span></tt> command:</p>
<pre class="literal-block">
% python setup.py --help
</pre>
<p>To see an inventory of building and packaging commands, issue the
command:</p>
<pre class="literal-block">
% python setup.py --help-commands
</pre>
<p>The following command will build and install the PyObjC package:</p>
<pre class="literal-block">
% python setup.py install
</pre>
<p>The setup.py system can also be used to create source and binary
distribution archives automatically.</p>
<p>The following command will build and open a binary installer for PyObjC,
py2app, tools, examples, and documentation:</p>
<pre class="literal-block">
% python setup.py bdist_mpkg --open
</pre>
<p>If you want to install the PyObjC package without examples, documentation,
or py2app, you can use the standard distutils install command:</p>
<pre class="literal-block">
% sudo python setup.py install
</pre>
<p>If you have multiple versions of Python installed on your system, the
above will only install PyObjC for whatever version of Python is the
default on the command line.   Make sure you are installing PyObjC
against the correct version of Python.</p>
<p>Note that there is a known bug in Python 2.3.0 
(as shipped with Mac OS X 10.3.x), such that when another framework Python is 
installed it will not link extensions (such as PyObjC) properly, rendering them
unusable.  If you intend to build PyObjC for Python 2.3.0, ensure that no other
framework Python is installed, such as a previous installation for Mac OS X
10.2.  For more information on this and other Python issues on Mac OS X,
please refer to the <a class="reference" href="http://pythonmac.org/wiki/FAQ">pythonmac.org FAQ</a>.</p>
<p>If you have a previous version of PyObjC installed, you may see an exception
such as <tt class="docutils literal"><span class="pre">Wrong</span> <span class="pre">version</span> <span class="pre">of</span> <span class="pre">PyObjC</span> <span class="pre">C</span> <span class="pre">API</span></tt>.  If this happens, you should
delete any previous installation of PyObjC and the build folder in your
new sources and try again.  PyObjC will typically be installed to a folder
of the same name in /Library/Python/2.3 or /Library/Python/2.3/site-packages.</p>
<p>To be able to build the wrappers for the WebKit framework (included with
Safari 1.0) on Mac OS X 10.2, you'll have to install the WebKit SDK. You can
download this from the <a class="reference" href="http://connect.apple.com">ADC website</a>.</p>
<p>PyObjC has limited support for <a class="reference" href="http://www.gnustep.org/">GNUstep</a>. See <a class="reference" href="Doc/gnustep.html">Doc/gnustep.txt</a> for 
more information.</p>
</div>
<div class="section" id="examples">
<h3><a name="examples">Examples</a></h3>
<p>The <a class="reference" href="Examples/00ReadMe.html">examples directory</a> contains a number of projects that demonstrate
various features of the PyObjC bridge. The scripts at the top level of
the <a class="reference" href="Examples/00ReadMe.html">examples directory</a> were mostly written to test a particular
feature of the bridge (or document a bug until a fix could be found).</p>
<p>CurrencyConverter and TableModel are both examples of standalone
Cocoa-Python applications.  To build and execute:</p>
<pre class="literal-block">
% cd TableModel
% python setup.py py2app
% open dist/TableModel.app
</pre>
<p>For projects that contain a Project Builder (.pbproj), you can build them
with Project Builder or Xcode.  Xcode (.xcode) projects can be built only
with Xcode.  However, all examples ship with a py2app-based setup.py, and
this is the preferred build method.</p>
</div>
<div class="section" id="project-templates">
<h3><a name="project-templates">Project Templates</a></h3>
<div class="section" id="xcode-on-mac-os-x-10-3">
<h4><a name="xcode-on-mac-os-x-10-3">Xcode on Mac OS X 10.3</a></h4>
<p>The <tt class="docutils literal"><span class="pre">Xcode</span></tt> directory contains some file and project that make it easier to
work with Python and PyObjC when using <a class="reference" href="http://www.apple.com/xcode">Xcode</a>.</p>
<p>Copy the templates in <tt class="docutils literal"><span class="pre">Xcode/File</span> <span class="pre">templates</span></tt> to <tt class="docutils literal"><span class="pre">/Library/Application</span> <span class="pre">Support/Apple/Developer</span> <span class="pre">Tools/File</span> <span class="pre">Templates</span></tt>. Copy the templates in <tt class="docutils literal"><span class="pre">Xcode/Project</span> <span class="pre">Templates</span></tt> to <tt class="docutils literal"><span class="pre">/Library/Application</span> <span class="pre">Support/Apple/Developer</span> <span class="pre">Tools/Project</span> <span class="pre">Templates</span></tt>.</p>
<p>There are two project templates:</p>
<ul>
<li><p class="first">Cocoa-Python Application</p>
<p>A project created from this template is designed to implement standalone,
pure-Python, applications that are compatible with Apple's build of Python as
well as all other builds of python that support PyObjC.</p>
<p>When building the 'install' target, the resulting application wrapper will
include the PyObjC package and can be launched on any stock OS X 10.3 system
without requiring PyObjC to be preinstalled.</p>
<p>Note that the optional 'BSD Subsystem' component of Mac OS X is required,
however it is installed by default and should be present on most systems.</p>
</li>
<li><p class="first">Cocoa-Python Document-based Application</p>
<p>This template works like the Cocoa-Python Application template in that it
is compatible with the Apple build of Python.   It creates an application 
that uses Cocoa's Multiple Document Architecture in the same fashion as the
default Cocoa Document-based Application supplied with Project Builder.</p>
</li>
</ul>
<p>Note that Python applications built on Mac OS X 10.3 are not compatible with
Mac OS X 10.2.  At this time, a Mac OS X 10.2 system must be used to build
Mac OS X 10.2 compatible applications.</p>
</div>
<div class="section" id="project-builder-on-mac-os-x-10-2">
<h4><a name="project-builder-on-mac-os-x-10-2">Project Builder on Mac OS X 10.2</a></h4>
<p>The <tt class="docutils literal"><span class="pre">ProjectBuilder</span> <span class="pre">Extras</span></tt> directory contains additional files that can
be used with Project Builder. The directory <tt class="docutils literal"><span class="pre">Specifications</span></tt> contains files
that enable syntax coloring for Python files in Project Builder.</p>
<p>The <tt class="docutils literal"><span class="pre">Project</span> <span class="pre">Templates</span></tt> directory contains project templates for
Project Builder.  These have to be copied to
<tt class="docutils literal"><span class="pre">/Developer/ProjectBuilder</span> <span class="pre">Extras/Project</span> <span class="pre">Templates/Application</span></tt> before
they are useable from Project Builder.</p>
<p>There are three templates available:</p>
<ul>
<li><p class="first">Cocoa-Python Application</p>
<p>A project created from this template is designed to implement standalone,
pure-Python, applications that are compatible with Apple's build of Python as
well as all other builds of python that support PyObjC.</p>
<p>When building the 'install' target, the resulting application wrapper will
include the PyObjC module and can be launched on any stock OS X 10.2 system
without requiring PyObjC to be preinstalled.</p>
</li>
<li><p class="first">Cocoa-Python-ObjC Application</p>
<p>A project created from this template includes an embedded framework project
into which all compiled (Objective-C) code can be placed.  Upon launch, 
the application automatically dynamically loads the embedded framework 
containing the compiled code.</p>
<p>Each Framework's Resources directory is automatically added to sys.path.</p>
</li>
<li><p class="first">Cocoa-Python Document-based Application</p>
<p>This template works like the Cocoa-Python Application template in that it
is compatible with the Apple build of Python.   It creates an application 
that uses Cocoa's Multiple Document Architecture in the same fashion as the
default Cocoa Document-based Application supplied with Project Builder.</p>
</li>
</ul>
<p>More information on project templates can be found in the Project
Builder documentation and/or release notes.</p>
</div>
</div>
</div>
<?
    include "footer.inc";
?>