def reading_and_editingdata():
    # Read the file
    datatext = open("data1.txt", "r")
    newtext = open("data2.txt", "w")

    # Getting the total of the numbers in data1 inside data2
    total = 0
    line = datatext.readline().strip()  # Strip to remove extra spaces/newlines

    while line != "":  # Loop until the end of the file
        newtext.write(line + "\n")  # Write each line with a newline
        total = total + float(line)  # Convert to float and add to total
        line = datatext.readline().strip()  # Read next line and strip

    # Write a separator between the data sets
    newtext.write("***********\n")

    # Write the total at the end
    newtext.write("Total sum is : %5.2f\n" % total)

    # Close the files
    datatext.close()
    newtext.close()

reading_and_editingdata()
