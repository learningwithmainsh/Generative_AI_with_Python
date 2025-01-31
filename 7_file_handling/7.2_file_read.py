#readline():Reads onle line at a time
with open("SampleFile.txt", "r") as file:
    filecontent = file.readline()
    print(filecontent)



#readlines():Reads file and return in lists
with open("SampleFile.txt", "r") as file:
    filecontent = file.readlines()
    print(filecontent)


# Read file and Print all lines
with open("SampleFile.txt", "r") as file:
    for line in file:
        print(line.strip())
