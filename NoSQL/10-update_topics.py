#!/usr/bin/env python3
""" Update document """
import pymongo


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school document based on the name

        Args:
            mongo_collection: collection to pass
            name: school name to update
            topics: list of topics
    
        Return:
            id of the new element
    """
    update_topics = mongo_collection.insert_one(kwargs)

    return (new_school.inserted_id)
