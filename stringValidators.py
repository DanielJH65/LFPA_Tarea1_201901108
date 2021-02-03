if __name__ == '__main__':
    s = input()
    s = list(s)
    num = False
    word = False
    digit = False
    lower = False
    upper = False
    for _ in s:
        if(_.isalnum()):
            num = True
        if(_.isalpha()):
            word = True
        if(_.isdigit()):
            digit = True
        if(_.islower()):
            lower = True
        if(_.isupper()):
            upper = True
    print(num)
    print(word)
    print(digit)
    print(lower)
    print(upper)