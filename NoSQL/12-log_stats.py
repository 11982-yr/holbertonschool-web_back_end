#!/usr/bin/env python3
"""
12-log_stats.py

Provides stats about Nginx logs stored in MongoDB:
Database: logs
Collection: nginx
"""

from pymongo import MongoClient


def main():
    """Main function"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # Total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: 0 for method in methods}

    # Aggregate method counts
    pipeline = [
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ]

    for doc in collection.aggregate(pipeline):
        if doc["_id"] in method_counts:
            method_counts[doc["_id"]] = doc["count"]

    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")

    # Count GET /status
    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_count} status check")


if __name__ == "__main__":
    main()
