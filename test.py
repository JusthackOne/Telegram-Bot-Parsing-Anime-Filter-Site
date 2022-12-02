import requests

r = requests.get('https://pub.idqqimg.com/qqmobile/qqapi.js?_bid=200')

print(r.headers['content-type'])


