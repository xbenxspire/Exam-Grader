'''
Created on Oct 7, 2023
@author: Benjamin Pierce
This program reads student's answers from a text file and will tell you whether the student passed or failed the exam 
(must score 15 of the 20 questions to pass).  
It will display the total correctly answered questions, total incorrectly answered questions, 
and a list showing the question numbers of the incorrectly answered questions.
'''
try:
    #check the file exists and look at it's contents
    inFile = open("test_answers.txt", 'r')
    contents = inFile.read()
    print(contents)
    inFile.close()
except IOError as e:
    print(e)
    
def main():
    #Define correct answers as a list
    correct_answers = [
        "A", "C", "A", "A", "D",
        "B", "C", "A", "C", "B",
        "A", "D", "C", "A", "D",
        "C", "B", "B", "D", "A"
        ]

    #Initialize variables to keep track of the student's score and incorrect answers
    num_correct = 0
    num_incorrect = 0
    incorrect_questions = []

    #Read the student's answers from the file created within the same file directory as program (answers typed in a list without numbers, periods or spaces)
    with open("test_answers.txt", "r") as file:
        test_answers = [line.strip() for line in file]
       
    #Check each student answer against the correct answers
    for i in range(len(test_answers)):
        if i < len(correct_answers):  #Check if there is a correct answer
            student_answer = test_answers[i].upper()  #Convert to upper case for comparison
            if student_answer == correct_answers[i]:
                num_correct += 1    #Add count to total correct answers
            else:
                num_incorrect += 1    #Add count to total incorrect answers
                incorrect_questions.append(i + 1)

    #Determine whether the student passed or failed
    if num_correct >= 15:    #If total correct answers are greater than or equal to 15, student passed
        result = "Pass"
    else:    #If total correct answers are not greater than or equal to 15, student failed
        result = "Fail"

    # Display the results
    print("Student's Exam Result:", result)
    print("Total Correct Answers:", num_correct)
    print("Total Incorrect Answers:", num_incorrect)
    if num_incorrect > 0:
        print("Incorrectly Answered Question(s):", incorrect_questions)
main()