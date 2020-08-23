import time
import nltk
import pandas as pd
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from validator_collection import checkers

nltk.download('punkt')

df = pd.read_csv(r"raw_data/newsArticlesWithLabels.tsv", sep="\t")

def eval_data_scrapping(df):

	artTitle, artSummary, artText, democrat_Vote, republican_Vote, unprocessed_Urls = ([] for i in range(6))
	for idx, row in df.iterrows(): 
    	try:
        	print('Running for {} file'.format(idx))
        	toi_article = Article(row['url'], language="en")
        	toi_article.download()
        	toi_article.parse()
        	toi_article.nlp()

        	artTitle.append(toi_article.title)
        	artText.append(toi_article.text)
        	artSummary.append(toi_article.summary)
        	democrat_Vote.append(row['democrat.vote'])
        	republican_Vote.append(row['republican.vote'])
    
    	except:
        	unprocessed_Urls.append(row['url'])
        	pass


	csv_format = {'ArtTitle' : artTitle, 'ArtText' : artText, "ArtSummary" : artSummary, 
              'Democrat_Vote':democrat_Vote, 'Republican_Vote':republican_Vote}

	eval_df = pd.DataFrame(csv_format)

	eval_df.to_csv(r'raw_data/evaluation_data.csv')


if __name__ == '__main__':
	eval_data_scrapping(df)