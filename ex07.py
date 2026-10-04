# %% [markdown]
# ### [ex07] Speed: loops, built-ins and NumPy

# %%
from timeit import timeit
from typing import Final

N: Final[int] = 10_000_000


# %%
def while_loop_based_sum(n: int = N) -> int:
    res = 0
    i = 0
    while i < n:
        res += i
        i += 1
    return res


def for_loop_based_sum(n: int = N) -> int:
    res = 0
    for i in range(n):
        res += i
    return res


def sum_range_based_sum(n: int = N) -> int:
    return sum(range(n))


# %%
dt_while = timeit(while_loop_based_sum, number=3)
dt_for = timeit(for_loop_based_sum, number=3)
dt_sum = timeit(sum_range_based_sum, number=3)

print(f"{dt_while = :.2f} s, {dt_for = :.2f} s, {dt_sum = :.2f} s")

# %%
try:
    import numpy as np
except ModuleNotFoundError:
    print("NumPy is not installed in this environment (it is available in Google Colab)")
else:
    def numpy_based_sum(n: int = N) -> int:
        return int(np.sum(np.arange(n, dtype=np.int64)))

    dt_np = timeit(numpy_based_sum, number=3)

    print(f"{dt_np = :.2f} s")
    print(f"{dt_while / dt_np = :.0f}, {dt_for / dt_np = :.0f}, {dt_sum / dt_np = :.0f}")
    print(while_loop_based_sum() == numpy_based_sum())
