# Write a function that accepts two arbitrary strings and returns a new string
# containing only the unique characters present in both inputs.
# Input:
# The function must accept two string parameters.
# Output:
# The function must return a string.


def unique_chars(str1, str2):
    """
    Function to return string containing unique and common chars in both strings
    :param str str1: string 1
    :param str str2: string 2
    :return str: string which contain unique and common chars
    """
    chars = []
    for ch in str1:
        if ch in str2 and ch not in chars:
            chars.append(ch)
    return ''.join(chars)


print(unique_chars('112345', '12345'))



