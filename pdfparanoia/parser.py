# -*- coding: utf-8 -*-
"""
pdfparanoia.parser
~~~~~~~~~~~~~~~

Deals with the existential nature of parsing pdfs.

"""

from io import BytesIO
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

def parse_pdf(handler):
    """
    Parses a PDF via pdfminer.
    """
    # reset to the beginning of the data
    handler.seek(0)

    parser = PDFParser(handler)
    doc = PDFDocument(parser)

    return doc

def parse_content(content):
    """
    Parses a PDF via pdfminer.
    """
    stream = BytesIO(content)
    parser = PDFParser(stream)
    doc = PDFDocument(parser)
    parser.set_document(doc)
    return doc
