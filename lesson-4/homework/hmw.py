# # Questions
# #2:continue ignores a given condition and loop continues while true, but break stops the loop when it meets certain condition

# #3 a for loop is generally used for a known number of iterations over a sequence, while a while loop is used when the number of iterations is unknown and depends on a dynamic condition

# #4 A nested for loop means placing one for loop inside another for loop.The outer loop runs first, and for each of its iterations, the inner loop runs completely.
# # for i in range(3):
# #     for j in range(3):
# #         print(i, j)
# #Homework
# # 1

# list1 = [1, 1, 2]
# list2 = [2, 3, 4]

# outlist=[]
# for i in list1:
#     if i not in list2:
#         outlist.append(i)
# for i in list2:
#     if i not in list1:
#         outlist.append(i)
# print(outlist)
# # 2
# n=5
# for i in range(1,n):
#     print(i**2)

# #3
# txt = 'assalom'
# result = []
# count = 0
# i = 0
# while i < len(txt):
#     result.append(txt[i])
#     count += 1
#     if count == 3 and i != len(txt) - 1: 
#         if txt[i] in "aeiouAEIOU" or (i > 0 and txt[i-1] == '_'):
#             count = 2  
#         else:
#             result.append('_')
#             count = 0
#     i += 1

# print(''.join(result))
# # #4
# import random
# p=random.randint(1,100)
# while True:
#         c=int(input('Your number '))
#         turn=0
        
#         if turn<10:
#             if c==p:
#                 print('You guessed it right')
#             elif c-p>50:
#                 print('Too high')
#                 turn+=1
#             elif p-c>50:
#                 print('Too low')
#                 turn+=1
#             else:
#                 print('Close')
#                 turn+=1
#         else:
#              print('You lost! The number is ',p)
#              q=input("Do you want to play again? ")
#              if q.lower() not in ['yes','y','ok']:
#                     break
            
# #5
# while True:
#     pw=input('Enter your password: ')
#     if len(pw)<8:
#         print('Password is short')
#     elif not any(char.isupper() for char in pw):
#         print('Password must contain an uppercase letter.')
#     else:
#         print('Password is strong.')
#         break
# #6
# pr=[]
# for i in range(1,100):
#     if i==2:
#         pr.append(i)
#     else:
#         for j in range(2,i):
#             if i%j==0 :
#                 break
#         else:
#             if i not in pr:
#                     pr.append(i)
# print(pr)



#  #bonus question


# options = ['rock', 'paper', 'scissors']

# pl_score = 0
# comp_score = 0

# while pl_score < 5 and comp_score < 5:
#     pl = input('Rock, paper or scissors: ').lower()

#     if pl not in options:
#         print('Invalid choice, try again.')
#         continue

#     comp = random.choice(options)
#     print(f'Computer chose: {comp}')

#     if pl == comp:
#         print('Draw')
#     elif (pl == 'rock' and comp == 'scissors') or \
#          (pl == 'paper' and comp == 'rock') or \
#          (pl == 'scissors' and comp == 'paper'):
#         print('1 point for you')
#         pl_score += 1
#     else:
#         print('1 point for computer')
#         comp_score += 1

#     print(f'Score for You: {pl_score} | Computer: {comp_score}')
#     print('-' * 30)


# if pl_score == 5:
#     print('You win the match!')
# else:
#     print('Computer wins the match!')


#3
txt=input()
done={'a','e','i','o','u'}
counts=0
ans=[]

for i in range(len(txt)):
    counts+=1
    ans+=txt[i]
    if i!=len(txt)-1 and counts>=3 and txt[i].lower() not in done:
        done.add(txt[i])
        ans.append('_')
        counts=0
print(''.join(ans))