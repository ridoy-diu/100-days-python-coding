# # dictionary

# name_age_dictionary = {"ridoy": 23, "joy": 25}

# print(name_age_dictionary["ridoy"])

# name_age_dictionary["rafi"] = 24
# print(name_age_dictionary)

# for key in name_age_dictionary:
#     print(key, name_age_dictionary[key])


# Grading Problem

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    score = student_scores[key]
    if score >= 91:
        student_grades[key] = "Outstanding"
    elif score >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"


print(student_scores)
print(student_grades)

# [] list
# {} dictionary

# nested list, dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Bangladesh": ["Dhaka", "Rajshahi", "Sylhet"]
}

print(travel_log["France"][1])

nested_list = [1, 2, [3, 4]]
print(nested_list[2][1])