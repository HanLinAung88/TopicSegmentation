from nltk.tokenize import sent_tokenize
import json

def load_data(data_file="./data/text_data.json"):
	data = json.load(open(data_file, 'r'))
	lectures = data['Frontiers and Controversies in Astrophysics']
	lecture_text = []
	ground_truth_boundaries = []
	for lecture in lectures:
		ground_truth_boundary = []
		split_text = lectures[lecture]
		text = list(split_text.values())
		tokenized_sents = [] 
		for subtopic_text in text:
			tokenized_subtopic = sent_tokenize(subtopic_text)
			tokenized_sents.extend(tokenized_subtopic)
			cur_segment = []
			if len(tokenized_sents) > 0:
				cur_segment = [1]
			cur_segment.extend([0 for i in range(len(tokenized_subtopic) - 1)])
			ground_truth_boundary.extend(cur_segment)
		text = "\n\n".join(tokenized_sents)
		lecture_text.append(text)
		ground_truth_boundaries.append(ground_truth_boundary)
	# print(lecture_text)
	return lecture_text, ground_truth_boundaries

