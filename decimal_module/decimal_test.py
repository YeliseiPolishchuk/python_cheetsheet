import decimal

print(0.2 + 0.1 == 0.3)
print(0.2 + 0.1)

# numbers after dot = 6
decimal.getcontext().prec = 6
# exact value of 1 / 7 = 0.142857
print(decimal.Decimal(1) / decimal.Decimal(7))  # 0.142857

decimal.getcontext().prec = 28
# 0.1428571428571428571428571429
print(decimal.Decimal(1) / decimal.Decimal(7))

# Decimal and float can't be operands in one exprression
# Decimal(0.1) / 0.2 will cause the error

decimal.getcontext().prec = 6
print(float(decimal.Decimal(0.1) + decimal.Decimal(0.2)) == 0.3)

print(decimal.Decimal(0.2) + decimal.Decimal(0.1) == decimal.Decimal(0.3))
print(decimal.Decimal(0.2) + decimal.Decimal(0.1) == decimal.Decimal(0.3) + decimal.Decimal(0.0))
