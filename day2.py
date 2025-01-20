# subscripting -> pulling out a particular element from a string
print("hello world"[-1]) #-1 last character in the string   

print("1" + "2")

print(122_234_838) # large Integers

print(type("messi"))
print(type(True))

# integer to string
print(str(123) + str(456))
# string to integer
print(int("12") + int("8"))


# Type error if you don't use str()
# concatenate str to str
print("Number of letters in your name: " + str(len(input("your name? "))))
   
print(5/3) #float
print(5//3) #int
print(2*3) 
print(2**3) #power ^



# PEMDAS
# parentheses, exponents, multiplication/division, addition/substraction
print(3*3+3//3-3)


# f string
name = "messi"
age = 38
goat = True
print(f"name = {name}, age = {age}, GOAT = {goat}")
