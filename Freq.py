with open('/usr/share/dict/words') as f:
    words = f.readlines()
    higher = 1000
words = [w.strip() for w in words]
words = [w.lower() for w in words]
freq = 'esiarntolcdugpmkhbyfvwzxqj'
for w in words:
    if len(w) != 5:
        continue
    if(len(set(list(w)))) != len(w):
        continue
    score = 0
    for i in w:
        if i in freq:
            score += freq.find(i)
        else:
            score += 1000
    else:
        if score < higher:
            print(w, score)
            higher = score
