print('Welcome. Lets find your BMI')

weight = input('Please enter your weight in kgs.   ')
height = input('Please enter your height in meters   ')

newWeight = float(weight)
newHeight = float(height)

def bmi_function():
    bmi = round(newWeight/(newHeight*newHeight)*10000)
    if bmi <= 18.5:
        print("you are underweight, please eat well") 
    elif bmi >18.6 and bmi < 24.8:
        print('You are healthy')
    elif bmi >24.9 and bmi < 29.9 :
        print('Overweight. control your diet')
    elif bmi >= 30.0:
        print('Obese, control your food and start working out')
    print(bmi)


bmi_function()