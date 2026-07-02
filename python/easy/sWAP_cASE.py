# Problem: Swap Case
# Link: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
# Descrição: Converter letras maiúsculas em minúsculas e vice-versa.

def swap_case(s):
    modified = []

    for i in s:
        if i == i.lower():
            modified.append(i.upper())
        else:
            modified.append(i.lower())

    return "".join(modified)

    #return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)