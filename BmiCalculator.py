# BMI Calculator

print ("Welcome to the BMI Calculator.")
h=float(input("What is your height in metres? "))
w=float(input("What is your weight in kg? "))
bmi= w/(h**2)
print("Your BMI is",bmi)
if bmi<18.5:
  print("You are underweight. Please increase the nutrient level in your diet.")
elif 18.5<bmi<25:
  print ("You have a normal weight.")
elif 25<bmi<30:
  print ("Congratulations, You have a normal weight.")
elif 25<bmi<30:
  print("You are overweight. Please maintain your diet plan and increase the amount of fibre intake in your diet.")
elif 30<bmi<35:
  print("You are obese.")
else:
  print ("You are clinically obese")