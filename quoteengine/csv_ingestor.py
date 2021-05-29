#!/usr/bin/env python3

import pandas as pd
from .quote_model import QuoteModel
from .interface import IngestorInterface

class CSVIngestor(IngestorInterface):
    """Read CSV files, extract lines and return a list of quotes."""

    @classmethod
    def parse(cls, path):
        """Read CSV files, extract lines and return a list of quotes."""
        csv = pd.read_csv(path)
        return [QuoteModel(**row) for index, row in csv.iterrows()]