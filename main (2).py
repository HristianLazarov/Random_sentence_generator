import random

def get_random_word(word):
  return random.choice(word)

names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligentrly", "warmly", "sadly", "rapitly"]
details = ["near the river", "at home", "in the park"]

print("Hello, this is your first random sentence:")

while True:
  r_name = get_random_word(names)
  r_places = get_random_word(places)
  r_verb = get_random_word(verbs)
  r_noun = get_random_word(nouns)
  r_adverb = get_random_word(adverbs)
  r_detil = get_random_word(details)
  print(f"{r_name} from {r_places} {r_adverb} {r_verb} {r_noun} {r_detil}")
  input("Click [Enter] to generate a new one.")