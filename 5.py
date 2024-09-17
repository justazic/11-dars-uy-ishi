def divide(a, b):
    if b == 0:
        raise ValueError("Nolga bo'lish mumkin emas!")
    return a / b

def square_root(x):
    if x < 0:
        raise ValueError("Manfiy sonning ildizi mavjud emas!")
    return x ** 0.5


import math_operations

try:
    result1 = math_operations.divide(10, 2)
    print(f"10 / 2 = {result1}")

    result2 = math_operations.divide(8, 0)
    print(f"8 / 0 = {result2}")

except ValueError as ve:
    print(f"Xato yuz berdi: {ve}")

try:
    result3 = math_operations.square_root(16)
    print(f"Ildiz 16 = {result3}")

    result4 = math_operations.square_root(-4)
    print(f"Ildiz -4 = {result4}")

except ValueError as ve:
    print(f"Xato yuz berdi: {ve}")