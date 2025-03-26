#Kaur Rajvir 816815
def main():
    words1 = filewords()
    words2=  filewords()

    #create a set containing the words common to both files.
    common = words1.intersection(words2)

    #Display the words in alphabetical order.
    print("The words that are common in both files.") 
    for word in sorted(common):
        print(" ",word)

    #create a set containing the words different from both files.(whats in first but not in second.)
    difference1 = words1.difference(words2)

    #Display the words in alphabetical order.
    print("The words that are in the first but not second.") 
    for word in sorted(difference1):
        print(" ",word)

    #create a set containing the words different from both files.(whats in second but not in first.)
    difference2 = words2.difference(words1)

    #Display the words in alphabetical order.
    print("The words that are in the second but not first.") 
    for word in sorted(difference2):
        print(" ",word)

    #All the Words that are in both files
    union = words1.difference(words2)

    #Display the words in alphabetical order.
    print("All the Words that are in both files.") 
    for word in sorted(union):
        print(" ",word)

def filewords():
    #Read the filename and open the file.
    filename= input("Enter the name of the file: ")
    inf = open(filename,"r")

    #Add all of the words to a dictionary.
    words = set()
    for line in inf:
        parts= line.split()
        for word in parts:
            words.add(word)
    return words

main()
