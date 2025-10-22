import pdfparanoia

def test_rsc():
    with open("tests/samples/rsc/3589bf649f8bb019bd97be9880627b7c.pdf", "rb") as fh:
        content = fh.read()

    # Check the PDF is from the RSC
    assert b"pubs.rsc.org" in content

    output = pdfparanoia.plugins.RoyalSocietyOfChemistry.scrub(content)

    # Check the PDF was output correctly and still contains the RSC url.
    assert b"pubs.rsc.org" in output

