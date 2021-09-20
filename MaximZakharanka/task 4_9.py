strings = ["hello", "world", "python", ]

def test_1_1(*ls):
	result = set()
	for i in string.ascii_lowercase:
        	number = 0
        	for el in ls:
            	if i in el.lower():
                	number += 1
        	if number == len(ls):
            		result.add(i)
	return result


def test_1_2(*args):
    chrs = list(set(''.join(args)))
    chrs.sort()
    return (chrs)


def test_1_3(*ls):
	result = set()
	for i in string.ascii_lowercase:
        	number = 0
        	for el in ls:
            	if i in el.lower():
                	number += 1
        	if number >= 2:
            		result.add(i)

	return result


def test_1_4(*args):
	    chrs = (''.join(args))
	    chrs_nu = []
	    for i in string.ascii_lowercase:
		    if i not in chrs:
			    chrs_nu.append(i)
	    chrs_nu.sort()
	    return(chrs_nu)
