#!/usr/bin/env python3
"""
Module that contains the function
top_students
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    pipeline = [
        {
            "$project": {
                "name": "$name",
                "topics": "$topics",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
