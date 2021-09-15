text = input().lower()
result = {}
for letter in text:
    result[letter] = result.get(letter, 0) + 1
print(result)
