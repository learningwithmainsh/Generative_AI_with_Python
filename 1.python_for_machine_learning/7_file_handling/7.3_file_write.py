# Writing the file in truncate mode It will create new file if not exist and overwrite content
with open("SampleFile1.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Writing file by python")


# Writing the file in append mode 
# It will create new file if not exist  and append content
with open("SampleFile2.txt", "a") as file:
    file.write("Hello, World!\n")
    file.write("Writing file by python")



#writeline(): Write a list of strings
#List of lines to be written to the file
lines = [
        "This is first line. \n"
        "This is second line. \n"
        "This is third line. \n"
        "This is fouth line. \n"
]

with open("SampleFile3.txt", "w") as file:
    file.writelines(lines)