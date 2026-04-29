#!/usr/bin/env python3
"""
Simple pagination module.

This module defines the Server class which loads a CSV dataset
and provides a get_page method to paginate the data.
"""

import csv
from typing import List


def index_range(page, page_size):
    """
    Return a tuple (start_index, end_index) for pagination.
    Page numbers are 1-indexed.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset.
        Uses index_range to compute start and end indexes.
        """
        # Validate inputs
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Compute index range
        start, end = index_range(page, page_size)

        dataset = self.dataset()

        # If out of range, return empty list
        if start >= len(dataset):
            return []

        return dataset[start:end]
