# Week 1.3, Session 2: Log Data Filtering

import csv

try:
    with open('site.log', 'r') as f:
        data = csv.DictReader(f)
        for row in data:
            if row['Request'] == 'POST /login' and row['Status_Code'] == '401':
                print(f"IP address {row['IP_Address']} failed to login at {row['Time']} on {row['Date']}")
except OSError:
    print("Could not open site.log")
