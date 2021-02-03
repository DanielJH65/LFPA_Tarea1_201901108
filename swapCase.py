def swap_case(s):
    resultado=''
    for _ in range(len(s)):
        if(s[_].isupper()):
            resultado+=(s[_].lower())
        else:
            resultado+=(s[_].upper())
    return resultado

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)