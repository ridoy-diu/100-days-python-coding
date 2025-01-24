# def calculate_love_score(name1, name2):
#     combined_name = (name1 + name2).lower()
#     t = combined_name.count("t")
#     r = combined_name.count("r")
#     u = combined_name.count("u")
#     e = combined_name.count("e")
#     l = combined_name.count("l")
#     o = combined_name.count("o")
#     v = combined_name.count("v")

#     true = t+r+u+e
#     love = l+o+v+e

#     print(str(true)+str(love))

# calculate_love_score("Kanye West", "Kim Kardashian")



# my way ---------------------------
def calculate_love_score(name1, name2):
    count1=count2=0

    combined_name = name1+name2

    for x in combined_name:
        if x in "true":
            count1+=1

    for y in combined_name:
        if y in "love":
            count2+=1

    love_score = str(count1)+str(count2)
    print(love_score)

calculate_love_score("Kanye West", "Kim Kardashian")