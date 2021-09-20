def get_pairs(lst: list):
    result = []
    if len(lst) > 1:
        for i in range(len(lst[:-1])):
            s = (lst[i], lst[i+1])
            result.append(s)
        return print(result)
    else:
        return None


get_pairs([1,2])
