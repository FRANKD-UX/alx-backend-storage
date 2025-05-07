#!/usr/bin/env python3
"""
Inserts a new document in a MongoDB collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection
    Args:
        mongo_collection: pymongo collection object
        **kwargs: key/value pairs to insert in the document
    Returns:
        _id of the newly inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
