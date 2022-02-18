file = open('p.txt', 'r')
dictionary ={}
i = 1
for line in file:
    x = line.split()
    dictionary[x[0].strip('. ')] = dictionary.get(x[0].strip('. '), '') + str(i) + ') ' + ' '.join(x[1:]) + '\n'
    i += 1
for key,value in dictionary.items(): print(key, ':\n', value, sep='')

file.close()

