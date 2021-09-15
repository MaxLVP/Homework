a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(end="\t")
for row in range(c, d + 1):
    print(row, end="\t")
print()
for column in range(a, b + 1):
    print(column, end='\t')
    for row in range(c, d + 1):
        print(row * column, end="\t")
    print()
