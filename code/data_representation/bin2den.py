def bin2den(num):
    result = 0
    num = num[::-1]
    for idx, i in enumerate(num):
        if i == "1":
            result += 2**idx
    return result

print(bin2den("10001011110011111110010011100111"))