# Week 1.3, Additional work: CSV handling

import csv

with open('student_data.csv', 'r') as f:
    data = list(csv.DictReader(f))
with open('report.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Name', 'Average'])
    writer.writeheader()
    for row in data:
        average = (int(row['Mathematics']) + int(row['Science']) + int(row['History'])) / 3
        writer.writerow({'Name': row['Name'], 'Average': f'{average:.2f}'})
