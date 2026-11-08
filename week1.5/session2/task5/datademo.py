# Week 1.5, Session 2: Task 5

from data import Dataset

filename = input("Enter a data file name: ")
dataset = Dataset(filename)
print(f"Dataset size: {len(dataset)}")
print(f"Mean: {dataset.mean()}")
print(f"Median: {dataset.median()}")
for value in dataset:
    print(value)
