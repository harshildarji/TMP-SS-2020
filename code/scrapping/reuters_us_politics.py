# https://medium.com/analytics-vidhya/how-to-scrape-news-headlines-from-reuters-27c0274dc13c
# https://github.com/je-suis-tm/web-scraping/blob/master/MENA%20Newsletter.py
# https://github.com/LuChang-CS/news-crawler/blob/master/article/reuters_article.py
# https://github.com/zaemyung/crawl-reuters/blob/master/crawler/crawler/spiders/reuters_spider.py
# https://github.com/monkeyclass/reuters/blob/master/reuters/spiders/reuters_spider.py
# https://github.com/garyjxgong/Reuters-News-Articles-Crawler
# https://www.geeksforgeeks.org/find_element_by_tag_name-driver-method-selenium-python/?ref=rp
# https://www.reuters.com/news/archive/politicsnews?view=page&page=11&pageSize=10

import time

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.reuters.com/news/archive/politicsnews?view=page&page=1755&pageSize=10')
headlines = []
article_content = []
dates = []
x = 1

while True:
    try:
        print('Executing iteration:', x)
        loadMoreButton = driver.find_element_by_class_name("control-nav-next")
        time.sleep(3)
        loadMoreButton.click()
        time.sleep(2)
        news_content = driver.find_elements_by_tag_name("p")
        for content in news_content[:len(news_content) - 3]:
            article_content.append(content.text)
        x = x + 1
    except NoSuchElementException:
        break

text_format = {'Text': article_content}
my_df = pd.DataFrame(text_format)
my_df.drop_duplicates(keep='first', inplace=True)
my_df.to_csv(r'./data/reuters_us_politics.csv', index=False, header=True)
