tuples = input().split(', ')
for i in range(len(tuples)):
    tuples[i] = tuples[i].lstrip("(")
    tuples[i] = tuples[i].rstrip(")")
lst = [str(i) for i in tuples]
m = ''.join(lst)
print(int(m))
