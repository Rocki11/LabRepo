#Bible Trivia
done = False
import time
import sys

def displayintro():
    print ('\nBible Quiz Beginners Level')
    time.sleep(1)
    print('\nTest your knowledge of the word of God')

    
def letthequizbegin():
    countcorrect = 0
    countwrong = 0
    print('1. Who is the Comforter?')
    print('A. Peter, B. Paul, C. Holy Spirit, D. Angel Gabriel')
    answer1 = input('Select the correct answer ' , )
    print('2. State the verse that says Jesus Christ the same yesterday, and today and for ever')
    print('A. James 5 vs 4, B. Hebrews 13 vs 8, C. Revelation 5 vs 10, D. 1 John 1 vs 2')
    answer2 = input('Select the correct answer ' , )
    print('3. What four books tell about Jesus life on Earth')
    print('A. Hebrews, Romans, 1 John, Colossians')
    print('B. 1 Peter, Acts, Jude, Mark')
    print('C. Matthew, John, Philemon, Revelations')
    print('D. Matthew, Mark, Luke, john')
    answer3 = input('Select the correct answer ' , )
    print('4. What is the longest book in the bible?')
    print('A. Acts, B. Deuteronomy, C, Psalms, D. Genesis')
    answer4 = input('Select the correct answer ' , )
    print('\nHere is your result')
    
    if answer1 == 'C' or answer1 == 'c':
        print('\nYou got question 1 right')
        countcorrect = countcorrect + 1
    else:
        print('You got question 1 wrong')
        countwrong = countwrong + 1
    if answer2 == 'B' or answer2 == 'b':
        countcorrect = countcorrect + 1
        print('you got question 2 right')
        #print('You got', countcorrect, 'questions right')
    else:
        print('you got question 2 wrong')
        countwrong = countwrong + 1
        #print('You got', countwrong, 'questions wrong')
    if answer3 == 'D' or answer3 == 'd':
        print('You got question 3 right')
        countcorrect = countcorrect + 1
    else:
        print('You got question 3 wrong')
        counwrong = countwrong + 1
    if answer4 == 'C' or answer4 == 'c':
        print('You got question 4 right')
        countcorrect = countcorrect + 1
        print('You got', countcorrect, 'questions right')
    else:
        print('You got question 4 wrong')
        countwrong = countwrong + 1
        print('You got', countwrong, 'questions wrong')            
              
                          
takethequizagain = 'yes'
while takethequizagain == 'yes' or takethequizagain == 'y':   
                               
    displayintro()
                        
    letthequizbegin()

    print('\nDo you want to take the quiz again? (Yes or No) ', )
    takethequizagain = input()

    
