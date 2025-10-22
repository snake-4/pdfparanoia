# -*- coding: utf-8 -*-

import pdfparanoia

def test_ieee():
    with open("tests/samples/ieee/9984106e01b63d996f19f383b8d96f02.pdf", "rb") as fh:
        content = fh.read()

    assert b"\n4 0 obj" in content
    assert b"\n7 0 obj" in content

    output = pdfparanoia.plugins.IEEEXplore.scrub(content)
    assert b"\n19 0 obj" not in output
    assert b"\n37 0 obj" not in output
    assert b"\n43 0 obj" not in output
    assert b"\n53 0 obj" not in output
    assert b"\n64 0 obj" not in output
    assert b"\n73 0 obj" not in output

