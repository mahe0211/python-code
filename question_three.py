# 3. Programming Challenge Description:
# Write 4 functions based on the following requirements
# a. Write a function that accepts an integer and returns True if the input is between
# 4 and 10, inclusive; otherwise, return False
# b. Write a function to test if a list contains any items. Return 'EMPTY' if it does not
# contain any items and 'NOT EMPTY' if it does.
# c. Write a function that accepts a file name and a string and writes the string to the
# file with the given file name.
# d. Write a function that accepts a list and doubles each value in the list. When no
# input parameter is provided, return an empty list.
# Input:
# N/A
# Output:
# N/A


def test_int_range(num):
    """
    Function to check number lies between 4 and 11 inclusive
    :param int num: number to test
    :return bool: return True or False
    """
    if num in range(4, 11):
        return True
    else:
        return False


print(test_int_range(4))


def test_list(arr):
    """
    Function to test given list is empty or not
    :param list arr: given list to test
    :return str: EMPTY or NOT EMPTY
    """
    if not arr:
        return "EMPTY"
    else:
        return "NOT EMPTY"


print(test_list([1]))
print(test_list([]))


def file_io(file, text):
    """
    Function to write given string along with given file name
    :param file: file name
    :param str text: text to write
    :return:
    """
    with open(file, 'w') as f_obj:
        f_obj.write(file + ' ' + text)


file_io('python.txt', 'Hello')


def doubles_elem(arr=None):
    """
    Function to multiply each element of list by 2
    :param list arr:
    :return list: list multiplied by 2
    """
    res = []
    if arr:
        for i in arr:
            res.append(2*i)
    return res


print(doubles_elem([1, 2, 3, 4, 5]))
print(doubles_elem())
