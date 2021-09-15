d = {'a': 10, 'd': 25, 'c': 4, 'b': 15}
def sort_dict(d):
    d2 = {}
    list_keys = list(d.keys())
    list_keys.sort()
    for i in list_keys:
        d2[i] = d[i]
    d = d2
    return d
print(sort_dict(d))
