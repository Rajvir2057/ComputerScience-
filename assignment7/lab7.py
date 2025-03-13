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
gold_total = 0
silver_total = 0
bronze_total = 0  # Initialize the bronze total.

#Print countries, counts, and row totals.
for i in range(Countries):
    total = 0  
    print("%15s" %countries[i], end="")

    #print each row element and update the row total.
    for j in range(Medals):
        print("%8d" %counts[i][j], end="")
        total = total + counts[i][j]


    #Display the row total and print a new line.
    grand_total = grand_total + total
    gold_total = gold_total + counts[i][0]
    silver_total = silver_total + counts[i][1]
    bronze_total = bronze_total + counts[i][2]

    #Display the row total and print a new line.
    print("%8d" % total)
print("-" * 50)
print("   Grand Total : ", "%5d"%gold_total,"%6d"%silver_total,"%7d"%silver_total,"%8d"%grand_total)