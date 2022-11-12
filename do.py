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
  maskre = re.compile("^" + mask.replace("_", ".") + "$")
  matches = [word for word in words if re.match(maskre, word) and not any((usedletter in word for usedletter in usedletters))]
  matches2 = sorted([(word.count(letter), word) for word in matches])
  first = matches2[0][0]
  if first==0:
    print("word:" + random.choice(matches))
  else:
    candidates = [match[1] for match in matches2 if match[0]==first]
    selectedword = random.choice(candidates)
    positions = [m.start() for m in re.finditer(letter, selectedword)]
    print(','.join((str(p) for p in positions)))

          