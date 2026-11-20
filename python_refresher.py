import time
import matplotlib.pyplot as plt
def fib1(num):
    if(num<=1):
        return 1
    else:
        return fib1(num-1) + fib1(num-2)
def fib2(num):
    a=1
    b=1
    for i in range(num):
        a,b = b,a+b
    return a
def compute_time(fn,limit):
    l =[]

    for i in range(limit):

        start_time = int(round(time.time() * 1000))

        fn(i)

        end_time = int(round(time.time() * 1000))
        time_taken = end_time - start_time
        l.append(time_taken)
    return l
print("fib1: ")
for i in range(15):
    print(fib1(i), end=",")
print("\n")
print("fib2: ")
for i in range(15):
    print(fib2(i), end=",")
print("\n")
# This line is for matplot lib to make a 
# graph to see the timeline of the deferent functions
# and able to make a difference between them
limit = 40
fib1_times = compute_time(fib1,limit)
fib2_times = compute_time(fib2,limit)
print(fib1_times)
print(fib2_times)
plt.figure()
plt.xlabel("fib(n)")
plt.ylabel("time (ms)")
plt.plot(fib1_times)
plt.plot(fib2_times)
plt.show()