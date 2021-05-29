#!/usr/bin/env python3

from .interface import IngestorInterface
from .quote_model import QuoteModel

class TextIngestor(IngestorInterface):
    """Read TXT files, extract lines and return a list of quotes."""

    @classmethod
    def parse(cls, path):
        """Read TXT files, extract lines and return a list of quotes."""
        file = open(path, "r", encoding="utf-8-sig")
        lines = file.readlines()
        file.close()
        x = [QuoteModel(*quote.rstrip("\n").split(" - ")) for quote in lines]
        return x