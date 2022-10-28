# with open('text.txt') as file:
#     for line in file:
#         l_dict = dict((a, b.strip()) for a, b in (element.split(':') for element in line.split(' ')))
#         print(l_dict)


class Triangle:
    def __init__(self, a):
        self.a = a

    def array(self):
        return self.a

    def __index__(self):
        return 1



    def __len__(self):
        return len(self.a)

    def __getitem__(self, key):
        return self.a[key]


a = Triangle([1, 2, 3, 4])
print(a.array())
print(a[1])


# class Thing(object):
#     def __index__(self, b):
#         return b
#
#
# thing = Thing()
# list_ = ['abc', 'def', 'ghi']
# print(list_[thing])
