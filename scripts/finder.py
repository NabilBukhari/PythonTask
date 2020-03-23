import sys


class Finder:

	def __init__(self):
		self.is_alive = True
		self.corpus = []

	"""Adds the list of strings to document corpus. 
	
	Takes a list of string and splits it into tokens. 
	Adds token into corpus after checking for duplicate values. 
	"""
	def update_corpus(self, string_list):
		tokenized_list = string_list.split()
		for token in tokenized_list:
			# Check if token was already present in corpus
			if token not in self.corpus:
				self.corpus.append(token)
			else:
				# Send duplicate entries to garbage collector
				print('Sorry, {} was sent to garbage..'.format(token))

	"""Shows a current state of document corpus."""
	def show_corpus(self):
		print(self.corpus)

	"""Finds the given string from a document corpus.
	
	The function will return all strings from the list that
	contain the exact same characters as the string passed into it.
	The order of the characters in the strings is not relevant.
	"""
	def find(self, search_string):
		matched_samples = []
		search_tokens = search_string.split()

		# Token is each word to be found from query.
		for token in search_tokens:
			# Term is each word in the corpus.
			for term in self.corpus:
				# Compares the length of current token to each term in corpus.
				if len(token) == len(term):
					# Sort strings of [term] and [token] and match them.
					if ''.join(sorted(term)) == ''.join(sorted(token)):
						matched_samples.append(term)

		print('The following items were matched for your string: {}'.format(matched_samples))

	"""Cancels the current execution."""
	def cancel(self):
		self.is_alive = False
		sys.exit()


if __name__ == '__main__':
	finder = Finder()
	while finder.is_alive:

		# Blank line for beautification.
		print()
		print("Please select one of the following options: ")
		action = input("[A]dd data to Corpus, [F]ind strings from Corpus, "
					   "[Q]uit the application, or [S]how Corpus: ").upper()

		# A switch case can also be used here. However no effect on performance.
		if action not in "AFQS" or len(action) != 1:
			print("I don't know how to do that..")
			continue
		if action == 'A':
			add_values_to_corpus = input("Please enter strings to update your corpus: ")
			finder.update_corpus(add_values_to_corpus)
		elif action == 'F':
			search_strings = input("Please enter strings to find from your corpus: ")
			finder.find(search_strings)
		elif action == 'S':
			finder.show_corpus()
		elif action == 'Q':
			print("closing the functionality. Good Bye!")
			finder.cancel()
			break
