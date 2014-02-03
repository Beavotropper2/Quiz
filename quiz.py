# Quiz Program
# Questions

from collections import namedtuple

class Question():
    question = ""
    a1 = ""
    a2 = ""
    a3 = ""
    a4 = ""
    wrongCount = 0
    attemptCount = 0
    rightAns = ""
    questionNum = -1
    complete = 0

    def __init__(self, q, a1, a2, a3, a4, wc, ac, ra, qn):
        self.question = q
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.wrongCount = wc
        self.attemptCount = ac
        self.rightAns = ra
        self.questionNum = qn


Question1 = Question("Which of the following most accurately describes a computer program?", 
                     "a. A collection of objects, all of the same type",
                     "b. A collection of objects of different type", 
                     "c. A list of instructions for objects to perform certain actions", 
                     "d. A set of instructions telling the computer how to perform tasks", 
                     0, 0, "d", 1)

Question2 = Question("What is an algorithm?", 
                     "a. A collection of objects, all of the same type", 
                     "b. A sequence of steps that are going to help you complete a task", 
                     "c. A list of instructions to perform certain actions", 
                     "d. All of the above", 
                     0, 0, "b", 2)

Question3 = Question("What are variables?", 
                     "a. Variables are used to store the data in a program", 
                     "b. Variables are used to represent the data", 
                     "c. Each variable has a unique name", 
                     "d. All of the above", 
                     0, 0, "d", 3)

Question4 = Question("How did we use variables in our app?", 
                     "a. We used variables to make the block editor bigger", 
                     "b. We used variables to store 'count'", 
                     "c. We used variables to eliminate loops", 
                     "d. We used variables to solve a problem", 
                     0, 0, "b", 4)

questions = (Question1, Question2, Question3, Question4)

# Quiz Logic

num_questions = 4
max_attempts = 2

questions_right = 0
questions_wrong = 0

def printQuestion(q):
    print(str(q.questionNum) + " " + q.question)
    print(q.a1)
    print(q.a2)
    print(q.a3)
    print(q.a4)
    
def getAnswer(question):
    question.attemptCount += 1
    answer = input("Answer: ")
    return str(answer)
    
for index in range(num_questions):
    attempts = 0
    question = questions[index]
    printQuestion(question)
    correct = 0
    while not correct:
        answer = getAnswer(question)
        if(answer == question.rightAns):
            print("Correct!")
            correct = 1
            question.complete = 1
        else:
            print("Incorrect... try again")
            question.wrongCount += 1
        attempts += 1
        if(attempts >= max_attempts):
            print("Sorry you have failed this question. The correct answer is: " + question.rightAns)
            correct = 1

        


