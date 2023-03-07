text_file = open('/Users/viman/Desktop/records.txt')
text = text_file.read()
sump = 0.0
sumn = 0.0

for word in text.split("\n"):
    if word == "/end":
        break
    if '+' in word:
        word = word.replace("+", "")
        sump += float(word)
    elif '-' in word:
        sumn += float(word)

print("You are owed, owe = ", sump, ", ", sumn, "\nYou are to be paid = ", sumn + sump)