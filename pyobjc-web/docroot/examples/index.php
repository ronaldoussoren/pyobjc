<?
$title = "Examples";
$cvs_author = '$Author: ronaldoussoren $';
$cvs_date = '$Date: 2004/02/21 19:47:55 $';

include "header.inc";
?>

<h1>Examples</h1>

<p>
Collected examples for the PyObjC module.  Includes command line tools, examples using Project Builder, and various examples of using the numerous APIs provided by Apple (and, eventually, GnuStep).
<p>
The examples are included in the source tarball and on the disk image containing the binary installer. You can drag the documentation and examples to you disk to install them.
<p>
The examples will be added to this website in the future. The following is 
a short snippet of PyObjC code that defines a new class. This class can
be used and instantiated both in Python and in Objective-C:
<PRE>

    class Demo (NSEnumerator):
      __slots__ = ('cnt',)

      def init(self):
        self.cnt = 10
        return self

      def nextObject(self):
        print "nextObject" ,  self.retainCount()
        if self.cnt == 0:
          return None
        self.cnt -= 1
        return self.cnt

      def __del__(self):
        print "Bye from Demo instance"

</PRE>

<?
include "footer.inc";
?>
