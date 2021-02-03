if __name__ == '__main__':
    N = int(input())
    lista=[]
    for _ in range(N):
        a = input().split()
        if(a[0]=='append'):
            lista.append(int(a[1]))
        elif(a[0]=='print'):
            print(lista)
        elif(a[0]=='insert'):
            lista.insert(int(a[1]),int(a[2]))
        elif(a[0]=='remove'):
            lista.remove(int(a[1]))
        elif(a[0]=='sort'):
            lista.sort()
        elif(a[0]=='pop'):
            lista.pop()
        elif(a[0]=='reverse'):
            lista.reverse()