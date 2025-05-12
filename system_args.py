import sys

if len(sys.argv) < 3:
    print("Usage: python script.py <filename> <text_to_save>")
    sys.exit(1)

filename = sys.argv[1]
text = sys.argv[2]

with open(filename, "w") as f:
    f.write(text)

print("The text was saved to the file.")
