"""
Helper module that makes it easier to import all of Quartz
"""

try:
    from Quartz.CoreGraphics import *
except ImportError:
    pass

try:
    from Quartz.ImageIO import *
except ImportError:
    pass

try:
    from Quartz.CoreVideo import *
except ImportError:
    pass

try:
    from Quartz.QuartzCore import *
except ImportError:
    pass

try:
    from Quartz.ImageKit import *
except ImportError:
    pass

try:
    from Quartz.PDFKit import *
except ImportError:
    pass

try:
    from Quartz.QuartzFilters import *
except ImportError:
    pass

try:
    from Quartz.QuickLookUI import *
except ImportError, msg:
    pass
