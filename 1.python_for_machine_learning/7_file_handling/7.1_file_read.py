# # Opening the File
# file = open("SampleFile.txt","r")
# print(file)
# print("Successfully able to Read the File...")
# file.close()

try:
    file = open("SampleFile.txt", "r")
    print("File Content:")
    for line in file:  # Iterate through each line
        print(line.strip())  # Print each line (strip removes extra newline characters)
except FileNotFoundError:
    print("Error: The file 'SampleFile.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed.")


# with statements
# With statements will close automatically when  afte block executed

# Open the file in read mode
try:
    with open("SampleFile.txt", "r") as file:
        # Read all contents of the file
        content = file.read()
        print("File Contents:\n")
        print(content)
except FileNotFoundError:
    print("The file does not exist. Please check the file name and path.")



