# loops

names = ["ridoy", "joy", "rafi", "rabbi"]

for name in names:
    print(name)


student_marks = [33, 42, 55, 12, 23, 52, 65, 37, 29, 60]

total = 0

for i in student_marks:
    total += i

print(total)

total_using_function = sum(student_marks)
print(total_using_function)


max_mark = 0
for i in student_marks:
    if i > max_mark:
        max_mark = i

print(max_mark)


# range
sum = 0
for i in range(1, 101):
    sum += i
print(sum)