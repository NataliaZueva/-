with open('text.txt') as file:
    for line in file:
        l_dict = dict((a, b.strip()) for a, b in (element.split(':') for element in line.split(' ')))
        print(l_dict)
