#!/usr/bin/env python3
"""
102-log_stats.py

Improves 12-log_stats.py by adding the top 10 most frequent IPs.

Database: logs
Collection: nginx
"""

from pymongo import MongoClient


def main():
    """Print stats about nginx logs in MongoDB."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # Total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {m: 0 for m in methods}

    # Aggregate method counts
    pipeline_methods = [
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ]
    for doc in collection.aggregate(pipeline_methods):
        if doc["_id"] in method_counts:
            method_counts[doc["_id"]] = doc["count"]

    for m in methods:
        print(f"\tmethod {m}: {method_counts[m]}")

    # Count GET /status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

    # Top 10 IPs
    print("IPs:")
    pipeline_ips = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    for doc in collection.aggregate(pipeline_ips):
        print(f"\t{doc['_id']}: {doc['count']}")


if __name__ == "__main__":
    main()
