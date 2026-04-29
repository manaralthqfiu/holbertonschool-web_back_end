#!/usr/bin/env python3
def index_range(page, page_size):
    """
    Return a tuple (start_index, end_index) for pagination.
    Page numbers are 1-indexed.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
