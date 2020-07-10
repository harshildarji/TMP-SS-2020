import os
import re

import nltk
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
    _cleaned = re.sub(r"(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|('s)|([^A-Za-z0-9\t])|(http\S+)", ' ', _text).split()
    cleaned = [lmtzr.lemmatize(w) for w in _cleaned]
    return (' '.join(cleaned)).strip().lower()


if __name__ == '__main__':
    files = ['news18', 'reuters', 'toi']

    with open('./raw_data.csv', 'w') as f:
        f.write('publisher,text\n')
        for file in files:
            print(f'Working on {file}.csv...')
            df = pd.read_csv(f'../scrapping/raw_data/{file}.csv')

            # if the CSV contains 'Title' and 'Summary' columns, merge them into 'Text' column
            if 'Title' in df.columns.values:
                df['Text'] = df['Title'] + ' ' + df['Text'] + ' ' + df['Summary']

            # line-by-line, clean and append to 'data.csv' along with the publisher
            for line in df['Text']:
                f.write(f'{file},{clean(line)}\n')
    f.close()

    # Drop NA and duplicates!
    data = pd.read_csv('./raw_data.csv')
    data = data.dropna()
    data = data.drop_duplicates(keep='first')
    data.to_csv('./data.csv', index=False)

    # delete raw_data.csv
    os.remove('./raw_data.csv')
