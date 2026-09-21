# Node: predict-before-run / name-vs-object
# Same as 02, but backup is a real copy instead of a second name.

scores = [70, 80, 90]
backup = list(scores)
backup.append(100)

total = len(scores)
best = scores[total - 1]

print(scores)
print(total)
print(best)
