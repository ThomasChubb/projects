#Thomas Chubb
#11/27/2022
#A health calc that calcualtes bmi and the heart rate intesity#
import sys
print(f'Please enter the following values for the user...')

try:
    height = int(input('Height in inches: '))
    weight = int(input('Weight in pounds: '))
    age = int(input('Current age: '))
    heart = int(input('Resting heart rate: '))

except:
    print(f'A numeric value must be input')
    sys.exit(1)

def calc_bmi(height, weight):
    kilograms = (weight / 2.205)
    meters1 = (height / 39.37)
    meters2 = (meters1 ** 2)
    bmi = (kilograms / meters2)
    return bmi


bmi = calc_bmi(height, weight)
bmi_rnd = round(bmi,2)

if bmi <= 18.5:
    bmistatus = 'underweight'
elif bmi > 18.5 and bmi < 25:
    bmistatus = 'normal weight'
elif bmi >= 25 and bmi < 29.9:
    bmistatus = 'overweight'
else:
    bmistatus = 'Obese'

print(f'Your BMI is: {bmi_rnd} you are {bmistatus}')
print(f'Excerise Intesnity Heart Rates:')
print(f'Intensity\t\tMax Heart Rate')

def calc_heartrate(age,heart):
    mhr = 220 - int(age)
    hrr = mhr - int(heart)
    for tr in range(50,100,5):

        mtz = (hrr * tr)/100
        ttz = int(mtz + (heart))
        print (f'{tr}%\t\t\t\t{ttz}')


calc_heartrate(age,heart)


