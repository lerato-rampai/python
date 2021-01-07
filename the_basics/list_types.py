members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]
student_grades = [59, 70, 90, 80, 49, 99]
print("Lists represent arrays of values that may change during the course of the program:")
print(members, pixel_values, student_grades)


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
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}
print("Dictionaries represent pairs of keys and values:")
print(phone_numbers, volcano_elevations)
print("")
print("Keys of a dictionary can be extracted with:")
print(phone_numbers.keys())

print("Values of a dictionary can be extracted with:")
print(phone_numbers.values())

#calculating the mean
mean = grades_sum / length
print(mean)

print(grades_sum)
print(student_grades.keys())

#tuple list types
mon_temperatures = (-1, 5, 9)
print(mon_temperatures)
print("Tuples represent arrays of values that are not to be changed during the course of the program:")

vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(vowels, one_digits)