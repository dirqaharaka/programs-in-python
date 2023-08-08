def bmi_calculator():
    height = float(input("Enter your height in meters :"))
    weight = float(input("Enter your weight in meters :"))

    bmi = weight / (height ** 2)
    print(f"Your BMI is : {bmi}")


bmi_calculator()

