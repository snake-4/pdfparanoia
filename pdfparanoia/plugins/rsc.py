from pdfparanoia.eraser import remove_object_by_id
from ..parser import iterate_objects
from ..plugin import Plugin
from pdfminer.pdftypes import PDFStream


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

    WATERMARKS = [
        b"Downloaded by ",
        b"Downloaded on ",
        b"Published on ",
        # b"View Article Online",
        # b"Journal Homepage",
        # b"Table of Contents for this issue",
    ]

    @staticmethod
    def scrub(content: bytes, verbose: bool = False) -> bytes:
        if b"pubs.rsc.org" not in content:
            return content

        for objid, obj in iterate_objects(content):
            if isinstance(obj, PDFStream):
                # watermarks tend to be in FlateDecode elements
                if "FlateDecode" in str(obj.attrs.get("Filter", "")):
                    data = obj.get_data()

                    for phrase in RoyalSocietyOfChemistry.WATERMARKS:
                        if phrase in data:
                            if verbose:
                                print(
                                    f'RoyalSocietyOfChemistry: Found object {objid} with "{phrase}"; omitting...'
                                )
                            content = remove_object_by_id(content, objid)

        return content
