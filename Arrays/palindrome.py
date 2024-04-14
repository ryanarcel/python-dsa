# write a palindrome

def reverse(str):

    # convert string into a list of characters
    str = list(str)

    start_index = 0
    end_index = len(str) - 1

    while end_index > start_index:
        #keep swapping the items
        str[start_index], str[end_index] = str[end_index], str[start_index]
        start_index += 1
        end_index -= 1

    # converts list into string
    return ''.join(str)

def is_palindrome(str):
    if str == reverse(str):
        return True
    else:
        return False
    
print(is_palindrome("cac"))