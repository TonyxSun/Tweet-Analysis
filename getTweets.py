import twint
import csv

def getLocations(loc):
    geoLocations = []
    if loc == "CA":
        filename = "canadacities.csv"
    elif loc == "US":
        filename = "uscities.csv"
    with open(filename) as cities:
        reader = csv.DictReader(cities)
        for row in reader:
            geoLocations.append(f"{row['lat']}, {row['lng']}, 8km") # read in city latitude/longitude. Default radius of 8km
        return geoLocations

def addHashtags(keys):
    # Add hashtag version of all search_keys to search_keys
    for i in range(len(keys)):
        
        key = keys[i].replace(" ", "")
        
        if "#" + key not in keys:
            keys.append ( "#" + key)
    return keys

def scrapeTweets(search_keys, country, geoCoords):
    # Scrape for each
    for key in search_keys:
        for loc in geoCoords:
            c = twint.Config()
            c.Search = key       # topic
            c.Limit = 500      # number of Tweets to scrape
            c.Store_csv = True       # store tweets in a csv file
            # c.Show_hashtags = True
            c.Since = "2019-12-31"
            c.Geo = loc
            c.Output = f"./output/{country}/{key}.csv"     # path to csv 
            twint.run.Search(c)
        
if __name__ == "__main__":
    geoCoords = getLocations("CA") 

    # Terms we want to scrape
    search_keys = ["Huawei", "5G", "cyber security", "cybersecurity", "China Canada trade", "Canada China trade", "Canada China relationship", "China Canada relationship"]
    scrapeTweets(addHashtags(search_keys), "CA", geoCoords)

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