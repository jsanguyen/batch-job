import requests
import sys

newFile = open("example.json", "x")
key = sys.argv[1]

try:
    response = requests.get("https://serpapi.com/search.json?engine=home_depot&q=oven&lowerbound=450&upperbound=500&api_key={}".format(key
))
    response.raise_for_status()
    content = response.text

    newFile.write(content)
    newFile.close()


except:
  
    newFile.write("Exception Occured")
    newFile.close()
 