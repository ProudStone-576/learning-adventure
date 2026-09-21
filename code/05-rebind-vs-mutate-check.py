# Node: mutate-vs-rebind
# wipe() moves its private name. empty() reaches through and changes the shared list.

def wipe(items):
    items = []

def empty(items):
    items.clear()

a = [1, 2]
b = [3, 4]

wipe(a)
empty(b)

print(a)
print(b)
