height = float(input("Height(cm)?"))
weight = float(input("Weight(kg)?"))
height = height/100
BMI = weight/(height**2)
if BMI < 16:
    print("severaly underweight")
elif BMI > 16 and BMI < 18.5:
    print("Underweight")
elif BMI > 18.5 and BMI < 25:
    print("Normal ")
elif BMI > 25 and BMI < 30:
    print("Overweight ")
else:
    print("Obese")