# https://stackoverflow.com/questions/36709165/beautifulsoup-object-of-type-response-has-no-len
# https://stackoverflow.com/questions/32468801/how-to-get-href-from-an-a-tag-inside-a-div
# https://stackoverflow.com/questions/23013220/max-retries-exceeded-with-url-in-requests

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
    links = [a['href'] for div in soup.find_all("div", attrs={"class": "blog-list-blog"}) for a in div.find_all('a')]
    return list(dict.fromkeys(links))


InvalidURL = list()


def get_short_news(url):
    if checkers.is_url(url):
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, "html.parser")
        short_news = soup.find("div", attrs={"class": "article-bnow-box"}).h2.text
    else:
        short_news = "Invalid URL given"
        InvalidURL.append(url)
    return short_news


UnProcessedUrls = list()


def get_news_details(url):
    try:
        toi_article = Article(url, language="en")
        toi_article.download()
        toi_article.parse()
        time.sleep(3)
        toi_article.nlp()

        ArticleTitle = toi_article.title
        ArticleText = toi_article.text
        ArticleSummary = toi_article.summary
        ArtPubDate = toi_article.publish_date
        return ArticleTitle, ArticleText, ArticleSummary, ArtPubDate

    except:
        UnProcessedUrls.append(url)
        return "No Text", "No Text", "No Text", "No Text"


News18_Articles = pd.DataFrame(columns=['Date', 'Title', 'Text', 'Summary', 'Link'])
invalid_url, ArtTitle, ArtTest, ArtSummary, ArtDate, processedURLs = ([] for i in range(6))

for i in range(1):
    print('Page number = ', i)
    pageUrl = 'https://www.news18.com/politics/page-' + '{}/'.format(i)
    processedURLs.append(pageUrl)
    ArtLinks = get_news_class_hrefs(pageUrl)

    for artLink in ArtLinks:
        if checkers.is_url(artLink):
            if not None:
                Title, Text, Summary, Date = get_news_details(artLink)
                temp_df = pd.DataFrame({'Date': Date,
                                        'Title': Title,
                                        'Text': Text,
                                        'Summary': Summary,
                                        'Link': artLink}, index=[0])
                News18_Articles = News18_Articles.append(temp_df, ignore_index=True, sort=True)
                ArtTitle.append(Title)
                ArtTest.append(Text)
                ArtSummary.append(Summary)
                ArtDate.append(Date)
        else:
            invalid_url.append(artLink)
    print('Total News Articles Scrapped =', len(ArtTitle))

News18_Articles.drop_duplicates(subset="Title", keep='first', inplace=True)

News18_Articles.to_csv(r'./data/news18.csv', index=False, header=True)
