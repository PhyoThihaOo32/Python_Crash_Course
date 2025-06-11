from pathlib import Path

# create a path object
path = Path("Files_And_Exceptions/pi_digits.txt")
# check if it exists
print(path.exists())
# get the absolute path
print(path.resolve())
# check if it's a file or directory
print(path.is_file())
print(path.is_dir())
# read text from the file
contents = path.read_text().rstrip()
print(contents)

# accessing file's line
# splitlines() method returns a list of all lines in the file

lines = contents.splitlines()

for index, line in enumerate(lines, start=1):
    print(f"{index}: {line}")

# working with a file's contents

pi_string = ""

for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))
