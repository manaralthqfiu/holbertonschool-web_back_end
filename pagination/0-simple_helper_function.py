#!/usr/bin/env python3
"""
Helper function for pagination.

This module provides the index_range function, which calculates
the start and end indexes for a given page and page size.
"""


def index_range(page, page_size):
    """
    Return a tuple (start_index, end_index) for pagination.
    Page numbers are 1-indexed.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
