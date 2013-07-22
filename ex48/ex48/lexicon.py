def scan(input):
	
	lexicon = {'direction': ['north', 'south', 'east', 'west'],
			   'verb': ['go', 'kill', 'eat'],
			   'stop': ['the', 'of', 'in'],
			   'noun': ['bear', 'princess'],
			   'number': range(10) # 0 - 9
	}
	list = []
	
	words = input.split()
	
	for word in words:
		for key in lexicon:
			if word.lower() in lexicon[key]: # is word in any of the dict keys?
				list.append((key, word)) # if TRUE, add the key/value tuple to list and break
				break
		else: # if above 'break' activates, skips this step
			list.append((str_to_num(word))) # is word a number? if not, then it must be an error
	
	return list

def str_to_num(s):
	try:
		return 'number', int(s)
	except ValueError:
		return 'error', s