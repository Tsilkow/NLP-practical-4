# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import sys
sys.path.append('./.')
from run import evaluate_places


evaluation_corpus_path = 'birth_dev.tsv'
with open(evaluation_corpus_path, 'r') as f:
    data = f.readlines()
    input_lines_total = len(data)

predictions = ['London'] * input_lines_total
total, correct = evaluate_places(evaluation_corpus_path, predictions)
print(f'Correct: {correct} out of {total}: {correct/total*100}')
