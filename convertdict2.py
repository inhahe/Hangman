import json
fin = open("cmudict.0.7a.txt","r")
fout = open("words.json", "w")
a = []
for l in fin:
  word = l.split(' ', 1)[0]
  if word.isalpha():
    a.append(word)
fout.write(json.dumps(a))
    
    