#Get user's height and weight input.
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

#Code to determine BMI
bmi = weight / height ** 2
bmi_rounded = round(bmi)

#Given parameters in Chart in ReadMe determine if BMI is underweight, normal weight, overweaight, obese
if bmi <= 18.5:
    bmi_interpretation = "you are underweight"
elif bmi is between 18.5 and 25:
    bmi_interpretation = "your weight is in a normal range"
elif bmi is between 25 and 30:
    
else:
    bmi_interpretation = "you are clinically obese"

#Display output
displayMessage = f"Your BMI is {bmi_rounded}"
print(displayMessage)