from pathlib import Path

path = Path("Files_And_Exceptions/empty.txt")
contents = "I love programming.\n"
contents += "I love creating games.\n"
contents += "I aslo love art!"
path.write_text(contents)
