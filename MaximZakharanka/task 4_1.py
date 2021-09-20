def replace_symbols(s):
    for i in range(len(s)):
        if s[i] =='"':
            s= s[0:i] + "'" + s[i+1:]
        elif s[i] == "'":
            s= s[0:i] + '"' + s[i+1:]
    return(print(s))
replace_symbols('Привет "я" пр\'и\'шел')
