a1 = [10, 45, 50, 47, 30, 25, 15, 20, 75, 1001]
a2 = [num for num in a1 if num > 30]
a3 = [num for num in a1 if num < 30]
a4 = [num for num in a1 if num == 30]
a5 = [num for num in a1 if num >= 30]
a6 = [num for num in a1 if num <= 30]
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)