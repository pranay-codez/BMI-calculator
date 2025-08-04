#SIMPLE BMI CALCULATOR

age=int(input("enter you age:"))#ages=>2-120
weight=int(input("enter your weight:"))#in kgs
height=int(input("enter your height:"))#in meter

BMI=((weight)/(height**2))*10000

print(BMI)

if(BMI<16):
    print("you are morbidly underweight")
elif(BMI<=17 and BMI>=16):
    print("you are underweight")
elif(BMI<=18.5 and BMI>17):
    print("slightly underweight")
elif(BMI<=25 and BMI>18.5):
    print("you are at normal weight")
elif(BMI<=30 and BMI>25):
    print("you are overweight")
else:
    print("you are morbidly overweight")

"BMI for adults"
# Severe Thinness   < 16     risk=high risk
# Moderate Thinness	16 - 17  risk=icreased
# Mild Thinness	   17 - 18.5 risk=minimal
# Normal	       18.5 - 25 risk=healthy
# Overweight	    25 - 30  risk=increased
# Obese 	         > 30    risk=high risk

 