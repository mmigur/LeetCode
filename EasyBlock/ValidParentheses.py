def isValid(s):
        stack = []

        for i in s:
                if i not in ')]}':
                        stack.append(i)
                elif stack:
                        x = stack.pop()
                        if (x == '(' and i != ')') or (x == '[' and i != ']') or (x == '{' and i != '}'):
                                return False
                else:
                        return False

        return False if stack else True

print(isValid('{}{}{}{}'))
print(isValid('{{{}'))