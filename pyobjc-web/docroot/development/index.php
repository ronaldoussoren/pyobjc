<?
$title = "Software";
$cvs_author = '$Author: ronaldoussoren $';
$cvs_date = '$Date: 2004/05/30 18:56:39 $';

include "header.inc";
?>

<h1>Development</h1>

<h2>Repository</h2>

<p>The PyObjC repository is a <a href="http://subversion.tigris.org">subversion</a> repository at <a href="http://svn.red-bean.com/pyobjc">http://svn.red-bean.com/pyobjc</a>.

<p>Martin Ott maintains a subversion package for Mac OS X. It can be downloaded from <a href="http://www.codingmonkeys.de/mbo/">his site</a>.

<p>You can fetch a snapshot of the current development tree using a WebDAV
   connection to <a href="http://svn.red-bean.com/pyobjc/trunk/">http://svn.red-bean.com/pyobjc/trunk/</a>, just copy the 'pyobjc' folder to a local disk.

<h2>Testing PyObjC</h2>

<p>PyObjC includes a large number of unittests. These can be started using
   the script <TT>Scripts/runPyObjCTests</TT>. 

<p>In the development version of PyObjC this script has been replaced by
   a <TT>test</TT> action in <TT>setup.py</TT>: <TT>python setup.py test</TT>.

<h2>Contributing to PyObjC</h2>

<p>The best way too contribute to PyObjC is by sending patches or (links to)
   examples to the list. Soon enough someone will get bored with applying
   your changes and you'll get access to the repository :-).

<?
include "footer.inc";
?>
