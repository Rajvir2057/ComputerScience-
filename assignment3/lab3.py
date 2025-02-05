y=True
while y:  
    #taking the string input from the user.
    user_input = input("Enter a string: ").strip()

    #string comparison (direct match with predinfined keywords)
    if user_input == "Python":
        print("The input is exactly 'Python'..")
    elif user_input == "code":
        print("The input is exactly 'code'..")
    elif user_input == "programming":
        print("The input is exactly 'programming'..")
    elif user_input == "Exit":
        print("Exiting the program...")
        break #Ends the program if the user says this...

    ## using string methods for analysis purposes..

    #checking if user puts lab
    if user_input.find("lab") != -1:
        print("The input contains 'lab'.")
    else:
        print("The input does not contain 'lab'.")
    
    #check if the user starts with "test" using startwith.
    if user_input.startswith("test"):
        print("The input starts with 'test'.")
    else:
        print("The input does not start with 'test'.")

    #checking if user made an input that has alphanumeric using isalnum()
    if not user_input.isalnum():
        print("The input contains a special character.")
    else:
        print("The input does not contain a special character.")

    #checking if user has no capital letter
    if user_input.islower():
        print("The input contains no capital letter.")
    else:
        print("The input does  contain a capital letter.")
    
    # checking if user has t
    if user_input.count("t") > 2:
        print("The input contains more than 2 't's.")
    else:
        print("The input does not contain more than 2 't's.")

    # code when the user does not have anything that was needed
    if user_input != "Python" and user_input != "Code" and user_input != "Exit":
        print("Your input does not much the predefined keywords.")

    #check whether continue with the loop..
    check = input("Do you wanna continue ? Enter yes to do so: ") 
if check.lower() == "yes":
    y = True
else: 
    y = False