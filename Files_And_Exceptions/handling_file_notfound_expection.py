from pathlib import Path

path = Path("Alice.txt")
try:
    content = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} doesn't exit.")
