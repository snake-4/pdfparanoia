# -*- coding: utf-8 -*-

from copy import copy
from ..parser import parse_content
from ..eraser import remove_object_by_id
from ..plugin import Plugin
from pdfminer.pdftypes import PDFObjectNotFound

class AmericanInstituteOfPhysics(Plugin):
    """
    American Institute of Physics
    ~~~~~~~~~~~~~~~

    These watermarks are pretty basic, but sometimes they don't have indexes
    attached for whatever reason.
    """

    @classmethod
    def scrub(cls, content, verbose=0):
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
                    length = obj.attrs["Length"]

                    # the watermark is never very long
                    if length < 1000:
                        #rawdata = copy(obj.rawdata)
                        data = copy(obj.get_data()).decode('ascii', 'ignore')

                        phrase="Redistribution subject to AIP license or copyright"
                        if phrase in data:
                            if verbose >= 1:
                                print(f"{cls.__name__}: Found object {objid} with \"{phrase}\"; omitting...")

                            evil_ids.append(objid)

        for objid in evil_ids:
            content = remove_object_by_id(content, objid)

        return content

