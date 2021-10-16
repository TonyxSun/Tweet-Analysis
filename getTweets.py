import twint

def main()

    # Terms we want to scrape
    search_keys = ["Huawei", "5G", "cyber security", "cybersecurity", "China Canada trade", "Canada China trade", "Canada China relationship", "China Canada relationship"]

    # Add hashtag version of all search_keys to search_keys
    for i in range(len(search_keys)):
        
        key = search_keys[i].replace(" ", "")
        
        if "#" + key not in search_keys:
            search_keys.append ( "#" + key)

    
    # Scrape for each
    for key in search_keys:
        c = twint.Config()
        c.Search = key       # topic
        c.Limit = 500      # number of Tweets to scrape
        c.Store_csv = True       # store tweets in a json file
        # c.Show_hashtags = True
        c.Near = "Toronto"
        c.Output = "./output/" + key + ".csv"     # path to csv 
        twint.run.Search(c)
        
if __name__ == "__main__":
    main()

"""

'''
get tweets by text
'''
#Veronica (seperating it out to prevent merge conflicts, not sure if it will work tbh, but I think just having 1 file looks better than 6 files. 
c = twint.Config()
c.Search = 'Huawei'       # topic
c.Limit = 500      # number of Tweets to scrape
c.Store_csv = True       # store tweets in a json file
# c.Show_hashtags = True
c.Output = "./output/Huawei.csv"     # path to json file

twint.run.Search(c)

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
c = twint.Config()
c.Username = 'WhiteHouse'       # username
c.Limit = 50      # number of Tweets to scrape
c.Store_csv = True       # store tweets in a csv file
c.Show_hashtags = True 
c.Output = "./output/cbcnewsbc.csv"    # path to json file

twint.run.Search(c)

#Tony
c = twint.Config()
c.Username = 'cbcnewsbc'       # topic
c.Limit = 50      # number of Tweets to scrape
c.Store_csv = True       # store tweets in a csv file
c.Show_hashtags = True 
c.Output = "./output/cbcnewsbc.csv"     # path to csv file

twint.run.Search(c)
"""