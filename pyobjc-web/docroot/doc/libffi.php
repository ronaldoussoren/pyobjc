<?
    $title = "Using LibFFI with PyObjC";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/05/04 12:56:38 $';

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
<p>PyObjC uses libffi to dynamicly call into Objective-C. We use libffi instead of
NSInvocation because the former makes it possible to call superclass methods,
and to generate stubs for use in Objective-C method tables on the fly.</p>
<p>It is currently possible to build a non-ffi build of PyObjC, but that is not
supported and will be removed as we use features from libffi to further 
improve the brigde.</p>
</div>
<?
    include "footer.inc";
?>