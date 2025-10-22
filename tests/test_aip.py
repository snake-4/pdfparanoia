import pdfparanoia

def test_aip():
    with open("tests/samples/aip/a7132c0d62d7c00e92e8e0553f480556.pdf", "rb") as fh:
        content = fh.read()

    assert b"\n4 0 obj\n" in content
    assert b"\n10 0 obj\n" in content

    output = pdfparanoia.plugins.AmericanInstituteOfPhysics.scrub(content)
    assert b"\n4 0 obj\n" not in output
    assert b"\n10 0 obj\n" not in output

