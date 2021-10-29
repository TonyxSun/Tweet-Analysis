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
        count = 0
        for row in reader:
            geoLocations.append(f"{row['lat']}, {row['lng']}, 8km") # read in city latitude/longitude. Default radius of 8km
            if count >= 500: # only get top x cities by population
                break
            count += 1
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
            c.Since = "2019-5-31"
            c.Lang = 'en'   # specify english results only
            c.Geo = loc
            c.Hide_output = True
            c.Output = f"./output/{country}/{key}.csv"     # path to csv 
            twint.run.Search(c)
        
if __name__ == "__main__":
    geoCoords = getLocations("US") 

    # Terms we want to scrape
    search_keys = [ "cyber security", "cybersecurity", "China Canada trade", "Canada China trade", "Canada China relationship", "China Canada relationship"]
    scrapeTweets(addHashtags(search_keys), "US", geoCoords)

