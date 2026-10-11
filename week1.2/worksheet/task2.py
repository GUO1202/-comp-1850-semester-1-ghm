# Worksheet 1.2: Task 2 Solution

def read_numbers():
    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    return numbers


numbers = read_numbers()
print(numbers)

if len(numbers) == 0:
    print("Error: no numbers provided")

minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers)

numbers.sort()
n = len(numbers)

if n % 2 != 0:
    median = numbers[n // 2]
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2


print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Mean: {mean}")
print(f"Median: {median}")
