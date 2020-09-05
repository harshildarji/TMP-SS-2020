import itertools
import multiprocessing
import random

import numpy as np
from gensim.models import Word2Vec

word2vec_model = Word2Vec.load('../generate_embeddings/embeddings.model')


def generate_combinations(seedwords, n):
    combinations = list()
    for i, _tuple in enumerate(itertools.combinations(random.sample(seedwords, len(seedwords)), n)):
        combinations.append(_tuple)
        if i > 25000:
            break
    return combinations


def generate_seed_words(combination):
    # compute mean of the vectors for n combination of words
    vectors = list()
    for i in combination:
        vectors.append(word2vec_model.wv[i])
    avg_vector = np.mean(vectors, axis=0)

    # get top 5 similar words for a word using the trained Word2Vec model
    similar_words = [x[0] for x in word2vec_model.wv.most_similar(positive=[avg_vector], topn=5)]

    return similar_words


def bias_word_generation():
    seedwords = ['radical', 'democrat', 'republican', 'bigot', 'racist']

    for i in range(25):
        combinations = generate_combinations(list(set(seedwords)), 5)

        pool = multiprocessing.Pool()
        similar_words = pool.map(generate_seed_words, combinations)
        pool.close()

        similar_words = [word for sublist in similar_words for word in sublist]
        seedwords += similar_words

        print('Loop: {}, Bias words length: {}'.format(i, len(set(seedwords))))

    # sort and write the bias words to the text file
    bias_words = sorted(list(set(seedwords)))
    with open('bias_words.txt', 'w') as f:
        for item in bias_words:
            f.write('{}\n'.format(item))
    f.close()


if __name__ == '__main__':
    bias_word_generation()

    read_file = open('bias_words.txt', 'r')
    words = read_file.read().split('\n')
    print('Total bias words: {}'.format(len(words) - 1))
