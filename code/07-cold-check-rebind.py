def f(x):
    x.append(1)
    x = [99]
    x.append(2)

y = [0]
f(y)
print(y)
