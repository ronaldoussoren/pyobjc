<?
$title = "Documentation";
$cvs_author = '$Author: ronaldoussoren $';
$cvs_date = '$Date: 2003/10/08 17:30:40 $';

include "header.inc";
?>


<h1>PyObjC Documentation</h1>

<h2>User Documentation</h2>

<p>
This documentation should focus on the user.  Of course, the user is really a developer, typically, that is interested in using PyObjC to develop applications without being terribly interested in the innards of the PyObjC module.
</p>

<ul>
<!-- USERDOC -->
<LI><A HREF="install.php">Installation Instructions</A>
<LI><A HREF="intro.php">An introduction to PyObjC</A>
<LI><A HREF="tutorial.php">Creating your first PyObjC application.</A>
<LI><A HREF="extending_objc_with_python.php">Tutorial - Adding Python code to an existing ObjC application</A>
<LI><A HREF="tutorial_reading.php">Understanding existing PyObjC examples</A>
<LI><A HREF="projectbuilder-syntaxhighlighting.php">Project Builder Python Support</A>
<LI><A HREF="pyobjctools.php">PyObjCTools: The PyObjC Toolbox</A>
<LI><A HREF="api-notes-macosx.php">Notes on supported APIs and classes on MacOS X</A>
<LI><A HREF="wrapping.php">How to wrap an Objective-C class library</A>
<!-- /USERDOC -->
</ul>

<h2>Developer Documentation</h2>

<p>
There is actually a good chunk of developer documentation in the source tree (thanks to Ronald!).  It needs to be refactored into this content tree along with </p>

<ul>
<!-- DEVDOC -->
<LI><A HREF="coding-style.php">Coding style for PyObjC</A>
<LI><A HREF="c-api.php">Documentation for the PyObjC C-API (Preliminary)</A>
<LI><A HREF="structure.php">Structure of the PyObjC package</A>
<LI><A HREF="architecture.php">PyObjC Architecture</A>
<LI><A HREF="classes.php">Python classes and Objective-C code</A>
<!-- /DEVDOC -->
</ul>

<?
include "footer.inc";
?>
