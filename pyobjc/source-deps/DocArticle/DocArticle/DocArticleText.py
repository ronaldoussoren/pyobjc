# Author: Bill Bumgarner
# Contact: bbum@codefab.com
# Copyright: 2002 - Bill Bumgarner - All Rights Reserved
# License: The MIT License -- see LICENSE.txt

"""
Defines various chunks o' static text that are spewed into Articles.

A sort of half-baked library of templates.  Currently extremely limited in scope.
"""

__docformat__ = 'reStructuredText'

contentStart = """<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
"""

headerStart = """<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
"""

titleStart = """<title>
"""
titleEnd = """</title>
"""

headerEnd = """</head>
"""

bodyStart = """<body>
"""
bodyEnd = """</body>
"""

contentEnd = """</html>
"""
