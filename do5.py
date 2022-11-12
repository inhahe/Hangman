import cgi, cgitb, json, random, re, json
cgitb.enable()
form = cgi.FieldStorage() 
words = open("madeupwords.txt", "r").readlines()
func = form.getvalue("function")
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers
if func=="getwordlen":
  minlen = form.getvalue("minlen", 5)
  maxlen = form.getvalue("maxlen", 100)
  words2 = [word.split("|") for word in words]
  words3 = [word[0] for for word in words2 if minlen <= len(word[0] <= maxlen]
  print(len(random.choice(words3))) #will give an error if minlen too large or maxlen <= 0
elif func=="getpositions":
  mask = form.getvalue("mask")
  letter = form.getvalue("letter")
  usedletters = form.getvalue("usedletters", "")
  usedletters2 = ''.join(list(set([char for char in mask if char != "_"])))
  dot = "[^" + usedletters2 + usedletters + "]" if usedletters2 or usedletters else "."
  maskre = re.compile("^" + mask.replace("_", dot) + "$")
  matches = [word for word in words2 if re.match(maskre, word[0].upper())]
  selectedword = random.choice(matches)
  if letter in match[0]:  
    positions = [m.start() for m in re.finditer(letter, selectedword[0].upper())]
    print(','.join((str(p) for p in positions)))
  else:
    print("word:" + selectedword[0].upper())
          