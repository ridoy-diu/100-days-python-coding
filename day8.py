# def greet(name):
#     print("hello", name) # , adds a space but + adds no space
#     print(f"how do you do {name}" + "?") 

# greet("ridoy")
# greet('joy')  # "" and '' both can be used
# greet(input("what is your name?\n"))

def life_in_weeks(age):
        remaining_age = 90 - age
        weeks = remaining_age * (365//7)
        print(f"You have {weeks} weeks left.")


age = int(input("What is your current age?\n"))
life_in_weeks(age)