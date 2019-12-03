def search4vowels(phrase:str) ->set:
	"""Return any vowel found in a supplied phrase"""
	vowel = set('aeiou')
	return vowel.intersection(sset(phrase))


def search4letters(phrase:str, letters:str='aeiou') ->set:
	"""Return a set of the 'letters' found in 'phrase'"""
	return set(letters).intersection(set(phrase))