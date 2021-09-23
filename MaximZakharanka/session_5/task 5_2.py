import re
def most_common_words(filepath, number_of_words=3):
    result = {}
    words = []
    with open(filepath) as file:
        for line in file.readlines():
            words.extend(re.findall(r'\w+', line.lower()))
    for word in words:
        result[word] = result.get(word, 0) +1
        list_res = list(result.items())
        list_res.sort(key=lambda i: i[1], reverse = True)
        list_result = [i[0] for i in list_res]
    print(list_result[:number_of_words])


most_common_words('data/lorem_ipsum.txt',6)

