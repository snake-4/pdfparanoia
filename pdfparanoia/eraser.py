"""
pdfparanoia.eraser
~~~~~~~~~~~~~~~

Tools to erase things from pdfs by direct manipulation of the pdf format.

"""

from typing import Callable


def _manipulate_pdf(
    content: bytes, objid: int, callback: Callable[[list[bytes]], None] | None = None
) -> bytes:
    """
    Iterates through a pdf looking for the object with the objid id. When the
    object is found, callback is called with a reference to the current list of
    output lines.
    """
    outlines = []
    lines = content.splitlines(keepends=True)  # change this
    last_line = None
    skip_mode = False
    for line in lines:
        cleanLine = (
            line.replace(b"\n", b"").replace(b"\r", b"").decode("ascii", "ignore")
        )
        if cleanLine == "":
            outlines.append(line)
            continue
        if not skip_mode:
            if last_line in ["endobj", "endobj ", None]:
                isStartOfObject = (
                    cleanLine[-3:] == "obj"
                    or cleanLine[-4:] == "obj "
                    or " obj <<" in cleanLine[0:50]
                    or " obj<<" in cleanLine[0:50]
                )
                if isStartOfObject and cleanLine.startswith(f"{objid} "):
                    skip_mode = True
                    last_line = cleanLine

                    if callback:
                        callback(outlines)

                    continue
            outlines.append(line)
        elif skip_mode and cleanLine == "endobj" or cleanLine == "endobj ":
            skip_mode = False
        last_line = cleanLine
    output = b"".join(outlines)
    return output


def remove_object_by_id(content: bytes, objid: int) -> bytes:
    """
    Deletes an object from a pdf. Mostly streams and FlateDecode stuff.
    """
    return _manipulate_pdf(content, objid)


def replace_object_with(content: bytes, objid: int, replacement: bytes) -> bytes:
    """
    Replaces an object from a pdf. Mostly streams. This is useful for replacing
    an encoded object with a plaintext object.
    """

    def _replace_object_with(outlines):
        outlines.append(
            f"{objid} 0 obj\n<</Length {len(replacement)+2}>>stream\n".encode(
                "ascii", "ignore"
            )
            + replacement
            + b"\nendstream\nendobj\n"
        )

    return _manipulate_pdf(
        content,
        objid,
        _replace_object_with,
    )
