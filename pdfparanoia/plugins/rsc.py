# -*- coding: utf-8 -*-

from copy import copy
from ..parser import parse_content
from ..plugin import Plugin
from pdfminer.pdftypes import PDFObjectNotFound

class RoyalSocietyOfChemistry(Plugin):
    """
    RoyalSocietyOfChemistry
    ~~~~~~~~~~~~~~~

    RSC watermarks each PDF with a "Downloaded" date and the name
    of the institution from which the PDF was downloaded.
    
    Watermarks removed:
        * "Downloaded by" watermark and timestamp on the each page
        * "Published on" watermark on the side of each page

    This was primary written for RSC PDF's from http://pubs.rsc.org
    """
        
    @classmethod
    def scrub(cls, content, verbose=0):
        replacements = []
        
        # List of watermark strings to remove
        watermarks = [
            "Downloaded by ",
            "Downloaded on ",
            "Published on ",
            #"View Article Online",
            #"Journal Homepage",
            #"Table of Contents for this issue",
        ]

        # Confirm the PDF is from the RSC
        if b"pubs.rsc.org" in content:
            
            # parse the pdf into a pdfminer document
            pdf = parse_content(content)

            # get a list of all object ids
            xref = pdf.xrefs[0]
            objids = xref.get_objids()

            # check each object in the pdf
            for objid in objids:
                obj = None
                try:
                    obj = pdf.getobj(objid)
                except PDFObjectNotFound:
                    continue

                if hasattr(obj, "attrs"):
                    # watermarks tend to be in FlateDecode elements
                    if "Filter" in obj.attrs and "FlateDecode" in str(obj.attrs["Filter"]):
                        rawdata = copy(obj.rawdata)
                        data = copy(obj.get_data()).decode('ascii', 'ignore')

                        # Check if any of the watermarks are in the current object
                        for phrase in watermarks:
                            if phrase in data:
                                if verbose >= 1:
                                    print(f"{cls.__name__}: Found object {objid} with \"{phrase}\"; omitting...")
                                
                                # We had a match so replace the watermark data with an empty string                 
                                replacements.append([rawdata, b''])
            
        for deets in replacements:
            # Directly replace the stream data in binary encoded object
            content = content.replace(deets[0], deets[1])

        return content


