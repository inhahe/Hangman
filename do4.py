import cgi, cgitb, json, random, re, json
cgitb.enable()
form = cgi.FieldStorage() 
wordsets = [l[1] for l in sorted(json.load(open("wordlevels.json", "r")).items(), key=lambda a:int(a[0]))]
func = form.getvalue("function")
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers
if func=="getwordlen":
  minlen = form.getvalue("minlen", 5)
  maxlen = form.getvalue("maxlen", 100)
  words2 = [word for wordset in wordsets for word in wordset if int(minlen) <= len(word) <= int(maxlen)]
  print(len(random.choice(words2))) #will give an error if minlen too large or maxlen <= 0
elif func=="getpositions":
  mask = form.getvalue("mask")
  letter = form.getvalue("letter")
  usedletters = form.getvalue("usedletters", "")
  usedletters2 = ''.join(list(set([char for char in mask if char != "_"])))
  dot = "[^" + usedletters2 + usedletters + "]" if usedletters2 or usedletters else "."
  maskre = re.compile("^" + mask.replace("_", dot) + "$")
  for wordset in wordsets:
    matches = [word for word in wordset if re.match(maskre, word.upper())]
    matches2 = [word for word in matches if word.upper().count(letter)]
    if matches2:
      selectedword = random.choice(matches2)
      positions = [m.start() for m in re.finditer(letter, selectedword.upper())]
      print(','.join((str(p) for p in positions)))
      break
  else:
    for wordset in wordsets:
      matches = [word for word in wordset if re.match(maskre, word.upper())]
      if matches:
        print("word:" + random.choice(matches).upper())
          