
numero = int(input(">"))
score = []

for i in range(1,numero):
    grade = int(input(f"Grade {i}:"))
    score.append(grade)
score.sort()
max = 0
max2 = 0
score2 = []
for x in score:
    if x > max:
        max = x
for z in score:
    if z != max:
        score2.append(z)
        for z in score2:
            if z > max2:
             max2 = z

print(max2)
print(score2)
print(score)
print(max)