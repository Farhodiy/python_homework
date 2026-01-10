#1st question Number data Type questions
number=float(input("Enter a number: "))
print(round(number,2))
#2nd question
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
print('max number:',max(a,b,c),',min number:',min(a,b,c))
#3rd question
Length=float(input("Enter the length in km: "))
print(f'Length in meters: {Length*1000} m')
print(f'Length in cm: {Length*100000} cm' )
#4th question
my_1st=int(input("Enter first number: "))
my_2nd=int(input("Enter second number: "))
print("Division:", divmod(my_1st,my_2nd))
#5th question
Temperature=float(input("Enter temperature in Celsius: "))
Fahreinheit=(Temperature*9/5)+32
print(f"Temperature in Fahreinheit: {Fahreinheit} F")
#6th question
Number= int(input("Number:"))
last_digit=Number%10
print("Last digit:",last_digit)
#7th question
given_number=int(input("Enter a number: "))
if given_number%2==0:
    print(f"{given_number} is even number")
else:
    print(f"{given_number} is odd number")
# 1st string data type question
import datetime
Name=input('What is your name?')
Year=int(input('What is your birth year?'))
getdate=datetime.datetime.now()
Age=getdate.year-Year
print(f'Your name is {Name} and you are {Age} years old')
2nd question

#3rd question
Sentence=input('Enter somthing:')
print(len(Sentence))
print(Sentence.upper())
print(Sentence.lower())
#4th question
text=input("Enter a string:")
reverse=text[::-1]
if text==reverse:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")
#5th question
Text=input("Enter a string:")
vowels="aeiouAEIOU"
consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vowel_count=0
consonant_count=0
for char in Text:
    if char in vowels:
        vowel_count+=1

for char in Text:
     if char in consonants:
        consonant_count+=1
print("Number of vowels in the string:",vowel_count)
print("Number of consonants in the string:",consonant_count)
#6th question
text=input("Enter a string:")
another_text=input("Enter another string:")
print(another_text in text)
# 7th question
my_str =input('Enter your sentence:')
replace = input("Replace:")
with_word = input('With:')
print(my_str.replace(replace,with_word))
#8th question
str1=input("Enter a string:")
print(f'first character is: {str1[0]} and last character is: {str1[-1]}')
#9th question
str2=input("string:")
reverse_str2=str2[::-1]
print(reverse_str2)
#10th question
sentence=input("Enter a sentence:")
words=sentence.split()
print(len(words))
#11th question
text2=input("Enter a string:")
has_digit=False
for char in text2:
    if char.isdigit():
        has_digit=True
        break
print(has_digit)
#12th question
mystring=input("Enter a string:")
mystrring2=input("Enter a string:")
mystring3=input("Enter a string:")
print(f'{mystring}-{mystrring2}-{mystring3}')
#13th question
given_string=input("Enter a string:")   
print(given_string.replace(' ',''))
#14th question
first_word=input("Enter first word:")
second_word=input("Enter second word:")
if first_word==second_word:
    print("Words are same")
else :
    print("Words are different")
#15th question
name1=input("Enter your string:")
words=name1.split()
l=[word[0].upper() for word in words]
print(''.join(l))
#16th question
s=input("Enter a string:")
character=input("Character that should be removed:")
removed=s.replace(character,'')
print(removed)
#17th question
q=input("Enter a string:")
vowels="aeiouAEIOU"
for char in q:
    if char in vowels:
        q=q.replace(char,'*')
print(q)
#18th question
t=input("Enter your sentence:")
firstword=t.split()[0]
lastword=t.split()[-1]
if firstword!=lastword:
    print("Sentence begins and ends with different words")
else:
    print("Sentence begins and ends with same words")
print(firstword)
print(lastword)
#1st question Boolean data type questions
username=input("Enter your username:")
password=input("Enter your password:")
if username=='' and  password=='':
    print("Login successful")
else:
    print("empty space is not allowed, please try again")
#2nd question
number1=int(input("Enter first number:"))
number2=int(input("Enter second number:"))
if number1==number2:
    print('Genius answer')
else:
    print('Try again')
#3rd question
number=int(input("Enter a number:"))
if number>0 and number%2==0:
    print(f"{number} is positive even number")
else:
    print(f"{number} is not positive even number")
#4th question
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))
if x!=y!=z:
    print("All numbers are different")
else:
    print("Not all numbers are different")
#5th question
k=input("Enter a string:")
m=input("Enter another string:")
if len(k)==len(m):
    print("Same length")
else:
    print("Different length")
# #6th question
numero=int(input("Enter a number: "))
if numero % 5 == 0 and numero % 3 == 0:
    print(f"{numero} is divisible by 3 and 5")
else:
    print(f"{numero} is not divisible by 3 and 5")
#7th question
w=float(input("Enter here:"))
e=float(input("Enter here:"))
if w+e>50.8:
    print("accepted")
else:
    print("not accepted")
if w>=10 and w<=20:
    print(f'{w} is in the range')
else:
    print(f'{w} is out of range')
if e>=10 and e<=20:
    print(f'{e} is in the range')
else:
    print(f'{e} is out of range')