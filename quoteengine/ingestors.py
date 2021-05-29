#!/usr/bin/env python3
"""This module reads quotes from files and returns a list of quotes."""
import os

from .pdf_ingestor import PDFIngestor
from .text_ingestor import TextIngestor
from .docx_ingestor import DocxIngestor
from .csv_ingestor import CSVIngestor
from .interface import IngestorInterface, extensions


class Ingestor(IngestorInterface):
    """Extract the extension of the file and returns the results."""

    @classmethod
    def parse(cls, path):
        """Extract the extension of the file and returns the results."""
        filename, file_extension = os.path.splitext(path)
        if not cls.verify(file_extension):
            raise ValueError("Unsupported file extension:", file_extension)
        if file_extension == extensions.get("TEXT"):
            return TextIngestor.parse(path)
        if file_extension == extensions.get("DOCX"):
            return DocxIngestor.parse(path)
        if file_extension == extensions.get("PDF"):
            return PDFIngestor.parse(path)
        if file_extension == extensions.get("CSV"):
            return CSVIngestor.parse(path)
