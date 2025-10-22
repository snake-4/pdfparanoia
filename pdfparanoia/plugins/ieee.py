from ..parser import iterate_objects
from ..eraser import remove_object_by_id
from ..plugin import Plugin
from pdfminer.pdftypes import PDFStream


class IEEEXplore(Plugin):
    """
    IEEE Xplore
    ~~~~~~~~~~~~~~~

    """

    @staticmethod
    def scrub(content: bytes, verbose: bool = False) -> bytes:
        for objid, obj in iterate_objects(content):
            if isinstance(obj, PDFStream):
                # watermarks tend to be in FlateDecode elements
                if "FlateDecode" in str(obj.attrs.get("Filter", "")):
                    if b"Authorized licensed use limited to: " in obj.get_data():
                        if verbose:
                            print(f"IEEEXplore: Found object {objid}; omitting...")

                        content = remove_object_by_id(content, objid)

        return content
