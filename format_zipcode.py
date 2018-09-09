def format_zipcode(zip_code):
    """
    Function to format zip code based on length
    :param str zip_code: zip code
    :return: result of function
    :rtype: str
    """
    # return zip code in right aligned format if length is less than or equals to 5
    if len(zip_code) <= 5:
        return '{:>5}'.format(zip_code)

    # retun the zip code by converting into string if length equals to 10
    if len(zip_code) == 10:
        return str(zip_code)
    # return the zip code separated by '-' if length equals to 9
    if len(zip_code) == 9:
        return '{}-{}'.format(zip_code[:5], zip_code[5:])


print(format_zipcode('12345'))
print(format_zipcode('1234567890'))
print(format_zipcode('123456789'))
print(format_zipcode('1234'))
