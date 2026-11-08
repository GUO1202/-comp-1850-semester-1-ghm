# Week 1.3, Session 2: Calculate Average Grade and Write to a File

with open('student_data.csv', 'r') as f:
    data = [line.strip().split(',') for line in f]
with open('report.txt', 'w') as f:
    for row in data[1:]:
        average = (int(row[2]) + int(row[3]) + int(row[4])) / 3
        f.write(f"{row[1]}: {average:.2f}\n")
