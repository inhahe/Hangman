from title_maker_pro.word_generator import WordGenerator
word_generator = WordGenerator(
  device="cuda",
  forward_model_path="D:\\limnoria\\plugins\\MadeUpWords\\forward-dictionary-model-v1\\",
  inverse_model_path="D:\\limnoria\\plugins\\MadeUpWords\\inverse-dictionary-model-v1\\",
  blacklist_path=r"D:\limnoria\plugins\MadeUpWords\blacklist.pickle",
  quantize=False,
)

words = open("madeupwords.txt", "r").readlines()
out = open("madeupwords.txt", "a")

for _ in range(30000-len(words)):
  while 1:
    result = word_generator.generate_word()
    if result:
      break
  out.write(f"{result.word}|{result.pos}|{result.topic}|{result.definition}|{result.example}\n")
  print(result.word)
  
  
