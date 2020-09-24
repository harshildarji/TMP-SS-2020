# Text Mining Project (SS-2020), Uni Passau
Topic: **Automating the Creation of Bias Lexica**

Our objective is to automate the process of creating bias lexica, and using this automatically generated bias lexica to classify biased statements using a supervised learning algorithm. In our project, we use _word2vec_ word embedding method to extract biased words from the dataset, then this extracted biased words are used as seeds to extract more biased words to effectively generate a comprehensive lexicon of biased words.

### How to execute the project?
Before running any of the scripts, following are some of the important third-party libraries needed to be installed beforehand:
```bash
pip3 install nltk pandas newspaper3k
pip3 install numpy
pip3 install gensim sklearn
```

Once the above mentioned packages are installed, run the scripts in the following sequence:
1. [code/scrapping/scrapping.py](https://github.com/harshildarji/TMP-SS-2020/blob/master/code/scrapping/scrapping.py)
2. [code/preprocessing/preprocessing.py](https://github.com/harshildarji/TMP-SS-2020/blob/master/code/preprocessing/preprocessing.py)
3. [code/generate_embeddings/generate_embeddings.py](https://github.com/harshildarji/TMP-SS-2020/blob/master/code/generate_embeddings/generate_embeddings.py)
4. [code/bias_words_generation/generating_bias_words.py](https://github.com/harshildarji/TMP-SS-2020/blob/master/code/bias_words_generation/generating_bias_words.py)
5. [code/evaluation/evaluation.py](https://github.com/harshildarji/TMP-SS-2020/blob/master/code/evaluation/evaluation.py)
