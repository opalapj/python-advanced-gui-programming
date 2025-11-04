# Seems to be easy, but logic is key to success.
def beauty(number):
    number = str(number)
    if "e" not in number and number.find(".") <= 10:
        number = number[:10]
        if "." in number:
            number = number.rstrip("0")
            if number[-1] == ".":
                return number[:-1]
            else:
                return number
        else:
            return number
    else:
        return ERROR


# Edube's solution, incorrect.
# def beauty(number):
#     number = str(number)
#     if 'e' in number:
#         return ERROR
#     if '.' in number:
#         while number[-1] == '0':
#             number = number[0:-1]
#     while len(number) > 10 and number[-1] != '.':
#         number = number[0:-1]
#     if number[-1] == '.':
#         number = number[0:-1]
#     if len(number) > 10:
#         return ERROR
#     return number


# '10' in 3. and 4. lines is width of display. Can be written as variable.
ERROR = "Error"
test_set = [
    12345678900.00001,
    1234567890.000001,
    123456780.0000001,
    12345670.00000001,
    1234560.000000001,
    123450.0000000001,
    12340.00000000001,
    1230.000000000001,
    120.0000000000001,
    10.00000000000001,
    0.000000000000001,
    12345678900.10001,
    1234567890.100001,
    123456780.1000001,
    12345670.10000001,
    1234560.100000001,
    123450.1000000001,
    12340.10000000001,
    1230.100000000001,
    120.1000000000001,
    10.10000000000001,
    0.100000000000001,
    12345678901.00001,
    1234567891.000001,
    123456781.0000001,
    12345671.00000001,
    1234561.000000001,
    123451.0000000001,
    12341.00000000001,
    1231.000000000001,
    121.0000000000001,
    11.00000000000001,
    1.000000000000001,
    12345678901.10001,
    1234567891.100001,
    123456781.1000001,
    12345671.10000001,
    1234561.100000001,
    123451.1000000001,
    12341.10000000001,
    1231.100000000001,
    121.1000000000001,
    11.10000000000001,
    1.100000000000001,
]
for n in test_set:
    print(beauty(n))
