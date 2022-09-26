# e = 7
# n = 77
#
# for d in range(100000):
#     if d * 7 % 60 == 1:
#         print(d)

print(list(lambda x: x* 7 % 60 == 1, 1000))