# Node: predict-before-run / name-vs-object, transferred into functions
# One of these functions changes the outside world. The other does not.

def add_item(items):
    items.append(99)

def add_number(n):
    n = n + 1

original = [1, 2]
count = 5

add_item(original)
add_number(count)

print(original)
print(count)
