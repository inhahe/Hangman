fin = open("cmudict.0.7a.txt","r")
fout = open("words.txt", "w")
for l in fin:
  word = l.split(' ', 1)[0]
  if word.isalpha():
    fout.write(word+"\n")
    
    