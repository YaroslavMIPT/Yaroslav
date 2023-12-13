def careless_div(a, b):
    if b == 0:
        if a == 0:
            return -17.5
        elif a > 0:
            return '+inf'
        elif a < 0:
            return '-inf'

    if a == 0:
        return 0

    if a % b == 0:
        return a // b
    return a / b

#tests

print(careless_div(1, 0))
print(careless_div(-1, 0))
print(careless_div(0, 0))
print(careless_div(1, 1))
print(careless_div(1, 1000))
print(careless_div(-27, -39))
print(careless_div(-6, -2))

print(careless_div(4, 2))  # 2
print(careless_div(5, 2))  # 2.5
print(careless_div(5, 0))  # inf