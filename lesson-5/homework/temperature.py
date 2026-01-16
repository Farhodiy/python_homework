# Task 1
def convert_cel_to_far(cel):
    ''' Converts degree in Celcius to degree in Fahrenheit'''
    return round(cel*9/5+32,2)
def convert_far_to_cel(far):
    '''Converts degree in Fahrenheit to degree in Celcius'''
    return round((far-32)*5/9,2)
cels=float(input('Enter temperature in degrees C: '))
print(convert_cel_to_far(cels))

fahr=float(input('Enter temperature in degrees F: '))
print(convert_far_to_cel(fahr))
