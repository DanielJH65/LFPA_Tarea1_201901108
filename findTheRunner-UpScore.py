if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(list(arr))
    i=len(arr)-1
    while(arr[i]==arr[i-1]):
        i-=1
    print(arr[i-1])