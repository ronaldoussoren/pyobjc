<?
$title = "Documentation";
$cvs_author = '$Author: ronaldoussoren $';
$cvs_date = '$Date: 2003/02/12 20:42:59 $';

include "header.inc";
?>


<h1>PyObjC Documentation</h1>

<p>
Some usefull documentation would be nice. The documents in this section are
work in progress and based on the CVS version of PyObjC. There are some 
differences in the semantics and interface w.r.t. PyObjC 0.8.
</p>

<h2>User Documentation</h2>

<p>
This documentation should focus on the user.  Of course, the user is really a developer, typically, that is interested in using PyObjC to develop applications without being terribly interested in the innards of the PyObjC module.
</p>

<ul>
<!-- USERDOC -->
<LI><A HREF="install.php">Installation Instructions</A>
<LI><A HREF="users.php">Userguide for PyObjC</A>
<LI><A HREF="warts.php">Odd features</A>
<LI><A HREF="wrapping.php">How to wrap an Objective-C class library</A>
<!-- /USERDOC -->
</ul>

<h2>Developer Documentation</h2>

<p>
There is actually a good chunk of developer documentation in the source tree (thanks to Ronald!).  It needs to be refactored into this content tree along with </p>

<ul>
<!-- DEVDOC -->
<LI><A HREF="coding-style.php">Coding style for PyObjC</A>
<LI><A HREF="structure.php">Structure of the PyObjC package</A>
<LI><A HREF="architecture.php">PyObjC Architecture</A>
<LI><A HREF="classes.php">Python classes and Objective-C code</A>
<LI><A HREF="libffi.php">Using LibFFI</A>
<!-- /DEVDOC -->
</ul>

<?
include "footer.inc";
?>
