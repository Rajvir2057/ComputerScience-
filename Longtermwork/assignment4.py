#Kaur Rajvir 816815
# A program that helps in practicing reading and writing in txt files.
import os 

#creating functions 
def options():
    print("1 : Take a test")
    print("2 : Add more questions")
    print("3 : Remove questions")
    print("4 : Modify questions")
    print("5 : Exit")

def take_test():
    #First create variables..
    Total_points = 0
    correct_answers = 0
    questions= 0

    #Read the questions from the file.
    infile = open("Test.txt" ,"r")
    read_question = infile.readline()

    while read_question != " ":
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
                print("Your answer is correct.")
                correct_answers += 1
                Total_points += int(answer[1])
            else:
                print("Your answer is incorrect.")
        read_question = infile.readline()
            
    print("User got "+str(correct_answers)+"out of"+str(questions)+" questions")
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

    #writing the questions to the file
    infile2.write(new_question+"\n")
    infile2.write(new_choice1+"\n")
    infile2.write(new_choice2+"\n")
    infile2.write(new_choice3+"\n")
    infile2.write(new_choice4+"\n")
    infile2.write(new_answer+"\n")

    #taking care of the number of questions the user needs to add
    print("Do you want to add more? ")
    while input("yes / no") == "yes":
        new_question = input("Enter new question: ")
        new_choice1 = input("Enter first choice: ")
        new_choice2 = input("Enter second choice: ")
        new_choice3 = input("Enter third choice: ")
        new_choice4 = input("Enter fourth choice: ")
        new_answer = input("Enter the answer with points eg a3: ")

        infile2.write(new_question+"\n")
        infile2.write(new_choice1+"\n")
        infile2.write(new_choice2+"\n")
        infile2.write(new_choice3+"\n")
        infile2.write(new_choice4+"\n")

        if input("yes/no") == "no":
            break
    infile2.close()

def remove_questions():
    #opening the file again.
    infile3 = open("Test.txt","r")
    outfile = open("temp.txt","w")
    pass

def modify_questions():
    pass 

#main function to get output from above functions.
def main():
    while True:
        options()
        userselecion = int(input("Enter your choice: "))
        if userselecion == 1 :
            take_test()
        elif userselecion == 2:
            add_questions()
        elif userselecion == 3:
            remove_questions()
        elif userselecion == 4:
            modify_questions()
        elif userselecion == 5:
            print("Program finished.")
            break
        else:
            print("Invalid option. Please try again.")
main()

