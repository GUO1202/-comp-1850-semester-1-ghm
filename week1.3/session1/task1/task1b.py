# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']
while fruit:
    print(fruit.pop())

# Before the first iteration: ['apple','pear','banana','orange']
# Before the fourth iteration: ['apple']; after the loop: []
# pop() removes the last item each time. An empty list is false,
# so the loop stops after four iterations.
