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

#dictionaries
temperatures = [29.8, 23.5, 34.5, 30.5]
student_grades = {"Mpho": 59, "Dineo": 70, "Letlotlo": 90, "Dimpho": 80, "Teboho": 49, "Lerato": 99}

grades_sum = sum(student_grades.values())
grades_sum = sum(student_grades.values())
length = len(student_grades)

#calculating the mean
mean = grades_sum / length
print(mean)

print(grades_sum)
print(student_grades.keys())