# -*- coding: utf-8 -*-

import unittest
import pdfparanoia

class IEEEXploreTestCase(unittest.TestCase):
    def test_ieee(self):
        file_handler = open("tests/samples/ieee/9984106e01b63d996f19f383b8d96f02.pdf", "rb")
        content = file_handler.read()
        self.assertIn(b"\n4 0 obj", content)
        self.assertIn(b"\n7 0 obj", content)

        output = pdfparanoia.plugins.IEEEXplore.scrub(content)
        self.assertNotIn(b"\n19 0 obj", output)
        self.assertNotIn(b"\n37 0 obj", output)
        self.assertNotIn(b"\n43 0 obj", output)
        self.assertNotIn(b"\n53 0 obj", output)
        self.assertNotIn(b"\n64 0 obj", output)
        self.assertNotIn(b"\n73 0 obj", output)

