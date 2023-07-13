import time

final_list = []
def factorial(n):
    time.sleep(0.1)

    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


def sum_factorial():
    for i in range(50):
        final_list.append(factorial(i))
    return sum(final_list)
result = sum_factorial()
print("Final SUM is {result}")
