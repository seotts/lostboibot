import Queue
import re
previousWords = Queue.Queue(maxsize = 10)
afterWords = []
hasFoundBoy = False

 #dictionary to switch pronouns. unfortunately it can't distinguish btwn NP "his" and determiner "his"
pronouns = {r'he':'she', r'him.':'her', r'his':'her', r'he\'.':'she\'', r'himself.':'herself', 
	    r'[\"\']*He':'She', r'[\"\']*Him.':'Her', r'[\"\']*His':'Her', r'[\"\']*He\'.':'She\'', r'[\"\']*Himself.':'Herself'}

def is_boy_match(word):
   is_match = re.match(r'[\"\']*boy.', word, re.I)
   return is_match
 
with open("one-line-text.txt", 'r') as f:
  for line in f:
    for word in line.split():
      if is_boy_match(word):
	
	
	hasFoundBoy = True
	
	sentence = ''
	
	#add previous words
	while not previousWords.empty():
	  sentence = sentence + " " + previousWords.get() + " "
	
	#add "boi"
	if word[0] in ['\"', '\'']:
	  sentence = sentence + word[:3] + "i" + word[4:]
	
	else:
	  sentence = sentence + word[:2] + "i" + word[3:]
	  
	#add next words
	
      else:
	for p in pronouns.keys():
	  if re.match(p, word):
	    word = "*" + pronouns[p] + "*"
	if hasFoundBoy:
	  if(len(sentence) + len(word) < 140):
	    sentence = sentence + " " + word
	  else:
	     print sentence
	     hasFoundBoy = False
	else:
	  previousWords.put(word)
	  if previousWords.full():
	    previousWords.get()
	#print previousWords
   
