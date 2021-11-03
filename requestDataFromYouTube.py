import json
import requests


x = requests.get('https://www.googleapis.com/youtube/v3/videos?id=Gs069dndIYk&key=AIzaSyA2jy7iGIs82PNFRcEiysunpDHlILGYwYs&part=snippet')


y = json.loads(x.text)
print(y["items"][0]["snippet"]["title"])
