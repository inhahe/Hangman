import cgi, cgitb, json, random, re
cgitb.enable()
form = cgi.FieldStorage() 
words = open("words.txt", "r").read().split("\n")
func = form.getvalue("function")
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers
if func=="getwordlen":
  minlen = form.getvalue("minlen", 5)
  maxlen = form.getvalue("maxlen", 100)
  words2 = [word for word in words if int(minlen) <= len(word) <= int(maxlen)]
  print(len(random.choice(words2))) #will give an error if minlen too large or maxlen <= 0
elif func=="getpositions":
  mask = form.getvalue("mask")
  letter = form.getvalue("letter")
  usedletters = form.getvalue("usedletters", "")
  usedletters2 = ''.join(list(set([char for char in mask if char != "_"])))
  dot = "[^" + usedletters2 + usedletters + "]" if usedletters2 or usedletters else "."
  maskre = re.compile("^" + mask.replace("_", dot) + "$")
  open("debug.txt","a").write("^" + mask.replace("_", dot) + "$"+"\n")
  matches = [word for word in words if re.match(maskre, word)]
  matches2 = [word for word in matches if word.count(letter)]
  if matches2:
    selectedword = random.choice(matches2)
    positions = [m.start() for m in re.finditer(letter, selectedword)]
    print(','.join((str(p) for p in positions)))
  else:
    print("word:" + random.choice(matches))
          