# -*- coding: utf-8 -*-
"""
pdfparanoia.parser
~~~~~~~~~~~~~~~

Deals with the existential nature of parsing pdfs.

"""

from io import BytesIO
from typing import Generator
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import PDFObjectNotFound


def _parse_content(content: bytes) -> PDFDocument:
    """
    Parses a PDF via pdfminer.
    """
    stream = BytesIO(content)
    parser = PDFParser(stream)
    doc = PDFDocument(parser)
    parser.set_document(doc)
    return doc


def iterate_objects(content: bytes) -> Generator[tuple[int, object]]:
    """
    Yields each object in a PDF via pdfminer.
    """
    pdf = _parse_content(content)
    xref = pdf.xrefs[0]
    objids = xref.get_objids()

    for objid in objids:
        try:
            obj = pdf.getobj(objid)
            yield objid, obj
        except PDFObjectNotFound:
            continue
