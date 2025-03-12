#Rajvir Kaur 816815
#This program prints a tale of medal winner counts with row totals.
#

Medals = 3
Countries =8

#create a list for countires.
countries = [  "Canada",
                "Italy",
                "Germany",
                "Japan",
                "Kazakhstan",
                "Russia",
                "South korea",
                "United States"]

#create a table of table counts
counts= [
    [ 0 , 3 , 0 ],
    [ 0 , 0 , 1 ],
    [ 0 , 0 , 1 ],
    [ 1 , 0 , 0 ],
    [ 0 , 0 , 1 ],
    [ 3 , 1 , 1 ],
    [ 0 , 1 , 0 ],
    [ 1 , 0 , 1 ],
]

#Print table header
print("        Country      Gold  Silver  Bronze    Total")

grand_total = 0 

#Print countries, counts, and row totals.
for i in range(Countries):
    total = 0  
    print("%15s" %countries[i], end="")

    #print each row element and update the row total.
    for j in range(Medals):
        print("%8d" %counts[i][j], end="")
        total = total + counts[i][j]


    grand_total = grand_total + total
    gold_total = gold_total + counts[j][0]

    #Display the row total and print a new line.
    print("%8d" % total)
print("-" * 50)
print("   Grand Total : ", "%30d"%grand_total)