def test_counter( lst):

  words = {}
  for word in lst:
    word = word
    if word in words:
      words[word] +=1
    else:
      words[word] = 1
  
  
  for k, v in words.items():
    print(f"{k}: {v}")
