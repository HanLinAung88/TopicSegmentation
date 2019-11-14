import numpy as np
from load_data import load_data
from models.text_tiling import TextTiling
from nltk.metrics.segmentation import windowdiff

DATA = load_data()
WINDOW_DIFF_K = 3

def evaluate_text_tiling(data):
	text_tiler = TextTiling()
	X = data[0]
	y = data[1]
	window_diffs = []
	for index, lecture_text in enumerate(X):
		boundaries = text_tiler.segment_text(lecture_text)
		ground_truth_boundaries = y[index]
		pred_boundaries = ''.join(str(boundary) for boundary in boundaries)
		ground_truth_boundaries = ''.join(str(boundary) for boundary in ground_truth_boundaries)
		k = int(len(ground_truth_boundaries)/float(2.0 * ground_truth_boundaries.count('1') + 1.0))
		window_diff_score = windowdiff(pred_boundaries, ground_truth_boundaries, k)
		window_diffs.append(window_diff_score)

	avg_window_diff_score = np.mean(np.array(window_diffs))
	print("Average window diff score:", avg_window_diff_score)
	return avg_window_diff_score


evaluate_text_tiling(DATA)
