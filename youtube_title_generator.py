import requests

Youtube_api_key = 'blablabla' # Votre clé API

search = 'how+to+scrape+title+in+youtube'
titles = []
response = requests.get('https://www.googleapis.com/youtube/v3/search?maxResults=200&key=' + Youtube_api_key + '&part=snippet&q=' + search + '&type=video')
content = response.json()
for el in content['items']:
    titles.append(el['snippet']['title'])

f = open('youtube_title.txt', "w", encoding="utf8")
for el in titles:
    f.write(el + '\n')

f.close()