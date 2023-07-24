#!/bin/env python
# Copyright ReportLab Europe Ltd. 2000-2008
# see license.txt for license details
import os
from reportlab import pdfgen

__doc__ = 'Test all demos'
__version__ = ''' $Id: testdemos.py 3269 2008-09-03 17:22:41Z rgbecker $ '''
_globals = globals().copy()

for p in ('pythonpoint/pythonpoint.py', 'stdfonts/stdfonts.py', 'odyssey/odyssey.py',
          'gadflypaper/gfe.py'):
    fn = os.path.normcase(os.path.normpath(os.path.join(
        os.path.dirname(pdfgen.__file__), '..', 'demos', p)))
    os.chdir(os.path.dirname(fn))
    with open(fn, 'r') as f:
        os.exec(f, _globals.copy())
    # execfile(fn, _globals.copy())  (no execfile in Python 3)
