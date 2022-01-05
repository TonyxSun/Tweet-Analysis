from getTweets import *
from sentiment_analysis import *
from datetime import date


geoCoords = getLocations("CA")
usernames = ['AtlanticCouncil', 'CFR_org', 'CSIS', 'icasDC', 'jshermcyber', "saistype", 'RobertCresanti', 'Dalzell60',
             'GovGaryLocke', 'ianbremmer', 'ZackCooper', 'chrismeserole', 'MichaelEOHanlon', 'SlaughterAM',
             'peterbergencnn', 'SammSacks', 'gwbstr', 'joshchin', 'lorandlaskai', 'tarah', 'kennedycsis', 'ConStelz',
             'GoodmanSherri', 'GotoEastAsia', 'wendyscutler', 'melkgriffith', 'NongHong_ICAS', 'ICAS_Zhang',
             'Doug_Bandow']
search_keys = ["Huawei", "5G", "cyber security", "cybersecurity", "China Canada trade", "Canada China trade",
               "Canada China relationship", "China Canada relationship"]
#scrapeTweetsEXCEL(addHashtags(search_keys), usernames)

df = combine_df("output")
clean_df = clean_data(df)
pos, neg, neu = sentiment_analysis(clean_df)
date = date.today()

with open("results.txt", 'a') as results:
    results.write(str(date) + ", " + str(pos) + ", " + str(neg) + ", " + str(neu))
