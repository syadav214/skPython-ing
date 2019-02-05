stu = []
score_set = set()
for _ in range(int(input())):
        name = input()
        score = float(input())
        score_set.add(score)
        stu.append([name,score])
stu.sort()
low = min(score_set)
score_set.remove(low)
second_lowest = min(score_set)

for singleStu in stu:
    if(singleStu[1]==second_lowest):
        print(singleStu[0])

