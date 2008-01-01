import os
import sys

from macosx_version import sw_vers, Version

VERSION = sw_vers()

CUSTOM_SCHEMES = dict(
#    xcode=dict(
#        description=u'(Optional) Xcode File and Project templates for PyObjC',
#        prefix='/Library/Application Support/Apple/Developer Tools',
#        source='Xcode',
#    ),
    docs=dict(
        description=u'(Optional) PyObjC Documentation',
        prefix='/Developer/Python/PyObjC/Documentation',
        source='Doc',
    ),
    examples=dict(
        description=u'(Optional) PyObjC Example Code',
        prefix='/Developer/Python/PyObjC/Examples',
        source='Examples',
    ),
)

options = dict(bdist_mpkg=dict(
    scheme_command=dict(doc='build_html'),
    custom_schemes=CUSTOM_SCHEMES,
    readme='Installer Package/%s/Resources/ReadMe.txt' % (
            '.'.join(map(str, VERSION.version[:2])),
    ),
))

#if VERSION < Version('10.3'):
#    del options['bdist_mpkg']['custom_schemes']['xcode']
if not os.path.exists(options['bdist_mpkg']['readme']):
    del options['bdist_mpkg']['readme']
