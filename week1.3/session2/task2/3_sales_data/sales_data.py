# Week 1.3, Session 2: Sales Data Statistics

try:
    with open('sales.csv', 'r') as f:
        data = [line.strip().split(',') for line in f]
    total = 0
    largest = None
    widgets = {}
    for row in data[1:]:
        amount = int(row[2])
        total = total + amount
        if largest is None or amount > int(largest[2]):
            largest = row
        product = row[1]
        widgets[product] = widgets.get(product, 0) + int(row[3])
    if largest is not None:
        print(f"Largest sale day: {largest[0]}, amount: {largest[2]}")
        print(f"Average sale amount: {total / (len(data) - 1):.2f}")
        best = max(widgets, key=widgets.get)
        print(f"Most sold widget: {best}, units: {widgets[best]}")
    else:
        print("No sales data")
except OSError:
    print("Could not open sales.csv")
