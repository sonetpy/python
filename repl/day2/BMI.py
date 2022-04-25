# BMI index | under weight > 25 | 25 <= over weight > 30 | obes =>30
height = float(input("enter your height: "))
weight = float(input("enter your weight: "))
bmi = float(weight / (height * height))
print(bmi)
if bmi < 25.0:
    print ("under weight")
elif (bmi >= 25.0 and bmi <= 30.0):
    print("over weight")
else:
    print("Obes")