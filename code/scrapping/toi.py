# https://timesofindia.indiatimes.com/topic/Politics
# https://stackoverflow.com/questions/23013220/max-retries-exceeded-with-url-in-requests
# https://stackoverflow.com/questions/36709165/beautifulsoup-object-of-type-response-has-no-len
# https://stackoverflow.com/questions/32468801/how-to-get-href-from-an-a-tag-inside-a-div

import time

import nltk
import pandas as pd
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from validator_collection import checkers

nltk.download('punkt')


def get_news_class_hrefs(url):
    """
    Finds all urls pointed to by all links inside
    'news' class div elements
    """
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    links = ['https://timesofindia.indiatimes.com' + a['href'] for div in soup.find_all("div", attrs={"class": "content"}) for a in div.find_all('a')]
    return links[1:]


def __get_article(url, sleep_time):
    toi_article = Article(url, language="en")
    toi_article.download()
    time.sleep(sleep_time)
    toi_article.parse()
    time.sleep(2)
    toi_article.nlp()

    ArticleTitle = toi_article.title
    ArticleText = toi_article.text
    ArticleSummary = toi_article.summary
    return ArticleTitle, ArticleText, ArticleSummary


def get_news_details(url):
    try:
        return __get_article(url, 0.5)

    except BaseException:
        return __get_article(url, 2)

    else:
        pass


TOI_Articles = pd.DataFrame(columns=['Title', 'Text', 'Summary'])
invalid_url, ArtTitle, ArtTest, ArtSummary, processedURLs = ([] for i in range(5))
for i in range(500):
    pageUrl = 'https://timesofindia.indiatimes.com/topic/Politics' + '/{}'.format(i)
    processedURLs.append(pageUrl)
    ArtLinks = get_news_class_hrefs(pageUrl)

    for artLink in ArtLinks:
        if checkers.is_url(artLink):
            Title, Text, Summary = get_news_details(artLink)
            temp_df = pd.DataFrame({'Title': Title,
                                    'Text': Text,
                                    'Summary': Summary}, index=[0])
            TOI_Articles = TOI_Articles.append(temp_df, ignore_index=True, sort=True)
            ArtTitle.append(Title)
            ArtTest.append(Text)
            ArtSummary.append(Summary)
        else:
            invalid_url.append(artLink)
    print('Total News Articles Scrapped =', len(ArtTitle))

TOI_Articles.to_csv(r'./data/toi.csv', index=False, header=True)

text_format = {'Title': ArtTitle, 'Text': ArtTest, 'Summary': ArtSummary}
my_df = pd.DataFrame(text_format)
my_df.to_csv(r'./data/toi.csv', index=False, header=True)
