### Intermediate report #2

#### Until now:
As mention in the [previous intermediate report](https://github.com/harshildarji/TMP-SS-2020/blob/master/intermediate-reports/intermediate_report_1.md), our goal was to complete the preprocessing of the scrapped data, which is now complete.

Here is some information on that:
- First, we removed any non-alphanumeric text from the data. These include any @ mentions, hashtags, or emoticons (*if any!*).
- Then, we planned to remove stopwords and perform lemmatization, but later we realized removing stopwords might not be a good idea as this might change the context of the sentence. 

  >**Example**:\
  <br>Consider the statement:\
  <br>"***The media praises Singh for a task, but Modi does not receive any praise from the same media for the same task.***"\
  <br>If we remove stopwords and perform lemmatization, we will get:\
  <br>"***the medium praise singh task modi receive praise medium task***"\
  <br>As we can see, this completely changed the context of the statement.
  
  Considering this effect, we only performed lemmatization on our data.
  
- Also, we decided to combine multiple feature columns (*if any exists!*) to make sure we are not missing anything important.
- After this, we stored all the data in a single CSV to make the further process easier.
- Following barplot shows the number of articles per publisher:
  
  ![bar_plot_number_of_articles](https://i.imgur.com/frabKhX.png)
- Following word-cloud confirms that our data is strictly politics related as many of the frequently used terms are political terms.

  ![wordcloud_political](https://i.imgur.com/QBkGXg7.png)


---
#### In future:
Our goal for the next two weeks is to generate word embeddings from our dataset and use a seed list of a few biased words to produce more of them.
- As mentioned in our [initial report](https://github.com/harshildarji/TMP-SS-2020/blob/master/project-report/initial_report.pdf), a seed list is a collection of initial biased words that can be used to extract more biased words from the corresponding word vector space.
- This step requires a little manual effort to select words that are very close to our seed words in the vector space and add those into the seed list.

---
#### Open question(s):
As this method is closely similar to the one used in the paper [Detecting Biased Statements in Wikipedia](https://dl.acm.org/doi/10.1145/3184558.3191640), we are also looking for alternative methods for our purpose.