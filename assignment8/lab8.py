#RAJVIR KAUR 816815

#create variables 
population_file = "worldpop.txt"
area_file = "worldarea.txt"
report_file = input("What's the name for the report file?: ")

#form a function to open the files.
def main ():
    popfile = open(population_file, "r")
    areafile = open(area_file,"r")
    reportfile= open(report_file,"w")

    #read the first poplulation data record.
    popdata = extractdatarecord(popfile)
    while len (popdata) ==2 :
        #read the next area data record.
        areadata = extractdatarecord(areafile)

        #Extract the data components from the two lists.
        country = popdata[0]
        population = popdata[1]
        area = areadata[1]

        #compute and print the population density.
        density = 0.0
        if area > 0: #protect against division by zero.
            density = population / area
        reportfile.write("%-40s%15.2f\n" % (country,density))

        popdata = extractdatarecord(popfile)

    popfile.close()
    area.file()
    reportfile.close()

def extractdatarecord(infile):
    line = infile.readline()
    if line == "":
        return []
    else:
        parts = line.rsplit(" ",1)
        parts[1] = int(parts[1])
        return parts
main()

