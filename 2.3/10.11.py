class MyList(list):
    def __init__(*args, **kwargs):
        list.__init__(*args, **kwargs)

    def __sub__(self, l):
        if len(self) <= len(l):
            f = list(l)
            f = [-i for i in f]
        else:
            f = list(self)
        c = min(len(self), len(l))
        for i in range(c):
            f[i] = self[i] - l[i]
        print(f"First list {self}, second list {l}. Subtraction on result: {f}")


a = MyList([1, 2, 3, 5])
a - [10, 3, 4, 5]
