#!/usr/bin/env python3
""" Schools by topic """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school having a specific topic

        Args:
            mongo_collection: collection to pass
            topic: topic searched
    
        Return:
            List of schools by topic
    """
    query: dict = {'topics': topic}
    schools: list = []

    for school in mongo_collection.find(query):
        schools.append(school)

    return schools
