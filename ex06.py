# %% [markdown]
# ### [ex06] Vectors and the nearest neighbour: a first model

# %%
import math

Vector = tuple[float, float]

# (petal length [cm], petal width [cm]), species - a small sample of the Iris dataset
TRAIN: list[tuple[Vector, str]] = [
    ((1.4, 0.2), "setosa"),
    ((1.5, 0.2), "setosa"),
    ((1.7, 0.2), "setosa"),
    ((1.6, 0.2), "setosa"),
    ((1.3, 0.3), "setosa"),
    ((4.7, 1.4), "versicolor"),
    ((3.5, 1.0), "versicolor"),
    ((4.8, 1.8), "versicolor"),
    ((3.8, 1.1), "versicolor"),
    ((4.4, 1.2), "versicolor"),
    ((6.0, 2.5), "virginica"),
    ((5.1, 2.0), "virginica"),
    ((5.7, 2.3), "virginica"),
    ((6.1, 1.9), "virginica"),
    ((5.6, 2.4), "virginica"),
]

TEST: list[tuple[Vector, str]] = [
    ((1.7, 0.4), "setosa"),
    ((1.6, 0.2), "setosa"),
    ((1.4, 0.3), "setosa"),
    ((4.5, 1.3), "versicolor"),
    ((4.4, 1.4), "versicolor"),
    ((4.2, 1.2), "versicolor"),
    ((6.6, 2.1), "virginica"),
    ((6.0, 1.8), "virginica"),
    ((5.2, 2.3), "virginica"),
    ((4.8, 1.8), "virginica"),
]


# %%
def dot(u: Vector, v: Vector) -> float:
    return sum(ui * vi for ui, vi in zip(u, v))


def norm(u: Vector) -> float:
    return math.sqrt(dot(u, u))


print(dot((1.0, 2.0), (3.0, 4.0)), norm((3.0, 4.0)))


# %%
def distance(u: Vector, v: Vector) -> float:
    """The Euclidean distance between u and v."""
    raise NotImplementedError  # TODO


def predict(x: Vector, train: list[tuple[Vector, str]]) -> str:
    """The label of the training example nearest to x."""
    raise NotImplementedError  # TODO


def accuracy(test: list[tuple[Vector, str]], train: list[tuple[Vector, str]]) -> float:
    """The fraction of test examples whose predicted label is correct."""
    raise NotImplementedError  # TODO


# %%
print(distance((0.0, 0.0), (3.0, 4.0)))  # expected: 5.0
print(predict((1.5, 0.3), TRAIN))  # expected: setosa
print(accuracy(TEST, TRAIN))  # expected: 0.9
