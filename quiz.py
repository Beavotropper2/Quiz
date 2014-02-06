# Quiz Program
# Questions

# Austen Calzadilla
# Jessica Rex

import question

# Quiz Logic

num_questions = question.num_questions
max_attempts = 2

questions_right = 0
questions_wrong = 0

# Print question and possible answers
def printQuestion(q):
    print("{0}. {1}".format(q.questionNum, q.question))
    print("  {0}".format(q.a1))
    print("  {0}".format(q.a2))
    print("  {0}".format(q.a3))
    print("  {0}".format(q.a4))
    
# Get answer from user
def getAnswer(q):
    q.attemptCount += 1
    answer = raw_input("Answer: ")
    return answer
    
# Start quiz loop
    
for index in range(num_questions):
    current_q = question.questions[index]
    printQuestion(current_q)
    
    done = 0
    while not done:
        answer = getAnswer(current_q)
        
        if(answer == current_q.rightAns):
            print("Correct!\n")
            current_q.complete = 1
            done = 1
        else:
            current_q.wrongCount += 1
            if current_q.wrongCount >= 2:
                print("Sorry, you have exceeded the max attempts.\n" +
                      "The correct answer is: {0}\n".format(current_q.rightAns))
                done = 1
            else:   
                print("Incorrect... try again\n")
                
attempts = correct = wrong = 0
for q in question.questions:
    correct += q.complete
    wrong += q.wrongCount
    attempts += q.complete + q.wrongCount
    
print("Attempts: {0}".format(attempts))
print("Correct: {0} --- Wrong: {1}".format(correct, wrong))