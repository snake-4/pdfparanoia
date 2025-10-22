# -*- coding: utf-8 -*-

from copy import copy
from ..parser import parse_content
from ..eraser import remove_object_by_id
from ..plugin import Plugin
from pdfminer.pdftypes import PDFObjectNotFound

class IEEEXplore(Plugin):
    """
    IEEE Xplore
    ~~~~~~~~~~~~~~~

    """

    @staticmethod
    def scrub(content: bytes, verbose: bool = False) -> bytes:
        evil_ids = []

        # parse the pdf into a pdfminer document
        pdf = parse_content(content)

        # get a list of all object ids
        xref = pdf.xrefs[0]
        objids = xref.get_objids()

        # check each object in the pdf
        for objid in objids:
            # get an object by id
            obj = None
            try:
                obj = pdf.getobj(objid)
            except PDFObjectNotFound:
                continue

            if hasattr(obj, "attrs"):
                # watermarks tend to be in FlateDecode elements
                if "Filter" in obj.attrs and "FlateDecode" in str(obj.attrs["Filter"]):
                    data = copy(obj.get_data()).decode('ascii', 'ignore')
                    phrase= "Authorized licensed use limited to: "
                    if phrase in data:
                        evil_ids.append(objid)
                        if verbose:
                            print(f"IEEEXplore: Found object {objid} with \"{phrase}\"; omitting...")
        
        for objid in evil_ids:
            content = remove_object_by_id(content, objid)

        return content

