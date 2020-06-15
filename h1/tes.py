# minggu 2


a = 3


def some_func():
    global a
    a = 5


some_func()
print(a)

# recursive
# def factorial_recursive(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial_recursive(x-1)


# print(factorial_recursive)
