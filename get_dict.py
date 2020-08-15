import requests

url = "http://norvig.com/ngrams/sowpods.txt"
data = requests.get(url=url, allow_redirects=False)
open("dict.txt", "w").write(data.content.decode())