<?
$title = "Documentation";
$cvs_author = '$Author: ronaldoussoren $';
$cvs_date = '$Date: 2004/05/30 18:56:39 $';

include "header.inc";
?>

<h1>Downloads</h1>

<h2>Stable release</h2>

<ul>
<li><a href="http://prdownloads.sourceforge.net/pyobjc/pyobjc-1.1-macosx10.2.dmg?download">PyObjC 1.1 installer package for Apple's Python (MacOS X 10.2)</a>
<li><a href="http://prdownloads.sourceforge.net/pyobjc/pyobjc-1.1-macosx10.3.dmg?download">PyObjC 1.1 installer package for Apple's Python (MacOS X 10.3)</a>
<li><a href="http://prdownloads.sourceforge.net/pyobjc/pyobjc-1.1.tar.gz?download">PyObjC 1.1 source release (a compressed tar archive)</a>
</ul>

<p>Users of MacPython can use the PyObjC PackageManager database to install 
   PyObjC: select ``File/open URL...`` in Package Manager and select one
   of the two URL below:
   <UL>
   <LI>MacOS X 10.2:"<CODE>http://pyobjc.sf.net/packman/pyobjc-stable-macosx10.2.plist</CODE>" 
   <LI>MacOS X 10.3:"<CODE>http://pyobjc.sf.net/packman/pyobjc-stable-macosx10.3.plist</CODE>" 
   </UL>
<p><b>NOTE:</b> upgrading earlier versions of PyObjC using the binary package
doesn't seem to work correctly. Please use the source installer when you
upgrade an earlier version of PyObjC.

<p>Older releases are available in the <a href="http://sourceforge.net/project/showfiles.php?group_id=14534">Files section of our SourceForge project</a>.

<p>If you want to install PyObjC from CVS you'll have to download the latest 
archive with libFFI <a href="http://prdownloads.sourceforge.net/pyobjc/libffi-src-20030921.tar.gz?download">here</a>. This is not an official libffi release, it contains a (small) number of changes to make it work correctly with PyObjC.

<h2>Unstable release</h2>

<p>There are no unstable releases at the moment.

<p>The <a href="http://subversion.tigris.org/">subversion</a> repository 
   can be accessed at <a href="http://svn.red-bean.com/pyobjc">http://svn.red-bean.com/pyobjc</a>.
<p>Many thanks to the folks at <a href="http://www.red-bean.com">red-bean.com</a> for allowing us to use their server.

<h2>Misc. other downloads</h2>

<p>
These downloads are not really related to PyObjC, but are available from
this location until they find another home.

<ul>
<li><a href="readline-0.0.0.tar.gz">Readline support for Apple python</a>
<li><a href="pyssl-0.0.0.tar.gz">SSL support for Apple python</a>
<li><a href="dump-methods.py">dump-methods: Script to dump XML-RPC interfaces</a>
</ul>

<?
include "footer.inc";
?>
