# # Zero Check Decorator

# def check(func):
#     def checker(a,b):
#         if b!=0:
#             return func(a,b)
#         else:
#             return "Dominator can't be zero"

#     return checker

# @check
# def div(a,b):
#     return a/b
# print(div(6,0))

# # Employee Records Manager

# status=True
# while status:
#     option=int(input("""
#     1. Add new employee record
#     2. View all employee records
#     3. Search for an employee by Employee ID
#     4. Update an employee's information
#     5. Delete an employee record
#     6. Exit
#     Enter your option:
#     """))
#     file_path = "/home/farhod/Farhod/python_homework/lesson-6/homework,py/employees.txt"
#     if option==1:
#         appending = input("Format (Employee ID, Name, Position, Salary): ")
#         try:
#                 with open(file_path, "a") as file:
#                         file.write(f'{appending}\n')
#         except Exception:
#                 print('Format is wrong')

#     elif option==2:
#         with open(file_path, "r") as file:
#             print(file.read())
#     elif option==3:
#         try:
#             empid = input("Employee's ID: ").strip()
#         except Exception:
#             print("ID should be a number")
#         else:
#             with open(file_path, "r") as file:
#                 for line in file:
#                     parts = line.strip().split(",")
#                     if parts[0] == empid:
#                         print(line)
#                         break
#                 else:
#                     print("Employee not found")
#     elif option==4:
#         try:
#             empid = input("Employee's ID: ").strip()
#         except Exception:
#             print("ID should be a number")
#         else:
#                 updated=False
#                 new_lines=[]
#                 with open(file_path, "r") as file:
#                         for line in file:
#                             parts = line.strip().split(",")
#                             if parts[0] == empid:
#                                 print("Current status: ", line.strip())
#                                 name=input('Employee\'s name: ')
#                                 job=input('Employee\'s position: ')
#                                 salati=input('Employee\'s salary: ')
#                                 new_line=f'{empid}, {name}, {job}, {salati}\n'
#                                 new_lines.append(new_line)
#                                 updated=True
#                             else:
#                                 new_lines.append(line)
#                 if updated:
#                             with open(file_path, "w") as file:
#                                 file.writelines(new_lines)
#                                 print("Employee record updated successfully.")
#                 else:
#                     print('Employee not found')
#     elif option==5:
#         try:
#             empid = input("Employee's ID: ").strip()
#         except Exception:
#             print("ID should be a number")
#         else:
#                 updated=False
#                 new_lines=[]
#                 with open(file_path, "r") as file:
#                         for line in file:
#                             parts = line.strip().split(",")
#                             if parts[0] == empid:
#                                 print("Current status: removed successfuly")
#                                 updated=True
#                             else:
#                                 new_lines.append(line)
#                 if updated:
#                             with open(file_path, "w") as file:
#                                 file.writelines(new_lines)
#                                 print("Employee record updated successfully.")
#                 else:
#                     print('Employee not found')

#     elif option==6:
#          print('You exited')
#          status=False
#          break
#     else:
#          print('Wrong option is selected')
         
     

# Word Frequency Counter
# File names
filename = "sample.txt"
report_file = "word_count_report.txt"

#  Checks if file exists, if not creates it
try:
    file = open(filename, "r")
    file.close()
except FileNotFoundError:
    text = input("sample.txt not found. Please enter a paragraph:\n")
    file = open(filename, "w")
    file.write(text)
    file.close()

# Asks user how many top words to display 
try:
    top_n = int(input("How many top common words to display? "))
except:
    top_n = 5

# Reads file content
file = open(filename, "r")
text = file.read().lower()
file.close()

# Removes punctuation manually
punctuation = ".,!?;:\"'()[]{}-_"
clean_text = ""

for char in text:
    if char not in punctuation:
        clean_text += char

#  Splits into words
words = clean_text.split()
total_words = len(words)

#  Counts word frequency
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

#  Sorts words by frequency (descending)
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# Displays output
print(f"\nTotal words: {total_words}")
print(f"Top {top_n} most common words:")

for i in range(min(top_n, len(sorted_words))):
    word, count = sorted_words[i]
    times = "time" if count == 1 else "times"
    print(f"{word} - {count} {times}")

#  Saves report to file
file = open(report_file, "w")
file.write("Word Count Report\n")
file.write(f"Total Words: {total_words}\n")
file.write(f"Top {top_n} Words:\n")

for i in range(min(top_n, len(sorted_words))):
    word, count = sorted_words[i]
    file.write(f"{word} - {count}\n")

file.close()

print(f"\nReport saved to '{report_file}'")




        
