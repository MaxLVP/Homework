def my_split(s, m=" "):
    list_split = []
    c = 0
    for i in range(len(s)):
        if s[i] == m:
            list_split.append(s[c:i])
            c = i+1
    list_split.append(s[c:])
    return(print(list_split))
my_split('Привет я : пришел', m = ':')
