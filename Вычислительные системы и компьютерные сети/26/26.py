s, part = 0, []
input_list = open("ping.txt", "r")
f = open("text.txt", 'w')
lines = input_list.readlines()[1:-4]
for line in lines:
    s = float(line[-8:-4])
    part.append(float(line[-8:-4]))
    f.write(f"{s}\n")
f.close()
input_list.close
