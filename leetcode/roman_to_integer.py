
def convert_to_int(l):
    if l == 'I': return 1
    elif l == 'V': return 5
    elif l == 'X': return 10
    elif l == 'L': return 50
    elif l == 'C': return 100
    elif l == 'D': return 500
    elif l == 'M': return 1000


def romanToInt(s):
    result = 0
    for i in range(len(s)):
        current_value = convert_to_int(s[i])
        if i+1 < len(s) and current_value < convert_to_int(s[i+1]):
            result -= current_value
        else:
            result += current_value
    return result


print(romanToInt(('III')))
print(romanToInt(('MCMXCIV')))

