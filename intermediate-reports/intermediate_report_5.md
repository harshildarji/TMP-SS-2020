
### Intermediate report #5

#### Until now:
As mentioned in the [previous progress report](https://github.com/harshildarji/TMP-SS-2020/blob/master/intermediate-reports/intermediate_report_4.md), our objective was to work on possible evaluation strategy.

Before working on the evaluation, we first made some minor changes in our bias generation script due to the issue of repetition. We also changed some parameters to make sure that generated bias words are not meaningless.
The new bias word list can be found at: [bias_words.txt](https://github.com/harshildarji/TMP-SS-2020/blob/master/code/bias_words_generation/bias_words.txt)

To have an evaluation dataset, we looked towards the paper, [Fair and Balanced? Quantifying Media Bias through Crowdsourced Content Analysis](https://academic.oup.com/poq/article-abstract/80/S1/250/2223443?redirectedFrom=fulltext).

Dataset provided by them provides annotations based on whether a particular news article is biased towards either democratic or republican party.

The last two columns of this evaluation dataset are `democrat.vote` and `republican.vote`.

Both these columns have one of the following five values:

-   very positive,
-   somewhat positive,
-   neutral,
-   somewhat negative,
-   very negative

As per our understanding, if both the columns have a neutral vote for a particular article, then we can safely assume that the article is not biased. If an article has label positive for one party and negative for the other, then we can say that the article is biased.

This dataset only provides the URLs to the news articles and not the actual articles, so we first scraped the data using the URLs provided in the before-mentioned dataset. Then we preprocessed this scrapped data and labeled each article based on the vote given to democratic and republican party.

The preprocessed evaluation dataset can be found at: [evaluation_data.csv](https://github.com/harshildarji/TMP-SS-2020/blob/master/code/preprocessing/evaluation_data.csv)

---
#### In future:
- In the next two weeks, we plan to annotate the evaluation dataset using our generated bias words list. Once this annotation is complete, we plan to compare our annotation with the existing one.
