
# function implementation

def rectangle_area(width, height):
    return width * height

# testing the function

print(f"Area is {rectangle_area(5, 3)}")
def even_numbers(number):
    return [n for n in range(number + 1) if n % 2 == 0]
def mean_average(numbers):
    return sum(numbers) / len(numbers) if numbers else None
print(even_numbers(10))
print(mean_average([2, 4, 6]))
