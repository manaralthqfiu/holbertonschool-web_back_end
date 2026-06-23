#!/usr/bin/env python3
"""
Module that contains the function schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic
    """
    schools = mongo_collection.find({"topics": topic})
    return [doc for doc in schools]