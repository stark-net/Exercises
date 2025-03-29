from playsound import playsound
first = int(input("Enter a NUM: "))
second = int(input("Enter a NUM: "))
if first == second:
    playsound('/media/stark/Local_Disk/Music/15_not_afraid.mp3')
else:
    s = str(input("Enter a string: "))
    S = s[len(s)/2]-1+s[len(s)+2]
    print(S)
