words = input().split(', ')
for i in range(len(words)):
    words[i] = words[i].lstrip("['")
    words[i] = words[i].rstrip("']")
result = []
for i in words:
    if i not in result:
        result.append(i)
result.sort()
print(result)
