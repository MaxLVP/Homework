f = open('data/unsorted_names.txt', 'r')
f_sort = open('data/sorted_names.txt', 'w')
sorted_names = []
for line in f.readlines():
    line = line.rstrip('\n')
    sorted_names.append(line)
sorted_names.sort()
for line in sorted_names:
    f_sort.write(f"{line} \n")
f.close()
f_sort.close()
