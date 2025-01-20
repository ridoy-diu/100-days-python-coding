import random
random_value = random.randint(1,10)
print(random_value)
# random_value = random.randbytes(4)
# print(random_value)

#module
# import TEST


val = random.random() # a <= N < b
print(round(val,3))
# random.uniform(a, b) # a <= N <= b


# print heads or tails
a = random.randint(0, 1)
if a == 0:
    print("Heads")
else: 
    print("Tails")


#list
name_of_people = ["ridoy", "joy", "rafi", "rabbi"]
print(name_of_people[1])
name_of_people.append("hasanul")
print(name_of_people)
name_of_people.insert(2, "nobody")
print(name_of_people)

# nested list
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])

print(dirty_dozen[1][1])