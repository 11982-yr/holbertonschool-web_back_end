#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Deletion-resilient pagination.

        Returns a dict with:
          - index: current start index
          - next_index: next index to query with
          - page_size: requested page size
          - data: list of rows
        """
        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed = self.indexed_dataset()
        # "valid range" means within the original indexing span (0..max_key)
        max_key = max(indexed.keys()) if indexed else 0
        assert index <= max_key

        data: List[List] = []
        current = index

        # Collect up to page_size existing rows, skipping deleted indices
        while len(data) < page_size and current <= max_key:
            if current in indexed:
                data.append(indexed[current])
            current += 1

        # current is now the first index after the last checked position
        return {
            "index": index,
            "next_index": current,
            "page_size": page_size,
            "data": data,
        }
