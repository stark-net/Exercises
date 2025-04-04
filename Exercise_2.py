import re
text = ""
print("Enter a string of English alphabet without spaces (at most 100 letters. Enter 0 to stop input):\n")
while True: 
    line = input()
    if line == "0":
        break
    elif line == "":
        continue
    if not line.isalpha() or (len(line) > 100):
        print("Your input has things which are not alphabet")
        continue
    text += line
result = re.findall("ab+c", text)
print("\n".join(result))