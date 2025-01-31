# file handling in python

try:
    with open("manish_photo.jpeg", "rb") as file:
        content = file.read()
        # Print the first 20 bytes in hexadecimal format for better readability
        print("Read binary content (first 20 bytes):", content[:20].hex())
except FileNotFoundError:
    print("Error: The file 'manish_photo.jpeg' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")