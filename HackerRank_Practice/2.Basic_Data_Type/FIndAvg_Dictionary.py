if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks.get(query_name)
    avg = sum(query_scores)/len(query_scores)
    print("{0:.2f}".format(avg))
