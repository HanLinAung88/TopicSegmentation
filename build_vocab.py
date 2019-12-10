from sklearn.model_selection import train_test_split
from nltk.tokenize import sent_tokenize, word_tokenize
from itertools import chain 
import json

def build_vocab(data_file="./data/text_data.json"):
	data = json.load(open(data_file, 'r'))
	tokenized_words = set()

	# TODO: change this to all lectures
	for course in data:
		lectures = data[course]
		for lecture in lectures:
			split_text = lectures[lecture]
			text = list(split_text.values())
			tokenized_sents = []
			for subtopic_text in text:
				tokenized_subtopic_words = word_tokenize(subtopic_text)
				for word in tokenized_subtopic_words:
					tokenized_words.add(word)

	vocab = list(tokenized_words)
	word2id = {k: v for v, k in enumerate(vocab)}
	id2word = {k: v for k, v in enumerate(vocab)}
	with open('data/word2id.json', 'w') as f:
		json.dump(word2id, f)
	with open('data/id2word.json', 'w') as f:
		json.dump(id2word, f)

build_vocab()