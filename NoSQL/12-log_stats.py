#!/usr/bin/env python3
"""
12-log_stats.py

Provides stats about Nginx logs stored in MongoDB:
Database: logs
Collection: nginx

Output format must match the project example exactly.
"""
from pymongo import MongoClient


def main():
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    total = collection.count_documents({})
    print(f"{total} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        count = collection.count_documents({"method": m})
        print(f"\tmethod {m}: {count}")

    status_checks = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")


if __name__ == "__main__":
    main()
