from ..parser import iterate_objects
from ..eraser import remove_object_by_id
from ..plugin import Plugin
from pdfminer.pdftypes import PDFStream


class AmericanInstituteOfPhysics(Plugin):
    """
    American Institute of Physics
    ~~~~~~~~~~~~~~~

    These watermarks are pretty basic, but sometimes they don't have indexes
    attached for whatever reason.
    """

    @staticmethod
    def scrub(content: bytes, verbose: bool = False) -> bytes:
        for objid, obj in iterate_objects(content):
            if isinstance(obj, PDFStream):
                # watermarks tend to be in FlateDecode elements
                if "FlateDecode" in str(obj.attrs.get("Filter", "")):
                    length = obj.attrs["Length"]

                    # the watermark is never very long
                    if length < 1000:
                        if (
                            b"Redistribution subject to AIP license or copyright"
                            in obj.get_data()
                        ):
                            if verbose:
                                print(
                                    f"AmericanInstituteOfPhysics: Found object {objid}; omitting..."
                                )

                            content = remove_object_by_id(content, objid)

        return content
