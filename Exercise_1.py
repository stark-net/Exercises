key = int(input("Enter shift amount (number): "))
print("Enter your text (at most 100 characters)")
print("Enter 0 in a new line to stop:\n")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
total_length = 0
lines = []
while True:
    line = input() 
    if line == "0":
        break
    
    total_length += len(line)
    if total_length > 100:
        print("Your input is too long")
    
    lines.append(line)

plain_text = "\n".join(lines)

ciphered_text = ""
    
for char in plain_text:
    if char.isalpha():
        upper_char = char.upper()
        index = alphabet.index(upper_char)
        new_index = (index + key) % 26
        ciphered_char = alphabet[new_index]
        ciphered_text += ciphered_char
    else:
        ciphered_text += char
print("\nYour ciphered text is:\n" + ciphered_text)
        
            
