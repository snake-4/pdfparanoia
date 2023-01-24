# -*- coding: utf-8 -*-

import unittest
import pdfparanoia

class AmericanInstituteOfPhysicsTestCase(unittest.TestCase):
    def test_aip(self):
        file_handler = open("tests/samples/aip/a7132c0d62d7c00e92e8e0553f480556.pdf", "rb")
        content = file_handler.read()
        self.assertIn(b"\n4 0 obj\n", content)
        self.assertIn(b"\n10 0 obj\n", content)

        output = pdfparanoia.plugins.AmericanInstituteOfPhysics.scrub(content)
        self.assertNotIn(b"\n4 0 obj\n", output)
        self.assertNotIn(b"\n10 0 obj\n", output)

