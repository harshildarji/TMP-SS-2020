import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, cohen_kappa_score

data = pd.read_csv('../preprocessing/data.csv')
with open('../bias_words_generation/bias_words.txt', 'r') as f:
    bias_words = [line.strip() for line in f.readlines()]

df_counts = pd.DataFrame(columns=['text', 'label', 'bias_word_count'])
for i in range(len(data)):
    text, label = data['text'][i], data['label'][i]
    count = 0
    for word in bias_words:
        if word in text.split():
            count += 1
    df_counts.loc[i] = [text] + [label] + [count]

grouped = df_counts.groupby(['label'])
biased = grouped.get_group(1)
unbiased = grouped.get_group(0)
threshold = (unbiased.bias_word_count.quantile([0.75]).values[0] + biased.bias_word_count.quantile([0.25])).values[0] / 2

annotated = pd.DataFrame(columns=['text', 'label', 'bias_word_count', 'annotation'])
for i in range(len(df_counts)):
    text, label, count = df_counts['text'][i], df_counts['label'][i], df_counts['bias_word_count'][i]
    annotation = 0 if count < threshold else 1
    annotated.loc[i] = [text] + [label] + [count] + [annotation]
annotated.to_csv('annotated_data.csv')

actual, predicted = annotated['label'].tolist(), annotated['annotation'].tolist()
accuracy, precision, recall, f1 = accuracy_score(actual, predicted), precision_score(actual, predicted), recall_score(actual, predicted), f1_score(actual, predicted)
ck = cohen_kappa_score(actual, predicted)
print('Accuracy:\t{}\nPrecision:\t{}\nRecall:\t\t{}\nF1:\t\t{}\nCohen-kappa:\t{}'.format(accuracy, precision, recall, f1, ck))

"""
Accuracy:       0.6050747393543525
Precision:      0.5808531746031746
Recall:         0.6169652265542677
F1:             0.598364844149208
Cohen-kappa:    0.21062286195898272
"""
