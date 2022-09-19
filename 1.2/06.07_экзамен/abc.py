# def read(title):
#     string = []
#     with open(title, "r", encoding='utf-8') as file:
#         for line in file:
#             string.append(list(line.split("\n")))
#             # print(string)
#     return string
#
#
# a = read("abc.txt")
#
# # v = input("Введите последовательность символов: ")
# v = "стол"
#
#
# for df in a:
#     ex = v in df[0]
#     if ex == True:
#         print(df[0])



with open("abc.txt", 'r', encoding='utf_8') as f: lst = f.readlines()
v = input("Введите последовательность символов: ")
a = list(filter(lambda i: v in i != True, lst))
if a != []:
    print(a)
else:
    print('Такой последовательности нет')
