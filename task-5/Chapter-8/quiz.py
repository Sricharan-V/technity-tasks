# Multiplication Quiz

import random, time
numberOfQuestions = 10
correctAnswers = 0
print("You get 8 seconds to answer a question")
def exit():
    print("Incorrect")
for questionNumber in range(numberOfQuestions):
    tries=0
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    start = time.time()
    a= int(input(f"{num1}*{num2}= "))
    end= time.time()
    elapsed= end-start
    if a==num1*num2 and elapsed<=8:
        print("Correct")
        correctAnswers+=1
        time.sleep(1)
    elif elapsed==9:
        print("Incorrect, out of time limit")

    elif a!=num1*num2 and elapsed<=8:
        for j in range(2):
            print("Incorrect, try to answer again")
            start_a=time.time()
            a= int(input(f"{num1}*{num2}= "))
            end_a=time.time()
            elapsed_a= end_a-start_a
            tries+=1
            if a==num1*num2 and elapsed_a<=8:
                print("Correct")
                correctAnswers+=1
                time.sleep(1)
                break
            else:
                print("Out of time limit")
                break

        print("Incorrect")

        if tries>3:
            break
    else:
        print("Incorrect")
print("Number of correct answers = ", correctAnswers)