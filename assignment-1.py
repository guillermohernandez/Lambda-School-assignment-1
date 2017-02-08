import requests
import webbrowser

url = 'http://google.com'
r = requests.get(url)
print (r.text)
local_url = './webpage.html'
webbrowser.open_new(local_url)