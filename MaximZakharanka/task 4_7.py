def foo(integers: list):
    result = []
    for i in integers:
        mult = 1
        for j in integers:
            if i != j:
                mult*=j
        result.append(mult)
    print(result)


foo([120, 60, 40, 30, 24])
