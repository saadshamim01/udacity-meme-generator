#!/usr/bin/env python3
from .quote_model import QuoteModel
from .interface import IngestorInterface
from docx import Document

class DocxIngestor(IngestorInterface):
    """Read DOCX files, extract lines and return a list of quotes."""

    @classmethod
    def parse(cls, path):
        """Read DOCX files, extract lines and return a list of quotes."""
        document = Document(path)
        quotes = []
        for paragraph in document.paragraphs:
            paragraph.text and quotes.append(
                QuoteModel(*paragraph.text.split(" - "))
            )
        return quotes