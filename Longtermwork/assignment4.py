#Kaur Rajvir 816815
# A program that helps in practicing reading and writing in txt files.
import os 

#creating functions 
def options():
    print("1 : Take a test")
    print("2 : Add more questions")
    print("3 : Remove questions")
    print("4 : Exit")
    
def take_test():
    print("\nBest of luck for the test.\n")

    #First create variables..
    Total_points = 0
    correct_answers = 0
    questions= 0

    #Read the questions from the file.
    infile = open("Test.txt" ,"r")
    read_question = infile.readline()

    while read_question != "":
        questions += 1
        #reading choices..
        choice1 =infile.readline()
        choice2 = infile.readline()
        choice3 = infile.readline()
        choice4 = infile.readline()
        answer= infile.readline()

        #printing the line in a specific format..
        print("Qn",str(questions)+" "+read_question+"A: "+choice1+"B: "+choice2+"C: "+choice3+"D: "+choice4)

        #taking user's answer..
        user_answer = input("Enter your answer: ")

        #error handling.
        while user_answer.lower() not in ["a","b","c","d"]:
            user_answer= input("Enter your answer: ")

        if user_answer ==answer[0].lower():
            correct_answers += 1
            Total_points += int(answer[1])
            print("Your answer is correct. +", answer[1], "points\n")
        else:
            print("Your answer is incorrect.\n")

        read_question = infile.readline()
            
    print("User got", correct_answers, "out of", questions, "questions")
    print("Your total score is: ",Total_points)
    infile.close()

def add_questions():
    #opening the file again.
    infile2 = open("Test.txt","a")

    #creating new questions to append in the file.
    new_question = input("Enter new question: ")
    new_choice1 = input("Enter first choice: ")
    new_choice2 = input("Enter second choice: ")
    new_choice3 = input("Enter third choice: ")
    new_choice4 = input("Enter fourth choice: ")
    new_answer = input("Enter the answer with points eg a3: ")

    if new_answer[0] in "abcd" and int(new_answer[1:]) > 0:
        #writing the questions to the file
        infile2.write(new_question+"\n")
        infile2.write(new_choice1+"\n")
        infile2.write(new_choice2+"\n")
        infile2.write(new_choice3+"\n")
        infile2.write(new_choice4+"\n")
        infile2.write(new_answer+"\n")
    else:
        print("You have to enter a, b, c, or d, and a number")

    #taking care of the number of questions the user needs to add
    print("Do you want to add more? ")
    while input("yes / no :") == "yes":
        new_question = input("Enter new question: ")
        new_choice1 = input("Enter first choice: ")
        new_choice2 = input("Enter second choice: ")
        new_choice3 = input("Enter third choice: ")
        new_choice4 = input("Enter fourth choice: ")
        new_answer = input("Enter the answer with points eg a3: ")

        if new_answer[0] in "abcd" and int(new_answer[1:]) > 0:
            infile2.write(new_question+"\n")
            infile2.write(new_choice1+"\n")
            infile2.write(new_choice2+"\n")
            infile2.write(new_choice3+"\n")
            infile2.write(new_choice4+"\n")
            infile2.write(new_answer+"\n")
        else:
            print("You have to enter a, b, c, or d, and a number")
            continue

        print("Do you want to add more? ")
        if input("yes/no :") == "no":
            break
    infile2.close()

def remove_questions():
    #open file to show list of questions
    infile3 = open("Test.txt","r")

    #show the questions list
    questions_list = []
    this_question = []
    
    for i, line in enumerate(infile3):
        if (i % 6 == 0) and i != 0:
            questions_list.append(this_question)
            this_question = []

        this_question.append(line)

    for i, q in enumerate(questions_list):
        print("Question", i, "---", q[0])


    infile3.close()

    #ask question to remove
    question_to_remove = int(input("Question to remove: "))

    #remove question from list
    questions_list.pop(question_to_remove)

    #opening the file again.
    outfile = open("temp.txt","w")

    #write back to the file to original
    for question in questions_list:
        outfile.writelines(question)
    outfile.close()

    #rename temporary file to the original
    os.remove("Test.txt")
    os.rename("temp.txt", "Test.txt")

#main function to get output from above functions.
def main():
    while True:
        options()
        userselection = int(input("Enter your choice: "))
        while userselection == '':
            userselection = int(input("Enter your choice: "))

        if userselection == 1 :
            take_test()
        elif userselection == 2:
            add_questions()
        elif userselection == 3:
            remove_questions()
        elif userselection == 4:
            print("Program finished.")
            break
        else:
            print("Invalid option. Please try again.")
main()

