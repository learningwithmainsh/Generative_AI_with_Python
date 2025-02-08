import os

# Get the current working directory
print(os.getcwd())

# Join paths correctly
path = os.path.join("/Users", "manishpandey", "manish/Generative_AI_with_Python/7_file_handling/python_file_path")
print(os.path.exists(path))  # Check if the path exists

# Check if a file or directory exists
print(os.path.isfile("readme.md"))  
print(os.path.isdir("/Users/manishpandey/manish/Generative_AI_with_Python/7_file_handling/python_file_path"))

from pathlib import Path

# Get the current working directory
print(Path.cwd())  # Call the method with ()

# Joining the Path

path = Path("/Users","/manishpandey/manish/Generative_AI_with_Python/7_file_handling/python_file_path")
print(path.exists())
print(path.is_file())
print(path.is_dir())