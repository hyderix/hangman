import requests

url = "http://norvig.com/ngrams/sowpods.txt"
data = requests.get(url=url, allow_redirects=False)
if open("hangman/dict.txt", "r").read().split("\n")[0:100] == data.content.decode().split("\n")[0:100]:
    open("hangman/dict.txt", "w").write(data.content.decode())