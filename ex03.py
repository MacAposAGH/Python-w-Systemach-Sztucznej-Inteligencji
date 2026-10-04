# %% [markdown]
# ### [ex03] Numbers: big integers and floating point arithmetic

# %%
import math

print(2 ** 200)  # integers have arbitrary precision
print(math.factorial(30))
print(7 / 2, 7 // 2, 7 % 2, -7 // 2)

# %%
print(0.1 + 0.2 == 0.3)

print(f"{0.1:.30f}")
print(f"{0.1 + 0.2:.30f}")
print(f"{0.3:.30f}")

# see: https://0.30000000000000004.com

# %%
xs = [0.1] * 10

acc = 0.0
for x in xs:
    acc += x

print(acc, acc == 1.0)
print(math.isclose(acc, 1.0))
print(math.fsum(xs), math.fsum(xs) == 1.0)
print(sum(xs), sum(xs) == 1.0)  # the result depends on the Python version (3.12 changed sum)


# %%
def ex03_1(x1: float, x2: float, x3: float) -> bool:
    s1 = x1 + x2 + x3
    s2 = x3 + x2 + x1

    return s1 == s2


print(ex03_1(0.1, 0.2, 0.3))

# %%
print(math.exp(700))

try:
    print(math.exp(710))
except OverflowError as err:
    print(f"OverflowError: {err}")

print(math.inf, -math.inf, math.inf - math.inf, math.nan == math.nan)
