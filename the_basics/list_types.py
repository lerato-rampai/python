student_grades = [59, 70, 90, 80, 49, 99]

#creating a range
list(range(2, 10))

#You can also specify a step as a third argument:
list(range(1, 10, 2))

#calculating the sum of the grades
grades_sum = sum(student_grades)
length = len(student_grades)

#calculating the mean
mean = grades_sum / length
print(mean)
