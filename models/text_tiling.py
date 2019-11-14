from nltk.tokenize import TextTilingTokenizer
from nltk.corpus import brown

class TextTiling:
	def __init__(self):
		self.model = TextTilingTokenizer()
		print("Initialized model")

	def segment_text(self, text):
		try:
			text_segmented = self.model.tokenize(text)
			boundaries = [0] * len(text.split('\n\n'))
			cur_index = 0
			for segment in text_segmented:
				segs = segment.split('\n\n')
				if segs[0] == '':
					segs = segs[1:]
				cur_index += len(segs)
				if cur_index != len(boundaries):
					boundaries[cur_index] = 1
			return boundaries
		except:
			print("No paragraph split")
			return None




