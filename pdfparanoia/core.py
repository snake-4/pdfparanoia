"""
pdfparanoia.core
~~~~~~~~~~~~~~~

This module provides most of the heavy lifting of pdfparanoia.

"""

from pdfparanoia.plugins import *


def scrub(content: bytes, verbose: bool = False) -> bytes:
    """
    Removes watermarks from a pdf and returns the resulting pdf as a string.
    """

    for plugin in [
        AmericanInstituteOfPhysics,
        IEEEXplore,
        JSTOR,
        RoyalSocietyOfChemistry,
        ScienceMagazine,
    ]:
        content = plugin.scrub(content, verbose=verbose)

    return content
