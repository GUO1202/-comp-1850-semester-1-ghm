"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"   #定义初始状态

remaining = states[state]  #设置remaining
print(f"Time {systime:03} State {state}")

for systime in range(1, maxtime + 1):
    remaining -= 1
    if remaining == 0: #剩余时间等于0的时候换成红色
        if state == "red":
            state = "red_amber"
        elif state == "red_amber":
            state = "green"
        elif state == "green":
            state = "amber"
        elif state == "amber":
            state = "red"
        remaining = states[state]
    print(f"Time {systime:03} State {state}")  #在每次循环结束时输出当前时间和状态

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14