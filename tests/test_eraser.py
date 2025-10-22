# -*- coding: utf-8 -*-

from pdfparanoia.eraser import remove_object_by_id

def test_remove_object_by_id():
    content = b""
    output = remove_object_by_id(content, 1)
    assert content == output

    content = b""
    output = remove_object_by_id(content, 2)
    assert content == output

    content = b""
    output = remove_object_by_id(content, 100)
    assert content == output

    content = b"1 0 obj\nthings\nendobj\nleftovers"
    output = remove_object_by_id(content, 2)
    assert content == output

    content = b"1 0 obj\nthings\nendobj\nleftovers"
    output = remove_object_by_id(content, 1)
    assert output == b"leftovers"

