### Intermediate report 6

#### Until now:
As mentioned in the [previous progress report](https://git.fim.uni-passau.de/padas/20ss-tmp/team01/-/blob/master/intermediate-reports/intermediate_report_5.md), our objective was to work on evaluation phase.

Our approach for evaluation is simple:
1. Count the number of biased words each article in our dataset contains,
2. Define a threshold for how much bias words an article should contain in order for it be considered as biased article,
3. Predict labels for each article using this threshold,
4. Compare our predictions with actual targets and get the results.

But while doing so, we faced a major problem. As mentioned before, our dataset had a higher number of news articles from Indian news media, and for this reason, many of the bias words in our list was written in Hindi-English.

Due to this, we were not able to get `bias_word_count` from evaluation dataset using that list of bias words.

For this reason, we decided to remove all of our old datasets, and replace it with the one with ground-truth available. Since we already had everything scripted, this did not take much longer. This change was pushed to master branch with commit 5a8b39ce7af249a480ca1d71d7554457a785f60b.

Once, we had our new dataset and a new list of biased words, we apply the above-mentioned evaluation strategy and it worked as expected.

The following are the results of our evaluation:

```
Accuracy:       0.6050747393543525
Precision:      0.5808531746031746
Recall:         0.6169652265542677
F1:             0.598364844149208
Cohen-kappa:    0.21062286195898272
```

Although the results are not up to the level we were expecting to achieve, but we believe this can be improved by increasing the list of biased words.

**Related issues: #23, #24, #25, #26, #27**

---
#### In future:
- Since our evaluation is complete, we plan to work on the documentation of our project for the next few weeks.
