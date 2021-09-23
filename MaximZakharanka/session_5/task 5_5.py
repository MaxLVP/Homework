def remember_result(func):
    result = ['None']
    def warpper(*args):
        print(f"Last result = '{result[-1]}'")
        value = func(*args)
        result.append(value)
    return warpper
        
@remember_result
def sum_list(*args):
    result = ""
    sum = 0
    for item in args:
        if type(item) == int:
            sum += item
        else:
            result += item
    if result == '' and sum > 0:
        result = sum
    print(f"Current result = '{result}'")
    return result
    
sum_list("a", "b")
sum_list("abc", "cde")
sum_list(3, 4, 5)
