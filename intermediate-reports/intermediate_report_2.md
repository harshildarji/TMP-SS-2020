### Intermediate report #2

#### Until now:
As mention in the [previous intermediate report](https://github.com/harshildarji/TMP-SS-2020/blob/master/intermediate-reports/intermediate_report_1.md), our goal was to complete the preprocessing of the scrapped data, which is complete.

Here is some information on that:
- First, we removed any non-alphanumeric text from the data. These include any @ mentions, hashtags, or emoticons (*if any!*).
- Then, we planned to remove stopwords and perform lemmatization, but later we realized removing stopwords might not be a good idea as this might change the context of the sentence. 

  >**Example**:\
  Consider the statement:\
  "***The media praises Singh for a task, but Modi does not receive any praise from the same media for the same task.***"\
  If we remove stopwords and perform lemmatization, we will get:\
  "***the medium praise singh task modi receive praise medium task***"\
  As we can see, this completely changed the context of the statement.
  
  Considering this effect, we only performed lemmatization on our data.
  
- Also, we decided to combine multiple feature columns (*if any exists!*) to make sure we are not missing anything important.
- After this, we stored all the data in a single CSV to make the further process easier.
- Following barplot shows the number of articles per publisher:
  
  ![bar_plot_number_of_articles](https://i.imgur.com/frabKhX.png)
- Following word-cloud confirms that our data is strictly politics related as many of the frequently used terms are political terms.

  ![wordcloud_political](https://i.imgur.com/QBkGXg7.png)


---
#### In future:


---
#### Open question(s):