def remember_result(func):
    result = []
    def warpper(a,b):
        value = func(a,b)
        if len(result) > 0:
            return(result[0])
        else:
            result.append(value)
            return(result[0])
    return warpper

@remember_result
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(3, 4))
print(sum_of_numbers(13, 42))
print(sum_of_numbers(134, 412))
