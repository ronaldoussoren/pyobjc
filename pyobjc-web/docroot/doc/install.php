<?
    $title = "Installation Instructions";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2004/04/12 09:22:46 $';

    include "header.inc";
?>
<div class="document" id="installation-instructions">
<h1 class="title">Installation Instructions</h1>
<!-- :authors: Bill Bumgarner, Ronald Oussoren -->
<div class="section" id="building-the-package">
<h1><a name="building-the-package">Building the package</a></h1>
<p>If you're using the sources from CVS you should first download a copy of 
libffi from <a class="reference" href="http://sourceforge.net/project/showfiles.php?group_id=14534">the PyObjC download site</a>.  Extract this in a convenient location
and update the variable <tt class="literal"><span class="pre">LIBFF_SOURCES</span></tt> at the top of setup.py.  The released
version of PyObjC includes a compatible version of libffi.</p>
<p>PyObjC is build and installed using the distutils package included with Python
2.0 and beyond.  This package provides a single interface for building and
packaging the module.   To see usage documentation for the module,
issue the <tt class="literal"><span class="pre">--help</span></tt> command:</p>
<pre class="literal-block">
% python setup.py --help
</pre>
<p>To see an inventory of building and packaging commands, issue the
command:</p>
<pre class="literal-block">
% python setup.py --help-commands
</pre>
<p>The following command will build and install the pyobjc module:</p>
<pre class="literal-block">
% python setup.py install
</pre>
<p>The setup.py system can also be used to create source and binary
distribution archives automatically.</p>
<p>Use <tt class="literal"><span class="pre">sudo</span></tt> to install the pyobjc module into a the Apple supplied
python's site-packages directory on OS X 10.2 and greater:</p>
<p>% sudo python setup.py install</p>
<p>If you have multiple versions of python installed on your system, the
above will only install pyobjc for whatever version of python is the
default on the command line.   Make sure you are installing python
against the correct version of python.</p>
<p>To be able to build the wrappers for the WebKit framework (included with
Safari 1.0), you'll have to install the WebKit SDK. You can download 
this from the <a class="reference" href="http://connect.apple.com">ADC website</a>.</p>
</div>
<div class="section" id="examples">
<h1><a name="examples">Examples</a></h1>
<p>The <a class="reference" href="Examples/00ReadMe.html">examples directory</a> contains a number of projects that demonstrate
various features of the PyObjC bridge. The scripts at the top level of
the <a class="reference" href="Examples/00ReadMe.html">examples directory</a> were mostly written to test a particular
feature of the bridge (or document a bug until a fix could be found).</p>
<p>CurrencyConverter and TableModel are both examples of standalone
Cocoa-Python applications.  To build and execute:</p>
<pre class="literal-block">
% cd TableModel
% python buildapp.py build
</pre>
<p>The WebServicesTool is an example of Cocoa-Python applications created via 
the Cocoa-Python project template found in the 
<tt class="literal"><span class="pre">ProjectBuilder</span> <span class="pre">Extras/Project</span> <span class="pre">Templates</span></tt> directory.  Use Project Builder 
to build the applications.</p>
</div>
<div class="section" id="project-templates">
<h1><a name="project-templates">Project Templates</a></h1>
<p>The <tt class="literal"><span class="pre">ProjectBuilder</span> <span class="pre">Extras</span></tt> directory contains additional files that can
be used with Project Builder. The directory <tt class="literal"><span class="pre">Specifications</span></tt> contains files
that enable syntax coloring for Python files in Project Builder.</p>
<p>The <tt class="literal"><span class="pre">Project</span> <span class="pre">Templates</span></tt> directory contains project templates for
Project Builder.  These have to be copied to
<tt class="literal"><span class="pre">/Developer/ProjectBuilder</span> <span class="pre">Extras/Project</span> <span class="pre">Templates/Application</span></tt> before
they are useable from Project Builder.</p>
<p>There are three templates available:</p>
<ul>
<li><p class="first">Cocoa-Python Application</p>
<p>A project created from this template is designed to implement standalone,
pure-Python, applications that are compatible with Apple's build of Python as
well as all other builds of python that support PyObjC.</p>
<p>When building the 'install' target, the resulting application wrapper will
included the PyObjC module and can be launched on any stock OS X 10.2 system
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
<?
    include "footer.inc";
?>