import time
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 15 + (35 - 15) * (1 - int(time.time())) % 21
start_time = time.time()
result = fibonacci(n)
end_time = time.time()

print("fib", n, "=", result)
print("fib", n, "took", end_time - start_time, "seconds")