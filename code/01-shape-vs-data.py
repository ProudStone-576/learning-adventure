"""
Does more data fix a model whose SHAPE is wrong?

We invent the true pattern ourselves, so we know the right answer
and can check whether the model recovered it.
"""
import numpy as np

np.random.seed(0)

# The true pattern. Salary rises fast early, then flattens.
# We chose this, so we know exactly what "correct" looks like.
def true_salary(years):
    return 40_000 + 12_000 * np.sqrt(years)


def make_data(n_rows):
    years = np.random.uniform(0, 40, n_rows)
    noise = np.random.normal(0, 2_000, n_rows)      # real data is never exact
    return years, true_salary(years) + noise


def fit_and_score(features, salary):
    # least squares: find the parameter values with the smallest squared error
    params, *_ = np.linalg.lstsq(features, salary, rcond=None)
    guesses = features @ params
    return np.abs(guesses - salary).mean(), params


def straight_line(years):
    # guess = b + w * years          <- cannot bend
    return np.column_stack([np.ones_like(years), years])


def bending(years):
    # guess = b + w * sqrt(years)    <- can bend
    return np.column_stack([np.ones_like(years), np.sqrt(years)])


print("true pattern:  salary = 40,000 + 12,000 * sqrt(years)\n")

for n in (100, 1_000_000):
    years, salary = make_data(n)
    err, _ = fit_and_score(straight_line(years), salary)
    print(f"straight line, {n:>9,} rows   ->  average error  ${err:>8,.0f}")

years, salary = make_data(100)
err, params = fit_and_score(bending(years), salary)
print(f"bending shape, {100:>9,} rows   ->  average error  ${err:>8,.0f}")
print(f"\nbending shape recovered:  b = {params[0]:,.0f}   w = {params[1]:,.0f}")
print("we put in:                b = 40,000   w = 12,000")
