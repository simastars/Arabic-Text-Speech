import pytesseract

# Load the Arabic language data
tessdata_dir = "arabic_text.txt"
pytesseract.pytesseract.tessdata_dir = tessdata_dir

# Read the Arabic text from a file
with open("arabic_text.txt", "r") as f:
    arabic_text = f.read()

# Convert the Arabic text to a string
arabic_text = arabic_text.strip()

# Recognize the Arabic text using Tesseract
result = pytesseract.image_to_string(arabic_text, lang="ara")

# Print the result
print(result)

