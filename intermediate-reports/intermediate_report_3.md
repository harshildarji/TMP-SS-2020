### Intermediate report #3

#### Until now:
As mentioned in the [previous progress report](https://github.com/harshildarji/TMP-SS-2020/blob/master/intermediate-reports/intermediate_report_2.md), our goal was to complete the script for generating word embeddings, which is now complete.

We followed the following procedure for this:
- Load [pre-processed data](https://github.com/harshildarji/TMP-SS-2020/blob/master/code/preprocessing/data.csv),
- Tokenize the data,
- Initiate word2vec model with following hyper-parameters:
  ```python
  model = Word2Vec(min_count=5,  # ignore all words with total absolute frequency than this
                     window=5,
                     size=300,  # dimensionality of the feature vectors
                     sample=6e-5,  # threshold for configuring which higher-frequency words are randomly down-sampled
                     alpha=0.03,
                     min_alpha=0.0007,
                     workers=cores - 1)
  ```
- Train model on tokenize data.
- Save the trained model locally.

This program output the following:
```bash
(base) root@darji:~/TMP-SS-2020/code/generate_embeddings# python generate_embeddings.py 
[nltk_data] Downloading package punkt to /root/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
Generating word embeddings...
- tokenizing the data
- using 39 out of 40 CPU cores
- building the vocabulary table
- training the word2vec model
- word2vec model saved at ./embeddings.model
- took 2.57 minutes
```

---
#### In future:
For the next two weeks, our goal is to complete the script for automatically generating the bias lexica.
- For this, we will use the approach of using a seed list and using it to identify more biased words from our dataset based on how close those words are to each other in vector space.

---
#### Open question(s):
As mentioned in the [previous progress report](https://github.com/harshildarji/TMP-SS-2020/blob/master/intermediate-reports/intermediate_report_2.md), we are still looking for an alternative method to automatically generate a biased-word lexicon.
