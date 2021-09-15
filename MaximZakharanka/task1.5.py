lst = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, \
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
result = []
for i in lst:
    for value in i.values():
        if value not in result:
            result.append(value)
print(result)
