#!/usr/bin/env python3
"""
Returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    Args:
        mongo_collection: pymongo collection object
    Returns:
        List of students sorted by average score in descending order
    """
    # Aggregate the data using MongoDB's aggregation pipeline
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                },
                "topics": 1
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    
    return list(mongo_collection.aggregate(pipeline))
