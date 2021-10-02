import string
class Cipher():
    
    def __init__(self, keyword):
        self.keyword = keyword
        
        
    def encode(self, en_string):
        end_string = ""
        crypto_ls = [i for i in self.keyword]
        alphabit_wo_key = [i for i in string.ascii_lowercase if i not in self.keyword]
        crypto_ls.extend(alphabit_wo_key)
        for i in range(len(en_string)):
            if en_string[i] not in '.\/[]{}()=-.,;:\'"1234567890~!`@#$%^&*<>?|=+_- ':
                if en_string[i].isupper():
                    letter = string.ascii_lowercase.find(en_string[i].lower())
                    end_string += crypto_ls[letter].upper()
                else:
                    letter = string.ascii_lowercase.find(en_string[i].lower())
                    end_string += crypto_ls[letter]
            else:
                end_string += en_string[i]
        
        return end_string
        
        
    def decode(self, dec_string):
        end_string = ""
        crypto_ls = [i for i in self.keyword]
        alphabit_wo_key = [i for i in string.ascii_lowercase if i not in self.keyword]
        crypto_ls.extend(alphabit_wo_key)
        for i in range(len(dec_string)):
            if dec_string[i] not in '.\/[]{}()=-.,;:\'"1234567890~!`@#$%^&*<>?|=+_- ':
                if dec_string[i].isupper():
                    letter = crypto_ls.index(dec_string[i].lower())
                    end_string += string.ascii_lowercase[letter].upper()
                else:
                    letter = crypto_ls.index(dec_string[i].lower())
                    end_string += string.ascii_lowercase[letter]
            else:
                end_string += dec_string[i]
        
        return end_string

cipher = Cipher("crypto")
print(cipher.encode("Hello world"))
print(cipher.decode("Fjedhc dn atidsn"))
