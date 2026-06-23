#!/usr/bin/env python3
"""
Advanced script that provides stats about Nginx logs,
including top 10 IPs
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Display total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Display methods count
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Display status check count
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")

    # Display top 10 IPs
    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = nginx_collection.aggregate(pipeline)
    for ip in top_ips:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")
