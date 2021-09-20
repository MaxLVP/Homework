def check_palyndrom(s:str):
    s = s.lower()
    s = s.split()
    s = ''.join(s)
    print(s)
    if s == s[::-1]:
        return True
    else:
        return False


check_palyndrom(input())
