def romanToInt(s):
        s = s.replace("IV", "IIII") \
        .replace("IX", "VIIII") \
        .replace("XL", "XXXX") \
        .replace("XC", "LXXXX") \
        .replace("CD", "CCCC") \
        .replace("CM", "DCCCC")

        result = 0
        data = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(len(s)):
                for j in data:
                        if s[i] == j:
                                result += data[j]
        return result

print('XXX')