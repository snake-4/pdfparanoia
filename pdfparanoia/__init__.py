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

import plugins
from .core import scrub
