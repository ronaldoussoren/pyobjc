<?
    $title = "Using LibFFI";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/02/12 20:43:02 $';

    include "header.inc";
?>
<table class="docinfo" frame="void" rules="none">
<col class="docinfo-name" />
<col class="docinfo-content" />
<tbody valign="top">
<tr><th class="docinfo-name">Author:</th>
<td>Ronald Oussoren</td></tr>
</tbody>
</table>
<p>PyObjC can optionally use libffi to dynamicly call into Objective-C. This is
an experimental extention.</p>
<p>LibFFI makes it unnecessary to build lists of method signatures that might be
used, and significantly reduces the size of the PyObjC extension. In the future
libFFI may also be used to replace existing method defitions on pure 
Objective-C classes and to add new methods to existing pure Objective-C classes.</p>
<p>To enable libFFI support:
- Build and install libffi 2.x, this is only available from a source
distribution of GCC.  Do NOT use the version from sources.redhat.com,
it doesn't support MacOS X at all.  The version I used (december 2002) 
doesn't allow you to build a shared library on MacOSX. This is not a 
problem, we don't want one anyway.
- Edit setup.py:
* Change the 'if 0:' before a definition of LIBFFI_CFLAGS to 'if 1:'.
* Change the definition of 'LIBFFI_BASE' to the proper value (probably /usr/local)
- Remove the directory 'build'
- Rebuild PyObjC.</p>
</div>
<?
    include "footer.inc";
?>