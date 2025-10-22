"""
pdfparanoia - pdf watermark remover library for academic papers
~~~~~~~~~~~~~~~

pdfparanoia is a pdf watermark remover library for academic papers. Basic
usage:

    >>> import pdfparanoia
    >>> pdf = pdfparanoia.scrub(open("nmat.pdf", "rb"))
    >>> file_handler = open("output.pdf", "wb")
    >>> file_handler.write(pdf)
    >>> file_handler.close()
"""

from . import plugins
from .core import scrub
