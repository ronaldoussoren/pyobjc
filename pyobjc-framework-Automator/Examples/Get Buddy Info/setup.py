"""
Script for building the example.

Usage:
    python setup.py py2app

Then install the bundle in dist into ~/Library/Automator.
"""
from distutils.core import setup
import py2app

infoPlist = dict(
    AMAccepts=dict(
        Container='List',
        Optional=False,
        Types=['com.apple.addressbook.person-object'],
    ),
    AMApplication=[
        'Address Book',
        'iChat',
    ],
    AMCanShowWhenRun = True,
    AMCategory = 'iChat',
    AMDefaultParameters = dict(),
    AMDescription = dict(
        AMDAlert='iChat must be running for this action to work properly.',
        AMDNote='Information will not be returned for the current user.',
        AMDSummary='This action returns the Instant Message information of the people passed from the previous action.',
    ),
    AMIconName='iChat',
    AMKeywords=(
        'Instant',
        'Message',
        'IM',
    ),
    AMName='Get Buddy Info',
    AMProvides=dict(
        Container='List',
        Types=[
            'com.apple.cocoa.string'
        ],
    )
)

setup(
    name='Get Buddy Info',
    plugin=['GetBuddyInfo.py'],
    data_files=[],
    options=dict(py2app=dict(
        extension=".action",
        plist=infoPlist,
    )),
)
