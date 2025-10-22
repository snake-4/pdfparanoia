# -*- coding: utf-8 -*-

import pdfparanoia

def test_jstor():
    with open("tests/samples/jstor/231a515256115368c142f528cee7f727.pdf", "rb") as fh:
        content = fh.read()

    assert b"\n18 0 obj \n" in content

    # this section will later be manipulated
    assert b"\n19 0 obj \n" in content

    output = pdfparanoia.plugins.JSTOR.scrub(content)

    # FlateDecode should be replaced with a decompressed section
    assert b"\n19 0 obj\n<</Length 2862>>stream" in output

