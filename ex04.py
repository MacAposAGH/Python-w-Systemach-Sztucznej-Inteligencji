# %% [markdown]
# ### [ex04] Names and objects: references, mutability, copies

# %%
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2, l1 is l2)

# %%
l3 = [1, 2, 3]
l4 = l3  # no copy: two names, one object
l4[0] = -1
print(f"{l3 = }, {l4 = }, {l3 is l4 = }")


# %%
def f1(lst: list[int]) -> None:
    lst = [10, 20, 30]  # rebinds the local name


def f2(lst: list[int]) -> None:
    lst.append(4)  # mutates the object


l5 = [1, 2, 3]
f1(l5)
print(f"{l5 = }")

l6 = [1, 2, 3]
f2(l6)
print(f"{l6 = }")

# %%
import copy

l7 = [1, [2, 3]]
l8 = l7.copy()  # shallow copy
l9 = copy.deepcopy(l7)

l7[1][0] = -2
print(f"{l7 = }, {l8 = }, {l9 = }")

# %%
t1 = (1, 2, 3)
s1 = "abc"

try:
    t1[0] = 0
except TypeError as err:
    print(f"TypeError: {err}")

s2 = s1.upper()  # a new object; s1 is unchanged
print(f"{s1 = }, {s2 = }")


# %%
def add_sample(x: float, batch: list[float] = []) -> list[float]:
    batch.append(x)
    return batch


print(add_sample(1.0))
print(add_sample(2.0))
print(add_sample.__defaults__)

# %%
row = [0.0] * 3
grid1 = [row] * 2  # two references to the same row
grid2 = [[0.0] * 3 for _ in range(2)]

grid1[0][0] = 1.0
grid2[0][0] = 1.0
print(f"{grid1 = }")
print(f"{grid2 = }")
