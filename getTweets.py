import twint

'''
get tweets by text
'''
#Veronica (seperating it out to prevent merge conflicts, not sure if it will work tbh, but I think just having 1 file looks better than 6 files. 

#Tony
c = twint.Config()
c.Search = 'Meng Wan Zhou'       # topic
c.Limit = 500      # number of Tweets to scrape
c.Store_csv = True       # store tweets in a json file
# c.Show_hashtags = True
c.Output = "./output/MengWZ.csv"     # path to json file

twint.run.Search(c)


'''
get tweets by hashtag
'''
#Veronica

#Tony

'''
get tweets by user
'''
#Veronica

#Tony
c = twint.Config()
c.Username = 'cbcnewsbc'       # topic
c.Limit = 50      # number of Tweets to scrape
c.Store_csv = True       # store tweets in a csv file
c.Show_hashtags = True 
c.Output = "./output/cbcnewsbc.csv"     # path to csv file

twint.run.Search(c)