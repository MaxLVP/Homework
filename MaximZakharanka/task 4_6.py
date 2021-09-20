def get_longest_word(s:str):
    words = s.split()
    print(max(words, key=len))
get_longest_word('Any pythonista like namespaces a lot.')
