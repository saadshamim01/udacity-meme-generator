#!/usr/bin/env python3
import subprocess
import os

from .text_ingestor import TextIngestor
from .interface import IngestorInterface

class PDFIngestor(IngestorInterface):
    """Read PDF files, extract lines and return a list of quotes."""

    @classmethod
    def parse(cls, path):
        """Read PDF files, extract lines and return a list of quotes."""
        text_file = "./pdf_to_text.txt"
        try:
            cmd = f"pdftotext -layout -nopgbrk {path} {text_file}"
            subprocess.run(cmd, shell=True, stderr=subprocess.STDOUT, check=True)
            quotes = TextIngestor.parse(text_file)
            os.remove(text_file)
            return quotes
        except:
            print("An error has occurred")
            return []