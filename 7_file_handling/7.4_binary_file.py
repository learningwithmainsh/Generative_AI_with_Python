# Binary Files handles non.text like images

with open ("manish_photo.jpeg", "rb") as file:
    content = file.read()
    print("Read binary content:", content[:20])