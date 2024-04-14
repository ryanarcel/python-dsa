# anagram is when all characters in a string is found in another string

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    str1 = sorted(list(str1))
    str2 = sorted(list(str2))

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
        
    return True


str1 = 'restful'
str2 = 'fluster'

print(is_anagram(str1, str2))