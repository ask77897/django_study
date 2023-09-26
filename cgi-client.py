from urllib.request import urlopen
from urllib.parse import urlencode

url = "https://127.0.0.1:8888/cgi-bin/cgi-server.py"

data = {
    'name' : 'Kim',
    'email' : 'a@gmail.com',
    'url' : 'http://www.google.com',
}

encDate = urlencode(data)
postData = encDate.encode('ascii')

f = urlopen(url, postData)
print(f.read().decode('cp949'))