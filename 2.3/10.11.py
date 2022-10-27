class MyList(list):
    def __init__(*args, **kwargs):
        list.__init__(*args, **kwargs)

    def __sub__(self, l):
        f = list(self)
        for i in range(len(list(l))):
            while l[i] in f:
                f.remove(l[i])
        print(f"First list {self}, second list {l}. Subtraction on result: {f}")


l = MyList([1, 1, 2, 4, 5, 5, 7])
l2 = [1, 2]
l - l2