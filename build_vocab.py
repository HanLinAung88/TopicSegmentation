from sklearn.model_selection import train_test_split
from nltk.tokenize import sent_tokenize, word_tokenize
from itertools import chain 
<<<<<<< HEAD
from nltk.corpus import stopwords
import json
import string
import re

STOPWORDS = set(stopwords.words('english'))
PUNCTUATIONS = set([punct for punct in string.punctuation])

def build_vocab(data_file="./data/text_data.json", top_n=1000):
	data = json.load(open(data_file, 'r'))
	tokenized_words_count = {}
	tokenized_words = set()
	data = json.load(open(data_file, 'r'))

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
					re_match = re.match("[a-zA-z]+", word)
					if re_match is not None and word.lower() not in STOPWORDS and word not in PUNCTUATIONS and len(word) >=2:
						word = re_match.group(0)
						if word in tokenized_words_count:
							tokenized_words_count[word] += 1
						else:
							tokenized_words_count[word] = 0
						tokenized_words.add(word)
	vocab = None
	if top_n:
		sorted_words_by_count = sorted(tokenized_words_count.items(), key=lambda kv: kv[1], reverse=True)
		sorted_words_by_count = sorted_words_by_count[:min(top_n, len(sorted_words_by_count))]	
		vocab = [word_tpl[0] for word_tpl in sorted_words_by_count]
	else:
		vocab = list(tokenized_words)
	word2id = {k: v for v, k in enumerate(vocab)}
	word2id["UNK"] = len(word2id)
	id2word = {k: v for k, v in enumerate(vocab)}
	id2word[str(len(word2id))] = "UNK"

	with open('data/word2id.json', 'w') as f:
		json.dump(word2id, f)
	with open('data/id2word.json', 'w') as f:
		json.dump(id2word, f)

build_vocab()
