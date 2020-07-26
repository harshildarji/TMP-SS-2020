import multiprocessing
from timeit import default_timer as timer

import nltk

nltk.download('punkt')
import pandas as pd
from gensim.models import Word2Vec


def get_tokens(data):
    """
    This method will tokenize the data which later will be used to generate word embeddings.
    """
    tokens = []
    for row in data['text']:
        token = nltk.word_tokenize(row)
        tokens.append(token)
    return tokens


def generate_embeddings(data, path):
    """
    This method will generate and save the word embeddings.
    """
    start = timer()
    print('Generating word embeddings...')

    print('- tokenizing the data')
    tokens = get_tokens(data)

    cores = multiprocessing.cpu_count()
    print('- using {} out of {} CPU cores'.format(cores - 1, cores))

    model = Word2Vec(min_count=20,  # ignore all words with total absolute frequency than this
                     window=5,
                     size=300,  # dimensionality of the feature vectors
                     sample=6e-5,  # threshold for configuring which higher-frequency words are randomly down-sampled
                     alpha=0.03,
                     min_alpha=0.0007,
                     negative=20,  # if > 0, negative sampling will be used
                     workers=cores - 1)

    # build the vocabulary table
    print('- building the vocabulary table')
    model.build_vocab(tokens, progress_per=10000)

    # model training
    print('- training the word2vec model')
    model.train(tokens, total_examples=model.corpus_count, epochs=5, report_delay=1)

    model.save(path)
    print('- word2vec model saved at {}'.format(path))

    end = timer()
    print('- took {:.2f} minutes'.format((end - start) / 60))


if __name__ == '__main__':
    data = pd.read_csv('../preprocessing/data.csv')
    generate_embeddings(data, './embeddings.model')
