#!/usr/bin/env python3
"""
Returns the list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic
    Args:
        mongo_collection: pymongo collection object
        topic: topic to search for
    Returns:
        List of schools that contain the topic
    """
    return list(mongo_collection.find({"topics": topic}))
