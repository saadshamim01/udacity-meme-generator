#!/usr/bin/env python3

extensions = {
    "TEXT": ".txt",
    "CSV": ".csv",
    "PDF": ".pdf",
    "DOCX": ".docx",
}


class IngestorInterface:
    """This class is an interface that is used by all other ingestors."""

    @classmethod
    def verify(cls, file_extension):
        """Check if a file extension is supported or not."""
        return file_extension in extensions.values()

    @classmethod
    def parse(cls, path):
        """Read files, extract lines and return a list of quotes."""
        pass
