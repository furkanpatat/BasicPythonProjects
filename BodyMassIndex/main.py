"""
Calculate the body mass index according to the height
 and weight values obtained from the user
and print the following text on the screen according to these rules.

If BMI is below 18.5 -------> Underweight

If BMI is between 18.5 and 25 ------> Normal

If BMI is between 25 and 30 --------> Overweight

If BMI is over 30 -------------> Obese
"""

height = float(input("Enter your height in meters (Ex: 1.83): "))
weigh = int(input("Enter your weight (Ex: 83): "))

bmi = weigh / (height ** 2)

if(bmi < 18.5):
    print("BMI: ",bmi, " Underweight")
elif(bmi>= 18.5 and bmi<25):
    print("BMI ",bmi," Normal")
elif(bmi>=25 and bmi<30):
    print("BMI:",bmi," Overweight")
else:
    print("BMI: ",bmi," Obese")


