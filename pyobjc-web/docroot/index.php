<?
$title = "Home";
$cvs_author = '$Author: ronaldoussoren $';
$cvs_date = '$Date: 2004/05/30 19:02:54 $';
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
<a href="software/index.php">PyObjC 1.3.7</a> was released on 6 July 2005.  See the <a href="doc/news.php">NEWS</a> for details.
</p>

<h1>Platform support</h1>

The development of the bridge is currently focused on 
<a href="http://www.apple.com/macosx/">Mac OS X</a> 10.2 and later. Earlier versions are not 
(and will never be) supported.
<p>
There is limited support for <a href="http://www.gnustep.org/">GNUstep</a>, 
most of the unittests pass on GNUstep on Linux/ix86. However, we do still have
some serious problems with real scripts.
<P>
Contact <a href="mailto:pyobjc-dev@lists.sourceforge.net">the mailinglist</a> if you want to help out with GNUstep support.

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
</ul>

<p>Our repository is hosted by <a href="http://www.red-bean.com/">red-bean.com</a>. The subversion repository can be accessed <a href="http://svn.red-bean.com/pyobjc/">here</a>.

</td></tr></table>


<?
include "footer.inc";
?>
