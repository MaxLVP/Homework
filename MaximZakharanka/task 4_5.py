def get_digits(num: int):
    num = str(num)
    digits = []
    for i in num:
        digits.append(int(i))
            
    return(print(tuple(digits)))
    

get_digits(int(input()))
