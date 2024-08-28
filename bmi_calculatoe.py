height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = weight/ height**2  

if bmi < 18.5:  # false
  print("You are under weight")

elif bmi < 25: #  bmi 45
  print("Your weight is normal")

elif bmi <30:
  print("You are over weight")

elif bmi <35:
  print("You are obese")

else:
  print("You are clinically obese")