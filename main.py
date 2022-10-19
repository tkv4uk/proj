print(" Введите N ")
n = int(input())
f1 = 0
f2 = 1
i = 0
while n - 1 > i:
    fn = f1 + f2
    f1 = f2
    f2 = fn
    i = i + 1

print(" Число фибоначчи ", fn)
