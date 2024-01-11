#Guillermo Gago-Balbi
#Lab 2 - Create-a-Quiz
#January 9th 2023
print('Welcome to my quiz! Good luck!')
print('There are 5 questions, all testing your general knowledge.')
#Introduction
print()
#Blank line
correct = 0
#Sets up a counter for the amount of correct answers

print('1. What is the capital of Canada?')
#First question with its options
print()
print('(a) Ottawa')
print('(b) Toronto')
print('(c) Montreal')
ans1 = str(input('Answer: '))
#Input for the user's answer

print()
if ans1 == 'a':
    print('Correct! 🍁')
    correct = correct+1
elif ans1=='A':
    print('Correct! 🍁')
#Providing this other option for the answer
    correct=correct+1
else:
    print('Incorrect.')
    
print()
print('2. Which artist sang God\'s plan?')
#Asking the second question with its options
print()
print('(a) Travis Scott')
print('(b) Kanye West')
print('(c) Drake')
ans2 = str(input('Answer: '))

print()
if ans2 == 'c':
    print('Correct! 🙏')
    correct = correct+1
elif ans2 == 'C':
    #Other option for answer
    print('Correct! 🙏')
    correct = correct+1
else:
    print('Incorrect.')
    
print()
print('3. Who is the soccer player with the most Ballon D\'ors?')
print()
print('(a) Cristiano Ronaldo')
print('(b) Pele')
print('(c) Lionel Messi')
ans3 = str(input('Answer: '))

print()
if ans3 == 'c':
    print('Correct! ⚽️')
    correct = correct+1
elif ans3=='C':
    print('Correct! ⚽️')
    correct = correct+1
else:
    print('Incorrect.')
    
print()
print('4. Who directed the movie Kill Bill (lowercase last name)?')
print()
ans4 = str(input('Answer: '))

print()
if ans4 == 'tarantino':
    print('Correct! 🥋')
    correct = correct+1
else:
    print('Incorrect.')
    
print()
print('5. What is the length of the hypotenuse of a right triangle if the other side lengths are 3 and 4?')
print()
ans5 = int(input('Answer(must be a number): '))

print()
if ans5 == 5:
    print('Correct! 🤓')
    correct = correct+1
else:
    print('Incorrect')
    
percent = (correct/5)*100
#This formula is used to find the percent and it uses the total correct answers amount
percent = int(percent)
#This makes it so the percent doesn't have a decimal

print()
print('Quiz complete!')
if correct == 1:
    print(f'You answered {correct} question correctly')
else:
    print(f'You answered {correct} questions correctly!')
print(f'That is a score of {percent} percent.')
#End of quiz statements
print('Rate YOUR quiz experience by sending an email to guillermo.g@gmail.com!')