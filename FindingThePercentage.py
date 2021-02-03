if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    i=0
    suma=0
    for _ in range(len(student_marks[query_name])):
        suma+= student_marks[query_name][_]
        i+=1
    promedio = suma/i
    print("{:0.2f}".format(promedio))