import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class ###(###):":
      "Make a class named ###",
    "class ###(object):\n\tdef __init__(self, ***)":
      "class ###",
    "class ###(object):\n\tdef ***(self, @@@)":
      "class ###",
    "*** = ###()":
      "Set *** to an instance of class ###.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# Drill phrases first?
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# Load words from the website
for word in urlopen(WORD_URL).readlines(): # technically, .readlines() isn't necessary anymore
    WORDS.append(word.strip().decode('ascii')) # http://stackoverflow.com/questions/16699362/python3-error-typeerror-cant-convert-bytes-object-to-str-implicitly
    
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("###"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
    
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
    
    for sentence in snippet, phrase:
        result = sentence[:]
        
        # fake class names
        for word in class_names:
            result = result.replace("###", word, 1)
        
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
        
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        
        results.append(result)
    
    return results

# Keep going until they hit CTRL-Z
try:
    while True:
        snippets = list(PHRASES.keys()) # In Python3, a d.items(), d.keys(), and d.values() creates
                                  # an iterator object. You need to explicitly convert that iterator
                                  # to a list using list()
        random.shuffle(snippets)
        
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            
            print(question)
            input("> ")
            print("ANSWER: %s\n\n" % answer)
except EOFError:
    print("\nBye")