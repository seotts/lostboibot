#in this file, we'll create a file with tweets in it

import Queue
import re
previousWords = Queue.Queue(maxsize = 10)
afterWords = []
hasFoundBoy = False

 #dictionary to switch pronouns. unfortunately it can't distinguish btwn NP "his" and determiner "his"
 #I added in the /b's. They mean that the string can only match at the beginning or end of a word 
 #(or both, if you put it on both ends). This fixes cases where "heartbeat" or "her" (!!!) were 
 #matching "he", etc
pronouns = {r'\bhe\b':'she', r'\bhim.':'her', r'\bhis\b':'her', r'\bhe\'.':'she\'', r'\bhimself.':'herself', 
        r'[\"\']*He\b':'She', r'[\"\']*Him.':'Her', r'[\"\']*His\b':'Her', r'[\"\']*He\'.':'She\'', r'[\"\']*Himself.':'Herself'}

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
          #maybe we can check if previousWords.get() ==boy?
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
   
