# pick a random name from the list of friends

import random

people = ["ridoy", "joy", "rafi", "rabbi", "nafi", "zawad"]

a = random.randint(0, len(people) - 1)
print(people[a])


# another way
print(random.choice(people))

