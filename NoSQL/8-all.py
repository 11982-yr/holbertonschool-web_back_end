#!/usr/bin/env python3
"""List documents"""
import pymongo


def list_all(mongo_collection) -> list:
    """Lists all documents in a collection
       Args:
           mongo_collection: collection of objects

        Return:
            List with documents, otherwise []
    """
    documents: list = []

    for document in mongo_collection.find():
        documents.append(document)

    return documents
