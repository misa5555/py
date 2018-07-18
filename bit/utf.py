def streamValidation(stream):
    # check the lengh of byte

    first = stream[0]
    k = 2 ** 7
    bytes = 0
    while first & k != 0:
        bytes += 1
        first <<= 1

    for i in range(bytes):
        if stream[i] & k == 0:
            return False
    return True

# print(streamValidation([197, 130, 1]))
print(streamValidation([145]))


def simplifyRational(numerator, denominator):
    diff = denominator - numerator
    is_negative_1 = False
    is_negative_2 = False

    if numerator < 0:
        is_negative_1 = True
        numerator = -1 * numerator
    if denominator < 0:
        is_negative_2 = True
        denominator = -1 * denominator

    while diff > 1 and (numerator % diff == 0 and denominator % diff == 0):
        numerator //= diff
        denominator //= diff
        diff = denominator - numerator

    if is_negative_1 ^ is_negative_2:
        numerator = -1 * abs(numerator)
        denominator = abs(denominator)

    if is_negative_1 and is_negative_2:
        denominator = -1 * (denominator)
        numerator = -1 * (numerator)

    return (numerator, denominator)
# simplifyRational(8, -5)


def simplifyRational(numerator, denominator):
    numerator_negative = False
    if (numerator < 0) ^ (denominator < 0):
        numerator_negative = True
    n1, n2 = sorted([abs(numerator), abs(denominator)])

    diff = n2 - n1

    while diff > 0:
        n2 = max(diff, n1)
        n1 = min(diff, n1)
        diff = n2 - n1

    if numerator_negative:
        numerator = -1 * abs(numerator)
        denominator = abs(denominator)
    return [numerator // n1, denominator // n1]
# print(simplifyRational(5235, 1495))
# print(simplifyRational(8, -5))
print(simplifyRational(239, 239))