from pathlib import Path

path = Path("Files_And_Exceptions/pi_million_digits.txt")
contents = path.read_text()
lines = contents.splitlines()

pi_thousand_digits = ""

for line in lines:
    pi_thousand_digits += line.strip()

print(pi_thousand_digits[:50])
print(len(pi_thousand_digits))

birthday = input("Enter your birthday in mmddyy format: ")

if birthday in pi_thousand_digits:
    print("Your birthday is in pi!")
else:
    print("Opps your birthday is not in Pi!")
