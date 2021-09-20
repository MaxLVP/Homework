def combine_dicts(*args):
    result = {}
    for dictionary in args:
        for k,v in dictionary.items():
            result[k] = result.get(k,0) + v
    return result
