<?
$title = "Home";
$cvs_author = '$Author: ronaldoussoren $';
$cvs_date = '$Date: 2003/10/09 05:51:09 $';
$is_home = 1;

$metatags = '<meta name="description" content="PyObjC, a universal bridge between the Objective-C and Python languages.">
<meta name="keywords" content="Mac OS X, Darwin, GNUStep, Unix, software, distribution, Python, Objective-C, ObjC, PyObjC">
';

include "header.inc";
?>

<p>
The PyObjC project aims to provide a bridge between the Python and Objective-C programming languages.  The bridge is intended to be fully bidirectional, allowing the Python programmer to take full advantage of the power provided by various Objective-C based toolkits and the Objective-C programmer transparent access to Python based functionality.</p>
<p>
The most important usage of this is writing Cocoa GUI applications on 
<a href="http://www.apple.com/macosx/">Mac OS X</a> in pure Python. See 
<a href="<? print $root; ?>doc/tutorial.php">our tutorial</a> for an example
of this.
<p>


<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr valign="top"><td width="50%">

<h1>News</h1>

<?
// Include news items
include $fsroot."news/news.inc";
?>
<div align="right"><a href="<? print $root; ?>news/index.php">All News...</a></div>


</td><td>&nbsp;&nbsp;&nbsp;</td><td width="50%">

<h1>Status</h1>

<p>
<a href="software/index.php">PyObjC 1.0</a> was released on 8 October 2003.  See the <a href="NEWS-1.0.txt">NEWS</a> for details.
</p>

<h1>Platform support</h1>

The development of the bridge is currently focused on 
<a href="http://www.apple.com/macosx/">Mac OS X</a> 10.2 and later. The 
current version has minimal support for MacOS X 10.1, earlier versions are not 
(and will never be) supported.
<p>
We want to offer the same level support for 
<a href="http://www.gnustep.org/">GNUstep</a>, but need volunteers with GnuStep
experience to make that happen. Contact <a href="mailto:pyobjc-dev@lists.sourceforge.net">the mailinglist</a> if you want to help out.

<h1>Resources</h1>

<p>
Support is currently limited to <a href="http://lists.sourceforge.net/mailman/listinfo/pyobjc-dev">the developer's mailing list</a>.
</p>

<p>
The PyObjC project is hosted by
<a href="http://sourceforge.net/">SourceForge</a>.
In addition to hosting this site and the downloads, SourceForge
provides the following resources for the project:
</p>
<ul>
<li><a href="http://sourceforge.net/projects/pyobjc/">Project page</a></li>
<li><a
href="http://sourceforge.net/tracker/?group_id=14534&atid=114534">Bug tracker</a></li>
<li><a href="http://sourceforge.net/project/showfiles.php?group_id=14534">Files</a></li>
<li>CVS (<a href="http://cvs.sourceforge.net/cgi-bin/viewcvs.cgi/pyobjc">browse online</a>, <a href="http://sourceforge.net/cvs/?group_id=14534">access instructions</a>)</li>

</ul>
<p>We have daily <a href="/cvs-snapshots">CVS snapshots</a>. The contents are a work in progress and may be instable, or not even compile.

</td></tr></table>


<?
include "footer.inc";
?>
