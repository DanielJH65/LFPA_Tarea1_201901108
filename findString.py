def count_substring(string, sub_string):
    contador=0
    for _ in range(len(string)):
        if(_<len(string)-2):
            if string[_:len(sub_string)+_] == sub_string:
                contador+=1
    return contador

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)