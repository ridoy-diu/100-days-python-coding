# Body Mass Index Calculator in metric  units

weight = float(input("what is your weight in kg?\n"))
height = float(input("what is your height in m?\n"))

bmi = weight / height**2

print("your BMI is " + str(round(bmi, 1)))

if bmi < 18.5:
    print("Condition: Underweight")
elif bmi < 25: 
    print("Condition: Healthy weight")
elif bmi < 30:
    print("Condition: Overweight")
elif bmi < 40:
    print("Condition: Obese")
else: 
    print("Condition: Severely Obese")


# BMI range for Men
# Under 18.5      : Underweight
# 18.5–24.9       : Healthy weight
# 25.0–29.9       : Overweight
# 30.0 or greater : Obese
# 40 or above     : Severely obese