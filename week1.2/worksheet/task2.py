# Worksheet 1.2: Task 2 Solution
from util import read_numbers
numbers = read_numbers()
print(numbers)

Minimum = min(numbers)
Maximum = max(numbers)
Mean = sum(numbers) / len(numbers)
Median = sorted(numbers)[len(numbers) // 2] if len(numbers) % 2 == 1 else (sorted(numbers)[len(numbers) // 2 - 1] + sorted(numbers)[len(numbers) // 2]) / 2

print(f"Minimum: {Minimum}")
print(f"Maximum: {Maximum}")
print(f"Mean: {Mean}")
print(f"Median: {Median}")
