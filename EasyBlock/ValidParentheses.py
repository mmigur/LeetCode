def isValid(s):
        stack = []
        brackets_dict = {
                '(': ')',
                '{': '}',
                '[': ']'
        }

        for char in s:
                if char in brackets_dict:
                        stack.append(char)
                elif not stack or brackets_dict[stack.pop()] != char:
                        return False

        return len(stack) == 0