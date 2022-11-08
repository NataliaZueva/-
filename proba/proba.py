import copy

from memory_profiler import profile


@profile
def function():
    x = list(range(1000000))  # allocate a big list
    y = copy.deepcopy(x)
    del x
    return y


if __name__ == "__main__":
    function()

