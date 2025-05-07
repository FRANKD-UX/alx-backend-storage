#!/usr/bin/env python3
"""
Provides enhanced stats about Nginx logs stored in MongoDB
Including top 10 most present IPs
"""
from pymongo import MongoClient


if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Get total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Get methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Get number of status check logs
    status_check = nginx_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check} status check")

    # Get top 10 IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    
    top_ips = nginx_collection.aggregate(pipeline)
    
    print("IPs:")
    for ip_data in top_ips:
        print(f"    {ip_data['_id']}: {ip_data['count']}")
