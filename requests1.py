# from urllib.request import urlopen
# f = urlopen("https://www.example.com")
# print(f.read(500).decode('utf-8'))

#----------#

# data='language=python&framwork=django'
# f=urlopen('https://127.0.0.1:8000', bytes(data, encoding='utf-8'))
# print(f.read().decode('utf-8'))

# import requests
# #GET
# response = requests.get('https://www.example.com/posts')
# #상태 코드
# status_code = response.status_code
# if status_code == 200:
#     data = response.json()
#     for post in data:
#         print(post['title'])
# else:
#     print(f"error: {response.text}")
    
#----------#
    
# from urllib.request import urlopen
# from html.parser import HTMLParser

# class ImgParser(HTMLParser):
#     def __init__(self):
#         super().__init__()
#         self.result = []
#     def handle_starttag(self, tag, attrs): #<tag> 를 처리하기 위해 오버라이딩
#         if tag != 'img':
#             return
#         if not hasattr(self, 'result'):
#             self.result = []
#         for name, value in attrs:
#             if name == 'src':
#                 self.result.append(value)
                
# def parserImage(data):
#     parser = ImgParser()
#     parser.feed(data)
#     dataSet = set(x for x in parser.result)# set은 중복 불가
#     return dataSet
    
# def main():
#     url = 'http://www.google.com'
    
#     f = urlopen(url)
#     charSet = f.info().get_param('charSet')
#     data = f.read().decode(charSet)
#     f.close()
    
#     dataSet = parserImage(data)
#     print("\n>>>>>> Fetch Image from", url)
#     print('\n'.join(sorted(dataSet)))
    
# if __name__ == '__main__':
#     main()

#----------#

# from pathlib import Path
# from http.client import HTTPConnection
# from urllib.parse import urljoin, urlunparse
# from urllib.request import urlretrieve
# from html.parser import HTMLParser

# class ImageParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         if tag != 'img':
#             return
#         if not hasattr(self, 'result'):
#             self.result = []
#         for name, value in attrs:
#             if name == 'src':
#                 self.result.append(value)
                
# def downloadImage(url, data) : 
#     downDir = Path('DOWNLOAD')
#     downDir.mkdir(exist_ok=True)
    
#     parser = ImageParser()
#     parser.feed(data)
#     dataSet = set(x for x in parser.result)
    
#     for x in sorted(dataSet):
#         imageUrl = urljoin(url, x)
#         basename = Path(imageUrl).name
#         targetFile = downDir / basename
        
#         print("Downloading...", imageUrl)
#         urlretrieve(imageUrl, targetFile)
        
# def main():
#     host = "www.google.com"
    
#     conn = HTTPConnection(host)
#     conn.request("GET", '')
#     resp = conn.getresponse()
    
#     charset = resp.msg.get_param('charset')
#     data = resp.read().decode(charset)
#     conn.close()
    
#     print("\n >>>>>>>>>>>>>>>>>>>> Download Image from ", host)
#     url = urlunparse(("http", host, '', '', '', ''))
#     downloadImage(url, data)
    
# if __name__ == '__main__':
#     main()

#----------#

# from http.server import HTTPServer, BaseHTTPRequestHandler

# class MyHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response_only(200, 'OK')
#         self.send_header('Content-Type', 'text/plain')
#         self.end_headers()
#         self.wfile.write(b'Hello World')
        
# if __name__ == "__main__":
#     server = HTTPServer(('', 8888), MyHandler)
#     print("Started WebServer on port 8888....")
#     print('Press ^C to quit WebServer.')
#     server.serve_forever()

#cgi-server - cgi-client#

from urllib.request import urlopen
from urllib.parse import urlencode

url = "https://127.0.0.1:8888/cgi-bin/cgi-server.py"

data = {
    'name' : 'Kim',
    'email' : 'a@gmail.com',
    'url' : 'https://www.google.com',
}

encDate = urlencode(data)
postData = encDate.encode('ascii')

f = urlopen(url, postData)
print(f.read().decode('cp949'))