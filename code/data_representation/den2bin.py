def den2bin(num):
    result = ""
    while num != 0:
        remainder = num % 2
        num //= 2
        result = str(remainder) + result
    if result == "":
        return 0
    return result

print(den2bin(2345657575))