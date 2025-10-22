"""
pdfparanoia.plugin
~~~~~~~~~~~~~~~

Defines how plugins work.

"""

from abc import ABC, abstractmethod


class Plugin(ABC):

    @staticmethod
    @abstractmethod
    def scrub(content: bytes, verbose: bool = False) -> bytes:
        """
        Removes watermarks from the given pdf.
        """
        raise NotImplementedError("must be implemented by the subclass")
