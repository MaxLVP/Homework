def split_by_index(s, indexes: list):
    start = 0
    splitted_string = []
    for end in indexes:
        if end == 0:
            start = end
        else:
            splitted_string.append(s[start:end])
            start = end
    if end <= len(s):
        splitted_string.append(s[end:])
    return(print(splitted_string))

split_by_index('long string that I want to split up', indexes = [0,5,12,17,82])
