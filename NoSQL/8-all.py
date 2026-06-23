#!/usr/bin/env python3
"""
Module that contains the function list_all
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    """
    schools = mongo_collection.find()

    if not schools:
        return []

    return [doc for doc in schools]