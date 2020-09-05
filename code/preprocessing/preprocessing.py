import re

import nltk
import numpy as np
import pandas as pd
from nltk.stem import WordNetLemmatizer

# download wordnet for lemmatizer and create lemmatizer object
nltk.download('wordnet')
lmtzr = WordNetLemmatizer()


def clean(_text):
    """
    This method removes any non-alphanumeric text from the given string and
    performs Lemmatization before returning the string.
    """
    _cleaned = re.sub(r"(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|('s)|([^A-Za-z\t])|(http\S+)", ' ', _text).split()
    cleaned = [lmtzr.lemmatize(w) for w in _cleaned]
    return (' '.join(cleaned)).strip().lower()


data = pd.read_csv('../scrapping/raw_data/raw_data.csv')
data = data.drop(data.columns[0], axis=1).drop_duplicates(subset='ArtText').dropna().reset_index(drop=True)
data = data[~data['ArtText'].str.contains('Please enable cookies on your web browser in order to continue.')].reset_index(drop=True)
data['label'] = np.where((data['Democrat_Vote'] == 'Neutral') & (data['Republican_Vote'] == 'Neutral'), 0, 1)
data['Text'] = data['ArtTitle'] + ' ' + data['ArtText'] + ' ' + data['ArtSummary']

with open('./data.csv', 'w') as f:
    f.write('text,label\n')
    for i, line in enumerate(data['Text']):
        f.write('{},{}\n'.format(clean(line), data['label'][i]))
f.close()
