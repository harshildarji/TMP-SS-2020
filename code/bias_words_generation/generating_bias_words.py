import itertools
import multiprocessing

import numpy as np
from gensim.models import Word2Vec

word2vec_model = Word2Vec.load('../generate_embeddings/embeddings.model')


def generate_combinations(seedwords_shortlisted, n):
    combination_seedwords = list()
    for _tuple in itertools.combinations(seedwords_shortlisted, n):
        combination_seedwords.append(_tuple)
    return combination_seedwords


def generate_seed_words(combination):
    global seedwords
    # compute mean of the vectors for n combination of words
    vectors = list()
    for i in combination:
        vectors.append(word2vec_model.wv[i])
    avg_vector = np.mean(vectors, axis=0)

    # get top 15 similar words for a word using the trained Word2Vec model
    similar_words = [x[0] for x in word2vec_model.wv.most_similar(positive=[avg_vector], topn=15)]

    return similar_words


def bias_word_generation():
    seedwords = ['harassing', 'dishonourable', 'politicizing', 'victimisation', 'hypocrite', 'electioneering', 'humiliation', 'condemnation', 'reciprocate', 'scandal']

    for n_combo in range(3, 6):
        combinations = generate_combinations(seedwords, n_combo)
        print('Combination of {}, Number of combinations: {}'.format(n_combo, len(combinations)))

        pool = multiprocessing.Pool()
        similar_words = pool.map(generate_seed_words, combinations)
        pool.close()

        seedwords += [word for sublist in similar_words for word in sublist]

        # apply set and convert back to list to make sure there are no repeating words
        seedwords = list(set(seedwords))
        print('- New seed-words length: {}'.format(len(seedwords)))

    # sort and write the bias words to the text file
    bias_words = sorted(seedwords)
    with open('bias_words.txt', 'w') as f:
        for item in bias_words:
            f.write('{}\n'.format(item))
    f.close()


if __name__ == '__main__':
    bias_word_generation()

    read_file = open('bias_words.txt', 'r')
    words = read_file.read().split('\n')
    print('Total bias words: {}'.format(len(words) - 1))
