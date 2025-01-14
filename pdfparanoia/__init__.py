# -*- coding: utf-8 -*-
"""
pdfparanoia - pdf watermark remover library for academic papers
~~~~~~~~~~~~~~~

pdfparanoia is a pdf watermark remover library for academic papers. Basic
usage:

    >>> import pdfparanoia
    >>> pdf = pdfparanoia.scrub(open("nmat.pdf", "r"))
    >>> file_handler = open("output.pdf", "w")
    >>> file_handler.write(pdf)
    >>> file_handler.close()

:copyright: (c) 2013 by Bryan Bishop.
:license: BSD.
"""

__title__ = "pdfparanoia"
__version__ = "0.0.17"
__build__ = 0x000017
__author__ = "Bryan Bishop <kanzure@gmail.com>"
__license__ = "BSD"
__copyright__ = "Copyright 2013 Bryan Bishop"

from .core import scrub
