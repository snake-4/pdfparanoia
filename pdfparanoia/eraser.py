# -*- coding: utf-8 -*-
"""
pdfparanoia.eraser
~~~~~~~~~~~~~~~

Tools to erase things from pdfs by direct manipulation of the pdf format.

"""

def manipulate_pdf(content: bytes, objid: int, callback, *args):
    """
    Iterates through a pdf looking for the object with the objid id. When the
    object is found, callback is called with a reference to the current list of
    output lines.
    """
    outlines = []
    lines = content.splitlines(keepends=True) # change this
    last_line = None
    skip_mode = False
    for line in lines:
        cleanLine = line.replace(b"\n", b"").replace(b"\r", b"").decode('ascii', 'ignore')
        if cleanLine == '':
            outlines.append(line)
            continue
        if not skip_mode:
            if last_line in ["endobj", "endobj ", None]:
                isStartOfObject = (cleanLine[-3:] == "obj" or cleanLine[-4:] == "obj " or " obj <<" in cleanLine[0:50] or " obj<<" in cleanLine[0:50])
                if isStartOfObject and cleanLine.startswith(f"{objid} "):
                    skip_mode = True
                    last_line = cleanLine
                    callback(outlines, *args)
                    continue
            outlines.append(line)
        elif skip_mode and cleanLine == "endobj" or cleanLine == "endobj ":
            skip_mode = False
        last_line = cleanLine
    output = b''.join(outlines)
    return output

def remove_object_by_id(content: bytes, objid: int) -> bytes:
    """
    Deletes an object from a pdf. Mostly streams and FlateDecode stuff.
    """
    def _remove_object(outlines): pass
    output = manipulate_pdf(content, objid, _remove_object)
    return output

def replace_object_with(content: bytes, objid: int, replacement: bytes) -> bytes:
    """
    Replaces an object from a pdf. Mostly streams. This is useful for replacing
    an encoded object with a plaintext object.
    """
    def _replace_object_with(outlines, details):
        objid = details["objid"]
        replacement = details["replacement"]

        output = bytearray(f"{objid} 0 obj\n<</Length {len(replacement)+2}>>stream\n".encode('ascii', 'ignore'))
        output.extend(replacement)
        output.extend(b"\nendstream\nendobj\n")
        outlines.append(bytes(output))

    output = manipulate_pdf(content, objid, _replace_object_with, {"objid": objid, "replacement": replacement})
    return output

