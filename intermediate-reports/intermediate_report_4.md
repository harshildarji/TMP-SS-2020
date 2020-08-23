### Intermediate report #4

#### Until now:
As mentioned in the [previous progress report](https://github.com/harshildarji/TMP-SS-2020/blob/master/intermediate-reports/intermediate_report_3.md), our objective was to build a vocabulary of bias words which is completed. 

We followed the following procedure for this:
- Load Word2Vec model,
- Read and parse the bias words list from the [repository](https://git.l3s.uni-hannover.de/hube/Bias_Word_Lists) and select 10 bias words manually.
- Retrive the vector representation of each word from the model.
  ```python
  Word2Vec_model.wv['word']
  ```
- Find top 15 words similar to the vector returned by the above step using.
  ```python
  Word2Vec_model.wv.most_similar(positive=[Vector], topn=15)
  ```
- For the first iteration we used each token of the shortlisted seed words but for the 2nd and 3rd iteration we formed all possible duplets and triplets respectively using the new list of words returned after each iteration.
  ```python
  def generate_seed_words(SeedWords_shortlisted, n):
    Combination_SeedWords = list()
    for _tuple in itertools.combinations(SeedWords_shortlisted, n):
        Combination_SeedWords.append(_tuple) 
    return Combination_SeedWords
  ```
- For each word in a duplet or triplet we repeat the step-3 (i.e retrive vectors) and calculate the element wise mean.
  ```python
  Avg_Vector = np.mean(vectors, axis=0)
  ```
- Post each iteration we write the extracted similar words to a .txt file and remove duplicates. 
- After all the process we have generated a set of 2958 unique bias words, in future depending on the use case we might extend the size of the vocabulary.

---
#### In future:
- For the next two weeks, our project will be directed towards determing possible evaluation strategies and further optimization of the generated embedding model.
