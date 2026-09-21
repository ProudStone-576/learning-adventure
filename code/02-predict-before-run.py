# Node: predict-before-run
# Predict every line of output BEFORE running. Track values, add nothing that isn't written.

scores = [70, 80, 90]
backup = scores
backup.append(100)

total = len(scores)
best = scores[total - 1]

print(scores)
print(total)
print(best)
