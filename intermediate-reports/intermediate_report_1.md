### Intermediate report #1

#### Until now:
- Completed scraping news articles from three major news-sites (refer [#2](https://github.com/harshildarji/TMP-SS-2020/pull/2)):
  1. News18 ([script](https://github.com/harshildarji/TMP-SS-2020/blob/master/code/scrapping/news18.py) | [csv](https://github.com/harshildarji/TMP-SS-2020/blob/master/code/scrapping/data/news18.csv))
  2. Reuters ([script](https://github.com/harshildarji/TMP-SS-2020/blob/master/code/scrapping/reuters_us_politics.py) | [csv](https://github.com/harshildarji/TMP-SS-2020/blob/master/code/scrapping/data/reuters_us_politics.csv))
  3. Times of India ([script](https://github.com/harshildarji/TMP-SS-2020/blob/master/code/scrapping/toi.py) | [csv](https://github.com/harshildarji/TMP-SS-2020/blob/master/code/scrapping/data/toi.csv))
- Some information about data:

|   |Total Articles|Nulls|Duplicates|After `dropna` and `drop_duplicates`|
|---|---|---|---|---|
|News18|19643|452|0|19191|
|Reuters|30808|0|431|30377|
|TOI|337|0|0|337|
|**Total**|50788|452|431|**49905**|

As of now, we have **49905** articles to work with after removing nulls and duplicates which we find sufficiently enough. If needed, we are ready to scrap more articles from other different sources.

---
#### In future:
In the next two weeks, we plan to complete the pre-processing of scrapped articles.

We will focus on:
- Cleaning the text (*removing non-alphanumeric characters, stopwords, hashtags or emoji, etc.*)
- Tokenization/Lemmatization (*if needed!*)

Also, at this stage, we will decide about the feature we will work with. For example, TOI has features, ***Title***, ***Text***, and ***Summary***. After pre-processing is done, we will decide which feature will be important for our purpose. Once the selection is completed, we will discard the remaining features.

At the end of the pre-processing step, we plan to keep a *single CSV* file with all the pre-processed data we need for further process.

---
#### Open question(s):
As of now, we plan to use NLTK for pre-processing purposes, but we are open to other libraries such as SpaCy and StandfordNLP.  So, in other words, we are yet to decide which library we will proceed with. This is still in discussion in issue [#1](https://github.com/harshildarji/TMP-SS-2020/issues/1).



