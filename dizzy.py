l = "T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _2 h8 n18 132 k24"

sp = l.split(" ")
temp = []
for _ in range(100):
    temp.append("-")
for _ in sp:
	c = _[0]
	i = int(_[1:])
	temp[i] = c
	answer = "".join(temp)
print(answer)
